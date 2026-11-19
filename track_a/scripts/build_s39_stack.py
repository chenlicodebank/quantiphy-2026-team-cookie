"""Series 39 (session 28b2ba80): stack per-population steps on a base Track A file, each step a per-question
combination of one question's own answers from different model runs (Opus line, DeepSeek-1017 + SAM 3 medians).

A spec is a JSON list of steps applied in order on the scored rows; each step selects rows by category / video
source / question kind (and optional id lists), then either copies a value from another file (`copy`; rows the file
lacks are skipped, and a collected re-answer run - s39_collect.py's id / new_t - counts as a file) or fuses
    value = exp(wA ln A + (1 - wA) ln B)   when |ln A/B| <= cap (else A is kept),
with A and B read from named files (`fuse`; `b_scale` puts B on A's factor convention first). A `conf` map makes the
weight per row: +`sure` when A's 26_30 session stated +/- <= 3 pct (or a sure word), +`hi` when the question's DeepSeek
runs spread widely (median |ln run/median| > .1), +`unsure_lo` (negative) when A was unsure and the runs agree within
.03; clipped to [`floor`, 1]. The compliance audit's OUT rows are never touched.

    python scripts/build_s39_stack.py --spec results/fulltest_s39_f2/spec.json --out results/fulltest_s39_f2 --name track_a_s39_f2.csv
"""
import argparse
import csv
import hashlib
import json
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def qkind(q):
    q = q.lower()
    if "acceler" in q:
        return "acc"
    if "speed" in q or "velocit" in q:
        return "vel"
    if re.search(r"displac|travel|path|distance (?:covered|moved)|how far", q):
        return "disp"
    if "distance" in q:
        return "dist"
    return "size"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", required=True)
    a = ap.parse_args()
    spec = json.loads((ROOT / a.spec).read_text())
    ds = pd.DataFrame(json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text()))
    ds["id"] = ds.row_idx + 1
    ds["cat"] = [("S" if it[0] == "S" else "D") + vt[1] for it, vt in zip(ds.inference_type, ds.video_type)]
    ds["qk"] = ds.question.map(qkind)
    meta = ds.set_index("id")
    scored = set(pd.read_csv(ROOT / "results/s26_scene_full/ledger.csv").id)
    out_rows = {int(r["id"]) for r in csv.DictReader(open(ROOT / "results/fulltest_s34_legit_a/changes.csv"))
                if r["group"] in ("human", "lenh", "weak")} | {1668}
    L = pd.read_csv(ROOT / "results/s26_scene_full/ledger.csv").set_index("id")
    agg = pd.read_csv(ROOT / "results/fulltest_s37_b9lat/aggregate.csv").drop_duplicates("id", keep="last").set_index("id")
    SURE, MID = {"high", "good", "fairly", "about"}, {"moderate-high", "moderate-good", "medium", "medium-high",
                                                      "moderate-to-good"}

    def opus_tier(i, av):
        """The 26_30 session's own stated uncertainty (build_s26_conf_split.py tiers) when A is that session's answer."""
        if i not in L.index or not (abs(float(L.answer[i]) - av) <= 1e-9 * max(1.0, abs(av))):
            return "na"
        pm, w = L.plus_minus_pct[i], str(L.confidence[i]).lower()
        if pd.notna(pm):
            return "sure" if pm <= 3 else ("mid" if pm <= 5 else "unsure")
        return "sure" if w in SURE else ("mid" if w in MID else "unsure")

    def ds_spread(i):
        """Median |ln(run / median)| over the question's own DeepSeek runs (B9's aggregate), bucketed."""
        if i not in agg.index:
            return "na"
        rs = np.array([float(x) for x in str(agg.runs[i]).split(";") if x not in ("", "nan") and float(x) > 0])
        if len(rs) < 2:
            return "na"
        sp = float(np.median(np.abs(np.log(rs / np.median(rs)))))
        return "lo" if sp <= 0.03 else ("mid" if sp <= 0.1 else "hi")

    files = {}
    for k, v in spec["files"].items():  # a build file (id, parsed_value) or a collected run (s39_collect.py: id, new_t)
        df = pd.read_csv(ROOT / v)
        files[k] = df.set_index("id")["new_t" if "new_t" in df.columns else "parsed_value"]
    base = pd.read_csv(ROOT / spec["base"])
    cur = base.set_index("id").parsed_value.copy()
    log = []
    for st in spec["steps"]:
        ids_in = set(st.get("ids", [])) or None
        ids_out = set(st.get("exclude_ids", []))
        for f in st.get("exclude_files", []):
            ids_out |= {int(r["id"]) for r in csv.DictReader(open(ROOT / f["path"])) if r.get(f["col"]) == f["val"]}
        n = 0
        for i in meta.index:
            if i not in scored or i in out_rows or i in ids_out or (ids_in is not None and i not in ids_in):
                continue
            m = meta.loc[i]
            if "cats" in st and m["cat"] not in st["cats"]:
                continue
            if "sources" in st and m["video_source"] not in st["sources"]:
                continue
            if "kinds" in st and m["qk"] not in st["kinds"]:
                continue
            before = float(cur[i])
            if st["op"] == "copy":
                if i not in files[st["from"]].index:
                    continue
                v = float(files[st["from"]][i])
            else:
                if (st["a"] != "cur" and i not in files[st["a"]].index) or i not in files[st["b"]].index:
                    continue
                av, bv = float(files[st["a"]][i]) if st["a"] != "cur" else before, float(files[st["b"]][i]) * st.get("b_scale", 1.0)
                w = st["wA"]
                if "conf" in st:  # fuse_conf: the weight moves with each answer's own stated / measured uncertainty
                    cm, t, sp = st["conf"], opus_tier(i, av), ds_spread(i)
                    if sp == "hi":
                        w += cm.get("hi", 0)
                    elif t == "sure":
                        w += cm.get("sure", 0)
                    elif t == "unsure" and sp == "lo":
                        w += cm.get("unsure_lo", 0)
                    w = min(1.0, max(cm.get("floor", 0.3), w))
                if not (av > 0 and bv > 0) or abs(np.log(av / bv)) > st.get("cap", 9) or w >= 1.0:
                    v = av
                else:
                    v = float(np.exp(w * np.log(av) + (1 - w) * np.log(bv)))
            v = float(f"{v:.6g}")
            if v != before:
                cur[i] = v
                n += 1
                log.append({"id": i, "step": st["name"], "cat": m["cat"], "source": m["video_source"], "kind": m["qk"],
                            "before": before, "after": v})
        print(f"{st['name']}: {n} rows")
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    base["parsed_value"] = base.id.map(cur)
    base.to_csv(out / a.name, index=False)
    pd.DataFrame(log).to_csv(out / "changes.csv", index=False)
    sha = hashlib.sha256((out / a.name).read_bytes()).hexdigest()
    ch = pd.DataFrame(log)
    man = {"series": "39", "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "spec": a.spec,
           "file": f"{a.out}/{a.name}", "sha256": sha, "rows_changed": len(ch),
           "by_step_cat": ch.groupby(["step", "cat"]).size().rename("n").reset_index().to_dict("records") if len(ch) else []}
    (out / "manifest.json").write_text(json.dumps(man, indent=1))
    print(json.dumps({k: man[k] for k in ("file", "sha256", "rows_changed")}, indent=1))


if __name__ == "__main__":
    main()
