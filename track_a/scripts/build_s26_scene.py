"""Series 26: the per-question Track A file from the two-phase agent (cc_agent_scene.py), 2026-10-18.

Every scored row (the template minus the 24 validation families) takes the answer of its own per-question session;
nothing else enters: no family-prior fold, no protected sibling facts, no pooling across renders, twins or questions
(the organisers' per-question rule of 2026-10-15). Rows of the validation families are not scored on the board and
keep the base's values. A scored row without a finite positive answer is reported and, only with --fallback,
filled from the base (the manifest lists every such row - a submission meant to be compliant needs zero).

    python scripts/build_s26_scene.py --runs results/s26_scene_full --out results/fulltest_s26_scene
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import pandas as pd

from cc_agent_run import VAL_STEMS, stem

ROOT = Path(__file__).resolve().parents[1]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="results/fulltest_s26_ccagent_full/track_a_s26_ccagent_full.csv")  # #186
    ap.add_argument("--runs", nargs="+", default=["results/s26_scene_full"])
    ap.add_argument("--out", default="results/fulltest_s26_scene")
    ap.add_argument("--name", default="track_a_s26_scene.csv")
    ap.add_argument("--fallback", action="store_true", help="fill unanswered scored rows from the base (reported)")
    ap.add_argument("--cats", default="S2,D2,S3,D3", help="categories that take the run's answers; the others keep the "
                                                          "base byte for byte (a paired read of part of the run)")
    a = ap.parse_args()
    dest = ROOT / a.out
    if dest.exists():
        raise SystemExit("Use a new build directory; never overwrite an evaluated artifact")
    base = pd.read_csv(ROOT / a.base, dtype=str)
    ans = {}
    for run in a.runs:
        for f in (ROOT / run / "clips").glob("*/answers.json"):
            for k, v in json.loads(f.read_text()).items():
                v = float(v)
                if math.isfinite(v) and v > 0:
                    ans[int(k)] = v
    cat = base.inference_type.str[0] + base.video_type.str[1]
    scored = ~base.video_id.str.strip().map(stem).isin(VAL_STEMS) & cat.isin(a.cats.split(","))
    missing = [int(i) for i, s in zip(base.id, scored) if s and int(i) not in ans]
    if missing and not a.fallback:
        raise SystemExit(f"{len(missing)} scored rows have no answer (first {missing[:10]}); rerun them or pass --fallback")
    out = base.copy()
    hit = scored & base.id.astype(int).isin(ans)
    out.loc[hit, "parsed_value"] = [repr(ans[int(i)]) for i in base.id[hit]]
    dest.mkdir(parents=True)
    out.to_csv(dest / a.name, index=False)
    old = pd.to_numeric(base.parsed_value, errors="coerce")
    new = pd.to_numeric(out.parsed_value, errors="coerce")
    moved = hit & ((new / old - 1).abs() > 0.01)
    summary = {
        "base": a.base, "runs": a.runs, "cats": a.cats, "rows": len(out), "scored_rows_in_cats": int(scored.sum()),
        "answered_scored": int(hit.sum()), "fallback_rows": missing,
        "moved_over_1pct_vs_base_by_cat": cat[moved].value_counts().to_dict(),
        "invalid": int((~(new > 0)).sum()), "labels_used": False,
        "sha256": {a.base: sha(ROOT / a.base), f"{a.out}/{a.name}": sha(dest / a.name), "builder": sha(__file__)}}
    (dest / "manifest.json").write_text(json.dumps(summary, indent=1) + "\n")
    print(json.dumps({k: v for k, v in summary.items() if k != "sha256"}, indent=1))


if __name__ == "__main__":
    main()
