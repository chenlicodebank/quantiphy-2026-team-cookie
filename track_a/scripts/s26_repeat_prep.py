"""Series 26, run 26_80 (2026-10-21): prepare two more independent answers ("repeat runs") of the 3D Track A questions whose
per-question answers are noisy from run to run, for a per-question median of three.

Why: 3D answers are variance-limited, and the noise is heavy-tailed. 26_36's 30 true repeat pairs on 3D S3 differ by more
than 30 pct in 23 pct of questions (2D D2: 3 pct). The lab render triples (the same capture and question on a complex,
simple and plain background, same reference answer) disagree by more than 10 pct on 56 pct of the D3 speed pairs and 33
pct of the S3 speed pairs, against 10 pct of the S3 size pairs. A median of three removes a single run's gross miss,
which a geometric mean of two only halves (26_36 judged the mean of two, by agreement with #186). Simulated with those
residuals: about +.07 a row on lab D3 speeds, +.02 on lab S3 speeds, +.04 on 3D accelerations, ~0 on lab sizes.

Compliance (organisers' rule of 2026-10-15): every run is a fresh session that sees only the video, its question, that
question's own prior / depth_info and the question-blind scene record, exactly as the first run; repeated runs of the
same question are allowed (challenge.md, per-question rule). The median is a function of one question's own runs.

Selection is by question type only, never by the answers, so a board read of the result is clean:
- P1: lab rows in S3 / D3 asking a speed, velocity, acceleration or path length (the label-noise-free part of their
  error is the session's own measurement);
- P2: simulation / segmentation rows in S3 / D3 asking an acceleration;
- P3: simulation / segmentation rows in D3 asking a size (--p3 all, or --p3-pilot N seeded rows, at most 2 a video, for a
  true-repeat spread read before the full set).
Rows whose current answer came from the 26_59 --real-scale re-ask are left out (their repeats would need that prompt).

Two out dirs, one per account pool, split by video, so no question folder is written by two pools at once (attempt
numbers come from each folder's history); each holds copies of the 26_30 scene records, the selected question folders and
the clip files, so results/s26_scene_full stays untouched. Two rerun specs per out dir (repeat 2 and repeat 3), run in
that order by the same pool.

    python scripts/s26_repeat_prep.py --out results/s26_repeat_1021 --p3-pilot 30
"""
import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

from s26_reask_prep import copy_video

ROOT = Path(__file__).resolve().parents[1]
RUN = "26_80"
TRIGGERS = {2: f"repeat run 2 of 3 ({RUN}, per-question median of three)",
            3: f"repeat run 3 of 3 ({RUN}, per-question median of three)"}


def qtype(q):
    q = q.lower()
    if "accel" in q:
        return "accel"
    if re.search(r"speed|veloc|velol", q):
        return "speed"
    if "displacement" in q:
        return "disp"
    if "distance" in q and re.search(r"travel|moved|cover|path", q):
        return "path"
    if re.search(r"distance|diatance", q):
        return "dist"
    return "size"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", default="results/s26_scene_full")
    ap.add_argument("--reask", default="results/s26_reask_1020")
    ap.add_argument("--out", required=True, help="prefix; _company and _personal are appended")
    ap.add_argument("--p3", action="store_true", help="every P3 row")
    ap.add_argument("--p3-pilot", type=int, default=0, help="N seeded P3 rows (at most 2 a video)")
    ap.add_argument("--only", default="P1,P2,P3", help="populations to include")
    ap.add_argument("--exclude-ids", help="file with ids already repeated (a later stage)")
    ap.add_argument("--b-share", type=float, default=0.67, help="share of the first-run cost for pool B")
    ap.add_argument("--seed", type=int, default=80)
    a = ap.parse_args()
    src = ROOT / a.run
    full = pd.read_csv(src / "ledger.csv")
    L = full.copy()
    L["qt"] = L.question.map(qtype)
    reask = pd.read_csv(ROOT / a.reask / "attempts.tsv", sep="\t")
    reasked = {int(x) for x in reask.ids.astype(str) if x.isdigit()}
    L = L[~L.id.isin(reasked)]
    sim = L.source.isin(["simulation", "segmentation"])
    pops = {"P1": (L.source == "lab") & L.category.isin(["S3", "D3"]) & L.qt.isin(["speed", "accel", "path"]),
            "P2": sim & L.category.isin(["S3", "D3"]) & (L.qt == "accel"),
            "P3": sim & (L.category == "D3") & (L.qt == "size")}
    keep = set(a.only.split(","))
    parts = []
    for name, m in pops.items():
        if name not in keep:
            continue
        g = L[m].assign(pop=name)
        if name == "P3" and not a.p3:
            if not a.p3_pilot:
                continue
            rng = np.random.default_rng(a.seed)
            g = g.sample(frac=1, random_state=rng.integers(1 << 31)).groupby("video").head(2).head(a.p3_pilot)
        parts.append(g)
    S = pd.concat(parts).drop_duplicates("id")
    if a.exclude_ids:
        done = set(json.loads(Path(a.exclude_ids).read_text()))
        S = S[~S.id.isin(done)]
    # split by video, cheapest-first greedy so pool B gets about its share of the first-run cost
    by_vid = S.groupby("video").cost.sum().sort_values(ascending=False)
    target, acc, pool_b = a.b_share * S.cost.sum(), 0.0, set()
    for vid, c in by_vid.items():
        if acc + c <= target or not pool_b:
            pool_b.add(vid)
            acc += c
    S["pool"] = np.where(S.video.isin(pool_b), "b", "a")
    for pool in ("a", "b"):
        out = ROOT / f"{a.out}_{pool}"
        if out.exists():
            raise SystemExit(f"{out} exists; use a new out dir")
        P = S[S.pool == pool]
        out.mkdir(parents=True)
        for vid in sorted(P.video.unique()):
            copy_video(src, out, vid, sorted(int(i) for i in full[full.video == vid].id), sorted(P[P.video == vid].id))
        P[["id", "video", "source", "category", "kind", "qt", "pop", "question", "prior", "answer", "cost", "pool"]].to_csv(
            out / "selection.csv", index=False)
        (out / "events.txt").write_text(",".join(sorted(P.video.unique())) + "\n")
        for n, trig in TRIGGERS.items():
            (out / f"rerun_r{n}.json").write_text(json.dumps({"trigger": trig, "ids": sorted(int(i) for i in P.id)},
                                                             indent=1) + "\n")
        guard = json.loads((src / f"guard_{pool}.json").read_text())
        guard["note"] = (f"{RUN} repeat runs ({pool.upper()} pool): two more phase-2 answers of each selected question on "
                         "copies of its 26_30 scene record, for a per-question median of three. Caps as 26_30's pools; "
                         "cost tables = 26_30's observed ones.")
        (out / f"guard_{pool}.json").write_text(json.dumps(guard, indent=1) + "\n")
        print(f"{pool}: {len(P)} questions on {P.video.nunique()} videos, first-run cost ${P.cost.sum():.0f}, "
              f"two repeats about ${2 * P.cost.sum():.0f}")
    print(S.groupby(["pop", "category", "qt"]).size().to_string())
    print(f"all: {len(S)} questions, two repeats about ${2 * S.cost.sum():.0f}")


if __name__ == "__main__":
    main()
