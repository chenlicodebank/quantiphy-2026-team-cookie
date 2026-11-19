#!/usr/bin/env python
"""SAM 3 as a measurement tool for the open Track B agent (method_queue 54, session 432d3a13, 2026-10-22).

A small HTTP server on the GH200 that keeps facebook/sam3 loaded and answers two question-agnostic calls from the DSH
bridge (dsh_scene.py --sam3-url): `segment` (text-prompted instances on one frame, mask extents in pixels, masks saved as
PNG into the session's workspace, one numbered overlay) and `track` (a SAM 3 video session for one phrase, every frame,
per-frame centre / box / area of every instance, the chosen one written as a CSV into the workspace). The model in the
session names the object from its own question and picks the instance from the overlay; nothing here sees a question.

Why (29_1): SAM 3's pixel speeds match Claude's own measurements within 5 pct on 81-91 pct of same-object pairs, but
the open agent never had it - its sessions threshold colours in hand-written OpenCV and lose the small or shadowed
objects. GPU work is serialised by one lock; a frame call takes a fraction of a second, a 50-100 frame track a few.

    ./venv/bin/python scripts/sam3_server.py --port 8790          # on the box, quantiphy venv (transformers 5.14)
    curl -s localhost:8790/health

Remote mode (35_2, 2026-10-23: the Track A Claude Code sessions run on the Mac, SAM 3 on the GH200 behind an ssh
tunnel): a request that names `video_id` (+ `split` test / val) instead of `video` / `ws` is answered from this
machine's copy of the same file (checked against the client's frame count and size), in a scratch folder, and the
files it writes (masks, overlay, track CSV) come back base64-encoded under `files` for scripts/sam3kit.py to write
into the session's own folder.
"""
import argparse
import base64
import json
import os
import re
import shutil
import sys
import tempfile
import threading
import time
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s18_common as C  # noqa: E402  (frame decoding)

LOCK = threading.Lock()
STATE = {}
COLORS = [(0, 0, 255), (0, 200, 0), (255, 0, 0), (0, 200, 255), (255, 0, 255), (255, 255, 0), (0, 128, 255),
          (128, 0, 255)]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")[:40] or "obj"


def load(args):
    import torch
    from transformers import Sam3Model, Sam3Processor

    import run_18_1_tracks as T

    tok = os.environ.get("HF_TOKEN")
    dev = torch.device(args.device or ("cuda" if torch.cuda.is_available() else "cpu"))
    t0 = time.time()
    STATE["img_model"] = Sam3Model.from_pretrained(args.sam3, token=tok).to(dev).eval()
    STATE["img_proc"] = Sam3Processor.from_pretrained(args.sam3, token=tok)
    va = argparse.Namespace(device=args.device, fp32=False, score=args.score, new_det_thresh=None, max_instances=8,
                            dedupe_iou=0.85, max_frames=0, post_max_edge=0, process_on_device=False,
                            hotstart_delay=None, hotstart_unmatch=None, sam3=args.sam3, threads=0, fps=args.track_fps)
    STATE["video"] = T.load_model(va)
    STATE["video_args"] = va
    STATE["T"] = T
    STATE["dev"] = dev
    STATE["score"] = args.score
    STATE["max_track_frames"] = args.max_track_frames
    print(f"sam3 server: {args.sam3} on {dev} in {time.time() - t0:.0f}s", flush=True)


def frame_of(video, i=None, t=None):
    props = STATE["T"].video_props(video)
    fps = props["fps"] or 24.0
    n = props["T"]
    if i is None:
        i = int(round(float(t or 0) * fps))
    i = max(0, min(int(i), n - 1))
    frames, fidxs, _, _ = C.read_frames(video, [i])
    if not frames:
        raise ValueError(f"cannot decode frame {i}")
    return frames[0], fidxs[0], fps, n, props


def mask_geometry(m):
    """Pixel extents of one boolean mask: principal-axis length / width, horizontal / vertical extents, centroid."""
    ys, xs = np.nonzero(m)
    if xs.size < 3:
        return None
    P = np.c_[xs, ys].astype(float)
    mu = P.mean(0)
    ev, evec = np.linalg.eigh(np.cov((P - mu).T))
    ax = evec[:, 1]
    s = (P - mu) @ ax
    q = (P - mu) @ evec[:, 0]
    ang = float(np.degrees(np.arctan2(-ax[1], ax[0]))) % 180.0  # image y down -> angle counter-clockwise from +x
    return dict(centroid=[round(float(mu[0]), 1), round(float(mu[1]), 1)], area_px=int(xs.size),
                length_px=round(float(s.max() - s.min() + 1), 1), width_px=round(float(q.max() - q.min() + 1), 1),
                axis_deg=round(ang, 1), horiz_px=int(xs.max() - xs.min() + 1), vert_px=int(ys.max() - ys.min() + 1))


def segment(req):
    import torch
    from PIL import Image

    video, ws = req["video"], Path(req["ws"])
    phrase = str(req["phrase"]).strip()
    rgb, fi, fps, n, props = frame_of(video, req.get("i"), req.get("t"))
    H, W = rgb.shape[:2]
    proc, model = STATE["img_proc"], STATE["img_model"]
    kw = dict(images=Image.fromarray(rgb), return_tensors="pt")
    if req.get("box"):
        kw.update(input_boxes=[[[float(x) for x in req["box"]]]], input_boxes_labels=[[1]])
        if phrase:
            kw["text"] = phrase
    else:
        kw["text"] = phrase
    inputs = proc(**kw).to(STATE["dev"])
    with LOCK, torch.no_grad():
        out = model(**inputs)
    res = proc.post_process_instance_segmentation(out, threshold=float(req.get("threshold") or STATE["score"]),
                                                  mask_threshold=0.5, target_sizes=[[H, W]])[0]
    order = np.argsort(-res["scores"].float().cpu().numpy())[:int(req.get("max_instances") or 6)]
    (ws / "masks").mkdir(exist_ok=True)
    (ws / "frames").mkdir(exist_ok=True)
    ov = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    inst = []
    for k, j in enumerate(order):
        m = res["masks"][int(j)].cpu().numpy().astype(bool)
        g = mask_geometry(m)
        if g is None:
            continue
        b = [round(float(x), 1) for x in res["boxes"][int(j)].tolist()]
        name = f"masks/{slug(phrase or 'box')}_f{fi}_k{k}.png"
        cv2.imwrite(str(ws / name), m.astype(np.uint8) * 255)
        border = bool(m[0].any() or m[-1].any() or m[:, 0].any() or m[:, -1].any())
        inst.append(dict(k=k, score=round(float(res["scores"][int(j)]), 3), box=b, touches_border=border, mask=name, **g))
        col = COLORS[k % len(COLORS)]
        cnts, _ = cv2.findContours(m.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(ov, cnts, -1, col, max(1, W // 640))
        x, y = int(b[0]), max(12, int(b[1]) - 4)
        cv2.putText(ov, str(k), (x, y), cv2.FONT_HERSHEY_SIMPLEX, max(0.6, W / 1600), col, max(1, W // 800), cv2.LINE_AA)
    tag = int(req["tag"]) if req.get("tag") is not None else len(list((ws / "frames").glob("seg_*.jpg")))
    ov_name = f"frames/seg_{tag:02d}_f{fi}.jpg"
    cv2.imwrite(str(ws / ov_name), ov, [cv2.IMWRITE_JPEG_QUALITY, 90])
    return {"meta": {"phrase": phrase, "frame": fi, "t_file": round(fi / fps, 4), "file_fps": fps, "frames": n,
                     "size": [W, H], "instances": inst, "overlay": ov_name,
                     "note": "pixel numbers are at full resolution; k numbers the outlines in the overlay"},
            "image": ov_name}


def track(req):
    T = STATE["T"]
    video, ws = req["video"], Path(req["ws"])
    phrase = str(req["phrase"]).strip()
    model, proc, device, dtype = STATE["video"]
    va = argparse.Namespace(**vars(STATE["video_args"]))
    props = T.video_props(video)
    fps, n = props["fps"] or 24.0, props["T"]
    every = max(1, int(req.get("every") or 1), int(np.ceil(n / STATE["max_track_frames"])))
    va.fps = fps / every
    anchor = None
    if req.get("box") and req.get("i") is not None:
        anchor = {"fidx": int(req["i"]), "box": [float(x) for x in req["box"]]}
    meta = {"video_id": Path(video).stem, "phrases": [phrase], "anchors": {phrase: anchor} if anchor else {},
            "ref_anchor": None, "native_fps": fps, "T": n}
    with LOCK:
        tracks, info = T.track_video(model, proc, device, dtype, video, meta, va)
    if not tracks:
        return {"meta": {"phrase": phrase, "instances": 0, "note": "SAM 3 found no instance of this phrase; try "
                         "another wording or segment with a box"}}
    if anchor:
        tracks.sort(key=lambda t: -(t["anchor_iou"] or 0))
    k = int(req.get("k") or 0) if not anchor else 0
    k = min(k, len(tracks) - 1)
    chosen = tracks[k]
    (ws / "tracks").mkdir(exist_ok=True)
    name = f"tracks/{slug(phrase)}_{k}.csv"
    rows = [f for f in chosen["frames"] if f[-1]]
    with open(ws / name, "w") as fh:
        fh.write("frame,t_file,cx,cy,x0,y0,x1,y1,area,touches_border\n")
        W, H = info["W"], info["H"]
        for f in rows:
            border = int(f[4] <= 1 or f[5] <= 1 or f[6] >= W - 2 or f[7] >= H - 2)
            fh.write(",".join(str(x) for x in f[:9]) + f",{border}\n")
    fr = np.array([[f[0], f[2], f[3]] for f in rows], float)
    summ = {}
    if len(fr) >= 3:
        tt = fr[:, 0] / fps
        vx, vy = np.polyfit(tt, fr[:, 1], 1)[0], np.polyfit(tt, fr[:, 2], 1)[0]
        summ = dict(n=len(fr), t_span=[round(tt[0], 3), round(tt[-1], 3)],
                    net_disp_px=round(float(np.hypot(*(fr[-1, 1:] - fr[0, 1:]))), 1),
                    linear_speed_px_s=round(float(np.hypot(vx, vy)), 2))
        if len(fr) >= 5:
            cx2, cy2 = np.polyfit(tt, fr[:, 1], 2), np.polyfit(tt, fr[:, 2], 2)
            res = np.sqrt(np.mean((np.polyval(cx2, tt) - fr[:, 1]) ** 2 + (np.polyval(cy2, tt) - fr[:, 2]) ** 2))
            summ.update(quad_accel_px_s2=[round(2 * cx2[0], 2), round(2 * cy2[0], 2)], quad_rms_px=round(float(res), 2))
    cands = [dict(k=j, sam_score=t["sam_score"], n_valid=t["summary"]["n_valid"], anchor_iou=t.get("anchor_iou"),
                  mean_speed_px_s=t["summary"].get("mean_speed_px_s")) for j, t in enumerate(tracks)]
    # overlay: up to six frames of the chosen track, box and centre path on the middle frame
    pick = [rows[int(x)] for x in np.linspace(0, len(rows) - 1, min(6, len(rows)))]
    mid, _, _, _, _ = frame_of(video, i=pick[len(pick) // 2][0])
    ov = cv2.cvtColor(mid, cv2.COLOR_RGB2BGR)
    for f in rows:
        cv2.circle(ov, (int(f[2]), int(f[3])), max(2, info["W"] // 600), (0, 255, 255), -1)
    for f in pick:
        cv2.rectangle(ov, (int(f[4]), int(f[5])), (int(f[6]), int(f[7])), (0, 0, 255), max(1, info["W"] // 900))
    tag = (int(req["tag"]) if req.get("tag") is not None
           else len(list((ws / "frames").glob("track_*.jpg"))) if (ws / "frames").exists() else 0)
    (ws / "frames").mkdir(exist_ok=True)
    ov_name = f"frames/track_{tag:02d}_{slug(phrase)}.jpg"
    cv2.imwrite(str(ws / ov_name), ov, [cv2.IMWRITE_JPEG_QUALITY, 88])
    return {"meta": {"phrase": phrase, "chosen_k": k, "file": name, "file_fps": fps, "every_frame": every,
                     "summary": summ, "candidates": cands, "overlay": ov_name,
                     "note": "boxes and centres in full-resolution pixels per frame; t_file = frame / file fps (convert "
                             "with question_fps as the method says); touches_border = 1 means the visible-box centre "
                             "is not the object's centre"}, "image": ov_name}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._send(200, {"ok": "img_model" in STATE})

    def do_POST(self):
        tmp = None
        try:
            req = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
            fn = {"/segment": segment, "/track": track}.get(self.path)
            if fn is None:
                return self._send(404, {"error": "unknown endpoint"})
            if "video_id" in req:  # remote mode: this machine's copy of the video, files returned inline
                req["video"] = remote_video(req)
                tmp = tempfile.mkdtemp(prefix="sam3_ws_")
                req["ws"] = tmp
            t0 = time.time()
            out = fn(req)
            out["meta"]["server_s"] = round(time.time() - t0, 2)
            if tmp:
                out["files"] = {str(p.relative_to(tmp)): base64.b64encode(p.read_bytes()).decode()
                                for p in Path(tmp).rglob("*") if p.is_file()}
            self._send(200, out)
        except Exception as exc:  # noqa: BLE001
            self._send(400, {"error": str(exc)[:800], "trace": traceback.format_exc()[-1200:]})
        finally:
            if tmp:
                shutil.rmtree(tmp, ignore_errors=True)


ROOT = Path(__file__).resolve().parents[1]
SPLIT_DIRS = {"test": ROOT / "data" / "test", "val": ROOT / "data" / "validation" / "validation_videos"}


def remote_video(req):
    """The server's copy of the client's video: same file name in data/test (or the validation folder, whose names
    can carry a leading space), and the same frame count and size, or the call is refused."""
    vid = re.sub(r"[^A-Za-z0-9_]", "", str(req["video_id"]))
    base = SPLIT_DIRS[req.get("split", "test")]
    path = next((p for p in (base / f"{vid}.mp4", base / f" {vid}.mp4") if p.exists()), None)
    if path is None:
        raise ValueError(f"no {vid}.mp4 in {req.get('split', 'test')} on the SAM 3 server")
    props = STATE["T"].video_props(str(path))
    want = req.get("check") or {}
    got = {"frames": props["T"], "width": props["W"], "height": props["H"]}
    if any(k in want and int(want[k]) != got[k] for k in got):
        raise ValueError(f"server copy of {vid} differs from the client's ({got} vs {want})")
    return str(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8790)
    ap.add_argument("--sam3", default="facebook/sam3")
    ap.add_argument("--score", type=float, default=0.3)
    ap.add_argument("--track-fps", type=float, default=30.0)
    ap.add_argument("--max-track-frames", type=int, default=160)
    ap.add_argument("--device", default=None, help="cuda / mps / cpu (default: cuda if present, else cpu)")
    args = ap.parse_args()
    load(args)
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"listening on 127.0.0.1:{args.port}", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()
