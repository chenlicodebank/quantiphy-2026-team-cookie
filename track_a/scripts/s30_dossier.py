"""Series 30 (2026-10-22, session 625fd803): per-question dossiers and the Opus adjudicator for the Track A entry.

The user's idea (2026-10-22): keep one context per question that collects every legitimate answer and trace for that
question, then let a reasoning session decide from the whole context. The rules it obeys were agreed with the user the
same day (reports/2026-10-22_perq_dossier_rules.md): a dossier holds only (L1) the question's own inputs, (L2)
question-blind computation on its video, (L3) outputs of runs that were given nothing else; never the output of a
session that held another question (the GLM v5r per-video agent, the #186-line agent), never another question's prior
or answer (not even as a row selector), never labels; and every reasoning session holds exactly one dossier.

Enforced by construction: candidates are read only from the out dirs of per-question runners listed in SOURCES (one
session = one question in each of them), deduplicated by notes text.

    python scripts/s30_dossier.py flags --cat S3 --sources simulation,segmentation --thr 0.25 --out results/s30_flags/s3_ds25.csv
    python scripts/s30_dossier.py build --ids-file results/s30_flags/s3_ds25.csv --out results/s30_dossier
    python scripts/s30_dossier.py adjudicate --ids-file results/s30_flags/s3_ds25.csv --dossier results/s30_dossier \
        --out results/s30_adj_s3 --account a --guard results/s30_adj_s3/guard_a.json
"""
import argparse
import csv
import hashlib
import json
import math
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
R = ROOT / "results"
BASE = R / "fulltest_s27_e2/track_a_s27_e2.csv"  # the Track A entry candidate E2 (prediction .8495-.8497)
# Per-question runners only (cc_agent_scene.py phase 2, dsh_scene.py, s30_codex_perq.py): every session in these dirs
# held exactly one question. Label = how the dossier names the source.
CLAUDE_DIRS = [("s26_scene_full", "26_30 per-question run"), ("s26_scene_spread", "26_36 second run"),
               ("s26_reask_1020", "26_59 real-scale re-ask"), ("s27_plaus_reask", "27_6 real-scale re-ask"),
               ("s27_gravity", "27_9 gravity-prior re-ask"), ("s27_valfam", "27_3 per-question run"),
               ("s26_repeat_1021_a", "26_80 repeat"), ("s26_repeat_1021_b", "26_80 repeat"),
               ("s30_realscale", "30_5 real-scale re-ask"), ("s30_adj_s3", "30_x adjudication"),
               ("s30_adj_s3_seg", "30_7 re-adjudication"), ("s30_adj_d3", "30_x adjudication"),
               ("s30_adj_s2", "30_x adjudication")]
# Every DeepSeek-1017 test run of the two-phase per-question harness (28_3 and later, incl. the Track B session's s29
# passes run for Track A's second opinions, run channel #121 / #122); sorted so the first answer of a question wins.
DEEPSEEK_DIRS = sorted(p.name for pat in ("s2[89]_test_dsf1017*", "s29_pass_*") for p in (ROOT / "results").glob(pat)
                       if (p / "sessions.jsonl").exists() or (p / "q").exists())
CODEX_DIRS = ["s30_codex_test"]
# Validation gate (labelled rows; the 26_30 validation run keyed its questions by their test ids, DeepSeek's 28_2 run
# by validation ids, mapped here by video and question text).
CLAUDE_DIRS_VAL = [("s26_scene_val", "26_30 per-question run"), ("s26_reask_1020_val", "26_59 real-scale re-ask")]
CODEX_DIRS_VAL = ["s30_codex_val"]
LOCK = threading.Lock()


def fnum(v):
    try:
        x = float(v)
        return x if math.isfinite(x) and x > 0 else None
    except (TypeError, ValueError):
        return None


def test_rows():
    rows = json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text())
    return {r["row_idx"] + 1: r for r in rows}


def base_values():
    with open(BASE, newline="", encoding="utf-8") as f:
        return {int(r["id"]): fnum(r["parsed_value"]) for r in csv.DictReader(f)}


def ledger():
    with open(R / "s26_scene_full/ledger.csv", newline="", encoding="utf-8") as f:
        return {int(r["id"]): r for r in csv.DictReader(f)}


def deepseek_answers(val=False):
    if val:
        return deepseek_val_answers()
    out = {}
    for d in DEEPSEEK_DIRS:
        p = R / d / "sessions.jsonl"
        if not p.exists():  # a pass synced as q/<video>__<id>/r<N>.json only (29_5 on the GH200)
            for rf in sorted((R / d / "q").glob("*__*/r*.json")):
                try:
                    fin = json.loads(rf.read_text()).get("final") or {}
                except json.JSONDecodeError:
                    continue
                for x in fin.get("answers") or []:
                    if fnum(x.get("value")):
                        out.setdefault(int(x["id"]), []).append({"dir": d, "repeat": rf.stem, "answer": fnum(x["value"]),
                                                                 "reason": x.get("reason", "")})
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            if e.get("kind") == "question" and fnum(e.get("answer")):
                out.setdefault(int(e["id"]), []).append({"dir": d, "repeat": e.get("repeat"), "answer": fnum(e["answer"]),
                                                         "reason": e.get("reason", "")})
    return out


def deepseek_val_answers():
    """28_2's validation answers, keyed by the test id of the same video and question."""
    tid = {(r["video_id"].strip(), r["question"].strip()): i for i, r in test_rows().items()}
    with open(ROOT / "data/validation/validation_dataset.csv", newline="", encoding="utf-8") as f:
        v2t = {int(r[""]): tid.get((r["video_id"].strip(), r["question"].strip())) for r in csv.DictReader(f)}
    out = {}
    for d in ("s28_val_dsf1017", "s28_gate_dsf1017_4v", "s28_gate_dsf1017"):
        if not (R / d / "sessions.jsonl").exists():
            continue
        for line in (R / d / "sessions.jsonl").read_text(encoding="utf-8").splitlines():
            e = json.loads(line)
            t = v2t.get(int(e.get("id", 0) or 0))
            if e.get("kind") == "question" and t and fnum(e.get("answer")) and t not in out:
                out[t] = [{"dir": d, "repeat": e.get("repeat"), "answer": fnum(e["answer"]), "reason": e.get("reason", ""),
                           "val_id": int(e["id"])}]
    return out


def cmd_flags(a):
    """Rows of one category whose compliant DeepSeek answer differs from the entry's by more than --thr (log)."""
    led, base, ds = ledger(), base_values(), deepseek_answers()
    srcs = set(a.sources.split(","))
    rows = []
    for i, r in led.items():
        if r["category"] != a.cat or r["source"] not in srcs or i not in ds or not base.get(i):
            continue
        d = ds[i][0]["answer"] if a.ds_dir is None else next((x["answer"] for x in ds[i] if x["dir"] == a.ds_dir), None)
        if not d:
            continue
        lr = math.log(d / base[i])
        if abs(lr) > math.log(1 + a.thr):
            rows.append({"id": i, "video": r["video"], "source": r["source"], "kind": r["kind"], "e2": base[i],
                         "deepseek": d, "ln_ratio": round(lr, 4)})
    rows.sort(key=lambda x: -abs(x["ln_ratio"]))
    out = ROOT / a.out
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["id"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} rows -> {out}")


def claude_attempts(qid, video, dirs=None):
    """Every Claude attempt at this question in the per-question runner dirs, deduplicated by notes text."""
    seen, out = set(), []
    for d, label in dirs or CLAUDE_DIRS:
        qdir = R / d / "q" / f"{video}__{qid}"
        if not qdir.exists():
            continue
        meta = {}
        if (R / d / "attempts.tsv").exists():
            with open(R / d / "attempts.tsv", newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f, delimiter="\t"):
                    if row["ids"] == str(qid):
                        meta[int(row["attempt"])] = row
        dirs = S.attempts(qdir) or [qdir]
        for ad in dirs:
            if not (ad / "answers.json").exists() or not (ad / "notes.md").exists():
                continue
            notes = (ad / "notes.md").read_text(encoding="utf-8", errors="replace")
            h = hashlib.sha256(notes.encode()).hexdigest()
            if h in seen:
                continue
            seen.add(h)
            try:
                ans = fnum(json.loads((ad / "answers.json").read_text()).get(str(qid)))
            except (ValueError, json.JSONDecodeError):
                ans = None
            n = int(ad.name[1:]) if ad.name.startswith("a") and ad.name[1:].isdigit() else 1
            m = meta.get(n, {})
            model = m.get("model_p2") or "claude-opus-5-5"
            out.append({"kind": "claude", "dir": d, "attempt": n, "label": label, "trigger": m.get("trigger", ""),
                        "model": model, "answer": ans, "notes": notes, "path": ad})
    return out


def cmd_build(a):
    rows, base, ds = test_rows(), base_values(), deepseek_answers(a.val)
    ids = read_ids(a)
    out = ROOT / a.out
    for qid in ids:
        r = rows[qid]
        video = r["video_id"].strip()
        qd = out / "q" / f"{video}__{qid}"
        shutil.rmtree(qd, ignore_errors=True)
        qd.mkdir(parents=True)
        cands = []
        for c in claude_attempts(qid, video, CLAUDE_DIRS_VAL if a.val else None):
            name = f"C{len(cands) + 1}"
            (qd / name).mkdir()
            (qd / name / "notes.md").write_text(c["notes"], encoding="utf-8")
            code = c["path"] / "code"
            if code.exists():
                shutil.copytree(code, qd / name / "code")
            who = "Claude Sonnet 5.5" if "sonnet" in c["model"] else "Claude Opus 5.5"
            cands.append({"name": name, "who": f"{who} (Claude Code agent), {c['label']}" +
                          (f", {c['trigger']}" if c["trigger"] and "first run" not in c["trigger"] else ""),
                          "answer": c["answer"], "source": f"{c['dir']} attempt {c['attempt']}"})
        for x in ds.get(qid, []):
            name = f"C{len(cands) + 1}"
            (qd / name).mkdir()
            final = ""
            for rf in sorted((R / x["dir"] / "q" / f"{video}__{x.get('val_id', qid)}").glob("r*.json")):
                try:
                    final = json.loads(rf.read_text()).get("final_text", "") or final
                except json.JSONDecodeError:
                    pass
            (qd / name / "notes.md").write_text(f"{x['reason']}\n\nFinal message:\n{final}\n", encoding="utf-8")
            cands.append({"name": name, "who": "DeepSeek-V4.1-Flash-1017 (open-weight coding agent, two-phase)",
                          "answer": x["answer"], "source": f"{x['dir']} {x['repeat']}"})
        for d in (CODEX_DIRS_VAL if a.val else CODEX_DIRS):
            cq = R / d / "q" / f"{video}__{qid}"
            if (cq / "answers.json").exists():
                name = f"C{len(cands) + 1}"
                (qd / name).mkdir()
                if (cq / "notes.md").exists():
                    shutil.copyfile(cq / "notes.md", qd / name / "notes.md")
                if (cq / "code").exists():
                    shutil.copytree(cq / "code", qd / name / "code")
                ans = fnum(json.loads((cq / "answers.json").read_text()).get(str(qid)))
                cands.append({"name": name, "who": "OpenAI GPT-6 Astra (Codex agent)", "answer": ans, "source": d})
        md = [f"# Earlier answers to question {qid}", "",
              "Each was made by a separate session that saw only this question, its video, its prior and depth_info.", ""]
        for c in cands:
            md += [f"## {c['name']}: {c['who']}", f"Answer: {c['answer']}", f"Notes and scripts: dossier/{c['name']}/", ""]
        (qd / "candidates.md").write_text("\n".join(md), encoding="utf-8")
        (qd / "candidates.json").write_text(json.dumps({"id": qid, "video": video, "entry_e2": base.get(qid),
                                                        "candidates": cands}, indent=1) + "\n")
        print(f"q{qid} {video}: {len(cands)} candidates " + ", ".join(f"{c['name']}={c['answer']}" for c in cands))


ADJ_SECTION = """Earlier answers to this same question (dossier/): separate sessions answered THIS question before you, each seeing
only this question, its video, its prior and depth_info, as you do - Claude sessions and agents built on other models.
dossier/candidates.md lists every answer; dossier/<name>/ holds that session's notes.md and its scripts. Their answers
disagree, so at least one of them is wrong, and it may be all of them. Count no votes: a difference comes from one
step - which object or which part of it, which dimension, which frame or time, the reference point, the focal length
or how depth_info was used, the time base, a convention above, or arithmetic. The Claude sessions are usually the more
careful measurers, but not always, and every session was sometimes wrong.

How to work:
1. Read inputs.json and look at the video first; write down which measurements the answer depends on.
2. Read dossier/candidates.md and each candidate's notes.md; find the step where the answers part ways.
3. Re-measure that step yourself in code from the video, and check each candidate's step against the conventions
   above and against the real size of any standard object. Do not average answers: decide which reading is right,
   or compute your own value when none is.
4. In notes.md, write the step where they part ways, your own measurement of it, and which candidate you agree with
   (if any) and why.
5. A segmentation video keeps the original scene's answers: if the object the question asks about was cut out with
   the background, the answer is still about that object (its typical real value, or an earlier session's estimate of
   it) - never re-read the question as being about a different object that is still visible.

"""


def cmd_adjudicate(a):
    """One Claude Code session per question: the video, a read-only copy of its question-blind scene record, its own
    inputs (current dataset row), and its dossier. Attempts, streams and ledgers as cc_agent_scene.py keeps them."""
    rows = test_rows()
    ids = read_ids(a)
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    a.out = out
    a.stop_name = f"STOP_{a.account}"
    a.commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                              text=True).stdout.strip()
    a.slots = threading.BoundedSemaphore(a.max_sessions)
    g = json.loads(Path(a.guard).read_text()) if a.guard else {}
    a.cost2 = S.P2_COST | {int(k): v for k, v in g.get("cost_p2", {}).items()}
    tools = (a.workdir / "tools").resolve()
    tools.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(C.HERE / "framekit2.py", tools / "framekit2.py")
    prompt_t = S.REAL_SCALE_PROMPT.replace("Method:\n", S.SIZE_NAMES + S.SIZE_NAMES_FLYERS + ADJ_SECTION + "Method:\n", 1)
    prompt_t = prompt_t.replace(
        "- scene/: a measurement record",
        "- dossier/: the earlier answers to this question (see below).\n- scene/: a measurement record", 1)
    assert "dossier/candidates.md" in prompt_t and prompt_t.count("- dossier/:") == 1
    (out / "prompt_template.txt").write_text(prompt_t, encoding="utf-8")

    def one(qid):
        r = rows[qid]
        vid = r["video_id"].strip()
        qdir = out / "q" / f"{vid}__{qid}"
        if (qdir / "answers.json").exists():
            return
        if (out / a.stop_name).exists():
            return
        dos = ROOT / a.dossier / "q" / f"{vid}__{qid}"
        scene = R / ("s26_scene_val" if a.val else "s26_scene_full") / "videos" / vid / "scene"
        if not dos.exists() or not scene.exists():
            print(f"q{qid}: missing dossier or scene record", flush=True)
            return
        ws = (a.workdir / f"{vid}__{qid}").resolve()
        S.wipe(ws)
        (ws / "frames").mkdir(parents=True)
        S.link_video(ROOT / "data/test" / f"{vid}.mp4", ws / f"{vid}.mp4")
        for src, dst in ((scene, ws / "scene"), (dos, ws / "dossier")):
            shutil.copytree(src, dst)
            for p in sorted(dst.rglob("*"), reverse=True):
                p.chmod(0o444 if p.is_file() else 0o555)
            dst.chmod(0o555)
        m = S.video_meta(ws / f"{vid}.mp4")
        inputs = {"video": f"{vid}.mp4", "video_source": r["video_source"].replace("segmentaion", "segmentation"),
                  "video_type": r["video_type"], "fps": m["fps"], "frames": m["frames"],
                  "duration_s": round(m["frames"] / m["fps"], 4), "width": m["width"], "height": m["height"],
                  "question": {"id": qid, "question": r["question"].strip(), "prior": (r["prior"] or "").strip(),
                               "depth_info": (r.get("depth_info") or "").strip() or None,
                               "prior_kind_to_question_kind": r["inference_type"], "question_fps": float(r["fps"])}}
        (ws / "inputs.json").write_text(json.dumps(inputs, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        stream = out / f"streams_{a.account}" / f"{vid}__q{qid}.jsonl"
        cat = ("S" if r["inference_type"][0] == "S" else "D") + r["video_type"][1]
        tier = (6 if r["video_source"] == "lab" else {"S3": 0, "D3": 1}.get(cat) if r["video_type"][1] == "3" else
                (2 if cat == "S2" else 3) if r["video_source"] == "internet" else (4 if cat == "S2" else 5))
        rec = S.claude(a, ws, prompt_t.format(ws=ws, py=C.PY, tools=tools, video=vid), stream, a.timeout_p2,
                       a.effort_p2, a.model_p2, a.max_turns_p2, est=a.cost2.get(tier, 1.5))
        rec["audit"] = C.audit(stream, ws, tools)
        answers = {}
        if (ws / "answers.json").exists():
            try:
                raw = json.loads((ws / "answers.json").read_text())
                answers = {str(int(k)): float(v) for k, v in raw.items() if v is not None and int(k) == qid}
            except (ValueError, TypeError):
                pass
        rec.update({"video": vid, "ids": [qid], "answered": len(answers), "account": a.account, "model": a.model_p2,
                    "effort": a.effort_p2, "commit": a.commit})
        (ws / "run.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
        S.keep_attempt(ws, qdir)
        res = rec["result"]
        S.log_attempt(out, {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "ids": str(qid), "video": vid,
                            "attempt": 1, "trigger": a.trigger, "account": a.account, "answer": json.dumps(answers),
                            "cost": res.get("total_cost_usd", ""), "turns": res.get("num_turns", ""),
                            "wall_s": rec["wall_s"], "timed_out": rec["timed_out"], "size_names": True,
                            "cache_ttl": a.cache_ttl or "default", "effort_p2": a.effort_p2, "model_p2": a.model_p2,
                            "commit": a.commit, "stream": str(stream.relative_to(out))})
        S.log(out, {"phase": "adj", "video": vid, "ids": qid, "answered": len(answers), "wall_s": rec["wall_s"],
                    "cost": res.get("total_cost_usd"), "turns": res.get("num_turns"),
                    "flags": len(rec["audit"]["flags"])})
        if not a.keep_workspace:
            S.wipe(ws)

    with ThreadPoolExecutor(max_workers=a.max_sessions) as ex:
        list(ex.map(lambda q: _safe(one, q), ids))


def _safe(fn, *args):
    try:
        return fn(*args)
    except RuntimeError as exc:
        print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] {exc}", flush=True)
    except Exception:  # noqa: BLE001 - one question's failure must not stop the pool
        import traceback
        print(traceback.format_exc(), flush=True)


def read_ids(a):
    ids = [int(x) for x in a.ids.split(",")] if getattr(a, "ids", None) else []
    if getattr(a, "ids_file", None):
        with open(ROOT / a.ids_file, newline="") as f:
            ids += [int(r["id"]) for r in csv.DictReader(f)]
    return ids


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("flags")
    f.add_argument("--cat", required=True)
    f.add_argument("--sources", default="simulation,segmentation")
    f.add_argument("--thr", type=float, default=0.25)
    f.add_argument("--ds-dir")
    f.add_argument("--out", required=True)
    b = sub.add_parser("build")
    b.add_argument("--ids")
    b.add_argument("--ids-file")
    b.add_argument("--out", default="results/s30_dossier")
    b.add_argument("--val", action="store_true", help="validation gate sources (labelled rows)")
    j = sub.add_parser("adjudicate")
    j.add_argument("--ids")
    j.add_argument("--ids-file")
    j.add_argument("--dossier", default="results/s30_dossier")
    j.add_argument("--out", required=True)
    j.add_argument("--account", required=True, choices=sorted(S.ACCOUNTS))
    j.add_argument("--guard")
    j.add_argument("--workdir", type=Path, default=Path("/private/tmp/qp_blind/s30_adj"))
    j.add_argument("--model-p2", default="claude-opus-5-5")
    j.add_argument("--effort-p2", default="high")
    j.add_argument("--max-turns-p2", type=int, default=150)
    j.add_argument("--timeout-p2", type=int, default=50)
    j.add_argument("--max-sessions", type=int, default=6)
    j.add_argument("--cache-ttl", choices=("5m", "1h"))
    j.add_argument("--trigger", default="30_x adjudication over the per-question dossier")
    j.add_argument("--keep-workspace", action="store_true")
    j.add_argument("--val", action="store_true", help="scene records of the 26_30 validation run")
    a = ap.parse_args()
    {"flags": cmd_flags, "build": cmd_build, "adjudicate": cmd_adjudicate}[a.cmd](a)


if __name__ == "__main__":
    main()
