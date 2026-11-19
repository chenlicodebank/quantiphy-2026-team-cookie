"""Series 37 self-audit of a Track B build (session 05e6b3c8, 2026-10-24): every row from its own question's runs.

Checks, independently of the builder's own bookkeeping:
  1. Shape: 3,289 rows in template order, every value finite and positive.
  2. Every per-question value: for each id, the median of the answers in q/<video>__<id>/r*.json of the run folders
     (only that question's folder is read), times the physical-scale k when aggregate.csv says the rule fired (k
     recomputed from that question's own 37_3 records), equals aggregate.csv's median.
  3. Every row the chain set (changes.csv) equals that per-question value times the factor its reason names (x1, x k,
     x s, or the row's own F from results/s33_lablat_open/factors.csv); open-geometry fills are listed apart.
  4. Every row outside changes.csv equals the L5 base the build names.
Prints counts per reason and every mismatch; exit 1 on any mismatch.

    python scripts/s37_audit.py results/fulltest_s37_<name>
"""
import json
import math
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import s37_final_b as S  # noqa: E402


def main():
    out = ROOT / sys.argv[1]
    man = json.loads((out / "manifest.json").read_text())
    f = pd.read_csv(out / man["file"]).set_index("id").parsed_value.astype(float)
    base = pd.read_csv(ROOT / man["base"]).set_index("id").parsed_value.astype(float)
    tmpl = pd.read_csv(ROOT / man["base"]).id.tolist()
    bad = []
    if pd.read_csv(out / man["file"]).id.tolist() != tmpl or len(f) != 3289:
        bad.append("shape: ids or order differ from the base")
    if not (np.isfinite(f) & (f > 0)).all():
        bad.append("non-finite or non-positive values")
    R = S.runs([d for d in man["runs"].split(",") if d], int(man.get("max_k") or 99))
    T = S.runs([d for d in man["runs"].split(",") if d], int(man.get("max_k") or 99), tagged=True)
    agg = pd.read_csv(out / "aggregate.csv").groupby("id").last()
    phys = S.scale_checks(man["physcheck"]) if man.get("physcheck") else {}
    cur = pd.DataFrame(json.loads(S.B.CURRENT.read_text()))
    prior_of = dict(zip(cur.row_idx + 1, cur.prior))
    per = {}
    for i, v in R.items():
        x = float(np.median(v))
        if i in agg.index and agg.loc[i, "rule"] == "physical_scale":
            own = [y for key, y in T.get(i, {}).items() if key.rsplit(":", 1)[0] != man["physcheck"]]
            x = S.physical(phys.get(i, []), own, prior_of.get(i, ""))[0]
        per[i] = x
        if i not in agg.index or not math.isclose(agg.loc[i, "median"], x, rel_tol=1e-9):
            bad.append(f"aggregate {i}: recomputed {x} vs aggregate.csv {agg.loc[i, 'median'] if i in agg.index else None}")
    ch = pd.read_csv(out / "changes.csv")
    fac = pd.read_csv(ROOT / "results/s33_lablat_open/factors.csv").set_index("id").F
    counts = {}
    for _, r in ch.iterrows():
        i, why = int(r.id), r.reason
        counts[why] = counts.get(why, 0) + 1
        if not why.startswith("ds_"):
            continue
        m = re.search(r"_x([\d.]+)$", why)
        mult = float(fac.loc[i]) if why.endswith("_xF") else float(m.group(1)) if m else 1.0
        want = per.get(i, float("nan")) * mult
        if not math.isclose(r.after, want, rel_tol=1e-9) or not math.isclose(f.loc[i], want, rel_tol=1e-9):
            bad.append(f"row {i} ({why}): file {f.loc[i]} vs per-question value x {mult} = {want}")
    rest = sorted(set(f.index) - set(ch.id))
    diff = [i for i in rest if not math.isclose(f.loc[i], base.loc[i], rel_tol=1e-12)]
    if diff:
        bad.append(f"{len(diff)} rows outside changes.csv differ from the base, e.g. {diff[:5]}")
    print(json.dumps({"file": man["file"], "rows_by_reason": counts, "rows_outside_changes": len(rest),
                      "questions_with_runs": len(R), "physical_scale_rows": int((agg.rule == "physical_scale").sum()),
                      "mismatches": len(bad)}, indent=1))
    for b in bad[:30]:
        print("MISMATCH", b)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
