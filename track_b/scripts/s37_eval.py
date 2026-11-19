"""Series 37 read of Track B files (session 05e6b3c8, 2026-10-24): two instruments, side by side.

1. Labelled test-resolution rows: the 128 test rows whose (video, question) equals a validation row (24 videos; the
   portal does not score them, test-no-public-validation). Validation labels score them per category (development
   evidence only; no label enters a prediction). The 480p validation split misjudged DeepSeek (Standing Rules), these
   are the same questions at test resolution.
2. The delta calibration of s29_predict.py / s33_predict.py: predicted board = #210's board read + the per-category
   slope x (agreement with E2 - #210's agreement), on the 3,012 scored rows (development evidence; E2 = Track A entry).

Paired video bootstrap of every file against the first (the reference) on instrument 1.

    python scripts/s37_eval.py [--write] results/fulltest_s33_b7const/track_b_s33_b7const.csv <more files>

--write saves each file's numbers as prediction_s37.json beside it (written before any board read).
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import probe_lib as pl  # noqa: E402

E2 = ROOT / "results/fulltest_s27_e2/track_a_s27_e2.csv"
E2LAT = ROOT / "results/fulltest_s31_lablat/track_a_s31_lablat.csv"  # E2 x 31_1's direction factor (s33_predict.py)
REF = ROOT / "results/fulltest_s28_b2/track_b_s28_b2.csv"
REF_BOARD = {"S2": .7704, "D2": .7876, "S3": .7663, "D3": .7197}  # #210


def tables():
    ds = pd.DataFrame(json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text()))
    ds["id"] = ds.row_idx + 1
    ds["cat"] = [("S" if it[0] == "S" else "D") + vt[1] for it, vt in zip(ds.inference_type, ds.video_type)]
    val = pd.read_csv(ROOT / "data/validation/validation_dataset.csv")
    lab = ds.merge(val[["video_id", "question", "ground_truth_posterior"]], on=["video_id", "question"])
    scored = sorted(set(pd.read_csv(ROOT / "results/s26_scene_full/ledger.csv").id))
    return ds.set_index("id"), lab, scored


def labelled(v, lab):
    s = pd.Series([pl.row_mra(v.get(i), g) for i, g in zip(lab.id, lab.ground_truth_posterior)], index=lab.id)
    return s


def macro(s, lab):
    return float(np.mean([s[lab.cat.values == c].mean() for c in pl.CATS]))


def main():
    ds, lab, scored = tables()
    e2 = pd.read_csv(E2).set_index("id").parsed_value
    e2l = pd.read_csv(E2LAT).set_index("id").parsed_value
    vr = pd.read_csv(REF).set_index("id").parsed_value
    cal = pd.read_csv(ROOT / "results/s28_val_read/proxy_calibration.csv")
    slope = {c: np.polyfit(cal[cal.cat == c].proxy, cal[cal.cat == c].true, 1)[0] for c in pl.CATS}
    ar = {c: np.mean([pl.row_mra(vr.get(i), e2.get(i)) for i in scored if ds.cat[i] == c]) for c in pl.CATS}
    arl = {c: np.mean([pl.row_mra(vr.get(i), e2l.get(i)) for i in scored if ds.cat[i] == c]) for c in pl.CATS}
    rng = np.random.default_rng(0)
    vids = lab.video_id.values
    uv = np.unique(vids)
    ref_s = None
    write = "--write" in sys.argv
    for f in [x for x in sys.argv[1:] if x != "--write"]:
        v = pd.read_csv(ROOT / f).set_index("id").parsed_value
        s = labelled(v, lab)
        per = {c: s[lab.cat.values == c].mean() for c in pl.CATS}
        pred = {c: REF_BOARD[c] + slope[c] * (np.mean([pl.row_mra(v.get(i), e2.get(i)) for i in scored
                                                         if ds.cat[i] == c]) - ar[c]) for c in pl.CATS}
        predl = {c: REF_BOARD[c] + slope[c] * (np.mean([pl.row_mra(v.get(i), e2l.get(i)) for i in scored
                                                          if ds.cat[i] == c]) - arl[c]) for c in pl.CATS}
        line = (f"{f}\n  labelled 128: " + " / ".join(f"{c} {per[c]:.3f}" for c in pl.CATS) +
                f" = macro {macro(s, lab):.4f} (row mean {s.mean():.4f})\n  predicted board (E2): " +
                " / ".join(f"{c} {pred[c]:.4f}" for c in pl.CATS) + f" = {np.mean(list(pred.values())):.4f}"
                f"\n  predicted board (E2 x direction F): " + " / ".join(f"{c} {predl[c]:.4f}" for c in pl.CATS) +
                f" = {np.mean(list(predl.values())):.4f}")
        res = {"file": f, "labelled_128": {**{c: round(float(per[c]), 4) for c in pl.CATS}, "macro": round(macro(s, lab), 4)},
               "predicted_board_E2_delta_from_210": {**{c: round(float(pred[c]), 4) for c in pl.CATS},
                                                     "macro": round(float(np.mean(list(pred.values()))), 4)},
               "predicted_board_E2xF_delta_from_210": {**{c: round(float(predl[c]), 4) for c in pl.CATS},
                                                       "macro": round(float(np.mean(list(predl.values()))), 4)}}
        if write:
            (ROOT / f).with_name("prediction_s37.json").write_text(json.dumps(res, indent=1) + "\n")
        if ref_s is None:
            ref_s = s
        else:
            d = (s - ref_s).values
            boots = []
            for _ in range(2000):
                pick = rng.choice(uv, len(uv))
                idx = np.concatenate([np.where(vids == p)[0] for p in pick])
                boots.append(d[idx].mean())
            line += (f"\n  vs first, labelled rows: {d.mean():+.4f} a row (video bootstrap p05 {np.percentile(boots, 5):+.4f}"
                     f", p95 {np.percentile(boots, 95):+.4f}); rows up {(d > 0).sum()} / down {(d < 0).sum()}")
        print(line)


if __name__ == "__main__":
    main()
