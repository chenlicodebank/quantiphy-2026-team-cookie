"""Series 43 (2026-10-26, session 0c8cbddf): recursive self-improvement over per-question contexts (the user's
context / RSI idea, 2026-10-26: "more context accumulates and each question gets higher accuracy ... change the harness
from experience ... more steps such as recheck ... the more organised the context, the higher the accuracy").

Two loops, both per question:
- The CONTEXT of one question grows round by round: ctx/<video>__<id>/ holds every earlier per-question answer to THIS
  question with its notes and scripts (Series 30 dossier sources + every Series 37 DeepSeek run), an organised
  CONTEXT.md, and after each round that round's investigation (round<k>/: notes, verdict, context update, scripts).
  The next round reads all of it.
- The HARNESS evolves between rounds: harness/v<k>/ holds the investigator's steps (rsi_section.txt) and a lessons
  library (LESSONS.md). A lesson enters only from a round's own reports, written as procedure, and passes `lint`
  (no digits tied to a question, no video or question ids, no object values).

Compliance (the organisers' per-question rule of 2026-10-15): every session holds exactly one question's context -
that question's own inputs, question-blind computation on its video, and answers of earlier sessions that each saw
only this question. The harness and lessons are question-agnostic procedure.

    python scripts/s43_rsi.py build --ids-file tmp/s43/cands.csv --out results/s43_rsi
    python scripts/s43_rsi.py run --round 1 --harness v1 --ids-file tmp/s43/cands.csv --out results/s43_rsi \
        --account a --guard results/s43_rsi/guard_a.json
    python scripts/s43_rsi.py collect --round 1 --out results/s43_rsi
    python scripts/s43_rsi.py lint --harness v2 --out results/s43_rsi
"""
import argparse
import csv
import json
import math
import re
import shutil
import subprocess
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import cc_agent_run as C
import cc_agent_scene as S
import s30_dossier as D

ROOT = C.ROOT
R = ROOT / "results"
INCUMBENT = R / "fulltest_s40_c1/track_a_s40_c1.csv"  # #223 (UTC 10-26 slot 3), the standing gray Track A upload
EXTRA_CLAUDE_DIRS = [("s39_2dmotion", "39_4 re-answer with the SAM 3 mask required"),
                     ("s40_third", "40_5 fresh per-question run")]
DS_RUNS = R / "s37_test_repeats"


def fnum(v):
    return D.fnum(v)


def deepseek_runs(qid, video):
    """Every completed Series 37 DeepSeek-1017 + SAM 3 run of this question (r1 = the 29_5 pass), with its summary and
    final message."""
    out = []
    for line in (DS_RUNS / "answers.jsonl").read_text(encoding="utf-8").splitlines():
        if f'"id": {qid},' not in line:
            continue
        e = json.loads(line)
        if int(e["id"]) != qid or e.get("finish") not in (None, "completed") or not fnum(e.get("answer")):
            continue
        final = ""
        rf = DS_RUNS / "q" / f"{video}__{qid}" / f"{e['record']}.json"
        if rf.exists():
            try:
                final = json.loads(rf.read_text()).get("final_text", "") or ""
            except json.JSONDecodeError:
                pass
        out.append({"record": e["record"], "answer": fnum(e["answer"]), "reason": e.get("reason", ""), "final": final})
    return out


def describe_incumbent(inc, cands, ds_med):
    if inc is None:
        return "unknown"
    for c in cands:
        if c["answer"] and abs(math.log(inc / c["answer"])) < 0.005:
            return f"the answer of {c['name']}"
    if ds_med and any(c["answer"] for c in cands if c["kind"] == "claude"):
        return ("a log-space blend of the Claude answers and the DeepSeek median (a fixed rule for rows where the two "
                "readers differ moderately), or a Claude answer times a fixed convention factor")
    return "derived from the answers below by a fixed rule"


def cmd_build(a):
    rows = D.test_rows()
    inc = {}
    with open(INCUMBENT, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            inc[int(r["id"])] = fnum(r["parsed_value"])
    out = ROOT / a.out
    for qid in D.read_ids(a):
        r = rows[qid]
        video = r["video_id"].strip()
        qd = out / "ctx" / f"{video}__{qid}"
        if qd.exists() and not a.force:
            continue
        shutil.rmtree(qd, ignore_errors=True)
        qd.mkdir(parents=True)
        cands = []
        for c in D.claude_attempts(qid, video, D.CLAUDE_DIRS + EXTRA_CLAUDE_DIRS):
            name = f"C{len(cands) + 1}"
            (qd / name).mkdir()
            (qd / name / "notes.md").write_text(c["notes"], encoding="utf-8")
            if (c["path"] / "code").exists():
                shutil.copytree(c["path"] / "code", qd / name / "code")
            who = "Claude Sonnet 5.5" if "sonnet" in c["model"] else "Claude Opus 5.5"
            cands.append({"name": name, "kind": "claude", "answer": c["answer"],
                          "who": f"{who} (Claude Code agent), {c['label']}" +
                                 (f", {c['trigger']}" if c["trigger"] and "first run" not in c["trigger"] else ""),
                          "source": f"{c['dir']} attempt {c['attempt']}"})
        runs = deepseek_runs(qid, video)
        for x in runs:
            name = f"C{len(cands) + 1}"
            (qd / name).mkdir()
            (qd / name / "notes.md").write_text(f"{x['reason']}\n\nFinal message:\n{x['final']}\n", encoding="utf-8")
            cands.append({"name": name, "kind": "deepseek", "answer": x["answer"],
                          "who": f"DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run {x['record']}",
                          "source": f"s37_test_repeats {x['record']}"})
        for d in D.CODEX_DIRS:
            cq = R / d / "q" / f"{video}__{qid}"
            if (cq / "answers.json").exists():
                name = f"C{len(cands) + 1}"
                (qd / name).mkdir()
                if (cq / "notes.md").exists():
                    shutil.copyfile(cq / "notes.md", qd / name / "notes.md")
                if (cq / "code").exists():
                    shutil.copytree(cq / "code", qd / name / "code")
                ans = fnum(json.loads((cq / "answers.json").read_text()).get(str(qid)))
                cands.append({"name": name, "kind": "codex", "answer": ans, "who": "OpenAI GPT-6 Astra (Codex agent)",
                              "source": d})
        ds = sorted(c["answer"] for c in cands if c["kind"] == "deepseek" and c["answer"])
        ds_med = ds[len(ds) // 2] if len(ds) % 2 else (math.exp((math.log(ds[len(ds) // 2 - 1]) +
                                                                 math.log(ds[len(ds) // 2])) / 2) if ds else None)
        cur = inc.get(qid)
        how = describe_incumbent(cur, cands, ds_med)
        dep = (r.get("depth_info") or "").strip() or "none"
        md = [f"# Context of question {qid} (organised record; every round adds to it)", "",
              "## Question", f"- Text: {r['question'].strip()}", f"- Its own prior: {(r['prior'] or '').strip()}",
              f"- Its own depth_info: {dep}", f"- question_fps: {r['fps']}",
              f"- Video: {video}.mp4 ({r['video_source'].replace('segmentaion', 'segmentation')}, {r['video_type']})", "",
              "## The answer currently submitted",
              f"{cur} - {how}.", "",
              "## Answers so far (each from a separate session that saw only this question, its video, prior and "
              "depth_info)", "",
              "| name | who | answer | x submitted |", "|---|---|---|---|"]
        for c in cands:
            ratio = f"{c['answer'] / cur:.3f}" if c["answer"] and cur else "-"
            md.append(f"| {c['name']} | {c['who']} | {c['answer']} | {ratio} |")
        if ds_med:
            md += ["", f"DeepSeek median over its {len(ds)} runs: {ds_med:.6g}."]
        md += ["", "Each candidate's notes.md and scripts are in context/<name>/.", "",
               "## Investigation rounds", "", "(none yet)", ""]
        (qd / "CONTEXT.md").write_text("\n".join(md), encoding="utf-8")
        (qd / "context.json").write_text(json.dumps({"id": qid, "video": video, "submitted": cur, "submitted_is": how,
                                                     "deepseek_median": ds_med, "candidates": cands}, indent=1) + "\n")
        print(f"q{qid} {video}: submitted {cur}; " + ", ".join(f"{c['name']}={c['answer']}" for c in cands), flush=True)


def provenance(qid, sub, e2, b9):
    """How the submitted value was made, in words an investigator can check (harness v2 onwards)."""
    if not sub or not e2:
        return None
    if abs(math.log(sub / e2)) < 0.002:
        return f"the Claude line's answer {e2:.6g}, unchanged"
    if b9:
        for w in (0.5, 0.6, 0.7):
            if abs(math.log(sub) - (w * math.log(e2) + (1 - w) * math.log(b9))) < 0.002:
                return (f"a fixed-rule blend exp({w} ln A + {1 - w:.1f} ln B) of the Claude line's answer A = {e2:.6g} and "
                        f"an earlier DeepSeek median B = {b9:.6g}; the rule blends every row of its population where the "
                        f"two differ by less than about 50 pct, so it is no judgement about this question")
    return (f"the Claude line's answer {e2:.6g} times a fixed convention factor {sub / e2:.4g} (a rule applied to every row "
            f"of its population and validated on held-out scores), or a blend of it")


def cmd_annotate(a):
    """Rewrite the '## The answer currently submitted' section of every context with the exact provenance."""
    out = ROOT / a.out
    e2 = {int(r["id"]): fnum(r["parsed_value"]) for r in csv.DictReader(open(R / "fulltest_s27_e2/track_a_s27_e2.csv"))}
    b9 = {int(r["id"]): fnum(r["parsed_value"])
          for r in csv.DictReader(open(R / "fulltest_s37_b9lat/track_b_s33_b9lat.csv"))}
    n = 0
    for ctx in sorted((out / "ctx").glob("*__*")):
        cj = json.loads((ctx / "context.json").read_text())
        q = cj["id"]
        p = provenance(q, cj["submitted"], e2.get(q), b9.get(q))
        if not p:
            continue
        md = (ctx / "CONTEXT.md").read_text(encoding="utf-8")
        head = "## The answer currently submitted\n"
        i = md.index(head) + len(head)
        j = md.index("\n## ", i)
        md = md[:i] + f"{cj['submitted']} - {p}.\n" + md[j:]
        (ctx / "CONTEXT.md").write_text(md, encoding="utf-8")
        cj["submitted_is"] = p
        (ctx / "context.json").write_text(json.dumps(cj, indent=1) + "\n")
        n += 1
    print(f"{n} contexts annotated")


def harness_prompt(hdir):
    sec = (hdir / "rsi_section.txt").read_text(encoding="utf-8")
    p = S.REAL_SCALE_PROMPT.replace("Method:\n", S.SIZE_NAMES + S.SIZE_NAMES_FLYERS + sec + "Method:\n", 1)
    p = p.replace("- scene/: a measurement record",
                  "- context/: this question's own context (CONTEXT.md and the earlier answers; see below).\n"
                  "- LESSONS.md: the lessons library of this harness version (see below).\n"
                  "- scene/: a measurement record", 1)
    p = p.replace("Finish by writing answers.json as {{\"<id>\": <number>}} with the question id from inputs.json, and "
                  "notes.md (method,\nkey measurements, the second-route check, confidence). Then reply with the JSON "
                  "object.",
                  "Finish by writing the files the investigation steps above ask for (answers.json, verdict.json, "
                  "context_update.md,\nnotes.md). Then reply with the verdict JSON object.")
    assert "context/CONTEXT.md" in p and p.count("- context/:") == 1 and "verdict.json" in p
    return p


def cmd_run(a):
    rows = D.test_rows()
    ids = D.read_ids(a)
    out = ROOT / a.out
    a.out = out
    a.stop_name = f"STOP_{a.account}"
    a.commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                              text=True).stdout.strip()
    a.slots = threading.BoundedSemaphore(a.max_sessions)
    g = json.loads(Path(a.guard).read_text()) if a.guard else {}
    a.cost2 = S.P2_COST | {int(k): v for k, v in g.get("cost_p2", {}).items()}
    hdir = out / "harness" / a.harness
    prompt_t = harness_prompt(hdir)
    (out / f"prompt_round{a.round}_{a.harness}.txt").write_text(prompt_t, encoding="utf-8")
    tools = (a.workdir / "tools").resolve()
    tools.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(C.HERE / "framekit2.py", tools / "framekit2.py")
    rk = f"round{a.round}"

    def one(qid):
        r = rows[qid]
        vid = r["video_id"].strip()
        ctx = out / "ctx" / f"{vid}__{qid}"
        if (ctx / rk / "verdict.json").exists() or (ctx / rk / "run.json").exists() and not a.redo:
            return
        if (out / a.stop_name).exists():
            return
        scene = R / "s26_scene_full" / "videos" / vid / "scene"
        if not ctx.exists() or not scene.exists():
            print(f"q{qid}: missing context or scene record", flush=True)
            return
        ws = (a.workdir / f"{vid}__{qid}").resolve()
        S.wipe(ws)
        (ws / "frames").mkdir(parents=True)
        S.link_video(ROOT / "data/test" / f"{vid}.mp4", ws / f"{vid}.mp4")
        shutil.copytree(scene, ws / "scene")
        shutil.copytree(ctx, ws / "context", ignore=shutil.ignore_patterns("run.json", "*.jsonl", "context.json"))
        shutil.copyfile(hdir / "LESSONS.md", ws / "LESSONS.md")
        for dst in (ws / "scene", ws / "context"):
            for p in sorted(dst.rglob("*"), reverse=True):
                p.chmod(0o444 if p.is_file() else 0o555)
            dst.chmod(0o555)
        (ws / "LESSONS.md").chmod(0o444)
        m = S.video_meta(ws / f"{vid}.mp4")
        inputs = {"video": f"{vid}.mp4", "video_source": r["video_source"].replace("segmentaion", "segmentation"),
                  "video_type": r["video_type"], "fps": m["fps"], "frames": m["frames"],
                  "duration_s": round(m["frames"] / m["fps"], 4), "width": m["width"], "height": m["height"],
                  "question": {"id": qid, "question": r["question"].strip(), "prior": (r["prior"] or "").strip(),
                               "depth_info": (r.get("depth_info") or "").strip() or None,
                               "prior_kind_to_question_kind": r["inference_type"], "question_fps": float(r["fps"])}}
        (ws / "inputs.json").write_text(json.dumps(inputs, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        stream = out / f"streams_{a.account}" / f"{vid}__q{qid}__{rk}.jsonl"
        cat = ("S" if r["inference_type"][0] == "S" else "D") + r["video_type"][1]
        tier = (6 if r["video_source"] == "lab" else {"S3": 0, "D3": 1}.get(cat) if r["video_type"][1] == "3" else
                (2 if cat == "S2" else 3) if r["video_source"] == "internet" else (4 if cat == "S2" else 5))
        rec = S.claude(a, ws, prompt_t.format(ws=ws, py=C.PY, tools=tools, video=vid), stream, a.timeout,
                       a.effort, a.model, a.max_turns, est=a.cost2.get(tier, 1.5))
        rec["audit"] = C.audit(stream, ws, tools)
        rec.update({"video": vid, "ids": [qid], "round": a.round, "harness": a.harness, "account": a.account,
                    "model": a.model, "effort": a.effort, "commit": a.commit})
        dst = ctx / rk
        shutil.rmtree(dst, ignore_errors=True)
        dst.mkdir(parents=True)
        for name in ("answers.json", "verdict.json", "context_update.md", "notes.md"):
            if (ws / name).exists():
                shutil.copyfile(ws / name, dst / name)
        for py in ws.glob("*.py"):
            if py.stat().st_size < 200_000:
                (dst / "code").mkdir(exist_ok=True)
                shutil.copyfile(py, dst / "code" / py.name)
        (dst / "run.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
        verdict = {}
        if (dst / "verdict.json").exists():
            try:
                verdict = json.loads((dst / "verdict.json").read_text())
            except json.JSONDecodeError:
                verdict = {"parse_error": True}
        append_round(ctx, a.round, a.harness, verdict, dst)
        res = rec["result"]
        S.log(out, {"phase": rk, "video": vid, "ids": qid, "answer": verdict.get("answer"),
                    "decision": verdict.get("decision"), "confidence": verdict.get("confidence"),
                    "wall_s": rec["wall_s"], "cost": res.get("total_cost_usd"), "turns": res.get("num_turns"),
                    "flags": len(rec["audit"]["flags"])})
        if not a.keep_workspace:
            S.wipe(ws)

    with ThreadPoolExecutor(max_workers=a.max_sessions) as ex:
        list(ex.map(lambda q: D._safe(one, q), ids))


def append_round(ctx, k, harness, verdict, dst):
    """Organise the round into CONTEXT.md: the verdict in one block, then the investigator's context update."""
    md = (ctx / "CONTEXT.md").read_text(encoding="utf-8").replace("\n(none yet)\n", "\n")
    upd = (dst / "context_update.md").read_text(encoding="utf-8") if (dst / "context_update.md").exists() else ""
    lines = [f"### Round {k} (harness {harness}; files in context/round{k}/)",
             f"- Answer: {verdict.get('answer')} ({verdict.get('decision')}, confidence {verdict.get('confidence')}"
             f", follows {verdict.get('follows')})",
             f"- Where the answers part: {verdict.get('crux')}",
             f"- Fault proven: {verdict.get('fault_found')}",
             f"- Closure on the prior: {verdict.get('closure_pct')} pct", "", upd.strip(), ""]
    (ctx / "CONTEXT.md").write_text(md.rstrip() + "\n\n" + "\n".join(lines), encoding="utf-8")


def cmd_collect(a):
    out = ROOT / a.out
    rk = f"round{a.round}"
    rows = []
    for ctx in sorted((out / "ctx").glob("*__*")):
        cj = json.loads((ctx / "context.json").read_text())
        v = {}
        if (ctx / rk / "verdict.json").exists():
            try:
                v = json.loads((ctx / rk / "verdict.json").read_text())
            except json.JSONDecodeError:
                v = {}
        run = json.loads((ctx / rk / "run.json").read_text()) if (ctx / rk / "run.json").exists() else {}
        if not run:
            continue
        ans = fnum(v.get("answer"))
        sub = cj["submitted"]
        rows.append({"id": cj["id"], "video": cj["video"], "round": a.round, "harness": run.get("harness", ""),
                     "submitted": sub, "deepseek_median": cj["deepseek_median"],
                     "answer": ans, "ln_vs_submitted": round(math.log(ans / sub), 4) if ans and sub else "",
                     "decision": v.get("decision", ""), "confidence": v.get("confidence", ""),
                     "follows": v.get("follows", ""), "closure_pct": v.get("closure_pct", ""),
                     "crux": str(v.get("crux", ""))[:300], "fault_found": str(v.get("fault_found", ""))[:300],
                     "lesson": str(v.get("lesson", ""))[:400], "cost": (run.get("result") or {}).get("total_cost_usd"),
                     "turns": (run.get("result") or {}).get("num_turns"), "timed_out": run.get("timed_out"),
                     "flags": len((run.get("audit") or {}).get("flags", []))})
    path = out / f"verdicts_{rk}.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["id"])
        w.writeheader()
        w.writerows(rows)
    n = len(rows)
    moved = sum(1 for r in rows if r["ln_vs_submitted"] != "" and abs(r["ln_vs_submitted"]) > 0.02)
    cost = sum(r["cost"] or 0 for r in rows)
    print(f"{n} verdicts, {moved} moved > 2 pct, ${cost:.1f} -> {path}")


def mra_row(a, t):
    r = abs(a - t) / abs(t)
    return sum(r < 1 - th for th in [0.5 + 0.05 * i for i in range(10)]) / 10


_REASK = None


def reask_revert(q, ans):
    """apply_rule.md class 2: a proposal nearer (in log) to the value a validated re-ask replaced than to the re-ask."""
    global _REASK
    if _REASK is None:
        _REASK = {int(r["id"]): (float(r["before"]), float(r["after"]))
                  for r in csv.DictReader(open(R / "fulltest_s27_e2/combine_rows.csv", newline=""))
                  if r["step"] in ("gravity", "u1") and float(r["before"]) > 0 and float(r["after"]) > 0}
    if q not in _REASK or not ans:
        return False
    b, af = _REASK[q]
    return abs(math.log(ans / b)) < abs(math.log(ans / af))


def cmd_proposals(a):
    """Questions of --ids-file whose newest verdict proposes a change that the apply rule would consider (switch / new,
    high / medium, not excluded): the list a verification round re-checks."""
    out = ROOT / a.out
    newest = {}
    for k in sorted(int(p.stem.split("round")[1]) for p in out.glob("verdicts_round*.csv")):
        for r in csv.DictReader(open(out / f"verdicts_round{k}.csv", newline="", encoding="utf-8")):
            newest[int(r["id"])] = r
    exj = json.loads((out / "excluded_physscale.json").read_text())
    excluded = set(exj.get("ids", [])) | set(exj.get("reask_revert_ids", []))
    ids = D.read_ids(a)
    keep = []
    for q in ids:
        r = newest.get(q)
        if not r or r["decision"] not in ("switch", "new") or r["confidence"] not in ("high", "medium"):
            continue
        if q in excluded or reask_revert(q, fnum(r["answer"])):
            continue
        keep.append(q)
    with open(ROOT / a.write, "w", newline="") as f:
        f.write("id\n" + "".join(f"{q}\n" for q in keep))
    print(f"{len(keep)} proposals to verify -> {a.write}")


def cmd_apply(a):
    """The rows a decision rule takes from the rounds (the newest round of a question wins), written as id,value for
    s43_strict_a.py --rsi, and the gray Track A file = the incumbent with those rows replaced, plus the bounds of the
    change per category (every changed row right / wrong against the other value)."""
    out = ROOT / a.out
    led = {int(r["id"]): r for r in csv.DictReader(open(R / "s26_scene_full/ledger.csv", newline="", encoding="utf-8"))}
    ncat = {}
    for r in led.values():
        ncat[r["category"]] = ncat.get(r["category"], 0) + 1
    take = {}
    for k in sorted(int(p.stem.split("round")[1]) for p in out.glob("verdicts_round*.csv")):
        for r in csv.DictReader(open(out / f"verdicts_round{k}.csv", newline="", encoding="utf-8")):
            take[int(r["id"])] = r
    conf_ok = set(a.confidence.split(","))
    ex_path = out / "excluded_physscale.json"
    exj = json.loads(ex_path.read_text()) if ex_path.exists() else {}
    excluded = set(exj.get("ids", [])) | set(exj.get("reask_revert_ids", []))
    rows = []
    for q, r in take.items():
        ans, sub = fnum(r["answer"]), fnum(r["submitted"])
        if not ans or not sub or r["decision"] not in ("switch", "new") or r["confidence"] not in conf_ok:
            continue
        if q in excluded or reask_revert(q, ans):
            continue
        # apply_rule.md 6: a first investigation under harness v2 that no later round re-checked needs high confidence
        if str(r.get("round")) == "1" and r.get("harness") in ("v2", "v3") and r["confidence"] != "high":
            continue
        if abs(math.log(ans / sub)) < a.min_move:
            continue
        if a.cats and led[q]["category"] not in a.cats.split(","):
            continue
        rows.append({"id": q, "value": ans, "cat": led[q]["category"], "submitted": sub, "decision": r["decision"],
                     "confidence": r["confidence"], "ln": round(math.log(ans / sub), 4)})
    rows.sort(key=lambda x: (x["cat"], x["id"]))
    with open(out / a.name, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "value", "cat", "submitted", "decision", "confidence", "ln"])
        w.writeheader()
        w.writerows(rows)
    bounds = {}
    for c in ("S2", "D2", "S3", "D3"):
        rc = [x for x in rows if x["cat"] == c]
        up = sum(mra_row(x["value"], x["value"]) - mra_row(x["submitted"], x["value"]) for x in rc) / ncat[c]
        dn = sum(mra_row(x["value"], x["submitted"]) - mra_row(x["submitted"], x["submitted"]) for x in rc) / ncat[c]
        bounds[c] = {"rows": len(rc), "all_right": round(up, 4), "all_wrong": round(dn, 4)}
    print(json.dumps({"rows": len(rows), "bounds": bounds}, indent=1))
    if a.build:
        src = INCUMBENT
        df = list(csv.DictReader(open(src, newline="", encoding="utf-8")))
        new = {x["id"]: x["value"] for x in rows}
        for r in df:
            if int(r["id"]) in new:
                r["parsed_value"] = f"{new[int(r['id'])]:.6g}"
        od = ROOT / a.build
        od.mkdir(parents=True, exist_ok=True)
        path = od / a.build_name
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(df[0]))
            w.writeheader()
            w.writerows(df)
        import hashlib
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        (od / "manifest.json").write_text(json.dumps({"incumbent": str(INCUMBENT.relative_to(ROOT)), "rsi_rows": a.name,
                                                      "confidence": a.confidence, "min_move": a.min_move,
                                                      "rows": len(rows), "bounds": bounds, "sha256": sha}, indent=1) + "\n")
        print(path, sha)


ID_RE = re.compile(r"(simulation|internet|captured|segment)\w*_\d{3,}|\bq\d{3,}\b|\b\d+(\.\d+)?\s*(m|cm|mm|km|s|m/s|"
                   r"km/h|m/s\^?2|px|pct|%)\b", re.I)


def cmd_lint(a):
    """Lessons may hold procedure only: no video or question ids, no measured values with units."""
    text = (ROOT / a.out / "harness" / a.harness / "LESSONS.md").read_text(encoding="utf-8")
    bad = [(i + 1, m.group(0)) for i, line in enumerate(text.splitlines()) for m in ID_RE.finditer(line)]
    for ln, s in bad:
        print(f"line {ln}: {s}")
    print("lint", "FAIL" if bad else "ok", f"({len(bad)} hits)")
    raise SystemExit(1 if bad else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--ids")
    b.add_argument("--ids-file")
    b.add_argument("--out", default="results/s43_rsi")
    b.add_argument("--force", action="store_true")
    r = sub.add_parser("run")
    r.add_argument("--round", type=int, required=True)
    r.add_argument("--harness", required=True)
    r.add_argument("--ids")
    r.add_argument("--ids-file")
    r.add_argument("--out", default="results/s43_rsi")
    r.add_argument("--account", required=True, choices=sorted(S.ACCOUNTS))
    r.add_argument("--guard")
    r.add_argument("--workdir", type=Path, default=Path("/private/tmp/qp_blind/s43_rsi"))
    r.add_argument("--model", default="claude-opus-5-5")
    r.add_argument("--effort", default="high")
    r.add_argument("--max-turns", type=int, default=150)
    r.add_argument("--timeout", type=int, default=50)
    r.add_argument("--max-sessions", type=int, default=8)
    r.add_argument("--cache-ttl", choices=("5m", "1h"))
    r.add_argument("--redo", action="store_true")
    r.add_argument("--keep-workspace", action="store_true")
    c = sub.add_parser("collect")
    c.add_argument("--round", type=int, required=True)
    c.add_argument("--out", default="results/s43_rsi")
    li = sub.add_parser("lint")
    li.add_argument("--harness", required=True)
    li.add_argument("--out", default="results/s43_rsi")
    ap_ = sub.add_parser("apply")
    ap_.add_argument("--out", default="results/s43_rsi")
    ap_.add_argument("--confidence", default="high,medium")
    ap_.add_argument("--min-move", type=float, default=0.02)
    ap_.add_argument("--name", default="apply.csv")
    ap_.add_argument("--build", help="folder for the gray Track A file (incumbent + the applied rows)")
    ap_.add_argument("--build-name", default="track_a_s43_rsi.csv")
    ap_.add_argument("--cats", help="only these categories, e.g. S3,D2")
    pr = sub.add_parser("proposals")
    pr.add_argument("--ids")
    pr.add_argument("--ids-file")
    pr.add_argument("--out", default="results/s43_rsi")
    pr.add_argument("--write", required=True)
    an = sub.add_parser("annotate")
    an.add_argument("--out", default="results/s43_rsi")
    a = ap.parse_args()
    {"build": cmd_build, "run": cmd_run, "collect": cmd_collect, "lint": cmd_lint, "apply": cmd_apply,
     "annotate": cmd_annotate, "proposals": cmd_proposals}[a.cmd](a)


if __name__ == "__main__":
    main()
