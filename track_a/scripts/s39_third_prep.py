"""Series 39, run 39_3 (2026-10-24, session 28b2ba80, login A): select
the scored Track A rows for a third per-question voice and write the id lists.

Rule (fixed before any session runs, per question only): a scored row is selected when its two current per-question
answers - the Opus line (E2; U1 for S3 lab motion, which reads the direction model) and the DeepSeek-1017 + SAM 3
median of the same question (B9lat; B9const x 1.19/1.25 for D3 lab motion, Track A's D3 lab constant) - differ by more
than |ln| .1. Rows whose Opus answer came from a special-reading re-ask (real-scale 26_59 / 27_6 / 30_5, the gravity
re-asks, the prop table), the compliance audit's OUT rows and rows the DeepSeek line lacks are left out. The third voice
is a fresh Opus 5.5 session of that one question with the SAM 3 mask as the required second route (35_2: +.023 on 32
labelled rows); its answer enters as the third member of a per-question median.

    python scripts/s39_third_prep.py --out results/s39_third
"""
import argparse
import csv
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TIER_COST = {0: 1.37, 1: 1.53, 2: 0.40, 3: 0.35, 4: 0.49, 5: 0.39, 6: 0.60}  # 26_30 phase-2 means, USD API-eq
SAM3_X = 1.3  # 35_2: $0.49 with --sam3-required against $0.38 plain
ORDER = ["S3", "D3", "D2", "S2"]


def qkind(q):
    q = q.lower()
    if "acceler" in q:
        return "acc"
    if "speed" in q or "velocit" in q:
        return "vel"
    if re.search(r"displac|travel|path|distance (?:covered|moved)|how far", q):
        return "disp"
    if "distance" in q:
        return "dist"
    return "size"


def tier(src, cat):
    if src == "lab":
        return 6
    if src == "internet":
        return 2 if cat.startswith("S") else 3
    if cat.endswith("3"):
        return 0 if cat == "S3" else 1
    return 4 if cat == "S2" else 5


def reask_ids():
    ids = set()
    for d in ("s26_reask_1020", "s30_realscale", "s27_gravity", "s27_plaus_reask"):
        f = ROOT / "results" / d / "attempts.tsv"
        if f.exists():
            for r in csv.DictReader(open(f), delimiter="\t"):
                if r.get("answer") and r["answer"] != "{}":
                    ids |= {int(x) for x in str(r["ids"]).split(",")}
    for r in csv.DictReader(open(ROOT / "results/fulltest_s27_e2/combine_rows.csv")):
        if r["step"] in ("gravity", "table"):
            ids.add(int(r["id"]))
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--thr", type=float, default=0.1)
    a = ap.parse_args()
    ds = pd.DataFrame(json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text()))
    ds["id"] = ds.row_idx + 1
    ds["cat"] = [("S" if it[0] == "S" else "D") + vt[1] for it, vt in zip(ds.inference_type, ds.video_type)]
    ds["kind"] = ds.question.map(qkind)
    ds["tier"] = [tier(s, c) for s, c in zip(ds.video_source, ds.cat)]
    scored = set(pd.read_csv(ROOT / "results/s26_scene_full/ledger.csv").id)
    out_rows = {int(r["id"]) for r in csv.DictReader(open(ROOT / "results/fulltest_s34_legit_a/changes.csv"))
                if r["group"] in ("human", "lenh", "weak")} | {1668}
    rd = lambda p: pd.read_csv(ROOT / p).set_index("id").parsed_value
    E2, U1 = rd("results/fulltest_s27_e2/track_a_s27_e2.csv"), rd("results/fulltest_s30_u1/track_a_s30_u1.csv")
    BL, BC = rd("results/fulltest_s37_b9lat/track_b_s33_b9lat.csv"), rd("results/fulltest_s37_b9const/track_b_s33_b9const.csv")
    skip = reask_ids() | out_rows
    rows = []
    for r in ds.itertuples():
        if r.id not in scored or r.id in skip:
            continue
        motion = r.video_source == "lab" and r.kind in ("vel", "disp", "acc")
        if motion and r.cat == "S3":
            av, bv = U1[r.id], BL[r.id]
        elif motion and r.cat == "D3":
            av, bv = E2[r.id], BC[r.id] * 1.19 / 1.25
        else:
            av, bv = E2[r.id], BL[r.id]
        if not (av > 0 and bv > 0):
            continue
        lr = abs(np.log(av / bv))
        if lr > a.thr:
            rows.append({"id": r.id, "video": r.video_id, "cat": r.cat, "source": r.video_source, "kind": r.kind,
                         "tier": r.tier, "A": av, "B": bv, "ln_ab": round(lr, 4),
                         "cost": round(TIER_COST[r.tier] * SAM3_X, 2)})
    S = pd.DataFrame(rows)
    S["order"] = S.cat.map({c: i for i, c in enumerate(ORDER)})
    S = S.sort_values(["order", "ln_ab"], ascending=[True, False]).drop(columns="order")
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    S.to_csv(out / "selection.csv", index=False)
    for c in ORDER:
        S[S.cat == c][["id"]].to_csv(out / f"ids_{c}.csv", index=False)
    print(S.groupby(["cat", "source"]).agg(n=("id", "size"), cost=("cost", "sum")).round(0).to_string())
    print(S.groupby("cat").agg(n=("id", "size"), cost=("cost", "sum")).round(0).to_string())
    print("total", len(S), "rows, $", round(S.cost.sum()), "API-eq; skipped special-reading rows", len(skip))
    # 39_4: every scored 2D simulation / segmentation speed or acceleration row (method_queue 62's population: the 35_2
    # pilot's gain sat on these), whatever the two answers say - a population read, not a disagreement selection.
    M = ds[ds.id.isin(scored) & ~ds.id.isin(skip) & ds.cat.isin(["S2", "D2"])
           & ds.video_source.isin(["simulation", "segmentation"]) & ds.kind.isin(["vel", "acc"])].copy()
    M["cost"] = [round(TIER_COST[t] * SAM3_X, 2) for t in M.tier]
    M = M.sort_values(["cat", "video_id", "id"], ascending=[False, True, True])
    M[["id", "video_id", "cat", "video_source", "kind", "tier", "cost"]].to_csv(out / "ids_2dmotion.csv", index=False)
    print("39_4 2D motion:", M.groupby(["cat", "video_source", "kind"]).size().to_dict(), "$", round(M.cost.sum()))


if __name__ == "__main__":
    main()
