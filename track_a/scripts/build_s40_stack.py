"""Series 40 (2026-10-25, Track A, user: cross-question information allowed) stack builder.

One spec (JSON) per build, applied in this order on the scored rows (unscored rows keep the first base file):
  1. base     - each category's rows from its own file: {"S2": path, ...}
  2. lines    - named partner lines: {"u2": path, ...}
  3. pool     - per line (base included), every equivalence group of rows that must share one label is replaced by
                its median (3+) / geometric mean (2): same canonical video (`_segmented` twin and lab `s` / `x`
                renders folded onto the original), same question, same prior text and depth_info.
                "pool": {"cats": ["S3", "D3"], "sources": ["lab", ...], "lines": ["base", "u2"]}
  4. fuse     - per category weights of the partner lines in a log-space weighted mean with the base:
                "fuse": {"w": {"S3": {"u2": 0.5}}, "max_ratio": 0.4, "sources": {...optional per cat list}}
                Rows where a partner is beyond max_ratio (|ln partner / base|) keep the base, or, with
                "tiebreak": path, take whichever of base / partner sits closer in log to the tiebreak line.
  5. facts    - rows whose asked value a sibling video's prior states (Series 24 family-prior detail) take it.
     (snap  - before facts: catalog snap, s40_catalog_snap.snap_rows; "kinds" limits the catalog, e.g. the
              validation split only, and "skip_facts": false keeps the sibling-fact rows in play.)
  6. fixes    - {"id": value} corrections applied last before scale (e.g. a sibling fact from the wrong scene)
  7. scale    - optional per-population multipliers: [{"cat": "S3", "source": "lab", "kind": "motion", "x": 1.05}]
Writes the upload file, changes.csv (every row that differs from the base) and manifest.json (spec + sha256).

    python scripts/build_s40_stack.py --spec results/fulltest_s40_p1/spec.json
"""
import argparse
import hashlib
import json
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
import sys  # noqa: E402
sys.path.insert(0, str(ROOT / "scripts"))
FACTS = "results/fulltest_s24_famprior/famprior_detail.csv"
EXCLUDE_ROOTS = {"internet_0025"}  # its _segmented file is a different, shorter cut (build_s26_twin_pool.py)
MOTION = r"velocity|speed|acceleration|displacement|distance|travel|moved|path"


def canon(v):
    v = v.replace("_segmented", "")
    return re.sub(r"(?<=\d)[sxX]$", "", v) if v.startswith("captured_") else v


def norm(s):
    return " ".join(str(s).lower().split())


def series(path):
    return pd.read_csv(ROOT / path).set_index("id").parsed_value.astype(float)


def pool(vals, groups):
    out = vals.copy()
    for ids in groups:
        v = vals.reindex(ids)
        v = v[np.isfinite(v) & (v > 0)]
        if len(v) < 2:
            continue
        p = float(np.median(v)) if len(v) >= 3 else float(np.exp(np.log(v).mean()))
        out.loc[ids] = p
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    a = ap.parse_args()
    spec_path = ROOT / a.spec
    spec = json.loads(spec_path.read_text())
    out = spec_path.parent
    led = pd.read_csv(ROOT / "results/s26_scene_full/ledger.csv").set_index("id")
    ds = pd.DataFrame(json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text()))
    ds["id"] = ds.row_idx + 1
    ds = ds.set_index("id").loc[led.index]
    cat, src = led.category, led.source
    motion = led.question.str.contains(MOTION, case=False)
    first_path = next(iter(spec["base"].values()))
    first = pd.read_csv(ROOT / first_path)
    base = pd.Series(np.nan, index=led.index)
    for c, p in spec["base"].items():
        s = series(p)
        m = cat == c
        base[m] = s.reindex(led.index[m]).values
    lines = {"base": base}
    for n, p in spec.get("lines", {}).items():
        lines[n] = series(p).reindex(led.index)
    key = pd.Series([(canon(v), norm(q), norm(p), str(d)) for v, q, p, d in
                     zip(ds.video_id, ds.question, ds.prior, ds.depth_info)], index=led.index)
    pl = spec.get("pool")
    if pl:
        m = cat.isin(pl["cats"]) & (src.isin(pl["sources"]) if pl.get("sources") else True)
        if pl.get("exclude_roots", False):
            m &= ~ds.video_id.map(canon).isin(EXCLUDE_ROOTS)
        tp = pl.get("pick")
        if not tp:
            groups = [list(g) for g in key[m].groupby(key[m]).groups.values() if len(g) > 1]
            for n in pl.get("lines", ["base"]):
                lines[n] = pool(lines[n], groups)
        else:
            # lab renders: the strict key (same prior and depth_info), median of the renders, as in P1 - P4
            ml = m & (src == "lab")
            groups = [list(g) for g in key[ml].groupby(key[ml]).groups.values() if len(g) > 1]
            for n in pl.get("lines", ["base"]):
                lines[n] = pool(lines[n], groups)
            # non-lab twins: one footage, one label even when the prior text or depth_info differ, so the group is
            # (canonical video, question). Members within tp["thr"] (|ln| of the base line) are pooled; a wider
            # group takes, in every line, the values of the member whose two Opus lines (tp["a"], tp["b"]) agree best
            # by at least tp["margin"] (a twin whose reference object is masked out reads another scale, and
            # averaging it in only halves the error); otherwise it is pooled too.
            lk = pd.Series([(canon(v_), norm(q)) for v_, q in zip(ds.video_id, ds.question)], index=led.index)
            mn = m & (src != "lab")
            ca, cb = lines[tp["a"]].copy(), lines[tp["b"]].copy()
            npool, npick = [], 0
            # video-pair level first: when a twin's answers sit systematically off its original's (median |ln| over
            # the shared questions > thr) and that twin's two Opus lines agree clearly worse over all its questions
            # (median |ln a/b| larger by >= margin), every shared question takes the better member's values
            vid = ds.video_id
            vcons = np.log(ca / cb).abs().groupby(vid).median()
            pair_best = {}
            pairs = {}
            for g in [list(g) for g in lk[mn].groupby(lk[mn]).groups.values() if len(g) > 1]:
                pairs.setdefault(tuple(sorted(set(vid[g]))), []).append(g)
            for vs, gs in pairs.items():
                if len(vs) != 2:
                    continue
                lr = []
                for g in gs:
                    bv = lines["base"].reindex(g)
                    a_ = bv[vid[g] == vs[0]].median()
                    b_ = bv[vid[g] == vs[1]].median()
                    if a_ > 0 and b_ > 0:
                        lr.append(abs(np.log(a_ / b_)))
                if len(lr) >= tp.get("pair_min", 3) and np.median(lr) > tp["thr"]:
                    c0, c1 = vcons.get(vs[0], np.nan), vcons.get(vs[1], np.nan)
                    if np.isfinite(c0) and np.isfinite(c1) and abs(c0 - c1) >= tp.get("margin", 0.05):
                        pair_best[vs] = vs[0] if c0 < c1 else vs[1]
            done = set()
            for vs, best_vid in pair_best.items():
                for g in pairs[vs]:
                    src_ids = [i for i in g if vid[i] == best_vid]
                    if not src_ids:
                        continue
                    for n in lines:
                        lines[n].loc[g] = lines[n][src_ids[0]]
                    done.update(g)
                    npick += 1
            print(f"twin pairs decided at video level: {len(pair_best)} {sorted(pair_best.values())}")
            for g in [list(g) for g in lk[mn].groupby(lk[mn]).groups.values() if len(g) > 1]:
                if set(g) & done:
                    continue
                bv = lines["base"].reindex(g)
                if not (bv > 0).all():
                    continue
                if np.log(bv.max() / bv.min()) <= tp["thr"]:
                    npool.append(g)
                    continue
                cons = np.log(ca.reindex(g) / cb.reindex(g)).abs()
                if not np.isfinite(cons).all() or cons.sort_values().iloc[1] - cons.min() < tp.get("margin", 0.05):
                    npool.append(g)  # no member stands out: pool as P1 - P4 did
                    continue
                best = cons.idxmin()
                for n in lines:
                    lines[n].loc[g] = lines[n][best]
                npick += 1
            for n in pl.get("lines", ["base"]):
                lines[n] = pool(lines[n], npool)
            print(f"twin groups pooled {len(npool)}, picked {npick}")
    v = lines["base"].copy()
    fu = spec.get("fuse")
    if fu:
        tb = series(fu["tiebreak"]).reindex(led.index) if fu.get("tiebreak") else None
        cap = fu.get("max_ratio", 0)
        from s40_catalog_snap import parse_q
        is_size = ds.question.map(lambda q: parse_q(q) is not None)
        for i in led.index:
            ws = fu["w"].get(cat[i])
            # per-population overrides: the first rule matching (category, source, static size or not) wins
            for r in fu.get("w_rules", []):
                if cat[i] in r["cats"] and src[i] in r["sources"] and (
                        r.get("kind") is None or (r["kind"] == "size") == bool(is_size[i])):
                    ws = r["w"]
                    break
            if not ws:
                continue
            allowed = fu.get("sources", {}).get(cat[i])
            if allowed and src[i] not in allowed:
                continue
            b = lines["base"][i]
            xs = {n: lines[n][i] for n in ws}
            if not (b > 0 and all(np.isfinite(x) and x > 0 for x in xs.values())):
                continue
            if cap and any(abs(np.log(x / b)) > cap for x in xs.values()):
                if tb is not None and len(xs) == 1 and np.isfinite(tb[i]) and tb[i] > 0:
                    x = next(iter(xs.values()))
                    v[i] = x if abs(np.log(x / tb[i])) < abs(np.log(b / tb[i])) else b
                continue
            wb = 1.0 - sum(ws.values())
            v[i] = float(np.exp(wb * np.log(b) + sum(ws[n] * np.log(xs[n]) for n in ws)))
    rules = spec.get("median_rules", [])
    if spec.get("median3"):
        md = spec["median3"]
        rules = [{"pair": md["lines"][:2], **md}] + rules
    for md in rules:
        # rows where the two "pair" lines disagree beyond thr take the median of the named lines (a per-row
        # tie-break; with an even count the geometric mean of the middle two)
        ls = [lines[n] if n in lines else series(n).reindex(led.index) for n in md["lines"]]
        pa, pb = (lines[n] if n in lines else series(n).reindex(led.index) for n in md["pair"])
        m = cat.isin(md["cats"]) & src.isin(md["sources"]) & (pa > 0) & (pb > 0)
        if md.get("only"):
            m &= led.index.isin(set(pd.read_csv(ROOT / md["only"]).id))
        for x in ls:
            m &= (x > 0) if md.get("require_all", True) else True
        m &= np.log(pa / pb).abs() > md["thr"]
        if md.get("kind") == "motion":
            m &= motion
        elif md.get("kind") == "size":
            m &= ~motion
        stack = np.log(np.vstack([x[m].where(x[m] > 0) for x in ls]))
        if md.get("agg") == "mean":
            # a geometric mean of the named lines (weights in "w", default equal): a third sample, not a selector
            w = np.array(md.get("w", [1.0] * len(ls)), dtype=float)[:, None]
            ok = np.isfinite(stack)
            v[m] = np.exp(np.nansum(stack * w, axis=0) / np.sum(w * ok, axis=0))
        else:
            v[m] = np.exp(np.nanmedian(stack, axis=0))
    fp = spec.get("fampool")
    if fp:
        from s40_catalog_snap import parse_q
        fam = json.loads((ROOT / "results/fulltest_s24_famprior/families.json").read_text())
        v2f = {v: k for k, vs in fam.items() for v in vs}
        rec = []
        for i in led.index:
            if src[i] not in ("simulation", "segmentation") or cat[i] not in fp.get("cats", ["S2", "D2", "S3", "D3"]):
                continue
            x = parse_q(ds.question[i])
            vid = ds.video_id[i]
            f = v2f.get(vid) or v2f.get(canon(vid))
            if x and f:
                rec.append((i, f, canon(vid), x[0], x[1]))
        R = pd.DataFrame(rec, columns=["id", "fam", "canon", "dim", "obj"])
        R["v"] = v.reindex(R.id).values
        for _, g in R.groupby(["fam", "dim", "obj"]):
            per = g.groupby("canon").v.median()
            if len(per) < 2 or per.max() / per.min() > fp.get("max_spread", 1.5):
                continue
            v.loc[g.id.values] = float(np.median(per.values))
    sn = spec.get("snap")
    if sn:
        from s40_catalog_snap import snap_rows
        S, _ = snap_rows(v, sn.get("near", .3), sn.get("lab", .15), sn.get("far", .12), sn.get("window", 12),
                         kinds=sn.get("kinds"), skip_facts=sn.get("skip_facts", True))
        if len(S):
            S = S[S.cat.isin(sn.get("cats", ["S2", "D2", "S3", "D3"]))]
            v.loc[S.id.values] = S.parsed_value.values
            S.to_csv(out / "snap_rows.csv", index=False)
    pr = spec.get("props")
    if pr:
        # Series 41 (Track B): the paper's appendix-B lab prop table (scripts/lab_props.py), after the catalog snap
        import lab_props as LP
        npr = 0
        for i in led.index[(src == "lab") & cat.isin(pr.get("cats", ["S2", "D2", "S3", "D3"]))]:
            nv, hit = LP.snap(ds.question[i], v[i], "lab", tol=pr.get("tol", 1.6))
            if hit is not None and abs(nv - v[i]) > 1e-9 * abs(v[i]):
                v[i] = nv
                npr += 1
        print(f"prop table: {npr} rows moved")
    if spec.get("facts"):
        f = pd.read_csv(ROOT / FACTS).set_index("id").parsed_value
        f = f[f.index.isin(led.index) & cat.reindex(f.index).isin(spec["facts"]).values]
        v.loc[f.index] = f.values
    for i, x in spec.get("fixes", {}).items():
        v[int(i)] = float(x)
    for s in spec.get("scale", []):
        m = cat == s["cat"]
        if s.get("source"):
            m &= src == s["source"]
        if s.get("kind") == "motion":
            m &= motion
        elif s.get("kind") == "size":
            m &= ~motion
        v[m] = v[m] * s["x"]
    v = v.map(lambda x: float(f"{x:.6g}"))
    full = first.set_index("id").parsed_value.astype(float).copy()
    full.loc[v.index] = v.values
    name = spec["name"]
    first.assign(parsed_value=full.reindex(first.id).values).to_csv(out / name, index=False)
    ch = pd.DataFrame({"cat": cat, "source": src, "base": base, "after": v})
    ch = ch[(ch.after - ch.base).abs() > 1e-9 * ch.base.abs()]
    ch.to_csv(out / "changes.csv")
    sha = hashlib.sha256((out / name).read_bytes()).hexdigest()
    man = {"series": "40", "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "spec": spec,
           "rows_changed": len(ch), "by_cat": ch.cat.value_counts().to_dict(), "file": str((out / name).relative_to(ROOT)),
           "sha256": sha}
    (out / "manifest.json").write_text(json.dumps(man, indent=1))
    print(json.dumps({k: man[k] for k in ("rows_changed", "by_cat", "file", "sha256")}, indent=1))


if __name__ == "__main__":
    main()
