"""Series 43 (2026-10-26, session 0c8cbddf): which rows of an uploaded Track A file still carry a value the aligned
2026-10-22 compliance judgments keep out (run channel #188; the deny groups of `s34_check_entry.py --deny-default`).

Per group, each id is counted as `out` (equals the ruled-out value), `clean` (equals the value the 10-22 builds put
there) or `other` (neither: moved since, e.g. by per-question fusion or an RSI answer; `pos` = median position of those
rows on the log scale from the out value (0) to the clean value (1)). degen and plaus rows were ruled ALLOWED (#188 items
1 and 5) and are listed for completeness. In the s32 lab0018 / labdist_f change files `after` is the ruled-out value.

    python scripts/s43_deny_audit.py results/fulltest_s43_strict_rsi/track_a_s43_strict_rsi.csv [more files]
"""
import csv
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "results"
GROUPS = [("fulltest_s34_legit_a/changes.csv", "before"), ("fulltest_s34_nogray_a/changes.csv", "before"),
          ("fulltest_s32_lab0018/changes.csv", "after"), ("fulltest_s32_labdist_f/changes.csv", "after")]
ALLOWED = {"degen", "plaus"}


def load(p):
    with open(p, newline="") as f:
        return list(csv.DictReader(f))


def same(a, b):
    return abs(a - b) <= 1e-4 * max(1.0, abs(b))


def groups():
    g = defaultdict(list)
    for f, out_col in GROUPS:
        clean_col = "after" if out_col == "before" else "before"
        name = None if "group" in load(R / f)[0] else Path(f).parent.name.replace("fulltest_s32_", "")
        for r in load(R / f):
            g[name or r["group"]].append((r["id"], float(r[out_col]), float(r[clean_col])))
    return g


def main():
    g = groups()
    for path in sys.argv[1:]:
        v = {r["id"]: float(r["parsed_value"]) for r in load(path)}
        print(path)
        for name, rows in g.items():
            c, pos = Counter(), []
            for i, out, clean in rows:
                x = v.get(i)
                if x is None:
                    c["missing"] += 1
                elif same(x, out) and not same(out, clean):
                    c["out"] += 1
                elif same(x, clean):
                    c["clean"] += 1
                else:
                    c["other"] += 1
                    if min(x, out, clean) > 0 and abs(math.log(clean / out)) > 1e-3:
                        pos.append(math.log(x / out) / math.log(clean / out))
            pos.sort()
            tag = " (allowed)" if name in ALLOWED else ""
            med = f" pos {pos[len(pos) // 2]:.2f}" if pos else ""
            print(f"  {name}{tag} n={len(rows)}: {dict(c)}{med}")


if __name__ == "__main__":
    main()
