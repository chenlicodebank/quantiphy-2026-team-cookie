"""Write an upload file = a base file with the RSI answers of a row list put in (the --build half of
scripts/s43_rsi.py cmd_apply, which built #225 from C1 on 2026-10-26: same csv module calls, same %.6g format).

    python build/overlay_rsi.py <base.csv> <rows.csv (id,value,...)> <out.csv>
"""
import csv
import sys
from pathlib import Path


def main():
    base, rows, out = sys.argv[1:4]
    df = list(csv.DictReader(open(base, newline="", encoding="utf-8")))
    new = {int(x["id"]): float(x["value"]) for x in csv.DictReader(open(rows, newline="", encoding="utf-8"))}
    for r in df:
        if int(r["id"]) in new:
            r["parsed_value"] = f"{new[int(r['id'])]:.6g}"
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(df[0]))
        w.writeheader()
        w.writerows(df)


if __name__ == "__main__":
    main()
