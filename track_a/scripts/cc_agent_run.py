"""Series 26 full test run: one blind Claude Code agent per video, on login B (2026-10-17).

Successor of cc_agent_pilot.py (validation pilot and test waves 1 / 1b). What changed and why:
- Account: login B instead of login A; `--safe-mode`
  (no CLAUDE.md, memory, skills, hooks or MCP) and `--no-session-persistence` (no transcripts in the login's
  projects dir), web tools and sub-agents refused, Bash allow-listed to the one Python interpreter.
- Inputs: every question carries its OWN prior and depth_info (the pilot sent the first row's to all of them; 6 test
  videos state different priors on different rows), and all questions of the footage are listed together: the
  `_segmented` twin and the lab `s` / `x` renders are the same footage with the background replaced, so one agent
  sees the event once, answers every one of its rows, and gets the variant videos as clean-mask aids. That is still
  one Claude Code session per video: a variant is the same video, not a second scene.
- Evidence: the priors other camera views of the scene family state (Series 24 families.json) are listed as world
  facts to cross-check against, never as camera facts.
- The reference-answer conventions in the prompt follow the paper's appendix C (time -> frame rounding, backward
  differences in Blender, forward differences in lab and internet, single planar scale on internet clips, origins).
- Answers land per event as soon as an agent finishes (`clips/<event>/answers.json` + `run.json`), so a partial run
  can be merged at any time; a rerun skips events that already have answers; `STOP` in the out dir drains the pool.

    python scripts/cc_agent_run.py --out results/s26_ccagent_full --workers 14
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[0]

PY = os.environ.get("QP_PYTHON", sys.executable)
CLAUDE = str(Path.home() / ".npm-global/bin/claude")
CONFIG_DIR = str(Path.home() / ".claude-b")  # login B
# 2026-10-18 (user): every run names its account explicitly (our run rules, "Inference accounts and run practice").
ACCOUNTS = {"a": str(Path.home() / ".claude-a"), "b": CONFIG_DIR}
VAL_STEMS = {"captured_0013", "captured_0021", "captured_0027", "captured_0034a", "captured_0041", "captured_0061",
             "internet_0001", "internet_0004", "internet_0005", "internet_0013", "internet_0019", "internet_0027",
             "simulation_0009", "simulation_0015", "simulation_0034", "simulation_0060", "simulation_0089",
             "simulation_0098", "simulation_0163", "simulation_0170", "simulation_0171", "simulation_0193",
             "simulation_0196", "simulation_0300"}  # validation families: not scored on the v3 board
LOCK = threading.Lock()

PROMPT = """You are measuring physical quantities from one short video for a benchmark. Work only inside this folder:
{ws}

Files here:
- inputs.json: the video's frame rate, size and source, and EVERY question about this footage. Each question has
  its own id, the video file it belongs to, its given prior and its depth_info (camera distances).
- {primary}.mp4: the video at original resolution.{variants}
Python with numpy, scipy, opencv (cv2), PIL and av: {py}
Viewer helper (writes PNG files that you then look at with the Read tool):
  {py} {tools}/framekit2.py info {primary}.mp4
  {py} {tools}/framekit2.py sheet {primary}.mp4 --n 16 --out frames/sheet.png
  {py} {tools}/framekit2.py frame {primary}.mp4 --t 1.5 [--crop X0 Y0 X1 Y1] [--scale 3] [--grid 50] --out frames/f.png
Write your own Python scripts for every measurement and keep them in this folder.

Rules: do not read, list or search any path outside this folder (running the Python interpreter and the helper is
fine); no web access; no other data. The only shell command you may run is the Python interpreter above, called by
its full path (for example `{py} measure.py`); other commands are refused. Memory is shared with other jobs: decode
frames inside your scripts as you need them, never hold a whole high-resolution video in memory, and keep scratch
files small (no dumps of whole videos).

Scoring: each answer is scored by its relative error - under 5 pct full credit, 10 pct about 0.9, 20 pct about 0.8,
50 pct about 0.4, 100 pct or more zero. A careful measurement 3 pct off is worth far more than a quick estimate, so
take the time to measure well.

Use all the evidence. Read every question before measuring: together they name the objects, the events (release,
bounce, impact, start and end of motion) and the times that matter. Every prior and every depth_info value given in
ANY question of this footage is an exact fact about this footage, usable for every question.{family}

How the reference answers were made (from the benchmark paper):
- The given prior is exact. Rendered scenes are not at real-world scale: the priors and depth_info set the scale;
  real-world knowledge is only a sanity check.
- Time: t = 0 is the first frame; time t means frame round(t x fps). Use the fps in inputs.json.
- simulation videos (Blender renders; 2D or 3D):
  * Positions are the object's origin in world space: a rigid object's origin (usually its centre), a human's
    pelvis/hip, a vehicle or other rig's root. Distances between objects are between these origins: the full 3D
    distance in 3D videos unless the question says horizontal or vertical; in-plane distance in 2D videos.
  * Speed at time t = |p(i) - p(i-1)| x fps at frame i = round(t x fps) (one-frame backward difference of the
    origin). Acceleration at t = (speed(i) - speed(i-1)) x fps, the change of scalar speed (for a uniformly
    accelerated object simply that constant). Average speed over an interval = mean of the per-frame speeds.
    Displacement between two times = straight-line distance between the two positions.
  * Sizes are the world-space axis-aligned bounding box (length / width / height = its extents). Human height: the
    question says which - rest standing height, or minimum / maximum height while walking; flying animals: minimum
    or maximum wingspan / width during flight.
  * depth_info = 3D Euclidean distance from the camera centre to the object's origin (not to its surface). The
    camera is fixed within a clip; its focal length is unknown and differs between clips (horizontal field of view
    anywhere from about 8 to 100 degrees), so estimate it: e.g. from the given depths plus a known size, or from
    two objects whose depths are given, and check it by reproducing the given values.
  * 2D videos: motion is in a plane facing the camera; one metres-per-pixel scale from the prior's object (its pixel
    size, pixel speed or pixel acceleration), unless clear perspective shows the objects are at different depths.
- segmentation videos are the same footage with the background replaced and have the original's answers.
- captured (lab) videos: real recordings, 24 fps, Orbbec Femto Mega RGB camera with a horizontal field of view of
  80 degrees: focal length = 0.5959 x image width in pixels (763 px at 1280 px width), principal point near the
  image centre, no zoom. depth_info gives the measured camera distance to the object centre at the stated times.
  Reference sizes were measured on the real objects with a ruler. Reference positions are object centres clicked in
  the main camera and back-projected with the measured depth; velocity = forward difference of those 3D centres over
  adjacent frames (smoothed over at least 5 frames), acceleration = second difference. The given acceleration
  prior of a falling or rolling ball can be gravity or slope physics; still measure.
- internet videos: real footage. The annotators measured in pixels: an object's pixel length along the main motion
  direction (e.g. bumper to bumper for a car) and a reference point's pixel position frame by frame, velocity as the
  forward difference and acceleration as the second difference, then converted EVERYTHING with ONE scale factor =
  prior world value / prior pixel value (planar assumption, no perspective correction). Reproduce that convention:
  a single scale from the prior, measured the same way. Check for camera motion before measuring motion; if the
  camera pans, measure against the background.

Method:
1. Get the video info, make a contact sheet, and view frames at every time a question mentions. Identify every object
   named in the questions and the priors. Look at zoomed crops (--scale 2-4) with --grid to read coordinates.
2. Measure in code rather than by eye: background subtraction or frame differencing for a static camera, colour
   thresholds, contours, template matching, optical flow. Draw masks and points on frames and LOOK at them to
   confirm they hit the right object and its full extent.
3. Scale: 2D -> metres per pixel from the prior; 3D -> pinhole geometry with depth_info, the focal length estimated
   from at least two independent references and checked by reproducing the prior and the other given values.
4. Motion: track the object in every frame around the asked time and follow the conventions above (light smoothing
   is fine; never fit across a bounce, impact or occlusion).
5. Check every answer by a second independent route (another reference, frame window or method) and for physical
   consistency with the other questions; when routes disagree, find out why before answering.
6. Answers are positive numbers in the unit each question asks for.

Finish by writing answers.json as {{"<id>": <number>, ...}} with EVERY question id in inputs.json, and notes.md
(method, key measurements, the second-route check, confidence per answer). Then reply with the JSON object.
"""

# --perq (2026-10-18, organisers' per-question rule of 2026-10-15): one session per video file, no variant videos, no
# scene-family facts, and every answer from the video plus that question's own prior and depth_info only. The
# reference conventions are byte-identical to PROMPT; only the evidence rules and the cross-check step change.
PERQ_RULE = """Answer every question independently (competition rule): each answer may use only the video and THAT question's
own prior and depth_info. Never use another question's prior, depth_info, wording or answer to infer it, and never
adjust an answer to agree with another question's answer. Measuring the video itself once (tracks, masks, the
camera) and reusing those measurements across questions is fine, but each answer's scale and every given fact must
come from its own question's prior and depth_info."""
PERQ_PROMPT = (PROMPT
               .replace("""Use all the evidence. Read every question before measuring: together they name the objects, the events (release,
bounce, impact, start and end of motion) and the times that matter. Every prior and every depth_info value given in
ANY question of this footage is an exact fact about this footage, usable for every question.{family}""", PERQ_RULE)
               .replace("""Identify every object named in the questions and the priors.""",
                        """For each question, identify the object it asks about and the object its own prior names.""")
               .replace("""5. Check every answer by a second independent route (another reference, frame window or method) and for physical
   consistency with the other questions; when routes disagree, find out why before answering.""",
                        """5. Check every answer by a second independent route (another frame window, reference point or method), using only that
   question's own prior and depth_info; when routes disagree, find out why before answering.""")
               .replace("""Displacement between two times = straight-line distance between the two positions.""",
                        """Displacement between two times = straight-line distance between the two positions; total
    distance traveled = path length, the sum of the per-frame displacements (not the net displacement).""")
               .replace("""acceleration = second difference.""",
                        """acceleration = second difference; total
  distance traveled = the sum of the frame-to-frame 3D displacements of the centre (path length)."""))
assert PERQ_PROMPT.count(PERQ_RULE) == 1 and "ANY question" not in PERQ_PROMPT and "other questions" not in PERQ_PROMPT

VARIANT_LINE = """
- {names}: the SAME footage re-published with the background replaced (plain colour or a simple backdrop),
  frame-aligned with {primary}.mp4. Useful for clean masks of the moving objects; static objects may be missing
  from them. Their questions are listed in inputs.json too and have the same true answers as the matching questions
  on {primary}.mp4."""

FAMILY_LINE = """

Other camera views of what is probably the same scene state these world facts (sizes, speeds or accelerations at
the stated times; their camera distances do not apply here). They may refer to a different object or scene, so use
them only as a cross-check of your scale, never instead of measuring:
{lines}"""


def stem(v):
    if v.startswith("captured_"):
        return re.sub(r"^(captured_\d{4}[ab]?)[sxX]$", r"\1", v)
    return v.replace("_segmented", "")


def tier(ev):
    src, cat = ev["source"], ev["category"]
    if src == "lab":
        return 6
    if src == "internet":
        return 2 if cat.startswith("S") else 3
    if cat.endswith("3"):
        return 0 if cat == "S3" else 1
    return 4 if cat == "S2" else 5


def build_events(packs, families, val=False, per_video=False):
    by_stem = {}
    for vid, p in packs.items():
        by_stem.setdefault(vid if per_video else stem(vid), []).append(vid)
    events = []
    for st, vids in by_stem.items():
        if (stem(st) in VAL_STEMS) != val:  # --val: only the validation families (labelled, unscored on the board)
            continue
        vids.sort(key=lambda v: (v != st, v))  # the plain clip first when it exists
        primary = vids[0]
        p = packs[primary]
        rows = [r for v in vids for r in packs[v]["rows"]]
        fam = []
        own = {r["ground_truth_prior"].strip() for r in rows}
        mates = sorted({m for v in vids for m in families.get(v, []) if stem(m) != st},
                       key=lambda m: abs(int(re.findall(r"\d{4}", m)[0]) - int(re.findall(r"\d{4}", primary)[0])))
        for m in ([] if per_video else mates):  # --perq: no other video's priors
            if m not in packs:
                continue
            for r in packs[m]["rows"]:
                line = r["ground_truth_prior"].strip()
                if line in own or re.search(r"9\.8\s*m/s", line) or any(line == f[1] for f in fam):
                    continue
                fam.append((m, line))
        events.append({"event": st, "primary": primary, "videos": vids, "source": p["source"],
                       "category": p["category"], "rows": rows, "family": fam[:12]})
    for ev in events:
        ev["tier"] = tier(ev)
    return events


def order(events, skip_first=()):
    """Round-robin over the non-lab tiers (bigger events first inside a tier), lab last."""
    tiers = {}
    for ev in sorted(events, key=lambda e: (-len(e["rows"]), e["event"])):
        tiers.setdefault(ev["tier"], []).append(ev)
    out = []
    nonlab = [t for t in sorted(tiers) if t != 6]
    while any(tiers.get(t) for t in nonlab):
        for t in nonlab:
            if tiers.get(t):
                out.append(tiers[t].pop(0))
    out += tiers.get(6, [])
    late = [e for e in out if e["event"] in skip_first]
    return [e for e in out if e["event"] not in skip_first] + late


def order_budget(events, skip_first=()):
    """Expected gain per unit of plan usage, measured 2026-10-17 19:45 UTC (the 5 h window, not the clock, binds):
    S2 first (2D sim, then internet: cheap clips, the heaviest per-row weight after S3), then 2D sim D2, 3D sim S3
    and internet D2 in turn, then 3D sim D3 (about 5x the cost of a 2D clip per row-unit gained), lab last."""
    tiers = {}
    for ev in sorted(events, key=lambda e: (-len(e["rows"]), e["event"])):
        tiers.setdefault(ev["tier"], []).append(ev)
    out = tiers.get(4, []) + tiers.get(2, [])
    mid = [5, 0, 3]
    while any(tiers.get(t) for t in mid):
        for t in mid:
            if tiers.get(t):
                out.append(tiers[t].pop(0))
    out += tiers.get(1, []) + tiers.get(6, [])
    late = [e for e in out if e["event"] in skip_first]
    return [e for e in out if e["event"] not in skip_first] + late


def five_hour_util(out):
    """Highest five-hour plan utilisation reported by the newest agent streams (rate_limit_event), or None."""
    import ast
    files = sorted((out / "streams").glob("*.jsonl"), key=lambda f: f.stat().st_mtime)[-6:]
    best = None
    for f in files:
        last = None
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            if '"rate_limit_event"' in line:
                last = line
        if not last:
            continue
        try:
            info = json.loads(last)["rate_limit_info"]
            info = ast.literal_eval(info) if isinstance(info, str) else info
            u = info["unifiedWindows"]["five_hour"]["utilization"]
        except (ValueError, KeyError, TypeError, SyntaxError):
            continue
        best = u if best is None else max(best, u)
    return best


def plan_state(out, extra=()):
    """Newest plan utilisation the agent streams report: five-hour and seven-day fractions and reset times (epoch s).
    Reads the newest 6 streams across this pool's out dir and `extra` out dirs (pools share one plan). A reading whose
    window has already reset is dropped, so the first agent of a fresh window can start."""
    import ast
    now = time.time()
    st = {"5h": None, "5h_reset": None, "7d": None, "7d_reset": None}
    files = [f for d in (out, *extra) for f in (Path(d) / "streams").glob("*.jsonl")]
    files = sorted(files, key=lambda f: f.stat().st_mtime)[-6:]
    for f in files:
        last = None
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            if '"rate_limit_event"' in line:
                last = line
        if not last:
            continue
        try:
            info = json.loads(last)["rate_limit_info"]
            info = ast.literal_eval(info) if isinstance(info, str) else info
            w5, w7 = info["unifiedWindows"]["five_hour"], info["unifiedWindows"]["seven_day"]
        except (ValueError, KeyError, TypeError, SyntaxError):
            continue
        if w5.get("resetsAt", 0) > now and (st["5h"] is None or w5["utilization"] > st["5h"]):
            st["5h"], st["5h_reset"] = w5["utilization"], w5["resetsAt"]
        if w7.get("resetsAt", 0) > now and (st["7d"] is None or w7["utilization"] > st["7d"]):
            st["7d"], st["7d_reset"] = w7["utilization"], w7["resetsAt"]
    return st


TIER_COST = {0: 3.2, 1: 5.7, 2: 0.9, 3: 0.85, 4: 1.25, 5: 1.6, 6: 7.0}  # USD API-equivalent an event, 10-17 means
TIER_WALL = {0: 820, 1: 1380, 2: 190, 3: 190, 4: 300, 5: 380, 6: 1800}  # seconds an event, 10-17 means; lab assumed
ADMIT = threading.Lock()


def inflight(a, tiers):
    """(event, tier, elapsed s) of every agent working now, read from the live workspaces of this pool's workdir and
    the extra workdirs. A workspace with no file written for 20 min is a leftover of a killed run, not an agent."""
    now, res = time.time(), []
    for wd in [a.workdir, *[Path(p) for p in a.extra_workdirs]]:
        if not Path(wd).exists():
            continue
        for ws in Path(wd).iterdir():
            inp = ws / "inputs.json"
            if ws.name == "tools" or not inp.exists():
                continue
            newest = max((f.stat().st_mtime for f in ws.rglob("*") if f.is_file()), default=0)
            if now - newest > 1200:
                continue
            res.append((ws.name, tiers.get(ws.name, 6), now - inp.stat().st_mtime))
    return res


def budget_gate(a, out, ev, tiers):
    """Admission control (user, 2026-10-17 21:10 UTC: up to 0.90 of the five-hour window, and every session that
    starts must finish - a session cut by the limit is not resumed, it is lost). Admit the event only if
        five-hour utilisation now + safety x (remaining cost of every in-flight agent + this event's cost) / (USD a pct)
    stays at or under the guard's limit; otherwise wait (the window resets, or in-flight estimates were too high).
    Guard file (JSON, re-read on every check): max_5h (a number, or [[UTC ISO, limit], ...] - the first entry still in
    the future applies), usd_per_pct, safety, max_7d. At the seven-day limit the pool stops. Call with ADMIT held."""
    from datetime import datetime, timezone
    said = 0.0
    while True:
        if (out / a.stop_name).exists():
            return False
        g = json.loads(Path(a.guard).read_text())
        lim5 = g.get("max_5h", 0.9)
        if isinstance(lim5, list):
            now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            lim5 = next((v for t, v in lim5 if t > now_iso), lim5[-1][1] if lim5 else 0.9)
        st = plan_state(out, a.state_dirs)
        if st["7d"] is not None and st["7d"] >= g.get("max_7d", 0.8):
            (out / a.stop_name).write_text(f"seven-day utilisation {st['7d']} >= {g.get('max_7d', 0.8)} at "
                                           f"{time.strftime('%H:%M:%S', time.gmtime())} UTC\n")
            print(f"weekly stop: seven-day utilisation {st['7d']}", flush=True)
            return False
        cost, wall = TIER_COST | {int(k): v for k, v in g.get("tier_cost", {}).items()}, TIER_WALL
        fl = inflight(a, tiers)
        rem = sum(cost[t] * max(0.3, 1 - el / wall[t]) for _, t, el in fl)
        proj = (st["5h"] or 0.0) + g.get("safety", 1.25) * (rem + cost[ev["tier"]]) / g.get("usd_per_pct", 3.0) / 100
        if proj <= lim5:
            return True
        if time.time() - said > 900:
            print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] wait {ev['event']}: five-hour {st['5h']} + in-flight "
                  f"{len(fl)} (~${rem:.0f}) + this ~${cost[ev['tier']]:.1f} -> {proj:.2f} > {lim5}", flush=True)
            said = time.time()
        ADMIT.release()  # let other workers' agents finish meanwhile
        time.sleep(60)
        ADMIT.acquire()


def setup(ev, ws, tools, perq=False):
    import av
    ws.mkdir(parents=True, exist_ok=True)
    (ws / "frames").mkdir(exist_ok=True)
    meta = {}
    for v in ev["videos"]:
        shutil.copyfile(ROOT / "data/test" / f"{v}.mp4", ws / f"{v}.mp4")
        with av.open(str(ws / f"{v}.mp4")) as c:
            s = c.streams.video[0]
            n = sum(1 for _ in c.decode(s))
            meta[v] = {"fps": round(float(s.average_rate), 6), "frames": n, "width": s.width, "height": s.height}
    p = meta[ev["primary"]]
    src = ev["source"].replace("segmentaion", "segmentation")
    inputs = {"video_source": src, "video_type": ev["rows"][0]["video_type"], "fps": p["fps"], "frames": p["frames"],
              "duration_s": round(p["frames"] / p["fps"], 4), "width": p["width"], "height": p["height"],
              "videos": {f"{v}.mp4": meta[v] for v in ev["videos"]},
              "questions": [{"id": int(r["id"]), "video": f"{r['video_id']}.mp4", "question": r["question"].strip(),
                             "prior": r["ground_truth_prior"].strip(),
                             "depth_info": (r.get("depth_info") or "").strip() or None,
                             "prior_kind_to_question_kind": r["inference_type"]} for r in ev["rows"]]}
    (ws / "inputs.json").write_text(json.dumps(inputs, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    variants = [v for v in ev["videos"] if v != ev["primary"]]
    vline = VARIANT_LINE.format(names=", ".join(f"{v}.mp4" for v in variants), primary=ev["primary"]) if variants else ""
    fline = FAMILY_LINE.format(lines="\n".join(f"  - {line}" for _, line in ev["family"])) if ev["family"] else ""
    return inputs, (PERQ_PROMPT if perq else PROMPT).format(ws=ws, py=PY, tools=tools, primary=ev["primary"],
                                                           variants=vline, family=fline)


def audit(stream_path, ws, tools):
    allowed = (str(ws), str(tools), PY.rsplit("/bin/", 1)[0], "frames/", "./")
    flags, calls = [], 0
    for line in stream_path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        msg = ev.get("message")
        if not isinstance(msg, dict):
            continue
        for item in msg.get("content") if isinstance(msg.get("content"), list) else []:
            if item.get("type") != "tool_use":
                continue
            calls += 1
            text = json.dumps(item.get("input") or {})
            paths = re.findall(r"(/(?:Users|private|tmp|home|var|etc|opt|Volumes)[^\s\"'\\]*)", text)
            bad = [p for p in paths if not p.startswith(allowed)]
            words = [w for w in ("quantiphy_neurips2026", "validation", "ground_truth_posterior")
                     if w in text.lower()]
            if bad or words or item.get("name") in ("WebFetch", "WebSearch", "Task", "Agent"):
                flags.append({"tool": item.get("name"), "paths": bad[:5], "words": words, "input": text[:300]})
    return {"tool_calls": calls, "flags": flags}


def run(ev, a):
    out = ROOT / a.out
    cdir = out / "clips" / ev["event"]
    if (cdir / "answers.json").exists() or (out / a.stop_name).exists():
        return None
    ws = (a.workdir / ev["event"]).resolve()
    if ws.exists():
        if a.skip_existing_ws:  # another pool is working on it
            return None
        shutil.rmtree(ws)
    if a.start_after:
        from datetime import datetime
        t0 = datetime.fromisoformat(a.start_after.replace("Z", "+00:00")).timestamp()
        while time.time() < t0:
            time.sleep(min(300, t0 - time.time()))
    if a.guard:
        with ADMIT:  # one admission at a time, held through setup so the next check sees this workspace
            if not budget_gate(a, out, ev, a.tiers):
                return None
            if (cdir / "answers.json").exists() or (a.skip_existing_ws and ws.exists()):
                return None  # finished or taken by another pool while this worker waited
            tools = (a.workdir / "tools").resolve()
            inputs, prompt = setup(ev, ws, tools, a.perq)
    if a.max_5h_util:
        u = five_hour_util(out)
        if u is not None and u >= a.max_5h_util:
            (out / a.stop_name).write_text(f"five-hour utilisation {u} >= {a.max_5h_util} at "
                                           f"{time.strftime('%H:%M:%S', time.gmtime())} UTC\n")
            print(f"budget stop: five-hour utilisation {u}", flush=True)
            return None
    if not a.guard:
        tools = (a.workdir / "tools").resolve()
        inputs, prompt = setup(ev, ws, tools, a.perq)
    else:
        tools = (a.workdir / "tools").resolve()
    env = os.environ.copy()
    for k in list(env):
        if k.startswith(("CLAUDE_CODE_", "CLAUDECODE", "ANTHROPIC_", "CODEX_")):
            env.pop(k)
    env.update({"CLAUDE_CONFIG_DIR": ACCOUNTS[a.account], "CLAUDE_CODE_SAFE_MODE": "1", "CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1",
                "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1", "CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS": "1"})
    timeout = a.timeout_min_3d if (ev["category"].endswith("3") or ev["source"] == "lab") else a.timeout_min
    cmd = [CLAUDE, "-p", "--verbose", "--output-format", "stream-json", "--safe-mode", "--no-session-persistence",
           "--permission-mode", "dontAsk", "--allowedTools", f"Read,Write,Edit,Glob,Grep,Bash({PY}:*)",
           "--disallowedTools", "WebFetch,WebSearch,Task,Agent", "--model", a.model, "--effort", a.effort,
           "--max-turns", str(a.max_turns)]
    stream = out / "streams" / f"{ev['event']}.jsonl"
    stream.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    with stream.open("w", encoding="utf-8") as f:
        proc = subprocess.Popen(cmd, cwd=ws, env=env, stdin=subprocess.PIPE, stdout=f, stderr=subprocess.STDOUT,
                                text=True)
        try:
            proc.communicate(prompt, timeout=timeout * 60)
            timed_out = False
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.communicate()
            timed_out = True
    wall = time.time() - t0
    result = {}
    for line in stream.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "result":
            result = e
    answers, err = {}, None
    if (ws / "answers.json").exists():
        try:
            raw = json.loads((ws / "answers.json").read_text())
            answers = {int(k): float(v) for k, v in raw.items() if v is not None}
        except (ValueError, TypeError) as exc:
            err = f"answers.json unreadable: {exc}"
    want = [q["id"] for q in inputs["questions"]]
    rec = {"event": ev["event"], "primary": ev["primary"], "videos": ev["videos"], "source": ev["source"],
           "category": ev["category"], "tier": ev["tier"], "wall_s": round(wall), "timed_out": timed_out,
           "answered": sum(1 for i in want if i in answers), "questions": len(want), "error": err,
           "result": {k: result.get(k) for k in ("is_error", "num_turns", "duration_ms", "total_cost_usd", "subtype")},
           "usage": result.get("usage"), "audit": audit(stream, ws, tools), "finished_utc": time.strftime(
               "%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    cdir.mkdir(parents=True, exist_ok=True)
    for name in ("notes.md", "inputs.json"):
        if (ws / name).exists():
            shutil.copyfile(ws / name, cdir / name)
    for py in ws.glob("*.py"):
        if py.stat().st_size < 200_000:
            (cdir / "code").mkdir(exist_ok=True)
            shutil.copyfile(py, cdir / "code" / py.name)
    (cdir / "run.json").write_text(json.dumps(rec, indent=1, default=str) + "\n", encoding="utf-8")
    if answers:  # written last: its presence marks the event done
        (cdir / "answers.json").write_text(json.dumps({str(k): v for k, v in answers.items()}, indent=1) + "\n")
    with LOCK:
        with (out / "progress.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps({k: rec[k] for k in ("event", "category", "source", "tier", "wall_s", "timed_out",
                                                    "answered", "questions", "finished_utc")}
                               | {"cost": rec["result"].get("total_cost_usd"), "turns": rec["result"].get("num_turns"),
                                  "flags": len(rec["audit"]["flags"]), "is_error": rec["result"].get("is_error")})
                    + "\n")
    print(f"[{rec['finished_utc']}] {ev['event']} {ev['category']}/{ev['source']} answered {rec['answered']}/"
          f"{rec['questions']} in {rec['wall_s']}s cost~{rec['result'].get('total_cost_usd')} "
          f"flags {len(rec['audit']['flags'])}", flush=True)
    if not a.keep_workspace:
        shutil.rmtree(ws, ignore_errors=True)
    return rec


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="results/s26_ccagent_full")
    ap.add_argument("--workdir", type=Path, default=Path("/private/tmp/qp_blind/full_20261017"))
    ap.add_argument("--packs", default="results/s26_test_prepared/blind_packs.json")
    ap.add_argument("--families", default="results/fulltest_s24_famprior/families.json")
    ap.add_argument("--account", required=True, choices=sorted(ACCOUNTS),
                    help="the login billed (a = ~/.claude-a, b = ~/.claude-b)")
    ap.add_argument("--perq", action="store_true", help="per-question rule: one session per video file, own prior and "
                                                       "depth_info only, no variants, no family facts (PERQ_PROMPT)")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--max-turns", type=int, default=200)
    ap.add_argument("--timeout-min", type=int, default=35)
    ap.add_argument("--timeout-min-3d", type=int, default=50)
    ap.add_argument("--workers", type=int, default=14)
    ap.add_argument("--events", help="comma list: run only these events (in this order)")
    ap.add_argument("--late", default="", help="comma list of events to push to the end of the queue")
    ap.add_argument("--val", action="store_true", help="run the 24 validation families instead of the scored test")
    ap.add_argument("--plan-only", action="store_true", help="write the ordered plan and exit")
    ap.add_argument("--keep-workspace", action="store_true")
    ap.add_argument("--order", choices=("tiers", "budget"), default="tiers")
    ap.add_argument("--stop-name", default="STOP", help="file in the out dir that drains this pool")
    ap.add_argument("--skip-existing-ws", action="store_true", help="skip events whose workspace exists (in flight)")
    ap.add_argument("--guard", help="JSON guard file: pause at the five-hour limit until the reset, stop at the "
                                    "seven-day limit (see budget_gate)")
    ap.add_argument("--start-after", help="UTC ISO time before which no agent starts, e.g. 2026-10-18T00:01:00Z")
    ap.add_argument("--extra-workdirs", nargs="*", default=[], help="other pools' workdirs: their agents count as in flight")
    ap.add_argument("--state-dirs", nargs="*", default=[], help="other pools' out dirs: their streams report the plan")
    ap.add_argument("--max-5h-util", type=float, default=0.0,
                    help="start no new agent once the plan's five-hour utilisation reaches this (0 = off)")
    a = ap.parse_args()
    packs = {p["video_id"]: p for p in json.loads((ROOT / a.packs).read_text())["videos"]}
    families = {}
    for members in json.loads((ROOT / a.families).read_text()).values():  # representative -> members
        for m in members:
            families[m] = members
    ordering = order_budget if a.order == "budget" else order
    events = ordering(build_events(packs, families, val=a.val, per_video=a.perq),
                      skip_first=set(filter(None, a.late.split(","))))
    a.tiers = {e["event"]: e["tier"] for e in build_events(packs, families, val=False, per_video=a.perq)
               + build_events(packs, families, val=True, per_video=a.perq)}
    if a.events:
        want = a.events.split(",")
        byname = {e["event"]: e for e in events}
        events = [byname[w] for w in want]
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    plan = [{"n": i, "event": e["event"], "primary": e["primary"], "videos": e["videos"], "source": e["source"],
             "category": e["category"], "tier": e["tier"], "rows": len(e["rows"]), "family_facts": len(e["family"])}
            for i, e in enumerate(events)]
    (out / "plan.json").write_text(json.dumps({"settings": {k: str(v) for k, v in vars(a).items()}, "events": plan},
                                              indent=1) + "\n")
    print(f"{len(events)} events, {sum(len(e['rows']) for e in events)} rows", flush=True)
    if a.plan_only:
        return
    tools = a.workdir / "tools"
    tools.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "framekit2.py", tools / "framekit2.py")
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        list(ex.map(lambda e: run(e, a), events))
    print("done", flush=True)


if __name__ == "__main__":
    main()
