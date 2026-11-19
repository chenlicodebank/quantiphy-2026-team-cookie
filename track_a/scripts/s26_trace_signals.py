"""Series 26, 2026-10-20: signals in the 26_30 per-question traces that point at fixable Track A errors.

Reads the 26_30 question ledger, the compliant #199 file and the per-question workspaces, and writes the rows each
signal reaches. Labels come only from places that already hold them: the validation split, and the Series 24
stated-fact rows (a sibling video's prior that states the asked quantity) used here as LABELS for a diagnosis, never
as answers - the per-question rule forbids the latter. #197 appears as a diagnostic column only.

- fixed_origin: a 3D render whose depth_info gives a walking character's distance at two times that changes by less
  than 0.1 m/s. The distance is then to a rig origin that stays put while the body walks, so "constant depth" does not
  mean the walk runs across the view; sessions that read it so get the scale wrong by up to 3x.
- named_axes: length / width of aircraft and butterflies, where the --size-names reading (length = longer horizontal
  extent) can swap a span and a length. Birds' length rows sit in fixed_origin videos.
- degenerate_prior: internet_0065, a gravity prior on a ball that only rolls (displacements of ~15 m beside the same
  clip's 2.7 m/s velocity answers).
- stale_clip: rows whose build value (stage_scene.csv, read from clips/<video>/answers.json) is not the question's
  current answer: rerun() updated a clip aggregate only if it already existed, and the pool still answering the video
  then wrote it from its own first-attempt values.

    python scripts/s26_trace_signals.py --out results/s26_trace_signals
"""
import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CREATURE = (r"human|person|man|woman|pedestrian|people|boatman|walker|cat|dog|horse|dragon|eagle|bird|deer|cow|shark|"
            r"turtle|fish|astronaut|robot|rabbit|cyclist|rider")
TH = np.array([.1, .2, .3, .4, .5, .6, .7, .8, .9, .95])


def mra(p, g):
    p, g = np.asarray(p, float), np.asarray(g, float)
    return ((np.abs(p - g) / np.abs(g))[:, None] < (1 - TH)[None, :]).mean(1)


def depth_rates(text):
    """{object: metres per second} for every object depth_info gives at two or more times."""
    by = {}
    for t, obj, val in re.findall(r"t\s*=\s*([\d.]+)\s*s?\s*,\s*distance_(.+?)_camera\s*=\s*([\d.]+)", str(text)):
        by.setdefault(obj.strip(), []).append((float(t), float(val)))
    out = {}
    for obj, tv in by.items():
        tv.sort()
        if len(tv) >= 2 and tv[-1][0] > tv[0][0]:
            out[obj] = (tv[-1][1] - tv[0][1]) / (tv[-1][0] - tv[0][0])
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", default="results/s26_scene_full")
    ap.add_argument("--build", default="results/fulltest_s26_compliant")
    ap.add_argument("--diag", default="results/fulltest_s26_u2/track_a_s26_u2.csv")  # #197, diagnostic only
    ap.add_argument("--facts", default="results/fulltest_s24_famprior/famprior_detail.csv")
    ap.add_argument("--out", default="results/s26_trace_signals")
    a = ap.parse_args()
    run, build, out = ROOT / a.run, ROOT / a.build, ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)

    L = pd.read_csv(run / "ledger.csv")
    sub = pd.read_csv(next(build.glob("track_a_*.csv")))[["id", "parsed_value", "depth_info"]]
    stage = pd.read_csv(build / "stage_scene" / "stage_scene.csv")[["id", "parsed_value"]]
    diag = pd.read_csv(ROOT / a.diag)[["id", "parsed_value"]]
    facts = pd.read_csv(ROOT / a.facts)[["id", "parsed_value", "source_line"]]
    M = (L.merge(sub.rename(columns={"parsed_value": "s199", "depth_info": "depth_text"}), on="id")
          .merge(stage.rename(columns={"parsed_value": "stage"}), on="id")
          .merge(diag.rename(columns={"parsed_value": "s197"}), on="id")
          .merge(facts.rename(columns={"parsed_value": "fact"}), on="id", how="left"))

    # fixed_origin
    fixed = set()
    for vid, text in M.drop_duplicates("video")[["video", "depth_text"]].itertuples(index=False):
        for obj, rate in depth_rates(text).items():
            if re.search(CREATURE, obj) and "bike" not in obj and abs(rate) < 0.1:
                fixed.add(vid)
    M["fixed_origin"] = M.video.isin(fixed)
    # named_axes
    M["named_axes"] = (M.question.str.contains(r"\b(length|width)\b", case=False)
                       & M.question.str.contains(r"\b(plane|airplane|aircraft|jet|butterfly)\b", case=False)
                       & ~M.fixed_origin)
    # degenerate_prior
    M["degenerate_prior"] = M.video.eq("internet_0065")
    # stale_clip
    cur = []
    for vid, qid in M[["video", "id"]].itertuples(index=False):
        f = run / "q" / f"{vid}__{qid}" / "answers.json"
        cur.append(float(json.loads(f.read_text())[str(qid)]) if f.exists() else np.nan)
    M["current"] = cur
    M["stale_clip"] = ~np.isclose(M.stage, M.current, rtol=1e-9)

    sig = ["fixed_origin", "named_axes", "degenerate_prior", "stale_clip"]
    M["signals"] = M[sig].apply(lambda r: ",".join(s for s in sig if r[s]), axis=1)
    R = M[M.signals != ""]
    R[["id", "video", "source", "category", "question", "prior", "signals", "s199", "stage", "current", "s197", "fact",
       "confidence", "plus_minus_pct", "cost"]].to_csv(out / "rows.csv", index=False)

    F = M[M.fact.notna()]
    summary = {"rows": len(M), "fixed_origin_videos": sorted(fixed)}
    for s in sig:
        x = M[M[s]]
        fx = x[x.fact.notna()]
        summary[s] = {"rows": int(len(x)), "by_category": x.category.value_counts().to_dict(),
                      "fact_rows": int(len(fx)),
                      "fact_mra_199": round(float(mra(fx.s199, fx.fact).mean()), 4) if len(fx) else None,
                      "first_run_cost_usd": round(float(x.cost.sum()), 1)}
    summary["fact_rows_all"] = {"rows": int(len(F)), "mra_199": round(float(mra(F.s199, F.fact).mean()), 4),
                                "mra_199_outside_fixed_origin":
                                    round(float(mra(F[~F.fixed_origin].s199, F[~F.fixed_origin].fact).mean()), 4)}
    (out / "summary.json").write_text(json.dumps(summary, indent=1) + "\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
