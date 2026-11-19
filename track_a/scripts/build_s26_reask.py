"""Series 26, run 26_60 (2026-10-20): the compliant Track A file #199 with the 26_59 --real-scale re-asks and the four
stale rows corrected.

- Every row of 26_59's selection (`results/s26_reask_1020/selection.csv`) takes the CURRENT answer of its own
  question folder (`q/<video>__<id>/answers.json`); a row whose re-ask failed keeps #199's value (reported). None of
  these rows is a lab row or one of the physical-scale clips, so #199's transforms do not touch them.
- The four rows #199 built from a stale clip aggregate (587 / 589 / 591 / 748; Code Dev Notes 2026-10-20) take the
  current answer of their 26_30 question folder.
- Every other row is #199 byte for byte. Rows are read from the per-question folders, never from clips/ (the race).
Each answer is still its own question's session (per-question rule); nothing else enters.

    python scripts/build_s26_reask.py --out results/fulltest_s26_reask
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
STALE = (587, 589, 591, 748)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def current(run, vid, qid):
    f = ROOT / run / "q" / f"{vid}__{qid}" / "answers.json"
    if not f.exists():
        return None
    v = json.loads(f.read_text()).get(str(qid))
    return float(v) if v is not None and np.isfinite(float(v)) and float(v) > 0 else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="results/fulltest_s26_compliant/track_a_s26_compliant.csv")  # #199
    ap.add_argument("--run", default="results/s26_reask_1020")
    ap.add_argument("--stale-run", default="results/s26_scene_full")
    ap.add_argument("--stages", default="1,2", help="which 26_59 stages take their re-asked answers")
    ap.add_argument("--cats", default="D2,D3,S3", help="categories that take changes; the others stay #199 (control)")
    ap.add_argument("--family", help="only selection rows whose video is in this scene family (families.json key)")
    ap.add_argument("--not-family", help="only selection rows whose video is NOT in this scene family")
    ap.add_argument("--families", default="results/fulltest_s24_famprior/families.json")
    ap.add_argument("--no-stale", action="store_true", help="leave the four stale rows as #199 has them")
    ap.add_argument("--ids-file", help="JSON {\"why\": ..., \"ids\": [...]}: only these selection rows take their re-ask")
    ap.add_argument("--out", default="results/fulltest_s26_reask")
    ap.add_argument("--name", default="track_a_s26_reask.csv")
    a = ap.parse_args()
    dest = ROOT / a.out
    if dest.exists():
        raise SystemExit("Use a new build directory; never overwrite an evaluated artifact")
    base = pd.read_csv(ROOT / a.base, dtype={"parsed_value": float})
    out = base.copy()
    pos = {int(i): k for k, i in enumerate(base.id)}
    cat = (base.inference_type.str[0] + base.video_type.str[1]).values
    S = pd.read_csv(ROOT / a.run / "selection.csv")
    S = S[S.stage.astype(str).isin(a.stages.split(","))]
    if a.family or a.not_family:  # evaluation grouping only (Codex review 2026-10-20, P2); inference stays per question
        fams = json.loads((ROOT / a.families).read_text())
        if a.family:
            S = S[S.video.isin(fams[a.family])]
        if a.not_family:
            S = S[~S.video.isin(fams[a.not_family])]
    S = S[S.category.isin(a.cats.split(","))]
    if a.ids_file:
        S = S[S.id.isin(json.loads((ROOT / a.ids_file).read_text())["ids"])]
    L = pd.read_csv(ROOT / a.stale_run / "ledger.csv").set_index("id")
    changes, kept = [], []
    for r in S.itertuples(index=False):
        v = current(a.run, r.video, r.id)
        k = pos[int(r.id)]
        if v is None:
            kept.append(int(r.id))
            continue
        changes.append({"id": int(r.id), "video": r.video, "cat": cat[k], "reason": r.reasons, "stage": int(r.stage),
                        "before": out.at[k, "parsed_value"], "after": v})
        out.at[k, "parsed_value"] = v
    for qid in () if a.no_stale else STALE:
        v = current(a.stale_run, L.at[qid, "video"], qid)
        k = pos[qid]
        changes.append({"id": qid, "video": L.at[qid, "video"], "cat": cat[k], "reason": "stale_clip", "stage": 0,
                        "before": out.at[k, "parsed_value"], "after": v})
        out.at[k, "parsed_value"] = v
    C = pd.DataFrame(changes)
    assert np.isfinite(out.parsed_value).all() and (out.parsed_value > 0).all()
    assert set(C.cat) <= set(a.cats.split(",")) and "S2" not in set(C.cat), "a control category would change"
    moved = C[~np.isclose(C.before, C.after, rtol=1e-9)]
    dest.mkdir(parents=True)
    out.to_csv(dest / a.name, index=False)
    C.to_csv(dest / "changes.csv", index=False)
    diff = int((~np.isclose(out.parsed_value.values, base.parsed_value.values, rtol=1e-12)).sum())
    manifest = {"run": "26_60", "base": a.base, "reask_run": a.run, "stages": a.stages, "cats": a.cats,
                "family": a.family, "not_family": a.not_family, "ids_file": a.ids_file, "stale_ids": [] if a.no_stale else list(STALE),
                "rows_taken": int(len(C)), "rows_moved": int(len(moved)), "rows_differing_from_base": diff,
                "moved_by_category": moved.cat.value_counts().to_dict(), "taken_by_category": C.cat.value_counts().to_dict(),
                "reask_failed_kept_base": kept,
                "sha256": {a.base: sha(ROOT / a.base), f"{a.out}/{a.name}": sha(dest / a.name)}}
    (dest / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    print(json.dumps(manifest, indent=1))


if __name__ == "__main__":
    main()
