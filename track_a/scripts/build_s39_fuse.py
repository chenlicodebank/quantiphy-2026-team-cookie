"""Series 39 (2026-10-24, session 28b2ba80, login A): cross-model fusion for Track A.

Each scored row's Track A answer (Opus per-question line, E2) is combined with the same question's Track B answer (the
per-question median of DeepSeek-1017 + SAM 3 runs, B9lat, #211) by a weighted geometric mean,
    value = exp(wA * ln A + (1 - wA) * ln B),
with one weight per category. Both inputs are per-question answers (each made from the question's own video, text,
prior and depth_info only), so the fusion is a per-question combination of model runs of the same question, which the
per-question rule allows (repeats / medians); Track A may use any model. Lab rows are left out (their label process,
prop table and motion factors differ between the two lines and are read separately); so are the compliance audit's OUT
rows and the 6 D2 lab rows of U1.

    python scripts/build_s39_fuse.py --out results/fulltest_s39_f1 --name track_a_s39_f1.csv --w S3=0.5,D3=0.7,D2=0.7
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import probe_lib as pl  # noqa: E402

A_FILE = "results/fulltest_s27_e2/track_a_s27_e2.csv"
B_FILE = "results/fulltest_s37_b9lat/track_b_s33_b9lat.csv"
U1_D2LAB = {2267, 2270, 2272, 2275, 2277, 2280}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=A_FILE)
    ap.add_argument("--b", default=B_FILE)
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--w", required=True, help="per-category Track A weight, e.g. S3=0.5,D3=0.7 (absent = untouched)")
    ap.add_argument("--sources", default="simulation,segmentation,internet", help="video sources fused")
    ap.add_argument("--max-ratio", type=float, default=0.0, help="fuse only rows with |ln A/B| <= this (0 = no cap)")
    a = ap.parse_args()
    w = {k: float(v) for k, v in (kv.split("=") for kv in a.w.split(","))}
    srcs = set(a.sources.split(","))
    ds = pd.DataFrame(json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text()))
    ds["id"] = ds.row_idx + 1
    ds["cat"] = [("S" if it[0] == "S" else "D") + vt[1] for it, vt in zip(ds.inference_type, ds.video_type)]
    scored = set(pd.read_csv(ROOT / "results/s26_scene_full/ledger.csv").id)
    import csv
    out_rows = {int(r["id"]) for r in csv.DictReader(open(ROOT / "results/fulltest_s34_legit_a/changes.csv"))
                if r["group"] in ("human", "lenh", "weak")} | {1668}
    base = pd.read_csv(ROOT / a.base)
    bv = pd.read_csv(ROOT / a.b).set_index("id").parsed_value
    meta = ds.set_index("id")
    changes = []
    vals = base.parsed_value.copy()
    for k, (i, av) in enumerate(zip(base.id, base.parsed_value)):
        if i not in scored or i in out_rows or i in U1_D2LAB:
            continue
        c, src = meta.cat[i], meta.video_source[i]
        if c not in w or src not in srcs:
            continue
        b = bv.get(i)
        if b is None or not np.isfinite(b) or b <= 0 or av <= 0:
            continue
        r = abs(np.log(av / b))
        if a.max_ratio and r > a.max_ratio:
            continue
        v = float(np.exp(w[c] * np.log(av) + (1 - w[c]) * np.log(b)))
        v = float(f"{v:.6g}")
        if v != av:
            vals.iloc[k] = v
            changes.append({"id": i, "cat": c, "source": src, "A": av, "B": b, "after": v, "ln_ab": round(r, 4)})
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    base = base.assign(parsed_value=vals)
    base.to_csv(out / a.name, index=False)
    ch = pd.DataFrame(changes)
    ch.to_csv(out / "changes.csv", index=False)
    sha = hashlib.sha256((out / a.name).read_bytes()).hexdigest()
    man = {"series": "39", "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "base": a.base,
           "b": a.b, "weights_A": w, "sources": sorted(srcs), "max_ratio": a.max_ratio, "rows_changed": len(ch),
           "by_cat": ch.cat.value_counts().to_dict() if len(ch) else {}, "file": f"{a.out}/{a.name}", "sha256": sha}
    (out / "manifest.json").write_text(json.dumps(man, indent=1))
    print(json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
