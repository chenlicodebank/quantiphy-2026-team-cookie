"""27_17 (2026-10-22, session 6e6e97e4): the Track A entry as a per-category choice of the series-27 components.

The series-27 builds form one chain, each step a disjoint set of rows (row sets checked when the chain was built):
    #203 -> U1 (27_8: valfam, real-scale re-asks, length-horizontal) -> U2a (27_10: gravity-prior re-asks)
         -> U2 (27_15: S3 lab speeds sqrt(v^2 + c^2)) -> U3 (27_11: lab prop table) -> U4 (27_13: lab displacements x1.0)
Categories are scored separately, so each upload's category delta reads that step's rows in that category. This
script overlays, category by category, only the steps the board read as gains:

    python scripts/build_s27_combine.py --keep "S2:u1;D2:u1,gravity;S3:u1,table;D3:u1,gravity,table,labdisp" \\
        --out results/fulltest_s27_entry --name track_a_s27_entry.csv

A step's row value is the one its own build wrote (a later step computed on top of an earlier one keeps that value even
when the earlier step is dropped; the steps touch disjoint rows, so this does not arise in the current chain).
"""
import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CHAIN = [  # (step, build before, build after)
    ("u1", "results/fulltest_s26_clean_fixes/track_a_s26_clean_fixes.csv", "results/fulltest_s27_u1/track_a_s27_u1.csv"),
    ("gravity", "results/fulltest_s27_u1/track_a_s27_u1.csv", "results/fulltest_s27_u2a/track_a_s27_u2.csv"),
    ("noise", "results/fulltest_s27_u2a/track_a_s27_u2.csv", "results/fulltest_s27_u2/track_a_s27_u2.csv"),
    ("table", "results/fulltest_s27_u2/track_a_s27_u2.csv", "results/fulltest_s27_u3/track_a_s27_u3.csv"),
    ("labdisp", "results/fulltest_s27_u3/track_a_s27_u3.csv", "results/fulltest_s27_u4/track_a_s27_u4.csv"),
]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(p):
    return pd.read_csv(ROOT / p, dtype={"parsed_value": float}).set_index("id").parsed_value


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--keep", required=True, help='per category: "S2:u1;D2:u1,gravity;..." (steps: '
                    + ", ".join(s for s, _, _ in CHAIN) + ")")
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--revert-ids", default="", help="CSV with an id column: these rows keep the #203 value whatever "
                    "--keep says (a single row a read refuted, or rows held out of a test)")
    a = ap.parse_args()
    dest = ROOT / a.out
    if dest.exists():
        raise SystemExit("Use a new build directory; never overwrite an evaluated artifact")
    keep = {}
    for part in a.keep.split(";"):
        cat, steps = part.split(":")
        keep[cat.strip()] = {s.strip() for s in steps.split(",") if s.strip()}
    cur = pd.DataFrame(json.load(open(ROOT / "data/test/test_dataset_current_20261021.json")))
    cur["id"] = cur.row_idx + 1
    cat = dict(zip(cur.id, cur.inference_type.str[0] + cur.video_type.str[1]))
    base_path = CHAIN[0][1]
    out = pd.read_csv(ROOT / base_path, dtype={"parsed_value": float})
    val = out.set_index("id").parsed_value.copy()
    seen, log = {}, []
    for step, before, after in CHAIN:
        b, f = load(before), load(after)
        diff = f.index[(b - f).abs() > 1e-9]
        for qid in diff:
            if qid in seen:
                raise SystemExit(f"row {qid} changed by both {seen[qid]} and {step}: resolve by hand")
            seen[qid] = step
            if step in keep.get(cat[qid], set()):
                val[qid] = f[qid]
                log.append(dict(id=qid, cat=cat[qid], step=step, before=b[qid], after=f[qid]))
    if a.revert_ids:
        rev = set(pd.read_csv(ROOT / a.revert_ids).id)
        base = load(base_path)
        for qid in rev:
            val[qid] = base[qid]
        log = [r for r in log if r["id"] not in rev]
    out["parsed_value"] = out.id.map(val)
    dest.mkdir(parents=True)
    out.to_csv(dest / a.name, index=False)
    ch = pd.DataFrame(log)
    ch.to_csv(dest / "combine_rows.csv", index=False)
    man = {"run": a.out, "base": base_path, "base_sha256": sha(ROOT / base_path), "keep": a.keep,
           "revert_ids": a.revert_ids,
           "changed": len(ch), "by_cat_step": ch.groupby(["cat", "step"]).size().rename("n").reset_index()
           .to_dict(orient="records") if len(ch) else [], "sha256": sha(dest / a.name)}
    (dest / "manifest.json").write_text(json.dumps(man, indent=1) + "\n")
    print(json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
