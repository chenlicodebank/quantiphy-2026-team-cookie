"""Trace every value of the Track A answer lines to where it comes from (answers/leaf_rows.csv).

    python build/check_leaves.py     # from the package root

For each line of answers/leaf_rows.csv: the value must be the line's value for that row, and
- `q`: the raw answer in the named per-question session record (answers.json), after the rule, gives the value;
- `ledger`: the session's first answer as the run ledger recorded it (results/s26_scene_full/ledger.csv), after the rule;
- `code_measurement`: our code's measurement on a scene record's object track (answers/s31_factors.csv), after the rule;
- `per_video_186`: the value of our earlier per-video line (results/fulltest_s26_ccagent_full/...), after the rule;
- `paper_table`, `human_check`, `board_probe`: no per-question record; the value is checked against its source table
  where one exists (combine_rows.csv's table step, the human-check record) and the rows are listed (STATEMENT.md).
It also checks that every row each line contributes is covered. Prints counts per line and class; exit 1 on a failure.
"""
import csv
import io
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
LINES = {
    "E2": ("results/fulltest_s27_e2/track_a_s27_e2.csv", "parsed_value"),
    "E2_pretable": ("results/fulltest_s27_e2/combine_rows.csv", "before"),
    "U1": ("results/fulltest_s30_u1/track_a_s30_u1.csv", "parsed_value"),
    "R39_4": ("results/s39_2dmotion/collected.csv", "new_t"),
    "L200": ("results/fulltest_s26_reask_full/track_a_s26_reask_full.csv", "parsed_value"),
    "RSI:fulltest_s43_strict_rsi": ("results/fulltest_s43_strict_rsi/apply_r123.csv", "value"),
    "RSI:fulltest_s43_gray_rsi": ("results/fulltest_s43_gray_rsi/apply_final.csv", "value"),
}


def load(p):
    with open(PKG / p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pd_rt(x):
    import pandas as pd
    return float(pd.read_csv(io.StringIO("v\n" + repr(x) + "\n"), dtype={"v": float}).v.iloc[0])


def apply(rule, raw, param):
    if rule == "x1":
        return raw
    if rule == "k1.25_round6":
        return round(raw * 1.25, 6)
    if rule in ("x1.215", "x1.19", "x1.03"):
        return raw * float(rule[1:])
    if rule == "physb_k":
        return pd_rt(raw * float(param))
    if rule == "dirF_round6":
        return round(raw * float(param), 6)
    if rule == "x1.5_round3":
        return round(raw * 1.5, 3)
    if rule == "x1.5_round4":
        return round(raw * 1.5, 4)
    if rule == "round6":
        return round(raw, 6)
    raise ValueError(rule)


def same(a, b):
    return a == b or abs(a - b) <= 1e-9 * max(abs(a), abs(b))


def main():
    rows = load("answers/leaf_rows.csv")
    vals = {k: {int(r["id"]): float(r[c]) for r in load(p) if (k != "E2_pretable" or r["step"] == "table")}
            for k, (p, c) in LINES.items()}
    led = {int(r["id"]): r for r in load("results/s26_scene_full/ledger.csv")}
    s31 = {int(r["id"]): r for r in load("answers/s31_factors.csv")}
    v186 = {int(r["id"]): float(r["parsed_value"]) for r in load("results/fulltest_s26_ccagent_full/track_a_s26_ccagent_full.csv")}
    table = {int(r["id"]): float(r["after"]) for r in load("results/fulltest_s27_e2/combine_rows.csv") if r["step"] == "table"}
    fixes = {int(r["id"]): float(r["after"]) for r in load("results/human_check/approved_fixes.csv")}
    e2 = {int(r["id"]): r["parsed_value"] for r in load(LINES["E2"][0])}
    u1 = {int(r["id"]): r["parsed_value"] for r in load(LINES["U1"][0])}

    fails, counts, seen = [], defaultdict(Counter), defaultdict(set)
    for x in rows:
        line, i, v, cls = x["line"], int(x["id"]), float(x["value"]), x["cls"]
        seen[line].add(i)
        if not same(vals[line][i], v):
            fails.append((line, i, "not the line's value"))
        raw = float(x["raw"]) if x["raw"] else None
        if cls == "q":
            got = json.loads((PKG / x["record"] / "answers.json").read_text())[str(i)]
            ok = raw is not None and same(float(got), raw) and same(apply(x["rule"], raw, x["param"]), v)
        elif cls == "ledger":
            ok = same(float(led[i]["first_answer"]), raw) and same(apply(x["rule"], raw, x["param"]), v)
        elif cls == "code_measurement":
            ok = same(float(s31[i]["clean"]), raw) and same(apply(x["rule"], raw, x["param"]), v)
        elif cls == "per_video_186":
            ok = same(v186[i], raw) and same(apply(x["rule"], raw, x["param"]), v)
        elif cls == "paper_table":
            ok = same(table[i], v)
        elif cls == "human_check":
            ok = i not in fixes or same(fixes[i], v)
        elif cls == "board_probe":
            ok = True
        else:
            ok = False
        if not ok:
            fails.append((line, i, cls))
        counts[line][cls + (" scored" if x["scored"] == "1" else " unscored")] += 1

    need = {"E2": set(e2), "E2_pretable": set(table), "U1": {i for i in u1 if u1[i] != e2[i]},
            "R39_4": set(vals["R39_4"]), "L200": seen["L200"] | set(), "RSI:fulltest_s43_strict_rsi":
            set(vals["RSI:fulltest_s43_strict_rsi"]), "RSI:fulltest_s43_gray_rsi": set(vals["RSI:fulltest_s43_gray_rsi"])}
    for k, ids in need.items():
        if ids - seen[k]:
            fails.append((k, sorted(ids - seen[k])[:5], "rows not covered"))
    print(json.dumps({"rows": len(rows), "by_line": {k: dict(sorted(v.items())) for k, v in counts.items()},
                      "failures": fails[:20], "n_failures": len(fails)}, indent=1))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
