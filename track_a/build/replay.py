"""Rebuild our Track A uploads from the answer lines and check their sha256.

    python build/replay.py          # from the package root; a few seconds

Inputs are the answer lines in results/ (their sha256 in LINES.json): E2 (the per-question Opus answers with the
Series 27 re-asks), U1 (E2 with the lab direction factor and the S2 adjudication), the 39_4 re-answers, the #200 line,
the RSI answers, and the per-question DeepSeek medians B9lat / B9const. build/check_leaves.py traces every Track A
line's values to their per-question records; our Track B package rebuilds B9lat and B9const from the DeepSeek run
records. Steps (our build scripts, unmodified, in scripts/):
  1. F1 = build_s39_fuse.py: per question, the weighted geometric mean of the Opus answer and the DeepSeek median.
  2. F2, F3 = build_s39_stack.py with their specs: the same fusion per population, the lab rows under matched factor
     conventions, and the 39_4 re-answers on the 2D simulation motion rows.
  3. #224 (the entry) = s43_strict_a.py: each category from its F file, the prop-table rows back to their pre-table
     answers fused like every other lab size row, the human-check rows back to the #200 line, then 14 RSI answers.
  4. C1 = build_s40_stack.py with its spec: the same splice plus the validation catalog snap.
  5. #225 (the alternative) = C1 with 29 RSI answers (build/overlay_rsi.py, the --build half of s43_rsi.py apply).
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
PY = sys.executable


def run(*args):
    print("+", " ".join(args), flush=True)
    subprocess.run([PY, *args], cwd=PKG, check=True, stdout=subprocess.DEVNULL)


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


def main():
    lines = json.loads((PKG / "LINES.json").read_text())
    bad = {p: s for p, s in lines["inputs"].items() if sha(p) != s}
    if bad:
        sys.exit(f"answer lines differ from LINES.json: {sorted(bad)}")
    for p in lines["built"]:
        (PKG / p).unlink(missing_ok=True)

    run("scripts/build_s39_fuse.py", "--out", "results/fulltest_s39_f1", "--name", "track_a_s39_f1.csv",
        "--w", "S3=0.5,D3=0.7,D2=0.7", "--max-ratio", "0.4")
    run("scripts/build_s39_stack.py", "--spec", "results/fulltest_s39_f2/spec.json", "--out", "results/fulltest_s39_f2",
        "--name", "track_a_s39_f2.csv")
    run("scripts/build_s39_stack.py", "--spec", "results/fulltest_s39_f3/spec.json", "--out", "results/fulltest_s39_f3",
        "--name", "track_a_s39_f3.csv")
    run("scripts/s43_strict_a.py", "--out", "results/fulltest_s43_strict_rsi", "--name", "track_a_s43_strict_rsi.csv",
        "--rsi", "results/fulltest_s43_strict_rsi/apply_r123.csv")
    run("scripts/build_s40_stack.py", "--spec", "results/fulltest_s40_c1/spec.json")
    run("build/overlay_rsi.py", "results/fulltest_s40_c1/track_a_s40_c1.csv",
        "results/fulltest_s43_gray_rsi/apply_final.csv", "results/fulltest_s43_gray_rsi/track_a_s43_gray_rsi.csv")

    res = {"intermediate": {p: sha(p) == s for p, s in lines["built"].items()}}
    sub = json.loads((PKG / "SUBMISSION.json").read_text())
    for ev, s in sub.items():
        got = sha(f"{s['build']}/{s['file']}")
        res[ev] = {"file": f"{s['build']}/{s['file']}", "submission_id": s["submission_id"], "sha256": got,
                   "byte_identical": got == s["sha256"]}
    print(json.dumps(res, indent=1))
    ok = all(res["intermediate"].values()) and all(v["byte_identical"] for k, v in res.items() if k != "intermediate")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
