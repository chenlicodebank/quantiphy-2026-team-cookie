"""Series 30, run 30_1 (2026-10-22, session 625fd803): one Codex session (OpenAI gpt-6-astra through the user's ChatGPT
plan) per question, as an independent second opinion for the Track A per-question dossiers
(reports/2026-10-22_perq_dossier_rules.md, agreed by the user the same day).

Each session works in its own folder outside the repo, holding only: the video, inputs.json with that ONE question
(test: the current dataset rows, data/test/test_dataset_current_20261021.json; val: the validation CSV) and the viewer
helper. No scene record (its measurements should not share the Claude scene record's), no other question, no network
(workspace-write sandbox), the user's Codex config ignored (no project docs). The prompt is the Track A answering
prompt (cc_agent_scene.py with --real-scale --size-names) without the scene-record lines. Every command a session runs
is audited for paths outside its folder; a flagged answer is kept but marked.

    python scripts/s30_codex_perq.py --split val --ids 1260,1263 --out results/s30_codex_val
    python scripts/s30_codex_perq.py --split test --ids-file results/s30_flags/s3_gross.csv --out results/s30_codex_test
"""
import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cc_agent_run as C  # noqa: E402
import cc_agent_scene as S  # noqa: E402

ROOT = C.ROOT
CODEX = str(Path.home() / ".npm-global/bin/codex")
LOCK = threading.Lock()


def build_prompt():
    p = S.REAL_SCALE_PROMPT.replace("Method:\n", S.SIZE_NAMES + S.SIZE_NAMES_FLYERS + "Method:\n", 1)
    edits = [
        ("- scene/: a measurement record of this video made before any question was known (scene.json, tracks/*.csv in "
         "pixels\n  and seconds, notes.md, scripts/). Read-only: copy a script out of it before changing it.\n",
         "- framekit2.py: the viewer helper below.\n"),
        ("that you then look at with the Read tool", "that you then open with your image viewing tool"),
        ("{tools}/framekit2.py", "framekit2.py"),
        (" The\nrecord in scene/ is a starting point, not the truth: check that it covers the right object and the right "
         "frames,\nre-measure what the answer depends on, and correct the record where it is wrong (or measure from "
         "scratch if it is\nmissing).\n", "\n"),
        (" The times in scene/ were computed at the file's fps before question_fps\n   was known: use their frame column, "
         "not their seconds.", ""),
        ("Find the asked object and the prior's object in scene/ and on frames", "Find the asked object and the prior's "
         "object on frames"),
        ("The only shell command you may run is the Python interpreter above, called by\nits full path (for example "
         "`{py} measure.py`); other commands are refused.",
         "Run Python by its full path (for example `{py} measure.py`) and keep every shell command inside\nthis folder."),
    ]
    for old, new in edits:
        assert p.count(old) == (3 if old == "{tools}/framekit2.py" else 1), old[:60]
        p = p.replace(old, new)
    assert "scene/" not in p and "Read tool" not in p, "scene-record lines left in the Codex prompt"
    return p + "\nWrite notes.md and every message in English.\n"


PROMPT = build_prompt()


def load_rows(split):
    if split == "test":
        rows = json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text())
        return {r["row_idx"] + 1: {"id": r["row_idx"] + 1, "video_id": r["video_id"].strip(), "source": r["video_source"],
                                   "video_type": r["video_type"], "fps": float(r["fps"]), "itype": r["inference_type"],
                                   "question": r["question"].strip(), "prior": (r["prior"] or "").strip(),
                                   "depth_info": (r.get("depth_info") or "").strip() or None, "gt": None}
                for r in rows}
    out = {}
    with open(ROOT / "data/validation/validation_dataset.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            i = int(r[""])
            out[i] = {"id": i, "video_id": r["video_id"].strip(), "source": r["video_source"].replace("segmentaion",
                                                                                                     "segmentation"),
                      "video_type": r["video_type"], "fps": float(r["fps"]), "itype": r["inference_type"],
                      "question": r["question"].strip(), "prior": r["ground_truth_prior"].strip(),
                      "depth_info": (r.get("depth_info") or "").strip() or None, "gt": r["ground_truth_posterior"]}
    return out


OUTSIDE = re.compile(r"(/Users/[^\s'\"]+|/Volumes/[^\s'\"]+|~/[^\s'\"]+|\.\./)")


def audit(stream, ws):
    """Commands of the session that name a path outside its folder (the Python binary excepted)."""
    flags, cmds = [], 0
    for line in stream.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = e.get("item") or {}
        if e.get("type") == "item.completed" and item.get("type") == "command_execution":
            cmds += 1
            cmd = item.get("command", "")
            for m in OUTSIDE.findall(cmd):
                if m.startswith(str(ws)) or m.startswith(C.PY) or m.startswith(str(Path.home() / "miniforge3")):
                    continue
                flags.append(m[:200])
    return {"commands": cmds, "outside_paths": sorted(set(flags))}


def run_one(row, a, out):
    vid, qid = row["video_id"], row["id"]
    qdir = out / "q" / f"{vid}__{qid}"
    if (qdir / "answers.json").exists() and not a.force:
        return json.loads((qdir / "answers.json").read_text())
    ws = (a.workdir / f"{vid}__{qid}").resolve()
    S.wipe(ws)
    (ws / "frames").mkdir(parents=True)
    S.link_video(ROOT / "data/test" / f"{vid}.mp4", ws / f"{vid}.mp4")
    shutil.copyfile(C.HERE / "framekit2.py", ws / "framekit2.py")
    m = S.video_meta(ws / f"{vid}.mp4")
    inputs = {"video": f"{vid}.mp4", "video_source": row["source"], "video_type": row["video_type"], "fps": m["fps"],
              "frames": m["frames"], "duration_s": round(m["frames"] / m["fps"], 4), "width": m["width"],
              "height": m["height"],
              "question": {"id": qid, "question": row["question"], "prior": row["prior"], "depth_info": row["depth_info"],
                           "prior_kind_to_question_kind": row["itype"], "question_fps": row["fps"]}}
    (ws / "inputs.json").write_text(json.dumps(inputs, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    prompt = PROMPT.format(ws=ws, py=C.PY, tools=ws, video=vid)
    stream = out / "streams" / f"{vid}__q{qid}.jsonl"
    stream.parent.mkdir(parents=True, exist_ok=True)
    cmd = [CODEX, "exec", "--json", "--ephemeral", "--skip-git-repo-check", "--ignore-user-config", "-s",
           "workspace-write", "-C", str(ws), "-m", a.model, "-c", f'model_reasoning_effort="{a.effort}"', "-c",
           'approval_policy="never"', "-o", str(ws / "last_message.txt"), "-"]
    t0 = time.time()
    with stream.open("w", encoding="utf-8") as f:
        proc = subprocess.Popen(cmd, cwd=ws, stdin=subprocess.PIPE, stdout=f, stderr=subprocess.STDOUT, text=True)
        try:
            proc.communicate(prompt, timeout=a.timeout_min * 60)
            timed_out = False
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.communicate()
            timed_out = True
    usage = {}
    for line in stream.read_text(encoding="utf-8", errors="replace").splitlines():
        if '"turn.completed"' in line:
            try:
                usage = json.loads(line).get("usage") or usage
            except json.JSONDecodeError:
                pass
    answers, err = {}, None
    if (ws / "answers.json").exists():
        try:
            raw = json.loads((ws / "answers.json").read_text())
            answers = {str(int(k)): float(v) for k, v in raw.items() if v is not None and int(k) == qid}
        except (ValueError, TypeError) as exc:
            err = f"answers.json unreadable: {exc}"
    rec = {"id": qid, "video": vid, "split": a.split, "model": a.model, "effort": a.effort, "answer": answers.get(str(qid)),
           "wall_s": round(time.time() - t0), "timed_out": timed_out, "error": err, "usage": usage,
           "audit": audit(stream, ws), "commit": a.commit, "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    qdir.mkdir(parents=True, exist_ok=True)
    for name in ("answers.json", "notes.md", "inputs.json", "last_message.txt"):
        if (ws / name).exists():
            shutil.copyfile(ws / name, qdir / name)
    for py in ws.glob("*.py"):
        if py.name != "framekit2.py" and py.stat().st_size < 200_000:
            (qdir / "code").mkdir(exist_ok=True)
            shutil.copyfile(py, qdir / "code" / py.name)
    (qdir / "run.json").write_text(json.dumps(rec, indent=1) + "\n")
    with LOCK:
        with (out / "progress.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
    print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] q{qid} {vid} -> {rec['answer']} ({rec['wall_s']} s, "
          f"in {usage.get('input_tokens')} out {usage.get('output_tokens')}, outside {len(rec['audit']['outside_paths'])})",
          flush=True)
    if not a.keep_workspace:
        S.wipe(ws)
    return answers


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--split", choices=("test", "val"), required=True)
    ap.add_argument("--ids", help="comma list of question ids")
    ap.add_argument("--ids-file", help="CSV with an id column")
    ap.add_argument("--out", required=True)
    ap.add_argument("--workdir", type=Path, default=Path("/private/tmp/qp_blind/s30_codex"))
    ap.add_argument("--model", default="gpt-6-astra")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--timeout-min", type=int, default=40)
    ap.add_argument("--force", action="store_true", help="re-run questions already answered in --out")
    ap.add_argument("--keep-workspace", action="store_true")
    ap.add_argument("--print-prompt", action="store_true")
    a = ap.parse_args()
    if a.print_prompt:
        print(PROMPT)
        return
    a.commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                              text=True).stdout.strip()
    rows = load_rows(a.split)
    ids = [int(x) for x in a.ids.split(",")] if a.ids else []
    if a.ids_file:
        with open(a.ids_file, newline="") as f:
            ids += [int(r["id"]) for r in csv.DictReader(f)]
    missing = [i for i in ids if i not in rows]
    if missing:
        sys.exit(f"ids not in the {a.split} rows: {missing[:10]}")
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    a.workdir = a.workdir / a.split
    (out / "settings.json").write_text(json.dumps({k: str(v) for k, v in vars(a).items()}, indent=1) + "\n")
    print(f"{len(ids)} questions, {a.workers} in parallel, model {a.model} / {a.effort}", flush=True)
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        list(ex.map(lambda i: run_one(rows[i], a, out), ids))


if __name__ == "__main__":
    main()
