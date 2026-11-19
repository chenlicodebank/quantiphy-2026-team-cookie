"""37_2 (2026-10-24, session 05e6b3c8): which questions get one more run under the adaptive repeat policy.

Policy fixed before any test read (simulated on the 63 validation questions with seven runs: one run .775, two .788,
three .791, adaptive .797 at 2.6 runs a question): r3 when r1 and r2 differ by more than --a in |ln| (or one of them is
missing); r4 and r5 when the three runs spread more than --b in ln(max / min). Only the question's own runs decide.
Writes <out>/ids_<card|nocard>_<cat>_r<k>.txt (the r1 card split of s35_repeat_ids.py) and prints the counts.

    python scripts/s37_next_ids.py results/s37_test_repeats --k 3 [--a 0.05]
    python scripts/s37_next_ids.py results/s37_test_repeats --k 4 [--b 0.3]
"""
import argparse
import glob
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def answer(f):
    try:
        r = json.loads(Path(f).read_text())
    except (OSError, ValueError):
        return None
    a = (r.get("final") or {}).get("answers") or []
    v = a[0].get("value") if a else None
    return float(v) if isinstance(v, (int, float)) and v > 0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--k", type=int, required=True, help="the repeat to schedule (3, or 4 for r4 + r5)")
    ap.add_argument("--a", type=float, default=0.05)
    ap.add_argument("--b", type=float, default=0.3)
    a = ap.parse_args()
    out = ROOT / a.out
    # <out>/POLICY.json (2026-10-24 05:40 UTC) overrides --a / --b for pipelines already running, so the budget can
    # tighten the policy without restarting them (no answer is read to set it)
    pol = out / "POLICY.json"
    if pol.exists():
        o = json.loads(pol.read_text())
        a.a, a.b = float(o.get("a", a.a)), float(o.get("b", a.b))
        print(f"POLICY.json: a {a.a}, b {a.b}")
    groups = {}
    for name in ("ids_card_S2", "ids_card_D2", "ids_nocard_S3", "ids_nocard_D3"):
        p = out / f"{name}.txt"
        if p.exists():
            for i in p.read_text().strip().split(","):
                groups[int(i)] = name
    need, waiting = {}, 0
    for d in sorted(glob.glob(str(out / "q" / "*"))):
        i = int(Path(d).name.split("__")[-1])
        if i not in groups:
            continue
        rs = {k: answer(f"{d}/r{k}.json") for k in range(1, 6) if Path(f"{d}/r{k}.json").exists()}
        if a.k == 3:
            if 2 not in rs:
                waiting += 1
                continue
            r1, r2 = rs.get(1), rs.get(2)
            go = r1 is None or r2 is None or abs(math.log(r1 / r2)) > a.a
        else:
            if 3 not in rs:
                continue
            v = [x for k, x in rs.items() if k <= 3 and x]
            go = len(v) < 2 or math.log(max(v) / min(v)) > a.b
        if go and a.k not in rs:
            need.setdefault(groups[i], []).append(i)
    for name, ids in sorted(need.items()):
        (out / f"{name}_r{a.k}.txt").write_text(",".join(map(str, sorted(ids))) + "\n")
        print(f"{name}_r{a.k}: {len(ids)}")
    print(f"total r{a.k}: {sum(map(len, need.values()))}; questions still without r2: {waiting}")


if __name__ == "__main__":
    main()
