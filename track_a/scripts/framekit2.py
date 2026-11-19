"""Frame viewer for the blind per-clip measurement agent (Series 26 full run): writes PNGs the agent then looks at.

Same commands and output as framekit.py, but frames are decoded lazily - only the frames a command needs are kept in
memory - so a dozen agents can view 4K clips side by side on one machine.

    python framekit2.py info  VIDEO
    python framekit2.py sheet VIDEO --n 16 --out frames/sheet.png
    python framekit2.py frame VIDEO (--t SECONDS | --i INDEX) [--crop X0 Y0 X1 Y1] [--scale S] [--grid STEP] --out PNG

Coordinates are always original full-frame pixels; a crop is labelled with its offset so pixel readings stay in
the original frame. --grid draws labelled lines every STEP original pixels.
"""
import argparse
import json
import math
from pathlib import Path

import av
import cv2
import numpy as np


def grab(video, wanted):
    wanted = set(int(i) for i in wanted)
    out = {}
    with av.open(str(video)) as c:
        s = c.streams.video[0]
        for i, f in enumerate(c.decode(s)):
            if i in wanted:
                out[i] = f.to_ndarray(format="bgr24")
            if i >= max(wanted):
                break
    return out


def count_frames(video):
    with av.open(str(video)) as c:
        s = c.streams.video[0]
        fps = float(s.average_rate)
        n = 0
        h = w = None
        for f in c.decode(s):
            if n == 0:
                h, w = f.height, f.width
            n += 1
    return n, fps, w, h


def label(img, text, org=(6, 22)):
    cv2.putText(img, text, org, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 4, cv2.LINE_AA)
    cv2.putText(img, text, org, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)


def cmd_info(a):
    n, fps, w, h = count_frames(a.video)
    print(json.dumps({"frames": n, "fps": round(fps, 4), "duration_s": round(n / fps, 4),
                      "width": w, "height": h, "time_of_frame_i": "i / fps (frame 0 at t = 0)"}))


def cmd_sheet(a):
    total, fps, w, h = count_frames(a.video)
    n = min(a.n, total)
    idx = np.linspace(0, total - 1, n).round().astype(int)
    frames = grab(a.video, idx)
    cols = math.ceil(math.sqrt(n))
    tw = 480
    th = int(h * tw / w)
    sheet = np.zeros((th * math.ceil(n / cols), tw * cols, 3), np.uint8)
    for k, i in enumerate(idx):
        tile = cv2.resize(frames[int(i)], (tw, th))
        label(tile, f"i={i} t={i / fps:.3f}s")
        r, c = divmod(k, cols)
        sheet[r * th:(r + 1) * th, c * tw:(c + 1) * tw] = tile
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(a.out, sheet)
    print(json.dumps({"out": a.out, "frames": idx.tolist(), "fps": round(fps, 4)}))


def cmd_frame(a):
    total, fps, w, h = count_frames(a.video)
    i = a.i if a.i is not None else int(round(a.t * fps))
    i = max(0, min(total - 1, i))
    img = grab(a.video, [i])[i].copy()
    x0, y0 = 0, 0
    if a.crop:
        x0, y0, x1, y1 = (int(v) for v in a.crop)
        img = img[y0:y1, x0:x1].copy()
    if a.grid:
        hh, ww = img.shape[:2]
        for gx in range((x0 // a.grid + 1) * a.grid, x0 + ww, a.grid):
            cv2.line(img, (gx - x0, 0), (gx - x0, hh), (0, 255, 255), 1)
            label(img, str(gx), (gx - x0 + 2, 14))
        for gy in range((y0 // a.grid + 1) * a.grid, y0 + hh, a.grid):
            cv2.line(img, (0, gy - y0), (ww, gy - y0), (0, 255, 255), 1)
            label(img, str(gy), (2, gy - y0 - 3))
    if a.scale and a.scale != 1:
        img = cv2.resize(img, None, fx=a.scale, fy=a.scale, interpolation=cv2.INTER_CUBIC)
    label(img, f"i={i} t={i / fps:.3f}s offset=({x0},{y0})", (6, img.shape[0] - 8))
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(a.out, img)
    print(json.dumps({"out": a.out, "frame": i, "t": round(i / fps, 4), "crop_offset": [x0, y0], "scale": a.scale}))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("info"); p.add_argument("video"); p.set_defaults(fn=cmd_info)
    p = sub.add_parser("sheet"); p.add_argument("video"); p.add_argument("--n", type=int, default=16)
    p.add_argument("--out", required=True); p.set_defaults(fn=cmd_sheet)
    p = sub.add_parser("frame"); p.add_argument("video")
    g = p.add_mutually_exclusive_group(required=True); g.add_argument("--t", type=float); g.add_argument("--i", type=int)
    p.add_argument("--crop", type=float, nargs=4); p.add_argument("--scale", type=float, default=1.0)
    p.add_argument("--grid", type=int); p.add_argument("--out", required=True); p.set_defaults(fn=cmd_frame)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
