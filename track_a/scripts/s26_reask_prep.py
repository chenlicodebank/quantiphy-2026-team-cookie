"""Series 26, run 26_59 (2026-10-20, user go "do all"): prepare the --real-scale re-ask of the compliant Track A rows the
26_30 traces point at (method_queue item 38, baselines.md 2026-10-20 11:00-12:15 UTC).

Selection is by question type and video, never by which answers look wrong, so a board read of the result is clean:
- fixed character origin: every scored row of a 3D render whose depth_info gives a walking person's or animal's
  distance at two times changing by under 0.1 m/s (s26_trace_signals.py);
- flyers: bare "length" / "width" questions about birds, dragons, bats, butterflies and fixed-wing aircraft ("body
  length" and "wingspan" questions are unambiguous and stay);
- degenerate prior: the two internet clips whose gravity prior falls on a ball that only rolls (internet_0065 / 0066,
  per their own notes);
- lane: "width of the lane" in simulation / segmentation videos.
S2 rows are left out: too few for a category read of their own (the 30-row floor).

Stage 1 is the labelled check: the stated-fact rows inside the selection (their sibling-stated values are LABELS for
the gate, never inputs), minus the four suspect facts of the audit. Stage 2 is the rest, run only if the preregistered
gate (scripts/gate_26_59.py) passes. Out dir = copies of the 26_30 scene records, question folders and clip files, so
results/s26_scene_full stays untouched; streams and attempts are the new run's own.

    python scripts/s26_reask_prep.py --out results/s26_reask_1020
    python scripts/s26_reask_prep.py --val --out results/s26_reask_1020_val    # two labelled validation videos
"""
import argparse
import json
import re
import shutil
from pathlib import Path

import pandas as pd

from s26_trace_signals import CREATURE, depth_rates

ROOT = Path(__file__).resolve().parents[1]
FLYER = re.compile(r"\b(bird|birds|eagle|dragon|bat|butterfly|airplane|aeroplane|aircraft|jet|plane)\b(?!-)", re.I)
BARE_DIM = re.compile(r"\b(length|width)\b", re.I)
UNAMBIGUOUS = re.compile(r"body length|wingspan|wing span|xy-plane|flight path|distance", re.I)
DEGENERATE = ("internet_0065", "internet_0066")
SUSPECT_FACTS = {791, 1083, 1788, 1792}
VAL_VIDEOS = ("simulation_0060", "simulation_0193")
TRIGGER = "real-scale re-ask (26_59, --real-scale, user go 2026-10-20)"


def select(ledger, sub):
    M = ledger.merge(sub, on="id")
    fixed = set()
    for vid, text in M.drop_duplicates("video")[["video", "depth_text"]].itertuples(index=False):
        for obj, rate in depth_rates(text).items():
            if re.search(CREATURE, obj) and "bike" not in obj and abs(rate) < 0.1:
                fixed.add(vid)
    why = {}
    for r in M.itertuples(index=False):
        w = []
        if r.video in fixed:
            w.append("fixed_origin")
        if FLYER.search(r.question) and BARE_DIM.search(r.question) and not UNAMBIGUOUS.search(r.question):
            w.append("flyer_axes")
        if r.video in DEGENERATE:
            w.append("degenerate_prior")
        if r.source in ("simulation", "segmentation") and re.search(r"width of the lane", r.question, re.I):
            w.append("lane")
        if w and r.category != "S2":
            why[int(r.id)] = ",".join(w)
    return M, why


def copy_video(src, dst, vid, qids, asked):
    (dst / "videos" / vid).mkdir(parents=True, exist_ok=True)
    if not (dst / "videos" / vid / "scene").exists():
        shutil.copytree(src / "videos" / vid / "scene", dst / "videos" / vid / "scene")
        for f in ("run1.json",):
            if (src / "videos" / vid / f).exists():
                shutil.copyfile(src / "videos" / vid / f, dst / "videos" / vid / f)
    answers = {}
    for q in qids:  # the clip file holds every answer of the video, so the run never re-asks an unselected question
        answers[str(q)] = json.loads((src / "q" / f"{vid}__{q}" / "answers.json").read_text())[str(q)]
    for q in asked:  # only the re-asked questions' folders are copied (and later hold the new attempt)
        if not (dst / "q" / f"{vid}__{q}").exists():
            shutil.copytree(src / "q" / f"{vid}__{q}", dst / "q" / f"{vid}__{q}")
    (dst / "clips" / vid).mkdir(parents=True, exist_ok=True)
    (dst / "clips" / vid / "answers.json").write_text(
        json.dumps({k: answers[k] for k in sorted(answers, key=int)}, indent=1) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", default="results/s26_scene_full")
    ap.add_argument("--build", default="results/fulltest_s26_compliant/track_a_s26_compliant.csv")  # #199
    ap.add_argument("--facts", default="results/fulltest_s24_famprior/famprior_detail.csv")
    ap.add_argument("--val", action="store_true", help="prepare the labelled validation regression check instead")
    ap.add_argument("--val-run", default="results/s26_scene_val")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = ROOT / a.out
    if out.exists():
        raise SystemExit(f"{out} exists; use a new out dir")
    out.mkdir(parents=True)

    if a.val:
        src = ROOT / a.val_run
        cmp_ = pd.read_csv(src / "val_compare.csv")
        rows = cmp_[cmp_.video_id.isin(VAL_VIDEOS)]
        for vid, g in rows.groupby("answered_on"):
            copy_video(src, out, vid, sorted(g.id), sorted(g.id))
        rows[["id", "video_id", "answered_on", "category", "gt", "perq", "question"]].to_csv(out / "selection.csv",
                                                                                             index=False)
        (out / "events.txt").write_text(",".join(sorted(rows.answered_on.unique())) + "\n")
        (out / "rerun_val.json").write_text(json.dumps({"trigger": TRIGGER + " - validation check",
                                                        "ids": sorted(int(i) for i in rows.id)}, indent=1) + "\n")
        print(f"validation check: {len(rows)} questions on {rows.answered_on.nunique()} videos")
        return

    src = ROOT / a.run
    ledger = pd.read_csv(src / "ledger.csv")
    sub = pd.read_csv(ROOT / a.build)[["id", "parsed_value", "depth_info"]].rename(
        columns={"parsed_value": "s199", "depth_info": "depth_text"})
    M, why = select(ledger, sub)
    facts = pd.read_csv(ROOT / a.facts)[["id", "parsed_value", "source_line"]].rename(columns={"parsed_value": "fact"})
    S = M[M.id.isin(why)].merge(facts, on="id", how="left")
    S["reasons"] = S.id.map(why)
    S["stage"] = [1 if (pd.notna(f) and i not in SUSPECT_FACTS) else 2 for i, f in zip(S.id, S.fact)]
    for vid in sorted(S.video.unique()):
        copy_video(src, out, vid, sorted(ledger[ledger.video == vid].id), sorted(S[S.video == vid].id))
    S[["id", "video", "source", "category", "kind", "question", "prior", "reasons", "stage", "answer", "s199", "fact",
       "source_line", "cost"]].to_csv(out / "selection.csv", index=False)
    (out / "events.txt").write_text(",".join(sorted(S.video.unique())) + "\n")
    for st in (1, 2):
        ids = sorted(int(i) for i in S[S.stage == st].id)
        (out / f"rerun_stage{st}.json").write_text(json.dumps({"trigger": TRIGGER + f" - stage {st}", "ids": ids},
                                                              indent=1) + "\n")
    guard = json.loads((src / "guard_b.json").read_text())
    guard["note"] = ("26_59 --real-scale re-ask, pool B, started from a session opened on login B (run rule 3). "
                     "Caps as 26_30's pool B: max_5h 0.90, max_7d 0.85. Cost tables = 26_30's observed ones.")
    (out / "guard_b.json").write_text(json.dumps(guard, indent=1) + "\n")
    by = S.groupby(["stage", "category"]).size().unstack(fill_value=0)
    print(by.to_string())
    print(f"{len(S)} questions on {S.video.nunique()} videos; first-run cost ${S.cost.sum():.0f} "
          f"(stage 1 ${S[S.stage == 1].cost.sum():.0f}, stage 2 ${S[S.stage == 2].cost.sum():.0f})")
    print(S.reasons.value_counts().to_string())


if __name__ == "__main__":
    main()
