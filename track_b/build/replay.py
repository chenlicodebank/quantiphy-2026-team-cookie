"""Rebuild our Track B uploads from the per-question DeepSeek run records and check their sha256.

    python build/replay.py          # from the package root; about 2 minutes

Steps (each is one of our build scripts, unmodified, in scripts/):
  1. records.tar.xz is unpacked to results/ (every run of every question, compacted; and the scene records).
  2. #221 (the entry): s37_final_b.py takes each question's median over its runs (plus the physical-scale rule),
     then s33_final_b.py's lab factors, once with the lateral lab model and once with the constant one;
     s37_mix.py takes D3 from the constant build and S2 / D2 / S3 from the lateral build.
  3. #222 (the alternative): B9lat = the same s37_final_b.py build on the runs that had finished on 2026-10-24
     (results/b9_runs.csv lists them; they are hard-linked into results/b9_runs/); build_s40_stack.py then takes
     S2 / D2 / D3 from #221 and S3 from B9lat, and applies the validation catalog snap and the paper's prop table
     (results/fulltest_s43_k3/spec.json).
  4. Each rebuilt file's sha256 is compared with the uploaded file's (SUBMISSION.json).
"""
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
PY = sys.executable
RUNS = "results/s37_test_repeats,results/s37_physcheck"
B9RUNS = "results/b9_runs/s37_test_repeats,results/b9_runs/s37_physcheck"


def run(*args):
    print("+", " ".join(args), flush=True)
    subprocess.run([PY, *args], cwd=PKG, check=True, stdout=subprocess.DEVNULL)


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


def main():
    if not (PKG / "results/s37_test_repeats/q").is_dir():
        with tarfile.open(PKG / "records.tar.xz") as tf:
            tf.extractall(PKG, filter="data")
    for d in ("results/fulltest_s37_b10lat", "results/fulltest_s37_b10const", "results/fulltest_s37_b10mix",
              "results/fulltest_s37_b9lat", "results/fulltest_s37_b9const", "results/b9_runs"):
        shutil.rmtree(PKG / d, ignore_errors=True)
    for n in ("track_b_s43_k3.csv", "changes.csv", "manifest.json", "snap_rows.csv"):
        (PKG / "results/fulltest_s43_k3" / n).unlink(missing_ok=True)

    run("scripts/s37_final_b.py", "--runs", RUNS, "--physcheck", "results/s37_physcheck", "--base",
        "results/fulltest_s33_l5lat/track_b_s33_l5lat.csv", "--model", "lat", "--s3-tools",
        "--out", "results/fulltest_s37_b10lat")
    run("scripts/s37_final_b.py", "--runs", RUNS, "--physcheck", "results/s37_physcheck", "--base",
        "results/fulltest_s33_l5const/track_b_s33_l5const.csv", "--model", "const", "--s3-tools",
        "--out", "results/fulltest_s37_b10const")
    run("scripts/s37_mix.py", "--lat", "results/fulltest_s37_b10lat", "--const", "results/fulltest_s37_b10const",
        "--const-cats", "D3", "--out", "results/fulltest_s37_b10mix")

    for r in csv.DictReader(open(PKG / "results/b9_runs.csv", newline="")):
        src = PKG / r["folder"] / "q" / r["qdir"] / f"r{r['k']}.json"
        dst = PKG / "results/b9_runs" / Path(r["folder"]).name / "q" / r["qdir"] / f"r{r['k']}.json"
        dst.parent.mkdir(parents=True, exist_ok=True)
        os.link(src, dst)
    run("scripts/s37_final_b.py", "--runs", B9RUNS, "--physcheck", "results/b9_runs/s37_physcheck", "--base",
        "results/fulltest_s33_l5lat/track_b_s33_l5lat.csv", "--model", "lat", "--s3-tools",
        "--out", "results/fulltest_s37_b9lat")
    run("scripts/build_s40_stack.py", "--spec", "results/fulltest_s43_k3/spec.json")
    # B9const: not in either Track B file; our Track A package reads it (with B9lat) as the DeepSeek line it fuses
    run("scripts/s37_final_b.py", "--runs", B9RUNS, "--physcheck", "results/b9_runs/s37_physcheck", "--base",
        "results/fulltest_s33_l5const/track_b_s33_l5const.csv", "--model", "const", "--s3-tools",
        "--out", "results/fulltest_s37_b9const")

    sub = json.loads((PKG / "SUBMISSION.json").read_text())
    inter = sub.pop("intermediates")
    res = {"intermediates (read by our Track A package)": {p: sha(p) == s for p, s in inter.items()}}
    for ev, s in sub.items():
        got = sha(f"{s['build']}/{s['file']}")
        res[ev] = {"file": f"{s['build']}/{s['file']}", "submission_id": s["submission_id"], "sha256": got,
                   "byte_identical": got == s["sha256"]}
    print(json.dumps(res, indent=1))
    ok = all(res.pop("intermediates (read by our Track A package)").values())
    sys.exit(0 if ok and all(x["byte_identical"] for x in res.values()) else 1)


if __name__ == "__main__":
    main()
