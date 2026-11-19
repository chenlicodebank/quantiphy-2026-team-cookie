"""Series 37 Track B build (session 05e6b3c8, 2026-10-24): the declared s33_final_b.py chain on per-question medians.

Every question's answer is the median of its own DeepSeek-1017 + SAM 3 runs (r1 of results/s29_pass_sam3 copied into
the repeat folder, plus r2 / r3 / ... of the same configuration, 37_1 / 37_2), optionally followed by the 37_3
physical-scale rule on internet questions; the per-question values then go through s33_final_b.py unchanged (lab
factors k / s or the row's own F, S3 with tools, D3 lab open-geometry fill, no prop table, no E2 read), so the only
difference from the declared B7 file is how many runs of the same question feed each row.

With --physcheck also listed in --runs, the 37_3 sessions' own answers (on the prior's scale, the card tells them not to
change the answer) are one more run of the question in every median (counted once).

Physical-scale rule (fixed 2026-10-24 before any 37_3 answer was read): from each 37_3 session of the question, the
fenced scale_check block in its notes.md; k = standard_m / implied_m, the median over adult persons if any were
measured, else over balls; the rule fires when the session calls the clip self-filmed, |ln k| > ln 1.15 and
1/3 < k < 3, and (added 2026-10-24 03:45 UTC, after the one firing case so far, internet_0016 q2081 under a court-width
prior; no label read) only when the question's own prior is a speed or acceleration - the convention as 26_52 and the
28_6 card state it: a stated MOTION prior that contradicts the scene. Then every run of that question is brought to the prior's scale (a run closer to k x the 37_3 answer
than to the 37_3 answer itself already switched, so it is divided by k), and the row is median x k.

    python scripts/s37_final_b.py --runs results/s37_test_repeats [--physcheck results/s37_physcheck] \
        --base results/fulltest_s33_l5const/track_b_s33_l5const.csv --model const --s3-tools --out results/fulltest_s37_<name>
"""
import argparse
import glob
import json
import math
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_s28_trackb as B  # noqa: E402
import s33_final_b as F  # noqa: E402

PERSON = re.compile(r"person|adult|man\b|woman|rider|player|people|human|boy|girl|pedestrian|walker", re.I)
BALL = re.compile(r"ball", re.I)
BLOCK = re.compile(r"```\s*scale_check\s*\n(.*?)```", re.S)


def runs(dirs, max_k=99, tagged=False):
    """{id: [answers of r1..r<max_k>]} over the run folders (a question's runs may sit in several folders);
    tagged=True gives {id: {"<folder>:<k>": answer}}."""
    acc = {}
    for d in dirs:
        for f in glob.glob(str(ROOT / d / "q" / "*" / "r*.json")):
            k = int(Path(f).stem[1:])
            if k > max_k:
                continue
            r = json.loads(Path(f).read_text())
            a = (r.get("final") or {}).get("answers") or []
            if a and isinstance(a[0].get("value"), (int, float)) and a[0]["value"] > 0:
                acc.setdefault(int(Path(f).parent.name.split("__")[-1]), {})[f"{d}:{k}"] = float(a[0]["value"])
    return acc if tagged else {i: list(v.values()) for i, v in acc.items()}


def scale_checks(d):
    """{id: [(answer, k or None, self_filmed, objects)]} from the 37_3 sessions' notes."""
    out = {}
    for f in glob.glob(str(ROOT / d / "q" / "*" / "r*.json")):
        r = json.loads(Path(f).read_text())
        a = (r.get("final") or {}).get("answers") or []
        if not a:
            continue
        i = int(Path(f).parent.name.split("__")[-1])
        m = BLOCK.findall(r.get("notes.md") or "")
        k, sf, objs = None, False, []
        if m:
            try:
                blk = json.loads(m[-1].strip())
            except ValueError:
                blk = None
            if isinstance(blk, dict):
                sf = bool(blk.get("self_filmed"))
                for o in blk.get("objects") or []:
                    try:
                        im, st = float(o.get("implied_m")), float(o.get("standard_m"))
                    except (TypeError, ValueError):
                        continue
                    if im > 0 and st > 0:
                        objs.append((str(o.get("name", "")), st / im))
                ppl = [x for n, x in objs if PERSON.search(n)]
                balls = [x for n, x in objs if BALL.search(n)]
                if ppl or balls:
                    k = float(np.median(ppl or balls))
        out.setdefault(i, []).append((float(a[0]["value"]), k, sf, objs))
    return out


def physical(chk, own, prior):
    """Rule v2 (2026-10-24 08:15 UTC): (value, k, runs used) when the physical-scale rule applies, else None.

    chk = the question's 37_3 sessions [(answer, k, self_filmed, objects)], own = its other runs (37_3 answers
    excluded), prior = its prior text. Applies when the prior is a speed or acceleration and a majority of its 37_3
    sessions call the clip self-filmed with a usable k (1/3 < k < 3). P = answer x k of those sessions (the physical-scale
    estimate, anchored on the session's own standard-object check); every other run is read either as already physical
    (x) or as on the prior's scale (x k), whichever lies nearer P, and kept if within 25 pct of it; the row is the median
    of P and the kept runs; when the sessions' k is within 26_52's 15 pct the session's own scale stands (k = 1, the rule
    only drops runs far from it). On internet_0043 the runs of one question sit in two modes a factor ~2 apart (sessions switch
    to the physical scale on their own, unevenly), which v1 (fire only when |ln k| > ln 1.15) left unresolved when the
    37_3 session itself had landed on the physical scale (q3072: runs 24.7 / 24.8, 37_3 51.2 at k 1.03)."""
    if not B.SPEED.search(str(prior)):
        return None
    good = [(x, k) for x, k, sf, _ in chk if sf and k is not None and 1 / 3 < k < 3]
    if not good or len(good) * 2 <= len(chk):
        return None
    kp = float(np.median([k for _, k in good]))
    if abs(math.log(kp)) <= math.log(1.15):   # 26_52's threshold: the session's own scale already passes its check
        kp, good = 1.0, [(x, 1.0) for x, _ in good]
    P = float(np.median([x * k for x, k in good]))
    vals = [x * k for x, k in good]
    for x in own:
        a1, a2 = abs(math.log(x / P)), abs(math.log(x * kp / P))
        if min(a1, a2) < math.log(1.25):
            vals.append(x if a1 <= a2 else x * kp)
    return float(np.median(vals)), kp, len(vals)


def fires(k, sf, prior=None):
    """The rule. prior=None skips the prior test (s37_phys_read.py's per-session view)."""
    if prior is not None and not B.SPEED.search(str(prior)):
        return False
    return k is not None and sf and abs(math.log(k)) > math.log(1.15) and 1 / 3 < k < 3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", required=True, help="repeat folder(s) with q/<video>__<id>/r<k>.json, comma-separated")
    ap.add_argument("--max-k", type=int, default=99, help="use only r1..r<max-k> of each folder")
    ap.add_argument("--physcheck", default="", help="37_3 folder; empty = no physical-scale rule")
    a, rest = ap.parse_known_args()
    dirs = [d for d in a.runs.split(",") if d]
    R = runs(dirs, a.max_k)
    agg, log = {}, []
    phys = scale_checks(a.physcheck) if a.physcheck else {}
    cur = pd.DataFrame(json.loads(B.CURRENT.read_text()))
    prior_of = dict(zip(cur.row_idx + 1, cur.prior))
    for i, v in R.items():
        med = float(np.median(v))
        agg[i] = med
        log.append(dict(id=i, n_runs=len(v), runs=";".join(f"{x:.6g}" for x in v), median=med, k="", rule=""))
    T = runs(dirs, a.max_k, tagged=True)
    for i, chk in phys.items():
        own = [x for key, x in T.get(i, {}).items() if key.rsplit(":", 1)[0] != a.physcheck]
        res = physical(chk, own, prior_of.get(i, ""))
        if res is None:
            continue
        agg[i], k, n = res
        log.append(dict(id=i, n_runs=n, runs=";".join(f"{x:.6g}" for x in own), median=agg[i], k=k,
                        rule="physical_scale"))
    B.ds_answers = lambda d: dict(agg)     # every --ds / --refill lookup in s33_final_b reads the aggregated answers
    sys.argv = [sys.argv[0]] + rest + ["--ds", "s37_aggregate"]
    F.main()
    out = ROOT / rest[rest.index("--out") + 1]
    pd.DataFrame(log).to_csv(out / "aggregate.csv", index=False)
    man = json.loads((out / "manifest.json").read_text())
    man.update(series="37", runs=a.runs, max_k=a.max_k, physcheck=a.physcheck, ds="per-question median of --runs",
               questions=len(R), runs_per_question=pd.Series([len(v) for v in R.values()]).value_counts().to_dict(),
               physical_scale_rows=int(sum(1 for x in log if x["rule"] == "physical_scale")))
    (out / "manifest.json").write_text(json.dumps(man, indent=1, default=str) + "\n")
    print(json.dumps({k: man[k] for k in ("questions", "runs_per_question", "physical_scale_rows")}, default=str))


if __name__ == "__main__":
    main()
