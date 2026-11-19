"""Series 28 Track B candidate (2026-10-22, session eac5885a): the compliant Track B line #194 with three per-question
steps, every one validated on the labelled validation split before any read.

1. DeepSeek third voice (--ds <dsh_scene out dir>, 28_3): where the two-phase per-question DeepSeek-V4.1-Flash-1017 agent
   answered, the row becomes median(DeepSeek, #194, #163) - the validation analogue med(DeepSeek, med(GLM run1, rep2,
   pool49), pool49) read +.020 on 150 rows (video bootstrap +.007..+.040; S3 +.041, 28_2), while DeepSeek alone read
   +.004 (-.044..+.057). #163 (the pre-agent standing) plays pool49's part, as in Series 23's medians.
2. The 26_71 transforms: the three duplicate-or-drop re-encoded clips back on the file clock (#189's (q/f)^k divided
   out), and the lab motion label factors (S3 x1.215, D3 x1.19, 2D lab velocities x1.19; the constants the Track A board
   read, the label process of paper App. C). Unlike 26_71 nothing is blanked: 20 of the 277 validation-family rows are
   scored (#201), so every row is filled.
3. Lab prop sizes (scripts/lab_props.py): a lab size question about a prop the paper's appendix-B table lists takes the
   table value (11 of 12 such validation labels equal it; validation .88 -> .98 on the GLM answers).

Each answer depends on its own question only: its own answers from three Track B pipelines, a class constant, and the
paper's table.

    python scripts/build_s28_trackb.py --out results/fulltest_s28_b1                       # steps 2 + 3
    python scripts/build_s28_trackb.py --out results/fulltest_s28_b2 --ds results/s28_test_dsf1017 \
        --ds-replace results/s28_test_dsf1017_fixed,results/s28_test_dsf1017_phys --replace-fixed

--ds-replace takes DeepSeek's answer outright, for populations where the two older voices share one known error the
DeepSeek prompt corrects, so a median of three would keep it: the fixed character-origin renders (Track A 26_59: a
walking character's depth_info is its rig origin, the GLM runs sized those scenes from a walk that is not there) and
the self-filmed clips' physical scale (28_6). --replace-fixed also replaces the S3 rows of the fixed-origin renders
that --ds covers.
"""
import argparse
import glob
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

import lab_props as LP

ROOT = Path(__file__).resolve().parents[1]
B194 = ROOT / "results/fulltest_s26_trackb_perq_plus/track_b_s26_perq_plus.csv"
B163 = ROOT / "results/fulltest_adopt_20261012/adopt_20261012.csv"
B185 = ROOT / "results/fulltest_s26_trackb_famcons2/track_b_s26_famcons2.csv"
B189 = ROOT / "results/fulltest_s26_timebase_b/track_b_s26_timebase.csv"
CURRENT = ROOT / "data/test/test_dataset_current_20261021.json"
LEDGER = ROOT / "results/s26_scene_full/ledger.csv"  # the 3,012 scored ids
REENCODED = ("internet_0074", "internet_0008_segmented", "internet_0003_segmented")
SPEED = re.compile(r"veloc|velolicty|speed|accelerat", re.I)
DISP = re.compile(r"displacement", re.I)
PATH = re.compile(r"distance\s+travel|travel+ed|distance\s+moved", re.I)


def load(p):
    d = pd.read_csv(p, dtype=str).set_index("id")
    d.index = d.index.astype(int)
    return d, pd.to_numeric(d.parsed_value, errors="coerce")


SWITCH = re.compile(r"physical scale|standard (?:adult|object|person)|instead of the prior|prior'?s scale (?:is|was) "
                    r"(?:unusable|wrong|inconsistent)|not used as (?:a|the) (?:length )?scale", re.I)


def ds_notes(dirs):
    """{id: (answer, notes.md)} over the r1 sessions of the given dsh_scene out dirs."""
    out = {}
    for d in dirs:
        for f in glob.glob(str(ROOT / d / "q" / "*" / "r1.json")):
            r = json.loads(Path(f).read_text())
            a = (r.get("final") or {}).get("answers") or []
            if a:
                out[int(Path(f).parent.name.split("__")[-1])] = (float(a[0]["value"]), (r.get("notes.md") or "") +
                                                                  " " + str(a[0].get("reason") or ""))
    return out


def ds_answers(out_dir):
    """{id: DeepSeek answer} from a dsh_scene out dir (median over repeats when there are several)."""
    acc = {}
    for f in glob.glob(str(ROOT / out_dir / "q" / "*" / "r*.json")):
        r = json.loads(Path(f).read_text())
        a = (r.get("final") or {}).get("answers") or []
        if a:
            acc.setdefault(int(Path(f).parent.name.split("__")[-1]), []).append(float(a[0]["value"]))
    return {k: float(np.median(v)) for k, v in acc.items()}


CHAR = re.compile(r"human|person|man\b|woman|people|pedestrian|horse|rabbit|dog|cat\b|deer|elephant|astronaut|boy|girl|"
                  r"walker|character|cow|sheep", re.I)


def fixed_origin(cur):
    """Ids of rendered rows whose own depth_info gives a character two stamps less than 0.1 m/s apart (the rig origin)."""
    out = set()
    for i, r in cur.iterrows():
        if r.video_source not in ("simulation", "segmentation") or not isinstance(r.depth_info, str):
            continue
        ent = {}
        for line in re.split(r"[\n;]", r.depth_info):
            m = re.search(r"t\s*=\s*([\d.]+)\s*s?\s*,\s*distance_([A-Za-z_ ]+?)_?camera\s*=\s*([\d.]+)", line)
            if m:
                ent.setdefault(m.group(2).strip("_ ").lower(), []).append((float(m.group(1)), float(m.group(3))))
        for k, v in ent.items():
            v = sorted(v)
            if CHAR.search(k) and len(v) >= 2 and v[-1][0] > v[0][0] and abs(v[-1][1] - v[0][1]) / (v[-1][0] - v[0][0]) < 0.1:
                out.add(i)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--ds", default="", help="dsh_scene out dir(s) with DeepSeek test answers, comma-separated")
    ap.add_argument("--c163", default="", help="the compliant #163 CSV (29_7) in place of the raw file as the third voice")
    ap.add_argument("--series", default="28", help="series number in the output file name")
    ap.add_argument("--ds-replace", default="", help="dsh_scene out dir(s) whose DeepSeek answers replace the row")
    ap.add_argument("--replace-fixed", action="store_true", help="--ds rows on fixed-origin renders are replaced too")
    ap.add_argument("--ds-switch", default="", help="dsh_scene out dir(s) of the --physical-internet run (28_6): a row is "
                    "replaced only when its own notes declare the standard-object scale and it moves > 15 pct")
    ap.add_argument("--s3", type=float, default=1.215)
    ap.add_argument("--d3", type=float, default=1.19)
    ap.add_argument("--d2", type=float, default=1.19, help="velocities on the 2D lab clips")
    ap.add_argument("--no-props", action="store_true")
    a = ap.parse_args()
    out_dir = ROOT / a.out
    if out_dir.exists():
        raise SystemExit("Use a new build directory; never overwrite an evaluated artifact")

    base, v194 = load(B194)
    _, v163 = load(B163)
    if a.c163:  # 29_7: the compliant replay of #163 (the raw file carries cross-question writes on 704 rows)
        c = pd.read_csv(ROOT / a.c163).set_index("id")
        v163 = pd.to_numeric(c.compliant_163, errors="coerce").reindex(v163.index)
    _, v185 = load(B185)
    _, v189 = load(B189)
    cur = pd.DataFrame(json.loads(CURRENT.read_text()))
    cur["id"] = cur.row_idx + 1
    cur = cur.set_index("id")
    assert (cur.index == base.index).all() and (cur.video_id == base.video_id).all()
    cat = base.inference_type.str[0] + cur.video_type.str[1]
    src = cur.video_source
    q = cur.question  # the current wording (units and object names fixed after our download)
    new = v194.copy()
    log = []

    # 1. DeepSeek third voice, on #189's time base for #163 (S2 / D2 rate-mismatched rows; none in S3)
    tbf = (v189 / v185).where(~np.isclose(v189, v185, rtol=1e-9), 1.0)
    ds = {}
    for d in [x for x in a.ds.split(",") if x]:
        ds.update(ds_answers(d))
    fixed = fixed_origin(cur) if a.replace_fixed else set()
    for i, x in ds.items():
        if i in fixed:
            log.append((i, "ds_fixed_origin", new.loc[i], x))
            new.loc[i] = x
            continue
        m = float(np.median([x, v194.loc[i], v163.loc[i] * tbf.loc[i]]))
        if not np.isclose(m, new.loc[i], rtol=1e-12):
            log.append((i, "median_ds_194_163", new.loc[i], m))
        new.loc[i] = m
    rep = {}
    for d in [x for x in a.ds_replace.split(",") if x]:
        rep.update(ds_answers(d))
    for i, x in rep.items():
        log.append((i, "ds_replace", new.loc[i], x))
        new.loc[i] = x
    # 28_6: the sessions applied the physical-scale convention unevenly (a rider's height switched to 1.65 m while the
    # same clip's lamp kept the prior's scale), so only a row whose own session declared the switch moves
    for i, (x, notes) in ds_notes([x for x in a.ds_switch.split(",") if x]).items():
        if SWITCH.search(notes) and abs(np.log(x / new.loc[i])) > np.log(1.15):
            log.append((i, "ds_physical_scale", new.loc[i], x))
            new.loc[i] = x

    # 2a. re-encoded clips back on the file clock
    for i in base.index[base.video_id.isin(REENCODED) & ~np.isclose(tbf, 1.0)]:
        before = new.loc[i]
        new.loc[i] = before / tbf.loc[i]
        log.append((i, "reencoded_file_clock", before, new.loc[i]))
    # 2b. lab motion label factors
    fac = {"S3": a.s3, "D3": a.d3, "D2": a.d2}
    for i in base.index[src.eq("lab") & cat.isin(list(fac))]:
        qq, c = q.loc[i], cat.loc[i]
        if c == "D2" and not SPEED.search(qq):
            continue
        if not (SPEED.search(qq) or DISP.search(qq) or PATH.search(qq)):
            continue
        before = new.loc[i]
        new.loc[i] = before * fac[c]
        log.append((i, f"lab_motion_x{fac[c]}", before, new.loc[i]))

    # 3. lab prop sizes
    if not a.no_props:
        for i in base.index[src.eq("lab")]:
            before = new.loc[i]
            after, m = LP.snap(q.loc[i], before, "lab")
            if m is not None and not np.isclose(after, before, rtol=1e-12):
                new.loc[i] = after
                log.append((i, "lab_prop_table", before, after))

    bad = int((~np.isfinite(new) | (new <= 0)).sum())
    if bad:
        raise SystemExit(f"{bad} invalid values")
    scored = set(pd.read_csv(LEDGER).id.astype(int))
    out = base.copy()
    ch = new.index[~np.isclose(new, v194, rtol=1e-12)]
    out.loc[ch, "parsed_value"] = [repr(float(x)) for x in new.loc[ch]]
    out_dir.mkdir(parents=True)
    name = f"track_b_s{a.series}_{out_dir.name.split('_')[-1]}.csv"
    out.reset_index().to_csv(out_dir / name, index=False)
    lg = pd.DataFrame(log, columns=["id", "reason", "before", "after"])
    lg["video"] = lg.id.map(base.video_id)
    lg["cat"] = lg.id.map(cat)
    lg["scored"] = lg.id.isin(scored)
    lg.to_csv(out_dir / "changes.csv", index=False)
    sc = lg[lg.scored]
    man = {"series": a.series, "track": "B", "file": name, "c163": a.c163 or str(B163.relative_to(ROOT)), "base": str(B194.relative_to(ROOT)), "base_eval": 194,
           "ds_dirs": a.ds, "ds_rows": len(ds), "ds_replace_dirs": a.ds_replace, "ds_replace_rows": len(rep),
           "ds_switch_dirs": a.ds_switch,
           "replace_fixed": a.replace_fixed, "factors": fac, "props": not a.no_props,
           "rows_changed_vs_194": int(len(ch)), "scored_changed_vs_194": int(len(set(ch) & scored)),
           "scored_steps": {r: g.cat.value_counts().to_dict() for r, g in sc.groupby("reason")}}
    (out_dir / "manifest.json").write_text(json.dumps(man, indent=1) + "\n")
    print(json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
