"""Series 40 (2026-10-25, Track A, cross-question information allowed): snap static sizes to a reused-asset catalog.

Simulation scenes reuse one asset per object across their clips (and across the validation / test split), and the lab
reuses its props: a static size asked on one video is often stated elsewhere - as another video's prior, or as a
validation label. The catalog holds every "<dimension> of <object> = <value>" statement of the test priors, the
validation priors and the validation labels. A scored static-size row (no time qualifier) whose answer sits within a
threshold of a catalog value for the same (dimension, object) takes that value. Where a name is shared by different
assets the values sit far apart (validation: same-scene matches are exact, different assets 30-250 pct apart), so the
threshold depends on how close the stating video is:
  - simulation, stating video within --sim-window ids of the row's video (same scene range): --near (default .30)
  - lab prop, any lab video: --lab (default .15)
  - simulation from a farther scene: --far (default .12)
Internet rows and internet statements are never used. Rows the Series 24 sibling-prior facts already cover are left out.

    python scripts/s40_catalog_snap.py --answers results/fulltest_s40_p1/track_a_s40_p1.csv --out results/fulltest_s40_snap
"""
import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
UNIT = {"m": 1, "meter": 1, "meters": 1, "cm": .01, "centimeters": .01, "mm": .001, "millimeters": .001}
SIZE = "length|width|height|diameter|radius|size|depth|thickness|wingspan"
TIMED = r"at time|at \d|\bat t\b|between|from|average|maximum|minimum|initial|final|when|after|before|speed|velocity|acceler"


def clean(s):
    s = str(s).replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\b(" + SIZE + r")\s*\([^)]*\)", r"\1", s)


def nobj(o):
    o = o.lower().replace("'s", "").strip(" ?.")
    o = re.sub(r"^(the|a|an)\s+", "", o)
    return re.sub(r"\s+", " ", o)


def parse_prior(p):
    p = clean(p)
    m = re.search(r"(?:(?P<dim>" + SIZE + r")\s+of\s+(?:the\s+)?(?P<obj>[^=]+?)|(?P<obj2>[a-z ]+?)\s+(?P<dim2>" + SIZE +
                  r"))\s*=\s*(?P<val>[\d.]+)\s*(?P<unit>[a-z]*)", str(p).lower())
    if not m:
        return None
    obj = m.group("obj") or m.group("obj2")
    if re.search(r"\bat\b|\bt=|between|from", obj) or m.group("unit") not in UNIT:
        return None
    return m.group("dim") or m.group("dim2"), nobj(obj), float(m.group("val")) * UNIT[m.group("unit")]


def parse_q(q):
    ql = clean(q).lower()
    if re.search(TIMED, ql):
        return None
    m = re.search(r"(?:what is|what's) the (?P<dim>" + SIZE + r") of (?:the )?(?P<obj>.+?) in (?P<unit>meters|meter|m|cm|"
                  r"centimeters|mm|millimeters)\b", ql)
    if not m:
        m = re.search(r"(?:what is|what's) the (?P<obj>.+?)(?:'s)? (?P<dim>" + SIZE + r") in (?P<unit>meters|meter|m|cm|"
                      r"centimeters|mm|millimeters)\b", ql)
    if not m:
        return None
    return m.group("dim"), nobj(m.group("obj")), UNIT[m.group("unit")]


def canon(v):
    v = v.replace("_segmented", "")
    return re.sub(r"(?<=\d)[sxX]$", "", v) if v.startswith("captured_") else v


def num(v):
    m = re.search(r"_(\d+)", v)
    return int(m.group(1)) if m else -1


def build_catalog():
    T = pd.DataFrame(json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text()))
    T["id"] = T.row_idx + 1
    V = pd.read_csv(ROOT / "data/validation/validation_dataset.csv")
    cat = []
    for _, r in T.drop_duplicates(["video_id", "prior"]).iterrows():
        x = parse_prior(r.prior)
        if x:
            cat.append(("test_prior", r.video_id, r.video_source, *x))
    for _, r in V.drop_duplicates(["video_id", "ground_truth_prior"]).iterrows():
        x = parse_prior(r.ground_truth_prior)
        if x:
            cat.append(("val_prior", r.video_id, r.video_source, *x))
    for _, r in V.iterrows():
        x = parse_q(r.question)
        if x:
            cat.append(("val_label", r.video_id, r.video_source, x[0], x[1], float(r.ground_truth_posterior) * x[2]))
    C = pd.DataFrame(cat, columns=["kind", "video", "vsrc", "dim", "obj", "v"])
    C = C[C.vsrc != "internet"].copy()
    C["canon"] = C.video.map(canon)
    C["num"] = C.video.map(num)
    C["fam"] = np.where(C.vsrc == "lab", "lab", "sim")
    return T, C


def snap_rows(ans, near=0.30, lab=0.15, far=0.12, sim_window=12, kinds=None, skip_facts=True):
    """Rows (scored, not already sibling-fact rows) whose answer in `ans` (Series by id) snaps to a catalog value.

    kinds: catalog kinds to use (default all; ["val_label", "val_prior"] = the validation split only, no test prior).
    skip_facts: leave out the rows the Series 24 sibling-prior facts cover (False for a build that uses no test-side
    cross-question information, where that row list would itself be a second-order use).
    """
    T, C = build_catalog()
    if kinds:
        C = C[C.kind.isin(kinds)]
    led = pd.read_csv(ROOT / "results/s26_scene_full/ledger.csv").set_index("id")
    facts = set(pd.read_csv(ROOT / "results/fulltest_s24_famprior/famprior_detail.csv").id) if skip_facts else set()
    rows = []
    for _, r in T[T.id.isin(led.index) & ~T.id.isin(facts)].iterrows():
        if r.video_source == "internet":
            continue
        x = parse_q(r.question)
        if not x:
            continue
        dim, obj, f = x
        fam = "lab" if r.video_source == "lab" else "sim"
        c = C[(C.dim == dim) & (C.obj == obj) & (C.canon != canon(r.video_id)) & (C.fam == fam)]
        if not len(c):
            continue
        a_si = ans[r.id] * f
        best = None
        for _, e in c.iterrows():
            lr = abs(np.log(a_si / e.v))
            if fam == "lab":
                thr = lab
            else:
                # a far scene only for specific (multi-word) object names: "car" or "box" names different assets
                thr = near if abs(e.num - num(r.video_id)) <= sim_window else (far if len(obj.split()) >= 2 else 0.0)
            if lr <= thr and (best is None or lr < best[0]):
                best = (lr, e)
        if best is None or best[0] < 1e-9:
            continue
        lr, e = best
        rows.append({"id": r.id, "cat": led.category[r.id], "source": r.video_source, "video": r.video_id,
                     "question": r.question, "answer": ans[r.id], "parsed_value": float(f"{e.v / f:.6g}"),
                     "ln_ratio": round(float(np.log(a_si / e.v)), 4), "stated_by": e.video, "kind": e.kind})
    return pd.DataFrame(rows), C


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--answers", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--near", type=float, default=0.30)
    ap.add_argument("--lab", type=float, default=0.15)
    ap.add_argument("--far", type=float, default=0.12)
    ap.add_argument("--sim-window", type=int, default=12)
    a = ap.parse_args()
    ans = pd.read_csv(ROOT / a.answers).set_index("id").parsed_value.astype(float)
    R, C = snap_rows(ans, a.near, a.lab, a.far, a.sim_window)
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    R.to_csv(out / "snap_rows.csv", index=False)
    C.to_csv(out / "catalog.csv", index=False)
    print(len(R), "rows;", R.groupby("cat").size().to_dict() if len(R) else {})
    if len(R):
        print(R.assign(a=R.ln_ratio.abs()).groupby("cat").a.agg(["count", "mean", lambda s: (s > .05).sum()]).round(3))


if __name__ == "__main__":
    main()
