"""Series 39: collect a re-answer run's per-question answers next to the row's current Track A value (session 28b2ba80).

For every answered id of the run: old = the 26_30 first answer (results/s26_scene_full/q/<video>__<id>/answers.json),
cur = the base file's value (E2 line), new = the run's answer, and new_t = new x cur / old, so a per-question transform
that E2 applies on top of the raw answer (lab factor, physical scale, time base) carries over to the new answer.

    python scripts/s39_collect.py --run results/s39_2dmotion --base results/fulltest_s27_e2/track_a_s27_e2.csv
"""
import argparse
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--base", default="results/fulltest_s27_e2/track_a_s27_e2.csv")
    ap.add_argument("--first", default="results/s26_scene_full")
    a = ap.parse_args()
    run = ROOT / a.run
    base = pd.read_csv(ROOT / a.base).set_index("id").parsed_value
    rows = []
    for f in sorted((run / "q").glob("*__*/answers.json")):
        vid, q = f.parent.name.rsplit("__", 1)
        try:
            new = float(json.loads(f.read_text())[q])
        except (KeyError, ValueError, TypeError):
            continue
        of = ROOT / a.first / "q" / f"{vid}__{q}" / "answers.json"
        old = float(json.loads(of.read_text())[q]) if of.exists() else float("nan")
        cur = float(base[int(q)])
        ratio = cur / old if old and old == old and old > 0 else 1.0
        rows.append({"id": int(q), "video": vid, "old": old, "cur": cur, "new": new, "ratio_cur_old": round(ratio, 6),
                     "new_t": float(f"{new * ratio:.6g}")})
    df = pd.DataFrame(rows).sort_values("id")
    df.to_csv(run / "collected.csv", index=False)
    same = (abs(df.ratio_cur_old - 1) < 1e-6).mean() if len(df) else 0
    print(f"{len(df)} answers; cur == old on {same:.0%}; written {run / 'collected.csv'}")


if __name__ == "__main__":
    main()
