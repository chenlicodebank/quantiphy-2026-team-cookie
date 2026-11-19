"""Series 27 (2026-10-21, session 6e6e97e4): per-question answers for a LIST of question ids with the 26_30 harness.

cc_agent_scene.py answers whole videos (every question of a claimed video) or re-runs ids inside an existing run's out
dir. This wrapper answers only the listed ids, in a fresh out dir, with the same two phases and the same prompts:

- Phase 1 (question-blind scene record per video) is reused when an earlier run already holds one for that video
  (`--scene-from`, first match wins; a scene record depends on no question), else run here.
- Phase 2: one fresh session per listed question, as cc_agent_scene.phase2 (same workspace layout, prompt, audit,
  attempt history, streams). `--model-p2` / `--effort-p2` / `--real-scale` / `--size-names` pass through.

Question text, prior, depth_info, video_type, inference_type and question_fps come from the CURRENT dataset rows
(`data/test/test_dataset_current_20261021.json`, the repo state of 2026-10-09; CLAUDE.md "Re-asks read the current
dataset rows"), not from the older blind packs.

    python scripts/cc_scene_ids.py --ids-file results/s27_valfam/ids.csv --out results/s27_valfam --account b \\
        --guard results/s27_valfam/guard_b.json --scene-from results/s26_scene_val,results/s26_scene_val_lean
"""
import argparse
import json
import shutil
import subprocess
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import cc_agent_run as C
import cc_agent_scene as S

ROOT = S.ROOT
CURRENT = ROOT / "data/test/test_dataset_current_20261021.json"
# --lab-geometry (27_5, 2026-10-21): the lab label process (paper App. C: a ruler for sizes; depths read by hand off the
# ToF depth map at a clicked pixel) means a stated depth is a surface reading that can be wrong, and the #205 zero map
# puts D3 lab sizes at .816 against ~.95 on the simple props (balls, boards): the loss sits in boxes, books, jars, bins
# and furniture seen obliquely. Generic dataset knowledge only - no clip's value. Inserted before "Method:".
LAB_GEOMETRY = """Lab geometry (captured videos). The reference sizes were measured on the real objects with a ruler, and the depths
in depth_info were read by hand off the camera's time-of-flight depth map at a pixel clicked on the object (the
visible surface near its centre); a stated depth can be wrong, for instance an object stated nearer than another one
it visibly stands behind. So before you rely on a depth:
- Check it against the scene: occlusion order, where the object stands on the floor or table relative to objects whose
  depths are given, and the apparent size of any object whose real size you know (a ball of a stated diameter).
- Use the support plane: the floor (or the table top) is flat. Back-project the contact points of two or three objects
  resting on it whose depths are given, fit the plane (camera height and tilt), and check the given depths against it.
  An object resting on the plane can then be located in 3D from its contact point alone.
- If the asked object's stated depth disagrees with that evidence by more than about 10 pct, use the geometric estimate
  and say so in notes.md.
For box-like, flat or elongated objects (books, boxes, bins, bags, boards, tables, pens), measure each asked edge in 3D:
back-project both ends of the edge (on the support plane, or at the object's depth) and take their distance, instead of
one pixel extent at one depth - an edge that runs away from the camera is foreshortened, and an upright edge seen from
above is shortened. Length is the longest horizontal edge, width the shorter horizontal edge, height the vertical one.

"""
# --lab-physics (27_12, 2026-10-22): lab footage is real, so a ball in free flight follows gravity exactly, while our
# pixel-and-depth derivatives on 24 fps clips are noisy and read low (validation captured_0027s: a ball dropped at t = 0
# carries the label 2.02 m/s at 0.2 s, about g x 0.2, against our measured 1.57). Generic physics only - no clip's value.
LAB_PHYSICS = """Lab motion (captured videos). These are real recordings, so physics holds exactly: an object in free flight (dropped,
thrown, bouncing between contacts) accelerates at g = 9.8 m/s^2 straight down, and a ball rolling down a straight
incline accelerates uniformly. Frame-to-frame derivatives of clicked or tracked positions at 24 fps are noisy, so for
any speed, acceleration or displacement of such an object:
- Find the motion segment that contains the asked time (release, contacts and bounces split segments; a held object is
  at rest until it is released - find the release frame).
- Fit the segment in 3D with a physics model: for free flight a parabola with the vertical acceleration fixed at
  9.8 m/s^2 (horizontal velocity constant); for rolling on an incline a constant acceleration along the incline. Use
  the 3D positions from the image and the depths, and let the fit determine the release time and initial velocity.
- Report the model's value at the asked time: the speed is the norm of the 3D velocity, the acceleration the norm of
  the acceleration vector. Check the fit's residuals; if the model does not fit (pushed, pulled, hand-held), say so and
  measure directly instead.

"""


def current_rows():
    rows = json.loads(CURRENT.read_text())
    return {r["row_idx"] + 1: r for r in rows}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", help="comma list of question ids")
    ap.add_argument("--ids-file", help="CSV with an id column")
    ap.add_argument("--out", required=True)
    ap.add_argument("--account", required=True, choices=sorted(S.ACCOUNTS))
    ap.add_argument("--guard", required=True, help="guard JSON (max_5h, max_7d, usd_per_pct, safety, cost_p1, cost_p2)")
    ap.add_argument("--scene-from", default="", help="comma list of earlier run dirs whose videos/<video>/scene to reuse")
    ap.add_argument("--workdir", type=Path, default=Path("/private/tmp/qp_blind/s27_ids"))
    ap.add_argument("--packs", default="results/s26_test_prepared/blind_packs.json")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--model-p2", default="claude-opus-5-5")
    ap.add_argument("--effort-p2", default="high")
    ap.add_argument("--max-turns", type=int, default=300)
    ap.add_argument("--max-turns-p2", type=int, default=150)
    ap.add_argument("--timeout-p1", type=int, default=90)
    ap.add_argument("--timeout-p2", type=int, default=45)
    ap.add_argument("--workers", type=int, default=4, help="videos in flight")
    ap.add_argument("--q-workers", type=int, default=4, help="phase-2 sessions in flight per video")
    ap.add_argument("--max-sessions", type=int, default=8, help="claude processes in flight overall")
    ap.add_argument("--lean", action="store_true")
    ap.add_argument("--size-names", action="store_true")
    ap.add_argument("--real-scale", action="store_true")
    ap.add_argument("--lab-geometry", action="store_true", help="insert LAB_GEOMETRY before 'Method:' (lab rows)")
    ap.add_argument("--lab-physics", action="store_true", help="insert LAB_PHYSICS before 'Method:' (lab motion rows)")
    ap.add_argument("--cache-ttl", choices=("5m", "1h"))
    ap.add_argument("--keep-workspace", action="store_true")
    ap.add_argument("--max-5h-util", type=float, default=0.0)
    ap.add_argument("--stop-name")
    ap.add_argument("--sam3-url", default="", help="SAM 3 helper server (as cc_agent_scene.py; 39_4)")
    ap.add_argument("--sam3-required", action="store_true", help="the SAM 3 mask as the required second route (35_2)")
    ap.add_argument("--plan-only", action="store_true")
    a = ap.parse_args()
    extra = (LAB_GEOMETRY if a.lab_geometry else "") + (LAB_PHYSICS if a.lab_physics else "")
    if extra:  # phase2 reads these module globals at call time
        for name in ("ANSWER_PROMPT", "REAL_SCALE_PROMPT"):
            p = getattr(S, name)
            assert p.count("Method:\n") == 1
            setattr(S, name, p.replace("Method:\n", extra + "Method:\n", 1))
    a.stop_name = a.stop_name or f"STOP_{a.account}"
    a.commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                              text=True).stdout.strip()
    a.slots = threading.BoundedSemaphore(a.max_sessions)
    g = json.loads(Path(a.guard).read_text())
    a.cost1 = S.P1_COST | {int(k): v for k, v in g.get("cost_p1", {}).items()}
    a.cost2 = S.P2_COST | {int(k): v for k, v in g.get("cost_p2", {}).items()}

    ids = []
    if a.ids:
        ids += [int(x) for x in a.ids.split(",") if x.strip()]
    if a.ids_file:
        import csv
        ids += [int(r["id"]) for r in csv.DictReader(open(a.ids_file))]
    ids = list(dict.fromkeys(ids))

    packs = {p["video_id"]: p for p in json.loads((ROOT / a.packs).read_text())["videos"]}
    events = C.build_events(packs, {}, val=False, per_video=True) + C.build_events(packs, {}, val=True, per_video=True)
    cur = current_rows()
    byid = {}
    for ev in events:
        for r in ev["rows"]:
            c = cur[int(r["id"])]
            if c["video_id"].strip() != r["video_id"].strip():
                raise SystemExit(f"id {r['id']}: packs video {r['video_id']} != current {c['video_id']}")
            # every row of the event, so phase 1's 2D / 3D flag (rows[0]["video_type"]) is current too
            r.update({"question": c["question"], "ground_truth_prior": c["prior"] or "", "depth_info": c["depth_info"],
                      "video_type": c["video_type"], "inference_type": c["inference_type"], "fps": c["fps"]})
            byid[int(r["id"])] = (ev, r)
    missing = [i for i in ids if i not in byid]
    if missing:
        raise SystemExit(f"ids not in the packs: {missing}")
    jobs = {}
    for i in ids:
        ev, r = byid[i]
        jobs.setdefault(ev["primary"], (ev, []))[1].append(r)

    out = a.out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    plan = {"settings": {k: str(v) for k, v in vars(a).items() if k not in ("slots", "cost1", "cost2")},
            "videos": [{"video": v, "tier": ev["tier"], "ids": [int(r["id"]) for r in rows]}
                       for v, (ev, rows) in jobs.items()]}
    (out / f"plan_{a.account}.json").write_text(json.dumps(plan, indent=1) + "\n")
    print(f"{len(jobs)} videos, {len(ids)} questions", flush=True)
    if a.plan_only:
        return
    tools = a.workdir / "tools"
    tools.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(C.HERE / "framekit2.py", tools / "framekit2.py")
    if a.sam3_url:
        shutil.copyfile(C.HERE / "sam3kit.py", tools / "sam3kit.py")
        (tools / "sam3.json").write_text(json.dumps({"url": a.sam3_url, "split": "test"}) + "\n")
    sources = [ROOT / s for s in a.scene_from.split(",") if s.strip()]

    def one_video(item):
        vid, (ev, rows) = item
        keep = out / "videos" / vid / "scene"
        if not (keep / "scene.json").exists():
            for s in sources:
                src = s / "videos" / vid / "scene"
                if (src / "scene.json").exists():
                    shutil.rmtree(keep, ignore_errors=True)
                    shutil.copytree(src, keep)
                    (out / "videos" / vid / "scene_from.txt").write_text(str(src.relative_to(ROOT)) + "\n")
                    print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] {vid}: scene record reused from {src}",
                          flush=True)
                    break
        if not (keep / "scene.json").exists() and not S.safe(S.phase1, ev, a, out):
            return
        with ThreadPoolExecutor(max_workers=a.q_workers) as ex:
            parts = list(ex.map(lambda r: S.safe(S.phase2, ev, [r], a, out), rows))
        answers = {k: v for p in parts for k, v in p.items()}
        if answers:
            cdir = out / "clips" / vid
            cdir.mkdir(parents=True, exist_ok=True)
            f = cdir / "answers.json"
            with S.LOCK:
                cur_ans = json.loads(f.read_text()) if f.exists() else {}
                cur_ans.update(answers)
                f.write_text(json.dumps(dict(sorted(cur_ans.items(), key=lambda kv: int(kv[0]))), indent=1) + "\n")
        if not a.keep_workspace:
            S.wipe(a.workdir / vid)

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        list(ex.map(one_video, jobs.items()))
    got = {}
    for f in (out / "clips").glob("*/answers.json"):
        got.update(json.loads(f.read_text()))
    print(f"done: {sum(str(i) in got for i in ids)} of {len(ids)} questions answered", flush=True)


if __name__ == "__main__":
    main()
