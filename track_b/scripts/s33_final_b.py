"""The Track B entry assembler (session 20cfd3a2, 2026-10-22): every scored row from a per-question open answer.

Chain, in order, on the GRAY-free L5 overlay (s33_build.py; user ruling #163):
  1. S2 and D3 on 3D simulation / segmentation videos: the 29_5 DeepSeek-with-SAM-3 answer replaces the row (B5's
     pinned rule d3sim=replace, s2=replace; no Track A value is read).
  2. D2: the per-question DeepSeek answer replaces the row (the funded pass, user ruling #170); the six 2D lab
     velocities are clean motion, so they take the lab factor (s under --model lat, the validation-fitted k otherwise).
  3. D3 lab: the per-question DeepSeek answer. Motion rows (velocity / displacement / path / acceleration) are clean 3D
     motion and take the lab factor (the row's own direction factor F under --model lat where s33_lablat_open has one,
     else k). The geometric mean with the 33_1 re-enacted label / the open pair geometry, registered in #170 with a
     validation check before any test use, FAILED that check (18 validation lab motion rows: DeepSeek alone .711 vs the
     rule .694 at k = 1.25, .778 vs .761 at s = 1.5; on the 9 rows with a label .667 vs .633 / .800 vs .767), so the
     default is DeepSeek alone (--geo restores the rule); the open geometry answers only rows DeepSeek left without an
     answer (`--fill-open`, on by default). No prop-table snap.
  4. Rows of the 247-row refill (results/s30_refill/ids.csv, user ruling #161) take its per-question answer; S3 rows
     with no DeepSeek answer in L5 take one from --ds if it now exists (q1522 / q1536).
Rows none of these reach keep the L5 value; scripts/s33_provenance.py then lists their sources.

    python scripts/s33_final_b.py --base results/fulltest_s33_l5const/track_b_s33_l5const.csv --model const \
        --ds results/s29_pass_sam3 [--refill results/s29_pass_refill] --out results/fulltest_s33_b7const
"""
import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_s28_trackb as B  # noqa: E402
import s31_lablat as L  # noqa: E402
import s33_lablat_open as O  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="an L5 overlay (s33_build.py on B6base)")
    ap.add_argument("--ds", required=True, help="dsh_scene out dir(s) with the per-question DeepSeek answers, comma-separated")
    ap.add_argument("--refill", default="", help="dsh_scene out dir of the 247-row refill")
    ap.add_argument("--model", choices=("lat", "const"), required=True)
    ap.add_argument("--k", type=float, default=1.25)
    ap.add_argument("--s", type=float, default=1.5)
    ap.add_argument("--geo", action="store_true", help="D3 lab: geometric mean of DeepSeek and the open geometry (the "
                    "#170 rule; refuted on validation, so off by default)")
    ap.add_argument("--no-fill-open", action="store_true", help="do not let the open geometry answer D3 lab rows "
                    "DeepSeek left without an answer")
    ap.add_argument("--s3-tools", action="store_true", help="S3 rows with an answer in --ds (the with-tools pass) take it")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out_dir = ROOT / a.out
    if out_dir.exists():
        raise SystemExit("Use a new build directory; never overwrite an evaluated artifact")
    base, vb = B.load(ROOT / a.base)
    cur = pd.DataFrame(json.loads(B.CURRENT.read_text()))
    cur["id"] = cur.row_idx + 1
    cur = cur.set_index("id")
    cat = base.inference_type.str[0] + cur.video_type.str[1]
    src, q = cur.video_source, cur.question.str.strip()
    motion = q.str.contains(B.SPEED) | q.str.contains(B.DISP) | q.str.contains(B.PATH)
    ds = {}
    for d in a.ds.split(","):
        ds.update(B.ds_answers(d))
    fac = pd.read_csv(ROOT / "results/s33_lablat_open/factors.csv").set_index("id").F
    tracks = O.load_s18("test")
    new, log = vb.copy(), []

    def put(i, v, why):
        log.append((i, why, new.loc[i], v))
        new.loc[i] = v

    for i, x in sorted(ds.items()):
        c, s_ = cat.loc[i], src.loc[i]
        if c == "S2" or (c == "D3" and s_ in ("simulation", "segmentation")):
            put(i, x, "ds_replace_" + ("s2" if c == "S2" else "d3sim"))
        elif c == "D2":
            if s_ == "lab" and q.loc[i] and B.SPEED.search(q.loc[i]):
                k = a.s if a.model == "lat" else a.k
                put(i, x * k, f"ds_d2lab_vel_x{k}")
            else:
                put(i, x, "ds_replace_d2")
        elif c == "D3" and s_ == "lab":
            v, why = x, "ds_d3lab"
            if motion.loc[i]:
                if a.model == "lat" and i in fac.index and np.isfinite(fac.loc[i]):
                    v, why = x * float(fac.loc[i]), why + "_xF"
                else:
                    v, why = x * a.k, why + f"_x{a.k}"
                if a.geo:
                    lab, kind, how = O.label_value(tracks, cur.loc[i, "video_id"], q.loc[i], cur.loc[i, "depth_info"] or "",
                                                   a.s if a.model == "lat" else 1.0)
                    if lab and lab > 0:
                        lab = lab if a.model == "lat" else lab * a.k
                        v, why = math.sqrt(v * lab), why + "_geo_label"
            elif a.geo:
                pd_, Fp, how = O.pair_geometry(tracks, cur.loc[i, "video_id"], q.loc[i], cur.loc[i, "depth_info"] or "")
                if pd_ and pd_ > 0:
                    v, why = math.sqrt(v * pd_), why + "_geo_pair"
            put(i, v, why)
        elif c == "S3" and (a.s3_tools or i in (1522, 1536)):
            # S3 rows answered by the with-tools configuration take it (29_4: .813 vs 28_3's .753 on the same 30 rows;
            # rule fixed before the S3 pass was read); lab motion takes the lab factor as on D3
            v, why = x, "ds_s3_tools" if i not in (1522, 1536) else "ds_s3_leftover"
            if s_ == "lab" and motion.loc[i]:
                if a.model == "lat" and i in fac.index and np.isfinite(fac.loc[i]):
                    v, why = x * float(fac.loc[i]), why + "_xF"
                else:
                    v, why = x * a.k, why + f"_x{a.k}"
            put(i, v, why)
    if not a.no_fill_open:      # D3 lab rows with no DeepSeek answer: the 33_1 open geometry, where it exists
        for i in base.index[src.eq("lab") & cat.eq("D3")]:
            if i in ds:
                continue
            if motion.loc[i]:
                lab, kind, how = O.label_value(tracks, cur.loc[i, "video_id"], q.loc[i], cur.loc[i, "depth_info"] or "",
                                               a.s if a.model == "lat" else 1.0)
                if lab and lab > 0:
                    put(i, lab if a.model == "lat" else lab * a.k, "open_label_fill")
            else:
                pd_, Fp, how = O.pair_geometry(tracks, cur.loc[i, "video_id"], q.loc[i], cur.loc[i, "depth_info"] or "")
                if pd_ and pd_ > 0:
                    put(i, pd_, "open_pair_fill")
    if a.refill:
        ids = set(pd.read_csv(ROOT / "results/s30_refill/ids.csv").id.astype(int))
        for i, x in B.ds_answers(a.refill).items():
            if i in ids:
                put(i, x, "refill_ds")
    if int((~np.isfinite(new) | (new <= 0)).sum()):
        raise SystemExit("invalid values")
    scored = set(pd.read_csv(B.LEDGER).id.astype(int))
    out = base.copy()
    ch = new.index[~np.isclose(new, vb, rtol=1e-12)]
    out.loc[ch, "parsed_value"] = [repr(float(x)) for x in new.loc[ch]]
    out_dir.mkdir(parents=True)
    name = f"track_b_s33_{out_dir.name.split('_')[-1]}.csv"
    out.reset_index().to_csv(out_dir / name, index=False)
    lg = pd.DataFrame(log, columns=["id", "reason", "before", "after"])
    lg["video"] = lg.id.map(base.video_id)
    lg["cat"] = lg.id.map(cat)
    lg["scored"] = lg.id.isin(scored)
    lg.to_csv(out_dir / "changes.csv", index=False)
    sc = lg[lg.scored]
    man = {"series": "33", "track": "B", "file": name, "base": a.base, "ds": a.ds, "refill": a.refill, "model": a.model,
           "k": a.k, "s": a.s, "geo": a.geo, "fill_open": not a.no_fill_open, "s3_tools": a.s3_tools, "rows_set": int(len(lg)), "rows_changed": int(len(ch)),
           "scored_steps": {r: g.cat.value_counts().to_dict() for r, g in sc.groupby("reason")},
           "note": "no Track A value, track or note enters a row; lab factors: validation-fitted k / s (#163)"}
    (out_dir / "manifest.json").write_text(json.dumps(man, indent=1) + "\n")
    print(json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
