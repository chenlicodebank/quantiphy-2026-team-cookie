"""Series 43 (2026-10-26, session 0c8cbddf): the strict Track A file - the compliant per-category splice with every gray
item taken out, optionally with per-question RSI answers on top.

User, 2026-10-26 ~00:00 UTC: "ensure we have one valid result on track A ... grey area (such as from validation set and
quantiphy paper) are not sure if valid; so prepare for both". Taken out of the splice (S2 #213 F1 / D2 #215 F3 /
S3, D3 #214 F2):
- the paper's lab prop table (E2 step "table": S3 53 / D3 144 rows) - each row goes back to its pre-table E2 value and
  then through the same per-question fusion F2 gave every other lab size row (S3: with B9lat x1.03, wA .5; D3: with
  B9const, wA .6; cap .4);
- the human-check choices of 2026-10-21 (q248, q282, q618, q1668, q1670, q1934, q3051: a person chose among the agent's
  readings) - back to the #200 values; q879 keeps 5.7, the agent's own measurement recomputed (its notes wrote 57.0);
- the validation catalog snap is not applied (the splice predates it).
`--rsi <csv id,value>` overlays per-question RSI answers on rows that are not human-check rows.

    python scripts/s43_strict_a.py --out results/fulltest_s43_strict_a [--rsi results/s43_rsi/apply_round1.csv]
"""
import argparse
import hashlib
import json
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "results"
BASE = {"S2": "fulltest_s39_f1/track_a_s39_f1.csv", "D2": "fulltest_s39_f3/track_a_s39_f3.csv",
        "S3": "fulltest_s39_f2/track_a_s39_f2.csv", "D3": "fulltest_s39_f2/track_a_s39_f2.csv"}
HUMAN = [248, 282, 618, 1668, 1670, 1934, 3051]
FUSE = {"S3": ("fulltest_s37_b9lat/track_b_s33_b9lat.csv", 1.03, 0.5),
        "D3": ("fulltest_s37_b9const/track_b_s33_b9const.csv", 1.0, 0.6)}
CAP = 0.4


def series(path):
    return pd.read_csv(R / path).set_index("id").parsed_value.astype(float)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", default="track_a_s43_strict.csv")
    ap.add_argument("--rsi")
    a = ap.parse_args()
    led = pd.read_csv(R / "s26_scene_full/ledger.csv").set_index("id")
    first = pd.read_csv(R / BASE["S2"])
    out = first.copy().set_index("id")
    val = out.parsed_value.astype(float).copy()
    for c, p in BASE.items():
        ids = led.index[led.category == c]
        val.loc[ids] = series(p).reindex(ids).values
    splice = val.copy()
    steps = []
    cr = pd.read_csv(R / "fulltest_s27_e2/combine_rows.csv")
    for _, r in cr[cr.step == "table"].iterrows():
        q, c = int(r["id"]), r["cat"]
        bfile, bscale, wa = FUSE[c]
        b = series(bfile).get(q, np.nan) * bscale
        v = float(r["before"])
        if np.isfinite(b) and b > 0 and abs(np.log(v / b)) <= CAP:
            v = float(np.exp(wa * np.log(v) + (1 - wa) * np.log(b)))
        steps.append({"id": q, "cat": c, "step": "table_out", "before": val[q], "after": round(v, 6)})
        val[q] = round(v, 6)
    v200 = series("fulltest_s26_reask_full/track_a_s26_reask_full.csv")
    for q in HUMAN:
        steps.append({"id": q, "cat": led.category[q], "step": "human_out", "before": val[q], "after": v200[q]})
        val[q] = v200[q]
    if a.rsi:
        rsi = pd.read_csv(ROOT / a.rsi).set_index("id")["value"].astype(float)
        for q, v in rsi.items():
            if q in HUMAN or q not in led.index:
                continue
            steps.append({"id": q, "cat": led.category[q], "step": "rsi", "before": val[q], "after": v})
            val[q] = v
    od = ROOT / a.out
    od.mkdir(parents=True, exist_ok=True)
    out["parsed_value"] = val.reindex(out.index).values
    # the upload keeps the template's text column in step with the value
    if "prediction" in out.columns:
        out["prediction"] = out["parsed_value"].map(lambda x: f"{x:.6g}")
    path = od / a.name
    out.reset_index().to_csv(path, index=False)
    pd.DataFrame(steps).to_csv(od / "changes.csv", index=False)
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    diff = (val.reindex(splice.index) != splice)
    man = {"written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "base": BASE, "rsi": a.rsi,
           "steps": pd.DataFrame(steps).groupby(["step", "cat"]).size().reset_index().values.tolist() if steps else [],
           "rows_vs_splice": int(diff.sum()), "file": str(path.relative_to(ROOT)), "sha256": sha}
    (od / "manifest.json").write_text(json.dumps(man, indent=1) + "\n")
    print(json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
