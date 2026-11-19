"""35_4 prep (2026-10-23): the job lists for the Track B median-of-three test pass (method_queue 59).

Every test question already has one DeepSeek-1017 + SAM 3 answer (results/s29_pass_sam3/q/<video>__<id>/r1.json, the
29_5 / 29_9 / 29_10 passes behind the declared B7 file). A repeat must be the same configuration as the question's r1,
so this splits the ids by the one prompt flag the r1 sessions differ in (the 29_6 method card, read from each r1's
recorded system prompt; every r1 had the SAM 3 tools and none the physical-internet line) and orders them by the
validation gate's gain per dollar (35_1: S2 +.039 at ~$0.03 a question for two runs, D3 +.031 at ~$0.07, S3 +.011 at
~$0.08, D2 +.004 at ~$0.03). Writes <out>/ids_<card|nocard>_<cat>.txt and videos_<...>.txt (comma-separated) and a cost table.

    python scripts/s35_repeat_ids.py [--src results/s29_pass_sam3 --out results/s35_test_repeats]
"""
import argparse
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ORDER = ("S2", "D3", "S3", "D2")
CARD = "Method card (rules that hold"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", default="results/s29_pass_sam3")
    ap.add_argument("--out", default="results/s35_test_repeats")
    ap.add_argument("--test", default="data/test/test_dataset_current_20261021.json")
    a = ap.parse_args()
    src, out = ROOT / a.src, ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    test = pd.DataFrame(json.loads((ROOT / a.test).read_text()))
    test["id"] = test.row_idx + 1
    cat = dict(zip(test.id, test.inference_type.str[0] + test.video_type.str[1]))
    rows = []
    for f in sorted(src.glob("q/*/r1.json")):
        vid, i = f.parent.name.rsplit("__", 1)
        t = f.read_text()
        rec = json.loads(t)
        rows.append(dict(id=int(i), video=vid, cat=cat[int(i)], card=CARD in t, cost=rec.get("cost_usd") or 0.0))
    d = pd.DataFrame(rows)
    for (card, c), g in d.groupby(["card", "cat"]):
        name = f"ids_{'card' if card else 'nocard'}_{c}.txt"
        (out / name).write_text(",".join(str(i) for i in sorted(g.id)) + "\n")
        (out / name.replace("ids_", "videos_")).write_text(",".join(sorted(g.video.unique())) + "\n")
    tab = (d.groupby(["cat", "card"]).agg(questions=("id", "size"), videos=("video", "nunique"), r1_usd=("cost", "sum"))
             .assign(two_more_runs_usd=lambda x: (2 * x.r1_usd).round(2)).reset_index())
    tab["order"] = tab.cat.map({c: k for k, c in enumerate(ORDER)})
    tab = tab.sort_values(["order", "card"]).drop(columns="order")
    tab.to_csv(out / "cost_table.csv", index=False)
    print(tab.to_string(index=False))
    print(f"total: {len(d)} questions, two more runs ~${2 * d.cost.sum():.2f} at the r1 bill")


if __name__ == "__main__":
    main()
