#!/usr/bin/env python
"""26_50: lab motion calibration over the best Track A rows per category.

The lab motion labels (speeds, accelerations, displacements, distances travelled) are built from hand-clicked
object centres and the Orbbec ToF depth at the click, differenced frame to frame (QuantiPhy App. D.2), so they
carry the sensor's noise; the Claude agents measure clean motion and read low against them. Evidence before any
board read: the 26_10 agent on the 18 labelled lab motion rows (results/s26_ccagent_val/val_scored.csv) has
label / answer median 1.34, and x1.30 lifts those rows .650 -> .733 (leave-one-video-out .650 -> .683); the public
VihanAggarwal repo's class probes on its own Opus 5.5 answers (research/PROBES.md "m11 class calibration probes",
2026-10-19) read lab motion x1.06 at S3 +.005 / D3 +.001 and x0.94 at S3 -.009 / D3 -.002 (their parabola peaks
near x1.10), with their lab focal at 711 px against our 763, i.e. their lateral speeds already 7 pct higher.

Build: #186 on S2 / D2 (control), #193 (26_41 / A2) on S3 / D3, then every lab S3 / D3 row whose question asks
a velocity, speed, acceleration, displacement or distance travelled is multiplied by --s3 / --d3. Rows that hold
a stated value from another video (Series 24 famprior rows, kept in #186) are left alone. One value per row; each
answer is a function of its own answer only (per-question rule: a class constant, no other question's input).

Usage: python scripts/build_s26_labcal.py --s3 1.15 --d3 1.10 --out results/fulltest_s26_labcal1 --name track_a_s26_labcal1.csv
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MOTION = re.compile(r"veloc|velolicty|speed|accelerat|displacement|distance\s+travel|travel+ed|distance\s+moved", re.I)
# Lab object sizes (ruler-measured labels); the agents' pixel extent x own depth / 763 px reads them low on val
# (20 rows: label / answer median 1.05, x1.04 .915 -> .950, leave-one-video-out .945).
SIZE = re.compile(r"\b(?:diameter|height|length|width|size|thickness|long|wide|tall|radius)\b", re.I)
NOT_SIZE = re.compile(r"distance|rebounce|rebound|maximum|minimum|reached|from the (?:floor|ground|desk|table)|above", re.I)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="results/fulltest_s26_ccagent_full/track_a_s26_ccagent_full.csv")
    ap.add_argument("--s3d3", default="results/fulltest_s26_conf_a2/track_a_s26_conf_a2.csv")
    ap.add_argument("--famprior", default="results/fulltest_s24_famprior/famprior_rows.csv")
    ap.add_argument("--template", default="data/test/template_local.csv")
    ap.add_argument("--s3", type=float, required=True)
    ap.add_argument("--d3", type=float, required=True)
    ap.add_argument("--d2", type=float, default=1.0, help="lab motion factor for the few lab D2 rows (2D lab clips)")
    ap.add_argument("--size-s3", type=float, default=1.0)
    ap.add_argument("--size-d3", type=float, default=1.0)
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", required=True)
    a = ap.parse_args()

    t = pd.read_csv(ROOT / a.template)
    t["cat"] = t.inference_type.str[0] + t.video_type.str[1]
    base = pd.read_csv(ROOT / a.base)
    s3d3 = pd.read_csv(ROOT / a.s3d3)
    assert (base.id.values == t.id.values).all() and (s3d3.id.values == t.id.values).all()
    fam = set(pd.read_csv(ROOT / a.famprior).id)

    out = base.copy()
    take = t.cat.isin(["S3", "D3"]).values
    out.loc[take, "parsed_value"] = s3d3.loc[take, "parsed_value"].values
    from_a2 = int((out.parsed_value.values != base.parsed_value.values).sum())

    motion = (t.video_source.eq("lab") & t.cat.isin(["S3", "D3", "D2"]) & t.question.str.contains(MOTION)
              & ~t.id.isin(fam)).values
    factor = np.where(t.cat.eq("S3"), a.s3, np.where(t.cat.eq("D2"), a.d2, a.d3))
    old = out.parsed_value.values.copy()
    out.loc[motion, "parsed_value"] = old[motion] * factor[motion]
    size = (t.video_source.eq("lab") & t.cat.isin(["S3", "D3"]) & t.question.str.contains(SIZE)
            & ~t.question.str.contains(MOTION) & ~t.question.str.contains(NOT_SIZE) & ~t.id.isin(fam)).values
    sfactor = np.where(t.cat.eq("S3"), a.size_s3, a.size_d3)
    out.loc[size, "parsed_value"] = old[size] * sfactor[size]
    assert np.isfinite(out.parsed_value).all() and (out.parsed_value > 0).all()

    dest = ROOT / a.out
    dest.mkdir(parents=True, exist_ok=True)
    out.to_csv(dest / a.name, index=False)
    ch = t.loc[motion, ["id", "video_id", "cat", "inference_type", "question"]].copy()
    ch["before"] = old[motion]
    ch["after"] = out.parsed_value.values[motion]
    ch.to_csv(dest / "changes.csv", index=False)
    man = {
        "run": "26_50",
        "base": a.base, "s3d3_from": a.s3d3, "famprior": a.famprior,
        "factors": {"S3": a.s3, "D3": a.d3, "D2": a.d2},
        "size_factors": {"S3": a.size_s3, "D3": a.size_d3},
        "rows_from_a2_differing_from_base": from_a2,
        "lab_motion_rows": {c: int(((t.cat == c).values & motion).sum()) for c in ["S3", "D3", "D2"]},
        "lab_size_rows": {c: int(((t.cat == c).values & size).sum()) for c in ["S3", "D3"]},
        "regex": MOTION.pattern,
        "sha256": {a.base: sha(ROOT / a.base), a.s3d3: sha(ROOT / a.s3d3), f"{a.out}/{a.name}": sha(dest / a.name)},
    }
    (dest / "manifest.json").write_text(json.dumps(man, indent=1))
    print(json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
