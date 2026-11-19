"""Series 26, run 26_15 (2026-10-18): the per-question Claude Code agent in two phases - a question-blind scene record per
video, then one session per question.

The organisers' rule of 2026-10-15 asks for every question to be answered independently, without other questions or
their answers or priors. cc_agent_run.py --perq still shows a video's questions together and relies on the prompt to
keep them apart. Here the separation is structural (the user's idea, 2026-10-18: understand the whole video first,
then let that understanding serve each question):

- Phase 1, one session per video file, sees NO question, prior or depth_info: it inventories every object a question
  could name and records tracks, extents, events and camera cues in pixels and seconds (scene/scene.json,
  scene/tracks/*.csv, scene/notes.md, scene/scripts/).
- Phase 2, one fresh session per question, in its own workspace: the video, a read-only copy of that video's scene
  record, and that ONE question with its own prior and depth_info. No session ever sees a second question, and no
  workspace holds another question's files.

Answers land as clips/<video>/answers.json once every question of the video is answered (same layout as
cc_agent_run.py, so its scorers and builders read them). `--group` instead answers the questions that share the same
prior and depth_info in one phase-2 session (cheaper; not strictly one question a session).

    python scripts/cc_agent_scene.py --val --events simulation_0060,internet_0019 --out results/s26_scene_val
"""
import argparse
import json
import os
import shutil
import subprocess
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import cc_agent_run as C

ROOT = C.ROOT
LOCK = threading.Lock()
ACCOUNTS = {"a": str(Path.home() / ".claude-a"), "b": str(Path.home() / ".claude-b")}
# USD API-equivalent a session, first estimates (26_10 per-event means split into the scene and per-question parts);
# the guard's cost_p1 / cost_p2 tables override them once a run has measured its own.
P1_COST = {0: 2.2, 1: 2.5, 2: 0.6, 3: 0.6, 4: 0.8, 5: 0.65, 6: 1.0}
P2_COST = {0: 0.45, 1: 0.45, 2: 0.3, 3: 0.3, 4: 0.3, 5: 0.3, 6: 0.35}

RULES = """Rules: do not read, list or search any path outside this folder (running the Python interpreter and the helper is
fine); no web access; no other data. The only shell command you may run is the Python interpreter above, called by
its full path (for example `{py} measure.py`); other commands are refused. Memory is shared with other jobs: decode
frames inside your scripts as you need them, never hold a whole high-resolution video in memory, and keep scratch
files small (no dumps of whole videos)."""

TOOLS = """Python with numpy, scipy, opencv (cv2), PIL and av: {py}
Viewer helper (writes PNG files that you then look at with the Read tool):
  {py} {tools}/framekit2.py info {video}.mp4
  {py} {tools}/framekit2.py sheet {video}.mp4 --n 16 --out frames/sheet.png
  {py} {tools}/framekit2.py frame {video}.mp4 --t 1.5 [--crop X0 Y0 X1 Y1] [--scale 3] [--grid 50] --out frames/f.png"""

CONVENTIONS = C.PERQ_PROMPT[C.PERQ_PROMPT.index("How the reference answers were made"):C.PERQ_PROMPT.index("Method:")]

SCENE_PROMPT = """You are preparing a measurement record of one short video for a benchmark about physical quantities (sizes,
distances, speeds, accelerations). No question is given in this session. Afterwards, separate sessions will each get
ONE question about this video, together with that question's own reference fact (a known size, speed or acceleration
of one object) and, for 3D videos, camera distances, and will answer it starting from your record. So record
everything such a question could ask about, in pixels and seconds. Do not guess any metric scale.

Work only inside this folder:
{ws}

Files here:
- inputs.json: the video's frame rate, frame count, size, source (simulation, segmentation, lab or internet) and
  whether it is a 2D or a 3D scene. Nothing else is known about the questions.
- {video}.mp4: the video at original resolution.
""" + TOOLS + """
Write your own Python scripts for every measurement.

""" + RULES + """

What to record (write scene/scene.json, scene/tracks/<object>.csv and scene/notes.md; keep every script in
scene/scripts/; keep the whole record under about 2 MB):
1. Inventory: every object a question might name - everything that moves, people and animals, vehicles, balls and
   props, furniture, ground features and markings. For each: a short name, what tells it apart from similar objects
   (colour, position, role), whether it moves, and the frames where it is visible.
2. Tracks of every moving object, every frame it is visible: frame, time, the reference point (simulation: the
   object's origin - a rigid object's centre, a human's pelvis, a vehicle's root; lab and internet: the visible
   centre), the bounding box, the mask extents (length along its main axis, width across it, height), and an
   occlusion flag. Draw the tracks and masks on frames and look at them to confirm they hit the right object and its
   full extent.
3. Static objects: pixel extents (length, width, height, along their own axes where perspective allows) and image
   position at a clear frame.
4. Events with frame and time: start and end of motion, release, bounce, impact, contact, direction changes.
5. Camera: static or moving (if it pans or shakes, the per-frame background shift). For 3D scenes: perspective cues
   (ground plane, horizon or vanishing points) and how the apparent size of each moving object changes over time.
6. Per moving object: pixel speed over time (one-frame differences and a lightly smoothed curve), pixel acceleration,
   and which simple model fits each segment (constant velocity, constant acceleration, ease in / ease out), with its
   residual.
scene/notes.md: what each file holds, how it was measured, how reliable each item is, and anything ambiguous (similar
objects, occlusion, shadows, motion blur).

So that you record the right points, these are the conventions the reference answers follow:
""" + CONVENTIONS + """
Finish when the record is complete and checked, then reply with a one-paragraph summary of scene/notes.md.
"""

ANSWER_PROMPT = """You are answering ONE question about one short video for a benchmark. Work only inside this folder:
{ws}

Files here:
- inputs.json: the video file's frame rate (fps), size and source, and THE question: its id, its text, its own prior
  (an exact fact about this video), its own depth_info (camera distances, when given) and the frame rate stated
  with the question (question_fps).
- {video}.mp4: the video at original resolution.
- scene/: a measurement record of this video made before any question was known (scene.json, tracks/*.csv in pixels
  and seconds, notes.md, scripts/). Read-only: copy a script out of it before changing it.
""" + TOOLS + """
Write your own Python scripts for every measurement and keep them in this folder.

""" + RULES + """

Scoring: the answer is scored by its relative error - under 5 pct full credit, 10 pct about 0.9, 20 pct about 0.8,
50 pct about 0.4, 100 pct or more zero. A careful measurement 3 pct off is worth far more than a quick estimate, so
take the time to measure well.

Answer from the video and this question's own prior and depth_info only: the metric scale must come from them. The
record in scene/ is a starting point, not the truth: check that it covers the right object and the right frames,
re-measure what the answer depends on, and correct the record where it is wrong (or measure from scratch if it is
missing).

""" + CONVENTIONS + """Method:
1. Read the question, its prior and depth_info. Find the asked object and the prior's object in scene/ and on frames
   at every time the question or prior names (zoomed crops with --scale 2-4 and --grid to read coordinates).
2. Measure in code rather than by eye, and draw masks and points on frames to confirm them.
3. Scale: 2D -> metres per pixel from the prior; 3D -> pinhole geometry with depth_info, the focal length estimated
   from at least two independent references and checked by reproducing the prior and the given distances.
4. Follow the conventions above (light smoothing is fine; never fit across a bounce, impact or occlusion).
5. Check the answer by a second independent route (another frame window, reference point or method); when routes
   disagree, find out why before answering.
6. Time base: use question_fps for every time and frame conversion, also when the file's fps differs: the reference
   answers time every clip by question_fps. The times in scene/ were computed at the file's fps before question_fps
   was known: use their frame column, not their seconds. When the two rates differ, note the file rate in notes.md.
7. Lab method card (captured videos; the paper's camera, no fitted value): focal f = 0.5959 x image width in pixels.
   A size = this question's depth_info distance to that object x its pixel extent along the asked dimension / f,
   with the pixel extent measured in code on a clear frame near the stated time. A position = back-projection
   ((u - cx) / f, (v - cy) / f, 1) x the depth at that time; distances and displacements are between such 3D points.
8. The answer is a positive number in the unit the question asks for.

Finish by writing answers.json as {{"<id>": <number>}} with the question id from inputs.json, and notes.md (method,
key measurements, the second-route check, confidence). Then reply with the JSON object.
"""
# --lean (user, 2026-10-18, after 26_15 cost a question about 3x the per-video agent): the scene record keeps the
# inventory, tracks, static extents, events and camera, and drops the per-object motion models - every answering
# session fits the motion its own question needs anyway. Written as it goes, so a turn cap never loses the record.
LEAN_SCENE_PROMPT = (SCENE_PROMPT
                     .replace("""6. Per moving object: pixel speed over time (one-frame differences and a lightly smoothed curve), pixel acceleration,
   and which simple model fits each segment (constant velocity, constant acceleration, ease in / ease out), with its
   residual.
""", """Keep the record focused: no motion models, speeds or accelerations (each answering session fits the motion its own
question needs). Write scene.json and the track files early and update them as you go, so the record is usable even
if this session is cut short.
"""))
assert LEAN_SCENE_PROMPT != SCENE_PROMPT and "Keep the record focused" in LEAN_SCENE_PROMPT
# --size-names (2026-10-18): one question at a time, "width" of a TV stand or sofa was read as its long side - in 10
# of the first 29 objects that the template asks both a length and a width of, 26_30 gave the two the same value. The
# validation answers name the shorter horizontal side width (cars, the 75 x 60 cm table). Goes before "Method:".
SIZE_NAMES = """Named sizes (as in the validation answers): length is the object's longer horizontal extent and width
the shorter horizontal extent across it. A car's length runs bumper to bumper and its width wheel to wheel; a 75 x 60
cm table has length 75 and width 60; the width of a sofa, bed, desk, TV stand, bench or keyboard is its front-to-back
depth, not its long side. Height is the vertical extent. For an upright flat object (a door, screen, painting, board or
mirror) width is the horizontal extent across its face. If a name is still ambiguous, give the value under each
reading in notes.md and answer with the reading above.

"""
assert "{family}" not in SCENE_PROMPT and "ANY question" not in ANSWER_PROMPT and "Displacement between" in CONVENTIONS
# The shared conventions predate question_fps. In the answering prompt the time base is question_fps on every row: the
# board reads of 2026-10-18 (#188: 35 rows moved from question_fps to the file rate lost S2 -.0034 / D2 -.0041; #189:
# Track B rows moved to question_fps won D2 +.0042) show the reference answers time rate-mismatched clips by it. This
# replaces step 6's per-question choice (3f78e5f), which sent about 1 in 7 such rows to the file rate (run channel
# #35-#37). Phase 1 sees only the file rate and keeps the original line.
ANSWER_PROMPT = ANSWER_PROMPT.replace(
    "time t means frame round(t x fps). Use the fps in inputs.json.",
    "time t means frame round(t x question_fps).")
assert "Use the fps in inputs.json" not in ANSWER_PROMPT and "round(t x question_fps)" in ANSWER_PROMPT
# --real-scale (26_59, 2026-10-20; method_queue item 38, baselines.md 2026-10-20 11:00-12:15 UTC). The 26_30 traces show
# convention misses the answering prompt invites: "Rendered scenes are not at real-world scale" let sessions keep a 5.5 m
# person (every simulation prior that names a person is realistic); in 21 renders a walking character's depth_info is a
# rig origin that barely moves, which sessions read as a walk across the view; --size-names' "length = longer horizontal
# extent" turned an eagle's length into its wingspan. Two rare readings ride along: a road scene's unnamed "lane", and a
# prior whose motion the clip never shows. Each is knowledge of how the dataset is made; no question's value goes in.
REAL_SCALE_OLD = ("- The given prior is exact. Rendered scenes are not at real-world scale: the priors and depth_info set "
                  "the scale;\n  real-world knowledge is only a sanity check.\n")
REAL_SCALE_NEW = """- The given prior is exact, and the prior and depth_info set the scale. Most rendered scenes are built at real-world
  scale: when the prior is a realistic value (a person walking at 1.3 m/s, a 1.8 m person, a 5 m car), the other
  standard objects have their real sizes too. Use that as a hard check on your scale: if it makes an adult person
  shorter than 1.5 m or taller than 2.0 m, a walking person slower than 0.9 or faster than 2.0 m/s, a car shorter than
  3 m or longer than 7 m, or another everyday object implausible by more than about 40 pct, your geometry is wrong (a
  focal length from an ill-conditioned route, a depth applied to the wrong point, an assumed direction of motion): find
  and fix the error. If you cannot, take the scale from the standard object and say so in notes.md. A scene may be
  scaled only when the prior itself is unrealistic (a 30 cm ice cube, a 0.05 m/s toy car) or its objects are models.
- A prior can describe a motion the clip never shows (gravity for a ball that only rolls or slides): it then gives no
  usable scale; take the scale from an object of known real size (a regulation ball, an adult person) and say so.
"""
CHARACTER_OLD = "    two objects whose depths are given, and check it by reproducing the given values.\n"
CHARACTER_NEW = CHARACTER_OLD + """  * Animated characters (people, animals): depth_info is the distance to the character's object origin, which can stay
    put while the body walks away from it. If a walking character's given distances barely change (under about
    0.1 m/s) although its body visibly moves, that does not mean it walks across the view: take its direction of
    motion from its path on the ground and its change of apparent size, and do not use that distance for the body at
    other times.
  * A road scene's "width of the lane", when the question names no particular lane, is the width of the road surface
    the vehicles drive on, curb to curb.
"""
SIZE_NAMES_FLYERS = """For animals, vehicles, aircraft and boats, length runs along the body and the direction of travel (beak to tail,
nose to tail, bow to stern) and width across it; a bird's, bat's, butterfly's or aircraft's wingspan is its width
(or wingspan), never its length, even when it is longer than the body.

"""
assert ANSWER_PROMPT.count(REAL_SCALE_OLD) == 1 and ANSWER_PROMPT.count(CHARACTER_OLD) == 1
REAL_SCALE_PROMPT = ANSWER_PROMPT.replace(REAL_SCALE_OLD, REAL_SCALE_NEW).replace(CHARACTER_OLD, CHARACTER_NEW)
# --sam3-url (35_2, 2026-10-23; method_queue 54 / the 2026-10-22 correction "SAM 3 for Opus was never tested"): the
# answering session also gets the SAM 3 segmenter and tracker (scripts/sam3kit.py -> scripts/sam3_server.py on the
# GH200). The helper sends the video's name, a frame or box and the phrase the session types, nothing of the question.
SAM3_ANCHOR = "Write your own Python scripts for every measurement and keep them in this folder.\n"
SAM3_TOOLS = """SAM 3 segmentation model (text- or box-prompted masks and video tracks; the helper talks to a local model server, which
is not web access, and sends only the frame and the phrase you type):
  {py} {tools}/sam3kit.py segment {video}.mp4 --phrase "white car" --i FRAME [--box X0 Y0 X1 Y1]
      -> every instance's score, box, centroid and mask extents in pixels (length_px / width_px along its principal
         axes, horiz_px, vert_px), its mask as a PNG in masks/ for your own code, and an overlay with numbered
         outlines in frames/ (look at it).
  {py} {tools}/sam3kit.py track {video}.mp4 --phrase "white car" [--k K | --box X0 Y0 X1 Y1 --i FRAME]
      -> the chosen instance's centre, box and area in every frame (tracks/<phrase>_<k>.csv, frame column first),
         the other candidates, and an overlay of the path in frames/.
  Frames are file frame indices; convert times with question_fps as step 6 says. Use the masks for clean extents
  and the tracks for motion, check every overlay (thin or low-contrast parts can be cut off, shadows or a touching
  object can be included), and compare with your own measurement before relying on either.
"""
assert ANSWER_PROMPT.count(SAM3_ANCHOR) == 1
# --sam3-required (35_2 arm A2, 2026-10-23): in arm A1 no session called the helper (Opus kept its own background
# differences on these clean clips), so A1 read as a second plain run; A2 makes the SAM 3 mask the required second route.
SAM3_REQUIRED = """  Required here: before answering, get a SAM 3 mask (segment) of every object your answer depends on (the asked object
  and the prior's object) on the frames you measure, compare its extents or centre with your own measurement, and when
  they differ by more than 3 pct find out which is right (look at both on a zoomed frame) and say so in notes.md.
"""


def link_video(src, dst):
    try:
        os.link(src, dst)
    except OSError:
        shutil.copyfile(src, dst)


def wipe(path):
    """Remove a workspace, including the read-only scene copy of a question whose pool died mid-session: on 2026-10-18
    12:32 UTC rmtree(ignore_errors=True) left one behind and the next copytree killed the 26_30b pool B."""
    if path.exists():
        for p in path.rglob("*"):
            if not p.is_symlink():
                p.chmod(0o755 if p.is_dir() else 0o644)
    shutil.rmtree(path, ignore_errors=True)


# Every attempt at a question is kept, as autoresearch keeps every version (user, 2026-10-18: "per sample answer
# evolving"): q/<video>__<id>/history/a<N>/ holds that attempt's notes, code, inputs, run.json and answers, attempts.tsv
# in the out dir gets one row per attempt (both pools append to it), and attempt N >= 2 streams to its own
# <video>__q<id>__a<N>.jsonl. The top-level q files stay the current attempt, so the builders read them unchanged.
ATTEMPT_COLS = ("utc", "ids", "video", "attempt", "trigger", "account", "answer", "previous", "cost", "turns", "wall_s",
                "timed_out", "size_names", "cache_ttl", "effort_p2", "model_p2", "commit", "stream")


def attempts(qdir):
    h = qdir / "history"
    return sorted((d for d in h.glob("a*") if d.name[1:].isdigit()), key=lambda d: int(d.name[1:])) if h.exists() else []


def keep_attempt(src, dst, names=("notes.md", "inputs.json", "run.json", "answers.json")):
    """Copy one attempt's small files (and its scripts) from src to dst, replacing what dst held."""
    dst.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(dst / "code", ignore_errors=True)
    for name in names:
        if (src / name).exists():
            shutil.copyfile(src / name, dst / name)
        elif (dst / name).exists():
            (dst / name).unlink()
    for py in list(src.glob("*.py")) + list((src / "code").glob("*.py")):
        if py.stat().st_size < 200_000:
            (dst / "code").mkdir(exist_ok=True)
            shutil.copyfile(py, dst / "code" / py.name)


def log_attempt(out, row):
    import fcntl
    path = out / "attempts.tsv"
    with open(path, "a+", encoding="utf-8") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        if not f.read(1):
            f.write("\t".join(ATTEMPT_COLS) + "\n")
        f.write("\t".join(str(row.get(c, "")).replace("\t", " ").replace("\n", " ") for c in ATTEMPT_COLS) + "\n")
        f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)


def backfill_first(out, qdir, trigger="first run (before the attempt history)"):
    """Turn a question answered before the history existed into attempt a1, once."""
    if attempts(qdir) or not (qdir / "run.json").exists():
        return
    keep_attempt(qdir, qdir / "history" / "a1")
    rj = json.loads((qdir / "run.json").read_text())
    ans = json.loads((qdir / "answers.json").read_text()) if (qdir / "answers.json").exists() else {}
    r = rj.get("result") or {}
    vid = qdir.name.rsplit("__", 1)[0]
    log_attempt(out, {"utc": "", "ids": ",".join(map(str, rj.get("ids", []))), "video": vid, "attempt": 1,
                      "trigger": trigger, "account": rj.get("account", ""), "answer": json.dumps(ans),
                      "cost": r.get("total_cost_usd", ""), "turns": r.get("num_turns", ""), "wall_s": rj.get("wall_s", ""),
                      "timed_out": rj.get("timed_out", ""),
                      "stream": f"streams_{rj.get('account', '')}/{vid}__q{(rj.get('ids') or [''])[0]}.jsonl"})


def video_meta(path):
    import av
    with av.open(str(path)) as c:
        s = c.streams.video[0]
        n = sum(1 for _ in c.decode(s))
        return {"fps": round(float(s.average_rate), 6), "frames": n, "width": s.width, "height": s.height}


def read_plan(d):
    """Newest five-hour / seven-day utilisation reported by the agent streams in d (rate_limit_event); a reading
    whose window has already reset is dropped."""
    import ast
    now, st = time.time(), {"5h": None, "7d": None}
    files = sorted(Path(d).glob("*.jsonl"), key=lambda f: f.stat().st_mtime)[-6:] if Path(d).exists() else []
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
            w = info["unifiedWindows"]
        except (ValueError, KeyError, TypeError, SyntaxError):
            continue
        for k, name in (("5h", "five_hour"), ("7d", "seven_day")):
            if w[name].get("resetsAt", 0) > now and (st[k] is None or w[name]["utilization"] > st[k]):
                st[k] = w[name]["utilization"]
    return st


INFLIGHT = {}
ADMIT = threading.Lock()


class admitted:
    """Admission control (user rulings 2026-10-17/18): start a session only if this account's five-hour use plus
    safety x (estimated remaining cost of its in-flight sessions + this one) / usd_per_pct stays under the guard's
    max_5h, so every session that starts can finish (a session cut by the plan limit is lost). At max_7d the pool
    stops. The guard file is re-read on every check; no guard (validation probes) = no admission control."""

    def __init__(self, a, est):
        self.a, self.est, self.key = a, est, None

    def __enter__(self):
        a, said = self.a, 0.0
        while a.guard:
            with ADMIT:
                g = json.loads(Path(a.guard).read_text())
                st = read_plan(a.out / f"streams_{a.account}")
                if st["7d"] is not None and st["7d"] >= g["max_7d"]:
                    (a.out / a.stop_name).write_text(f"{a.account}: seven-day {st['7d']} >= {g['max_7d']}\n")
                    raise RuntimeError(f"{a.account} weekly stop at {st['7d']}")
                now = time.time()
                rem = sum(e * max(0.3, 1 - (now - t0) / 1800) for e, t0 in INFLIGHT.values())
                proj = (st["5h"] or 0.0) + g.get("safety", 1.25) * (rem + self.est) / g["usd_per_pct"] / 100
                if proj <= g["max_5h"]:
                    self.key = object()
                    INFLIGHT[self.key] = (self.est, now)
                    return self
            if (a.out / a.stop_name).exists():
                raise RuntimeError("STOP")
            if time.time() - said > 900:
                print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] {a.account} waits: five-hour {st['5h']} + "
                      f"{len(INFLIGHT)} in flight (~${rem:.0f}) -> {proj:.2f} > {g['max_5h']}", flush=True)
                said = time.time()
            time.sleep(60)
        return self

    def __exit__(self, *exc):
        if self.key is not None:
            with ADMIT:
                INFLIGHT.pop(self.key, None)
        return False


def claude(a, ws, prompt, stream, timeout_min, effort, model, max_turns, est=1.0):
    env = os.environ.copy()
    for k in list(env):
        if k.startswith(("CLAUDE_CODE_", "CLAUDECODE", "ANTHROPIC_", "CODEX_")):
            env.pop(k)
    env.update({"CLAUDE_CONFIG_DIR": ACCOUNTS[a.account], "CLAUDE_CODE_SAFE_MODE": "1", "CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1",
                "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1", "CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS": "1",
                "DISABLE_AUTOUPDATER": "1"})
    if a.cache_ttl:  # set here: the CLAUDE_CODE_* strip above would drop it from the parent env
        env["CLAUDE_CODE_PROMPT_CACHE_TTL"] = a.cache_ttl
    cmd = [C.CLAUDE, "-p", "--verbose", "--output-format", "stream-json", "--safe-mode", "--no-session-persistence",
           "--permission-mode", "dontAsk", "--allowedTools", f"Read,Write,Edit,Glob,Grep,Bash({C.PY}:*)",
           "--disallowedTools", "WebFetch,WebSearch,Task,Agent", "--model", model, "--effort", effort,
           "--max-turns", str(max_turns)]
    stream.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    with a.slots, admitted(a, est), stream.open("w", encoding="utf-8") as f:
        # A Claude Code reinstall (auto-update) removes the binary for a moment: on 2026-10-18 11:57 UTC the 26_30b
        # pool B died on the FileNotFoundError. Retry for 5 minutes, then drain (RuntimeError) instead.
        for attempt in range(21):
            try:
                proc = subprocess.Popen(cmd, cwd=ws, env=env, stdin=subprocess.PIPE, stdout=f,
                                        stderr=subprocess.STDOUT, text=True)
                break
            except OSError as exc:
                if attempt == 20:
                    raise RuntimeError(f"cannot start {C.CLAUDE}: {exc}") from exc
                time.sleep(15)
        try:
            proc.communicate(prompt, timeout=timeout_min * 60)
            timed_out = False
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.communicate()
            timed_out = True
    result = {}
    for line in stream.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "result":
            result = e
    return {"wall_s": round(time.time() - t0), "timed_out": timed_out,
            "result": {k: result.get(k) for k in ("is_error", "num_turns", "duration_ms", "total_cost_usd", "subtype")},
            "usage": result.get("usage")}


def log(out, rec):
    with LOCK:
        with (out / "progress.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
    print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] " + " ".join(f"{k}={v}" for k, v in rec.items()), flush=True)


def budget_ok(a, out):
    if (out / a.stop_name).exists():
        return False
    if a.max_5h_util:
        u = read_plan(out / f"streams_{a.account}")["5h"]
        if u is not None and u >= a.max_5h_util:
            (out / a.stop_name).write_text(f"five-hour utilisation {u} >= {a.max_5h_util} at "
                                           f"{time.strftime('%H:%M:%S', time.gmtime())} UTC\n")
            return False
    return True


def phase1(ev, a, out):
    vid = ev["primary"]
    vdir = out / "videos" / vid
    if (vdir / "scene" / "scene.json").exists() or (vdir / "run1.json").exists():
        return True
    if not budget_ok(a, out):
        return False
    ws = (a.workdir / vid / "scene_ws").resolve()
    wipe(ws)
    (ws / "frames").mkdir(parents=True)
    (ws / "scene").mkdir()
    link_video(ROOT / "data/test" / f"{vid}.mp4", ws / f"{vid}.mp4")
    m = video_meta(ws / f"{vid}.mp4")
    src = ev["source"].replace("segmentaion", "segmentation")
    (ws / "inputs.json").write_text(json.dumps({
        "video": f"{vid}.mp4", "video_source": src, "scene": "3D" if ev["rows"][0]["video_type"][1] == "3" else "2D",
        "fps": m["fps"], "frames": m["frames"], "duration_s": round(m["frames"] / m["fps"], 4), "width": m["width"],
        "height": m["height"]}, indent=1) + "\n")
    tools = (a.workdir / "tools").resolve()
    stream = out / f"streams_{a.account}" / f"{vid}__p1.jsonl"
    rec = claude(a, ws, (LEAN_SCENE_PROMPT if a.lean else SCENE_PROMPT).format(ws=ws, py=C.PY, tools=tools, video=vid),
                 stream, a.timeout_p1, a.effort,
                 a.model, a.max_turns, est=a.cost1.get(ev["tier"], 2.5))
    rec["audit"] = C.audit(stream, ws, tools)
    rec["account"], rec["lean"] = a.account, a.lean
    rec["scene_files"] = sorted(str(p.relative_to(ws)) for p in (ws / "scene").rglob("*") if p.is_file())
    vdir.mkdir(parents=True, exist_ok=True)
    keep = vdir / "scene"
    shutil.rmtree(keep, ignore_errors=True)
    shutil.copytree(ws / "scene", keep, ignore=lambda d, names: [n for n in names if (Path(d) / n).is_file()
                                                                  and (Path(d) / n).stat().st_size > 2_000_000])
    (vdir / "run1.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
    log(out, {"phase": 1, "video": vid, "wall_s": rec["wall_s"], "timed_out": rec["timed_out"],
              "cost": rec["result"].get("total_cost_usd"), "turns": rec["result"].get("num_turns"),
              "scene_json": (keep / "scene.json").exists(), "flags": len(rec["audit"]["flags"])})
    return True


def phase2(ev, group, a, out, trigger=None):
    """One attempt at one question. trigger=None is the first attempt (skipped once answered); a trigger names a later
    attempt (a re-run), which never replaces the current answer with a failed one."""
    vid = ev["primary"]
    ids = [int(r["id"]) for r in group]
    qdir = out / "q" / f"{vid}__{'_'.join(map(str, ids))}"
    if trigger is None and (qdir / "answers.json").exists():
        return json.loads((qdir / "answers.json").read_text())
    if not budget_ok(a, out):
        return {}
    if trigger is not None:
        backfill_first(out, qdir)
    n = len(attempts(qdir)) + 1
    previous = json.loads((qdir / "answers.json").read_text()) if (qdir / "answers.json").exists() else {}
    ws = (a.workdir / vid / f"q_{ids[0]}").resolve()
    wipe(ws)
    (ws / "frames").mkdir(parents=True)
    link_video(ROOT / "data/test" / f"{vid}.mp4", ws / f"{vid}.mp4")
    shutil.copytree(out / "videos" / vid / "scene", ws / "scene")
    for p in sorted((ws / "scene").rglob("*"), reverse=True):
        p.chmod(0o444 if p.is_file() else 0o555)
    (ws / "scene").chmod(0o555)
    m = video_meta(ws / f"{vid}.mp4")
    src = ev["source"].replace("segmentaion", "segmentation")
    qs = [{"id": int(r["id"]), "question": r["question"].strip(), "prior": r["ground_truth_prior"].strip(),
           "depth_info": (r.get("depth_info") or "").strip() or None, "prior_kind_to_question_kind": r["inference_type"],
           "question_fps": float(r["fps"])} for r in group]
    inputs = {"video": f"{vid}.mp4", "video_source": src, "video_type": group[0]["video_type"], "fps": m["fps"],
              "frames": m["frames"], "duration_s": round(m["frames"] / m["fps"], 4), "width": m["width"],
              "height": m["height"]}
    inputs.update({"question": qs[0]} if len(qs) == 1 else {"questions": qs})
    (ws / "inputs.json").write_text(json.dumps(inputs, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    base = REAL_SCALE_PROMPT if a.real_scale else ANSWER_PROMPT
    if a.sam3_url:
        base = base.replace(SAM3_ANCHOR, SAM3_TOOLS + (SAM3_REQUIRED if a.sam3_required else "") + SAM3_ANCHOR, 1)
    names = SIZE_NAMES + (SIZE_NAMES_FLYERS if a.real_scale else "")
    prompt = base.replace("Method:\n", names + "Method:\n", 1) if a.size_names else base
    prompt = prompt if len(qs) == 1 else (
        prompt.replace("ONE question", "the questions listed in inputs.json (they share the same prior and "
                       "depth_info)").replace('{{"<id>": <number>}} with the question id',
                                              '{{"<id>": <number>, ...}} with every question id'))
    tools = (a.workdir / "tools").resolve()
    stream = out / f"streams_{a.account}" / (f"{vid}__q{ids[0]}.jsonl" if n == 1 else f"{vid}__q{ids[0]}__a{n}.jsonl")
    rec = claude(a, ws, prompt.format(ws=ws, py=C.PY, tools=tools, video=vid), stream, a.timeout_p2, a.effort_p2,
                 a.model_p2, a.max_turns_p2, est=a.cost2.get(ev["tier"], 0.45) * len(ids))
    rec["account"] = a.account
    rec["audit"] = C.audit(stream, ws, tools)
    answers, err = {}, None
    if (ws / "answers.json").exists():
        try:
            raw = json.loads((ws / "answers.json").read_text())
            answers = {str(int(k)): float(v) for k, v in raw.items() if v is not None and int(k) in ids}
        except (ValueError, TypeError) as exc:
            err = f"answers.json unreadable: {exc}"
    rec.update({"video": vid, "ids": ids, "answered": len(answers), "error": err, "attempt": n,
                "trigger": trigger or "first run", "stream": str(stream.relative_to(out))})
    (ws / "run.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
    if answers:
        (ws / "answers.json").write_text(json.dumps(answers, indent=1) + "\n")
    elif (ws / "answers.json").exists():
        (ws / "answers.json").unlink()
    keep_attempt(ws, qdir / "history" / f"a{n}")
    if answers or n == 1:  # the current attempt; a failed re-run leaves the previous one current
        keep_attempt(ws, qdir)
    r = rec["result"]
    log_attempt(out, {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "ids": ",".join(map(str, ids)),
                      "video": vid, "attempt": n, "trigger": trigger or "first run", "account": a.account,
                      "answer": json.dumps(answers), "previous": json.dumps(previous) if previous else "",
                      "cost": r.get("total_cost_usd", ""), "turns": r.get("num_turns", ""), "wall_s": rec["wall_s"],
                      "timed_out": rec["timed_out"], "size_names": a.size_names, "cache_ttl": a.cache_ttl or "default",
                      "effort_p2": a.effort_p2, "model_p2": a.model_p2, "commit": a.commit,
                      "stream": str(stream.relative_to(out))})
    log(out, {"phase": 2, "video": vid, "ids": ",".join(map(str, ids)), "answered": len(answers),
              "wall_s": rec["wall_s"], "cost": r.get("total_cost_usd"), "turns": r.get("num_turns"),
              "flags": len(rec["audit"]["flags"]), "attempt": n})
    if not a.keep_workspace:
        wipe(ws)
    return answers if answers or n == 1 else previous


def safe(fn, *args):
    try:
        return fn(*args)
    except RuntimeError as exc:  # weekly stop or STOP: drain
        print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] {exc}", flush=True)
    except Exception:  # anything else skips this video or question; a later pass retries it (2026-10-18)
        print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] {fn.__name__} {args[0]['primary']} failed:\n"
              f"{traceback.format_exc()}", flush=True)
    return {} if fn is phase2 else False


def claim(out, vid, account):
    """Atomic claim of a video by one pool (one pool per account over the same queue); a pool resumes its own."""
    d = out / "claims"
    d.mkdir(exist_ok=True)
    try:
        fd = os.open(d / vid, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, f"{account} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n".encode())
        os.close(fd)
        return True
    except FileExistsError:
        return (d / vid).read_text().split()[0] == account


def run_video(ev, a, out):
    vid = ev["primary"]
    cdir = out / "clips" / vid
    if (cdir / "answers.json").exists() or (out / a.stop_name).exists() or not claim(out, vid, a.account):
        return
    if not safe(phase1, ev, a, out):
        return
    if a.group:
        groups = {}
        for r in ev["rows"]:
            groups.setdefault((r["ground_truth_prior"].strip(), (r.get("depth_info") or "").strip()), []).append(r)
        groups = list(groups.values())
    else:
        groups = [[r] for r in ev["rows"]]
    with ThreadPoolExecutor(max_workers=a.q_workers) as ex:
        parts = list(ex.map(lambda g: safe(phase2, ev, g, a, out), groups))
    answers = {k: v for p in parts for k, v in p.items()}
    want = {str(int(r["id"])) for r in ev["rows"]}
    if want <= set(answers):
        cdir.mkdir(parents=True, exist_ok=True)
        (cdir / "answers.json").write_text(json.dumps({k: answers[k] for k in sorted(want, key=int)}, indent=1) + "\n")
    if not a.keep_workspace:
        wipe(a.workdir / vid)


def rerun(spec, events, a, out):
    """A later attempt at listed questions, before the queue: each in a fresh session that sees only its own question,
    as the first one did; a video's clips/<video>/answers.json takes the new answer once it exists."""
    byid = {int(r["id"]): (e, r) for e in events for r in e["rows"]}
    seen = set()
    if (out / "attempts.tsv").exists():
        import csv
        seen = {(row["ids"], row["trigger"]) for row in csv.DictReader(open(out / "attempts.tsv"), delimiter="\t")}
    jobs = [byid[i] for i in spec["ids"] if i in byid and (str(i), spec["trigger"]) not in seen]
    print(f"rerun '{spec['trigger']}': {len(jobs)} of {len(spec['ids'])} questions to run", flush=True)

    def one(job):
        ev, row = job
        new = safe(phase2, ev, [row], a, out, spec["trigger"])
        f = out / "clips" / ev["primary"] / "answers.json"
        if new and f.exists():
            with LOCK:
                cur = json.loads(f.read_text())
                cur.update(new)
                tmp = f.with_suffix(".tmp")
                tmp.write_text(json.dumps(cur, indent=1) + "\n")
                os.replace(tmp, f)

    with ThreadPoolExecutor(max_workers=a.max_sessions) as ex:
        list(ex.map(one, jobs))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="results/s26_scene_val")
    ap.add_argument("--workdir", type=Path, default=Path("/private/tmp/qp_blind/scene_20261018"))
    ap.add_argument("--packs", default="results/s26_test_prepared/blind_packs.json")
    ap.add_argument("--account", required=True, choices=sorted(ACCOUNTS),
                    help="the login billed (a = ~/.claude-a, b = ~/.claude-b)")
    ap.add_argument("--guard", help="JSON guard file for this account (max_5h, max_7d, usd_per_pct, safety, cost_p1, "
                                    "cost_p2); required for test-split runs")
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
    ap.add_argument("--max-sessions", type=int, default=10, help="claude processes in flight overall")
    ap.add_argument("--group", action="store_true", help="one phase-2 session per (prior, depth_info) group")
    ap.add_argument("--lean", action="store_true", help="LEAN_SCENE_PROMPT for phase 1 (no motion models)")
    ap.add_argument("--events", help="comma list of video files to run, in this order")
    ap.add_argument("--val", action="store_true", help="the validation families instead of the scored test videos")
    ap.add_argument("--order", choices=("tiers", "budget", "cost"), default="cost",
                    help="cost: cheapest tiers a question first (2D, internet, 3D S3, lab, 3D D3 last), so a budget "
                         "stop leaves the fewest questions unanswered")
    ap.add_argument("--stop-name", help="file in the out dir that drains this pool (default STOP_<account>)")
    ap.add_argument("--max-5h-util", type=float, default=0.0)
    ap.add_argument("--keep-workspace", action="store_true")
    ap.add_argument("--size-names", action="store_true",
                    help="tell each answering session that width is the shorter horizontal side (SIZE_NAMES)")
    ap.add_argument("--real-scale", action="store_true",
                    help="answering prompt REAL_SCALE_PROMPT (+ SIZE_NAMES_FLYERS with --size-names): real-scale check on "
                         "standard objects, rig-origin depths of walking characters, flyers' length / span (26_59)")
    ap.add_argument("--cache-ttl", choices=("5m", "1h"),
                    help="prompt-cache lifetime of every agent session (CLAUDE_CODE_PROMPT_CACHE_TTL). Default: Claude "
                         "Code's own, 1h on these plans. 5m writes cost $5/M instead of $8/M (26_30: writes were 46 pct "
                         "of spend), but a turn more than 5 minutes after the last one writes the whole prefix again")
    ap.add_argument("--rerun", help='JSON {"trigger": "...", "ids": [...]}: one more attempt at each listed question '
                                    "(answered ones too) before the queue; a question already re-run under the same "
                                    "trigger is skipped, so a restart does not repeat it")
    ap.add_argument("--sam3-url", default="",
                    help="SAM 3 server for the answering sessions (35_2), e.g. http://127.0.0.1:8791 through an ssh "
                         "tunnel to scripts/sam3_server.py on the GH200; adds SAM3_TOOLS to the answering prompt")
    ap.add_argument("--sam3-required", action="store_true",
                    help="with --sam3-url: the SAM 3 mask is the required second route (SAM3_REQUIRED, arm A2)")
    ap.add_argument("--plan-only", action="store_true")
    ap.add_argument("--start-after", help="UTC ISO time before which no session starts (e.g. right after a five-hour "
                                          "reset: a new out dir has no plan reading of its own yet)")
    a = ap.parse_args()
    a.stop_name = a.stop_name or f"STOP_{a.account}"
    a.commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                              text=True).stdout.strip()
    if not a.val and not a.guard and not a.plan_only:
        ap.error("a test-split run needs --guard (our run rules: Inference accounts and run practice)")
    a.slots = threading.BoundedSemaphore(a.max_sessions)
    g = json.loads(Path(a.guard).read_text()) if a.guard else {}
    a.cost1 = P1_COST | {int(k): v for k, v in g.get("cost_p1", {}).items()}
    a.cost2 = P2_COST | {int(k): v for k, v in g.get("cost_p2", {}).items()}
    packs = {p["video_id"]: p for p in json.loads((ROOT / a.packs).read_text())["videos"]}
    events = C.build_events(packs, {}, val=a.val, per_video=True)
    if a.order == "cost":
        rank = {4: 0, 5: 1, 2: 2, 3: 3, 0: 4, 6: 5, 1: 6}
        events = sorted(events, key=lambda e: (rank[e["tier"]], -len(e["rows"]), e["event"]))
    else:
        events = (C.order_budget if a.order == "budget" else C.order)(events)
    if a.events:
        byname = {e["event"]: e for e in events}
        events = [byname[w] for w in a.events.split(",")]
    out = a.out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    (out / f"plan_{a.account}.json").write_text(json.dumps({"settings": {k: str(v) for k, v in vars(a).items()
                                                                          if k not in ("slots", "cost1", "cost2")},
                                               "videos": [{"video": e["primary"], "category": e["category"],
                                                           "source": e["source"], "tier": e["tier"],
                                                           "questions": len(e["rows"])} for e in events]},
                                              indent=1) + "\n")
    print(f"{len(events)} videos, {sum(len(e['rows']) for e in events)} questions", flush=True)
    if a.plan_only:
        return
    if a.start_after:
        from datetime import datetime
        t0 = datetime.fromisoformat(a.start_after.replace("Z", "+00:00")).timestamp()
        while time.time() < t0:
            time.sleep(min(60, t0 - time.time()))
    tools = a.workdir / "tools"
    tools.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(C.HERE / "framekit2.py", tools / "framekit2.py")
    if a.sam3_url:
        shutil.copyfile(C.HERE / "sam3kit.py", tools / "sam3kit.py")
        (tools / "sam3.json").write_text(json.dumps({"url": a.sam3_url, "split": "test"}) + "\n")
    done = lambda e: (out / "clips" / e["primary"] / "answers.json").exists()
    if a.rerun:
        rerun(json.loads(Path(a.rerun).read_text()), events, a, out)
    while True:  # later passes retry this pool's unfinished videos (failed questions) until a pass makes no progress
        todo = [e for e in events if not done(e)]
        if not todo or (out / a.stop_name).exists():
            break
        with ThreadPoolExecutor(max_workers=a.workers) as ex:
            list(ex.map(lambda e: safe(run_video, e, a, out), todo))
        if sum(not done(e) for e in events) == len(todo):
            break
    for f in (out / "claims").glob("*") if (out / "claims").exists() else []:  # hand unfinished videos to the other pool
        if f.read_text().split()[0] == a.account and not (out / "clips" / f.name / "answers.json").exists():
            f.unlink()
    print(f"done: {sum(done(e) for e in events)} of {len(events)} videos answered", flush=True)


if __name__ == "__main__":
    main()
