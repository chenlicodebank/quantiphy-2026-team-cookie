"""Series 30 (2026-10-22, session 625fd803): the two Track A reads authorised by the user for the UTC 10-23 reset (run
channel #129 / #131 / #132), each one population per category against E2, each prediction written before its read.

U1 = E2 + the Series 31 lab file (session 2ac1aba4, frozen, sha256 cf43b72d... after #133; S3 lab + D3 lab rows) + Series 30's S2
     adjudication in the S2 seat + the 6 D2 lab rows of #140 (session 315f5fc7) in the D2 seat.
U2 = U1's winning categories + Series 30's S3 3D adjudication and D3 3D adjudication (+ the 30_5 re-asks); a U1
     category wins when its read beats E2's predicted value by two rounding units (+.0002).

    python scripts/s30_reset_plan.py u1                     # build results/fulltest_s30_u1/ + prediction.json
    python scripts/s30_reset_plan.py u2 --u1-read '{"S2": .8561, "D2": .8921, "S3": .8301, "D3": .8512}'
"""
import argparse
import csv
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable
E2_FILE = "results/fulltest_s27_e2/track_a_s27_e2.csv"
LAB_FILE = "results/fulltest_s31_lablat/track_a_s31_lablat.csv"
LAB_SHA = "cf43b72d3bfb914ecd9c627092d4d09d2d6aeabb351b24635f9ffcc6dcd45d5b"  # 2a9d29a1c (#133: q2861 track fix)
# E2's prediction (results/s27_fixes/e2_prediction.json): every E2 step read exactly on disjoint rows in #206-#209.
E2_PRED = {"S2": (0.8556, 0.8558), "D2": (0.8920, 0.8922), "S3": (0.8060, 0.8060), "D3": (0.8445, 0.8447)}
E2_MID = {c: round(sum(v) / 2, 4) for c, v in E2_PRED.items()}
WIN = 0.0002
# U1's D2 seat (run channel #140, session 315f5fc7): E2 + 6 D2 lab velocity rows (captured_0015 family) at x1.5 of the raw
# answer instead of x1.19 - a second test of the direction model on clean in-plane motion; prediction written first.
D2LAB_FILE = "results/fulltest_s32_d2lab/track_a_s32_d2lab.csv"
D2LAB_SHA = "febd409091a294cffdb54abc749886e1b8c4655c2f6c826cd132e505a4683c40"


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


# The compliance audit's OUT rows (run channel #152, results/fulltest_s34_legit_a/changes.csv): human-check corrections and
# rows chosen through other questions' answers. Series 30 never overlays them (q3051, a human-check row, had been flagged
# against its human-edited E2 value), so the reads stay clean and the legit entry keeps the audit's values.
LEGIT_FILE = "results/fulltest_s34_legit_a/track_a_s34_legit.csv"
# #188 (user, compliance judgments aligned): the degenerate-prior re-asks are allowed again; human-check corrections, the
# length-horizontal rows and the weak-clip physical scale stay out.
OUT_ROWS = sorted({r["id"] for r in csv.DictReader(open(ROOT / "results/fulltest_s34_legit_a/changes.csv"))
                   if r["group"] in ("human", "lenh", "weak")} | {"1668"}, key=int)


def tainted():
    """Series 30 rows whose dossier held a 27_6 re-ask. Excluded under #163 / #165; allowed again by #188 item 5 (each
    plausibility judge line held one question alone), so nothing is excluded now - kept for the record."""
    return set()
    out = set()
    for f in (ROOT / "results/s30_dossier/q").glob("*__*/candidates.json"):
        d = json.loads(f.read_text())
        if any("s27_plaus_reask" in c.get("source", "") for c in d["candidates"]):
            out.add(str(d["id"]))
    return out


def build(base, runs, out, name, extra=()):
    excl = sorted(set(OUT_ROWS) | tainted(), key=int)
    cmd = [PY, "scripts/build_s30.py", "--base", base, "--out", out, "--name", name, "--exclude", ",".join(excl),
           *extra]
    for r in runs:
        cmd += ["--run", r]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"build failed: {' '.join(cmd)}\n{r.stderr[-2000:]}")
    return json.loads((ROOT / out / "manifest.json").read_text())


def mra_pred(out, base_scores):
    subprocess.run([PY, "scripts/s30_predict.py", "--build", out, "--base",
                    ",".join(f"{k}={v}" for k, v in base_scores.items())], cwd=ROOT, check=True, capture_output=True)
    return json.loads((ROOT / out / "prediction.json").read_text())


def cmd_u1(a):
    assert sha(LAB_FILE) == LAB_SHA, "the Series 31 lab file changed since it was frozen (#131)"
    runs = [r for r in ["results/s30_adj_s2"] if (ROOT / r / "q").exists()]
    out = "results/fulltest_s30_u1"
    man = build(LAB_FILE, runs, out, "track_a_s30_u1.csv", ["--support-veto", "0.2"])
    assert set(man["by_cat"]) <= {"S2"}, f"U1 may change only S2 on top of the lab file: {man['by_cat']}"
    assert sha(D2LAB_FILE) == D2LAB_SHA, "the s32 D2 lab file changed since #140"
    d2ids = {r["id"] for r in csv.DictReader(open(ROOT / "results/fulltest_s32_d2lab/changes.csv"))}
    d2rows = {r["id"]: r for r in csv.DictReader(open(ROOT / D2LAB_FILE, newline="", encoding="utf-8"))}
    with open(ROOT / out / "track_a_s30_u1.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys())
    for r in rows:
        if r["id"] in d2ids:
            assert r["video_type"][1] == "2" and r["inference_type"][0] == "D", r["id"]
            r["parsed_value"] = d2rows[r["id"]]["parsed_value"]
    with open(ROOT / out / "track_a_s30_u1.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    man["sha256"] = sha(f"{out}/track_a_s30_u1.csv")
    man["d2_overlay"] = {"file": D2LAB_FILE, "sha256": D2LAB_SHA, "ids": sorted(d2ids)}
    (ROOT / out / "manifest.json").write_text(json.dumps(man, indent=1) + "\n")
    s2 = mra_pred(out, E2_MID)["categories"]["S2"]
    lab = json.loads((ROOT / "results/fulltest_s31_lablat/prediction.json").read_text())
    pred = {"written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "file": f"{out}/track_a_s30_u1.csv",
            "sha256": man["sha256"], "vs": "E2 (results/fulltest_s27_e2; prediction .8495-.8497, its steps read exactly)",
            "S2": {"population": "Series 30 S2 adjudication", "changed": s2["changed"], "delta": s2["delta"],
                   "score": s2["score"]},
            "D2": {"population": "6 D2 lab velocity rows x1.5 (session 315f5fc7, #140)",
                   "prediction_file": "results/fulltest_s32_d2lab/prediction.json",
                   "detail": json.loads((ROOT / "results/fulltest_s32_d2lab/prediction.json").read_text()),
                   "reading": "portal scorer (#144): D2 near 0..+.0005 over E2 favours s = 1.5, <= -.0006 favours ~1.2; "
                              "six rows cannot settle s alone"},
            "S3_D3": {"population": "Series 31 lab directional factor (session 2ac1aba4)",
                      "prediction_file": "results/fulltest_s31_lablat/prediction.json",
                      "model_holds": "S3 +.019..+.041, D3 +.003..+.010", "null": "S3 -.008..-.025, D3 -.007..-.014",
                      "portal_scorer": "rescored by session 20cfd3a2 before the read (run channel #144, "
                                       "results/s33_lablat_open/rescored_lab_predictions.json): model S3 +.013..+.025 / "
                                       "D3 +.001..+.005, null S3 -.008..-.015 / D3 -.005..-.008",
                      "detail": lab},
            "win_rule": "a category wins when its read beats E2's predicted midpoint by +.0002"}
    (ROOT / out / "prediction_u1.json").write_text(json.dumps(pred, indent=1) + "\n")
    print(json.dumps({k: v for k, v in pred.items() if k != "S3_D3"}, indent=1))


def cmd_u2(a):
    read = json.loads(a.u1_read)
    win = {c: read[c] - E2_MID[c] >= WIN for c in ("S2", "D2", "S3", "D3")}
    # The lab half's own reading rule (session 2ac1aba4, run channel #135, written before the read): S3 mixes the 12
    # 0034b prior-scale rows (positive under either model) with 143 direction rows; below +.005 the direction rows are
    # read as losing, so only the prior-scale rows stay. D3 (direction rows only) keeps at the usual +.0002.
    lab = list(csv.DictReader(open(ROOT / "results/fulltest_s31_lablat/changes.csv")))
    keep_s3_only = None
    if read["S3"] - E2_MID["S3"] < 0.005:
        win["S3"] = False
        keep_s3_only = {r["id"] for r in lab if r["cat"] == "S3" and r["how"] == "prior-scale"}
    # base for U2: E2 with U1's winning categories copied in
    with open(ROOT / E2_FILE, newline="", encoding="utf-8") as f:
        e2 = list(csv.DictReader(f))
        fields = list(e2[0].keys())
    with open(ROOT / "results/fulltest_s30_u1/track_a_s30_u1.csv", newline="", encoding="utf-8") as f:
        u1 = {r["id"]: r for r in csv.DictReader(f)}
    cat = {}
    for r in e2:
        cat[r["id"]] = ("S" if r["inference_type"][0] == "S" else "D") + r["video_type"][1]
    # In the partial case the 0034b rows are NOT put into U2, so U2's S3 reads the S3 adjudication alone against E2; the
    # 0034b rows still enter U4 by #135 / #188 (their own share is predicted positive under either model).
    base_rows = [u1[r["id"]] if win.get(cat[r["id"]]) else r for r in e2]
    out = ROOT / "results/fulltest_s30_u2"
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "u2_base.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(base_rows)
    # three chained builds, each with the rule its population was given before any read:
    # S3 3D adjudication with the Codex veto (prediction committed 11:56 UTC); the 30_5 real-scale re-asks as they are
    # (the board's record for that prompt: #200, 27_6); the D3 3D adjudication with the support veto (no Codex this week)
    man_s3 = build("results/fulltest_s30_u2/u2_base.csv", ["results/s30_adj_s3", "results/s30_adj_s3_seg"],
                   "results/fulltest_s30_u2/s3part", "s3.csv", ["--codex-veto", "0.2"])
    man_rs = build("results/fulltest_s30_u2/s3part/s3.csv", ["results/s30_realscale"],
                   "results/fulltest_s30_u2/rspart", "rs.csv")
    d3runs = [r for r in ["results/s30_adj_d3"] if (ROOT / r / "q").exists()]
    man_d3 = build("results/fulltest_s30_u2/rspart/rs.csv", d3runs, "results/fulltest_s30_u2/d3part", "d3.csv",
                   ["--support-veto", "0.2"])
    d2runs = [r for r in ["results/s30_adj_d2"] if (ROOT / r / "q").exists()]
    man = build("results/fulltest_s30_u2/d3part/d3.csv", d2runs, "results/fulltest_s30_u2", "track_a_s30_u2.csv",
                ["--support-veto", "0.2"])
    assert set(man_s3["by_cat"]) <= {"S3"} and set(man_rs["by_cat"]) <= {"D3", "S3"} and set(man_d3["by_cat"]) <= {"D3"}
    assert set(man["by_cat"]) <= {"D2"}
    base_scores = {c: (read[c] if win.get(c) else E2_MID[c]) for c in ("S2", "D2", "S3", "D3")}
    p3 = mra_pred("results/fulltest_s30_u2/s3part", base_scores)["categories"]["S3"]
    prs = mra_pred("results/fulltest_s30_u2/rspart", base_scores)["categories"]["D3"]
    pd = mra_pred("results/fulltest_s30_u2/d3part", base_scores)["categories"]["D3"]
    p2 = mra_pred("results/fulltest_s30_u2", base_scores)["categories"]["D2"]
    pd = {"changed": prs["changed"] + pd["changed"],
          "delta": [round(x + y, 4) for x, y in zip(prs["delta"], pd["delta"])]}
    pd["score"] = [round(base_scores["D3"] + d, 4) for d in pd["delta"]]
    pred = {"written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "file": "results/fulltest_s30_u2/track_a_s30_u2.csv", "sha256": man["sha256"], "u1_read": read,
            "u1_winners": win, "s3_lab_rows_kept_if_partial": sorted(keep_s3_only or []), "base_scores": base_scores,
            "S3": {"population": "Series 30 S3 3D adjudication (Codex veto)", "changed": p3["changed"],
                   "delta": p3["delta"], "score": p3["score"]},
            "D3": {"population": "Series 30 D3 3D adjudication (support veto) + 30_5 re-asks", "changed": pd["changed"],
                   "delta": pd["delta"], "score": pd["score"]},
            "D2": {"population": "Series 30 D2 adjudication (support veto)", "changed": p2["changed"],
                   "delta": p2["delta"], "score": p2["score"]},
            "S2": "control (equal to U1's winner or E2)"}
    (out / "prediction_u2.json").write_text(json.dumps(pred, indent=1) + "\n")
    print(json.dumps(pred, indent=1))


# #147 (315f5fc7): the direction model throughout (velocities x1.5, distances x F) when U1's D3 keeps the lab rows
LAB0018 = {True: ("results/fulltest_s32_lab0018_f15d", "3f15e645fe6ed4bd26f102d375e845a66fc0f075753878ae39748f6f8ea5c389"),
           False: ("results/fulltest_s32_lab0018", "8ee387053165a2f9042a04a98e8766f40cd1d181f487ed66a2c3068ffb87bf57")}


# #150 (315f5fc7): 27 lab "distance between A and B" rows x F (S3 8, D3 19), frozen; used only when U1's D3 keeps the
# lab rows (the direction model), sharing U3's D3 seat with 32_2c and filling U3's otherwise idle S3 seat
LABDIST = ("results/fulltest_s32_labdist_f", "1957704583748c5fff9a2935fb8dc5ffd91ae96528b1add661c81c26ae9777ed")


def cmd_u3(a):
    """U3 = U2 with each Series 30 population that lost in U2's read reverted to U2's base, plus the 30 captured_0018-family
    D3 rows of session 315f5fc7 (run channel #140 / #143) in the D3 seat - the x1.5 variant if U1's D3 read kept the lab
    direction rows, else the x1.19 one. Every other category equals U2's winners."""
    u2p = json.loads((ROOT / "results/fulltest_s30_u2/prediction_u2.json").read_text())
    read2 = json.loads(a.u2_read)
    base2 = u2p["base_scores"]
    keep = {"S3": read2["S3"] - base2["S3"] >= WIN, "D3": read2["D3"] - base2["D3"] >= WIN}
    d3_direction = bool(u2p["u1_winners"].get("D3"))
    with open(ROOT / "results/fulltest_s30_u2/u2_base.csv", newline="", encoding="utf-8") as f:
        base = {r["id"]: r for r in csv.DictReader(f)}
    with open(ROOT / "results/fulltest_s30_u2/track_a_s30_u2.csv", newline="", encoding="utf-8") as f:
        u2 = list(csv.DictReader(f))
        fields = list(u2[0].keys())
    folder, want = LAB0018[d3_direction]
    assert sha(f"{folder}/changes.csv") == want, f"{folder} changed since #143"
    lab18 = {r["id"]: r["after"] for r in csv.DictReader(open(ROOT / folder / "changes.csv"))}
    dist = {}
    if d3_direction:
        assert sha(f"{LABDIST[0]}/changes.csv") == LABDIST[1], "the lab distance file changed since #150"
        dist = {r["id"]: r["after"] for r in csv.DictReader(open(ROOT / LABDIST[0] / "changes.csv"))}
        assert not set(dist) & set(lab18)
    out = ROOT / "results/fulltest_s30_u3"
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for r in u2:
        c = ("S" if r["inference_type"][0] == "S" else "D") + r["video_type"][1]
        r = dict(base[r["id"]]) if c in keep and not keep[c] else r
        if r["id"] in lab18:
            assert c == "D3" and r["video_id"].startswith("captured_0018"), r["id"]
            r = dict(r, parsed_value=lab18[r["id"]])
        if r["id"] in dist:
            assert c in ("S3", "D3") and r["video_id"].startswith("captured_"), r["id"]
            r = dict(r, parsed_value=dist[r["id"]])
        rows.append(r)
    with open(out / "track_a_s30_u3.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    lab_pred = json.loads((ROOT / folder / "prediction.json").read_text())
    pred = {"written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "file": "results/fulltest_s30_u3/track_a_s30_u3.csv", "sha256": sha("results/fulltest_s30_u3/track_a_s30_u3.csv"),
            "u2_read": read2, "u2_base_scores": base2, "series30_kept": keep, "lab0018_variant": folder,
            "D3": {"population": "captured_0018 family, [2.0, 4.04] s capture window (session 315f5fc7)",
                   "base": read2["D3"] if keep["D3"] else base2["D3"], "prediction": lab_pred},
            "lab_distances": ({"file": LABDIST[0], "prediction": json.loads((ROOT / LABDIST[0] / "prediction.json").read_text())}
                              if dist else "not used (U1's D3 did not keep the lab rows)"),
            "S2_D2": "controls at U2's winners", "S3": "lab distance rows (8) if used, else a control"}
    (out / "prediction_u3.json").write_text(json.dumps(pred, indent=1) + "\n")
    print(json.dumps({k: v for k, v in pred.items() if k != "D3"}, indent=1))


# #188: the declared entry's base is 34_5 (34_3 + the degenerate-prior and plausibility re-asks restored)
NOGRAY_FILE = "results/fulltest_s34_aligned_a/track_a_s34_aligned.csv"
NOGRAY_SHA = "65c3a0592b1ff9b839a11a167bcbc720f989a0ef28d31f811e99a11724ffa413"


def cmd_u4(a):
    """U4 = the declared Track A entry under the user's rulings #163 / #188: session 14bbb4e6's aligned
    base 34_5 (= 34_3 + the degenerate-prior and plausibility re-asks; formerly 34_3 (39 OUT rows at legit values; no prop table, no plausibility-screen re-asks; lab motion x1.25 and lab sizes
    x1.0, both fitted on validation labels only) plus what the E2 reads U1 / U2 kept:
    - the Series 31 lab direction rows (s = 1.5, validation-supported), without the 12 captured_0034b prior-scale rows:
      S3 ones if U1's S3 gained >= +.005 (the #135 rule), D3 ones if U1's D3 gained >= +.0002;
    - the 6 captured_0015 D2 rows at x1.5 only together with U1's D3 lab rows (#152 / #154);
    - the S2 adjudication if U1's S2 gained; the S3 / D3 3D adjudications (+ the 30_5 re-asks) if U2's S3 / D3 gained;
    - the per-question DeepSeek refill of the 247 unscored validation-family rows.
    No captured_0018 window rows and no lab distance rows (#163). U3 is not uploaded."""
    assert sha(NOGRAY_FILE) == NOGRAY_SHA, "the no-GRAY base changed since #163"
    u2p = json.loads((ROOT / "results/fulltest_s30_u2/prediction_u2.json").read_text())
    read1, read2, base2 = u2p["u1_read"], json.loads(a.u2_read), u2p["base_scores"]
    s3_dir = read1["S3"] - E2_MID["S3"] >= 0.005
    d3_dir = read1["D3"] - E2_MID["D3"] >= WIN
    s2_win = bool(u2p["u1_winners"].get("S2"))
    keep2 = {c: read2[c] - base2[c] >= WIN for c in ("S3", "D3", "D2")}

    def changed(path):
        p = ROOT / path
        return {r["id"]: (r["after"], r.get("run", path)) for r in csv.DictReader(open(p))} if p.exists() else {}

    lab = list(csv.DictReader(open(ROOT / "results/fulltest_s31_lablat/changes.csv")))
    with open(ROOT / LAB_FILE, newline="", encoding="utf-8") as f:
        labv = {r["id"]: r["parsed_value"] for r in csv.DictReader(f)}
    take = {}
    for r in lab:
        # #135 with #188 item 1: S3 lab rows all kept on a +.005 gain, else only the 12 captured_0034b prior-scale rows
        if r["cat"] == "S3" and (s3_dir or r["how"] == "prior-scale"):
            take[r["id"]] = ("lab direction" if r["how"] != "prior-scale" else "0034b prior scale", labv[r["id"]],
                             LAB_FILE, "31_1 (prior-scale rows: re-asked from the row's own prior, trigger disclosed)")
            continue
        if r["how"] == "prior-scale":
            continue
        if r["cat"] == "D3" and d3_dir:
            take[r["id"]] = ("lab direction", labv[r["id"]], LAB_FILE,
                             "31_1: row's raw answer x |(1.5dX, 1.5dY, dZ)|/|V| from its own scene track + depth_info; "
                             "s = 1.5 fitted on validation labels (34_2)")
    if d3_dir:
        with open(ROOT / D2LAB_FILE, newline="", encoding="utf-8") as f:
            d2v = {r["id"]: r["parsed_value"] for r in csv.DictReader(f)}
        for i in {r["id"] for r in csv.DictReader(open(ROOT / "results/fulltest_s32_d2lab/changes.csv"))}:
            take[i] = ("D2 lab x1.5", d2v[i], D2LAB_FILE, "in-plane lab motion at the direction model's s = 1.5")
    if s2_win:
        for i, (v, run) in changed("results/fulltest_s30_u1/changes.csv").items():
            take[i] = ("S2 adjudication", v, run, "DeepSeek-1017 (29_5) differs >25 pct; Opus adjudication over the "
                       "per-question dossier; a change >20 pct needs another dossier answer within 15 pct")
    if keep2["S3"]:
        for i, (v, run) in changed("results/fulltest_s30_u2/s3part/changes.csv").items():
            take[i] = ("S3 adjudication", v, run, "DeepSeek-1017 (28_3) differs >25 pct; Opus adjudication over the "
                       "per-question dossier; a change >20 pct kept only if the question's Codex answer is nearer to it")
    if keep2["D3"]:
        for path, rule in (("results/fulltest_s30_u2/rspart/changes.csv",
                            "--real-scale re-ask, selected because the row's own notes call its size not at real scale"),
                           ("results/fulltest_s30_u2/d3part/changes.csv",
                            "DeepSeek-1017 (29_5) differs >25 pct; Opus adjudication over the per-question dossier; a "
                            "change >20 pct needs another dossier answer within 15 pct")):
            for i, (v, run) in changed(path).items():
                take[i] = ("D3 adjudication / 30_5", v, run, rule)
    if keep2["D2"]:
        for i, (v, run) in changed("results/fulltest_s30_u2/changes.csv").items():
            take[i] = ("D2 adjudication", v, run, "DeepSeek-1017 with SAM 3 (29_5 configuration) differs >25 pct; Opus "
                       "adjudication over the per-question dossier; a change >20 pct needs another dossier answer within 15 pct")
    refill_ids = {r["id"] for r in csv.DictReader(open(ROOT / "results/s30_refill/ids.csv"))}  # incl. the 87 #182 names
    # the Track B session answered the refill ids inside its main pass (sessions.jsonl refreshed 21:30 UTC, #198), not in
    # a separate folder; a dedicated results/s29_pass_refill/ wins if it ever appears
    rdir = ROOT / ("results/s29_pass_refill" if (ROOT / "results/s29_pass_refill/sessions.jsonl").exists()
                   else "results/s29_pass_sam3")
    if (rdir / "sessions.jsonl").exists():
        for line in (rdir / "sessions.jsonl").read_text(encoding="utf-8").splitlines():
            e = json.loads(line)
            i = str(e.get("id"))
            if e.get("kind") == "question" and i in refill_ids and float(e.get("answer") or 0) > 0:
                take.setdefault(i, ("unscored refill", repr(float(e["answer"])), str(rdir.relative_to(ROOT)),
                                    "DeepSeek-1017 per question on an unscored validation-family row"))
    else:
        for rf in sorted(rdir.glob("q/*__*/r*.json")):
            for x in (json.loads(rf.read_text()).get("final") or {}).get("answers") or []:
                i = str(x.get("id"))
                if i in refill_ids and float(x.get("value") or 0) > 0:
                    take.setdefault(i, ("unscored refill", repr(float(x["value"])), str(rdir.relative_to(ROOT)),
                                        "DeepSeek-1017 per question on an unscored validation-family row"))
    # refill ids without a refill answer (it may miss the reset): a clean placeholder from the row's own inputs (#178) -
    # its per-question Opus answer of the 26_30 validation runs (keyed by test id) where one exists, else the number in
    # its own prior, else 1.0. These rows are unscored; only the declared file's provenance changes.
    have = {i for i, t in take.items() if t[0] == "unscored refill"}
    missing = sorted(refill_ids - have, key=int)
    placeholder = []
    if missing:
        import re
        cur = json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text())
        val_ans = {}  # filled only where the validation run's question inputs equal the test row's
        for d in ("s26_scene_val", "s26_reask_1020_val", "s26_scene_val_lean"):
            for qd in sorted((ROOT / "results" / d / "q").glob("*__*")):
                i = qd.name.rsplit("__", 1)[1]
                if not (qd / "answers.json").exists() or not (qd / "inputs.json").exists() or int(i) > len(cur):
                    continue
                q = json.loads((qd / "inputs.json").read_text()).get("question") or {}
                row = cur[int(i) - 1]
                same = (q.get("question", "").strip() == row["question"].strip()
                        and (q.get("prior") or "").strip() == (row["prior"] or "").strip()
                        and (q.get("depth_info") or "").strip() == (row.get("depth_info") or "").strip()
                        and qd.name.rsplit("__", 1)[0] == row["video_id"].strip())
                v = json.loads((qd / "answers.json").read_text()).get(i)
                if same and v and float(v) > 0:
                    val_ans[i] = (float(v), f"results/{d}")
        for i in missing:
            if i in val_ans:
                v, src, rule = val_ans[i][0], val_ans[i][1], "per-question Opus answer (26_30 validation run)"
            else:
                m = re.search(r"(\d+(?:\.\d+)?)", cur[int(i) - 1]["prior"] or "")
                v = float(m.group(1)) if m and float(m.group(1)) > 0 else 1.0
                src, rule = "own prior", "placeholder: the number in the row's own prior (unscored row)"
            take[i] = ("unscored placeholder", repr(v), src, rule)
            placeholder.append({"id": i, "after": repr(v)})
    out_rows = set(OUT_ROWS) | tainted()
    clash = [i for i, t in take.items() if i in out_rows and t[0] not in ("unscored refill", "unscored placeholder")]
    assert not clash, f"an OUT or tainted row would be overlaid: {clash[:5]}"
    with open(ROOT / NOGRAY_FILE, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys())
    log = []
    for r in rows:
        if r["id"] in take:
            what, v, src, rule = take[r["id"]]
            log.append({"id": r["id"], "what": what, "before": r["parsed_value"], "after": v, "source": src, "rule": rule})
            r["parsed_value"] = v
    out = ROOT / "results/fulltest_s30_u4"
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "track_a_s30_u4.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    with open(out / "placeholder.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "after"])
        w.writeheader()
        w.writerows(placeholder)
    with open(out / "overlay.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "what", "before", "after", "source", "rule"])
        w.writeheader()
        w.writerows(log)
    assert len(rows) == 3289 and all(float(r["parsed_value"]) > 0 for r in rows)
    counts = {}
    for x in log:
        counts[x["what"]] = counts.get(x["what"], 0) + 1
    pred = {"written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "file": "results/fulltest_s30_u4/track_a_s30_u4.csv", "sha256": sha("results/fulltest_s30_u4/track_a_s30_u4.csv"),
            "base": f"{NOGRAY_FILE} (sha256 {NOGRAY_SHA[:12]}..., session 14bbb4e6, #163)", "u1_read": read1,
            "u2_read": read2, "kept": {"S3 lab direction": s3_dir, "D3 lab direction + D2 lab x1.5": d3_dir,
                                       "S2 adjudication": s2_win, **{f"{c} adjudication": v for c, v in keep2.items()}},
            "overlay_rows": counts,
            "expected": "no-GRAY base (about -.004 under the legit base 34_1, itself about -.003..-.004 under E2) plus the "
                        "kept populations' read gains; the lab direction rows replace the base's x1.25, not E2's x1.215 / "
                        "x1.19, so their gain against this base differs slightly from U1's read"}
    # the compliance audit's independent check (run channel #171, scripts/s34_check_entry.py): every row equals the
    # no-GRAY base or an allowed source's value, OUT ids denied; U4 is not uploaded without PASS
    allow = ["results/fulltest_s31_lablat/changes.csv", "results/fulltest_s32_d2lab/changes.csv",
             "results/fulltest_s30_u1/changes.csv", "results/fulltest_s30_u2/s3part/changes.csv",
             "results/fulltest_s30_u2/rspart/changes.csv", "results/fulltest_s30_u2/d3part/changes.csv",
             "results/fulltest_s30_u2/changes.csv"]
    over = []
    if any(t[0] == "unscored refill" for t in take.values()):
        over.append(str((rdir / "sessions.jsonl").relative_to(ROOT)))
    if placeholder:
        over.append("results/fulltest_s30_u4/placeholder.csv")
    cmd = [PY, "scripts/s34_check_entry.py", "--entry", "results/fulltest_s30_u4/track_a_s30_u4.csv", "--deny-default"]
    for x in allow:
        cmd += ["--allow", x]
    for x in over:
        cmd += ["--allow-over-deny", x]
    chk = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    (out / "check_entry.txt").write_text(chk.stdout + chk.stderr)
    pred["entry_check"] = "PASS" if chk.returncode == 0 and "PASS" in chk.stdout else "FAIL"
    (out / "prediction_u4.json").write_text(json.dumps(pred, indent=1) + "\n")
    print(json.dumps(pred, indent=1))
    if pred["entry_check"] != "PASS":
        sys.exit("U4 failed the entry check - not for upload; see results/fulltest_s30_u4/check_entry.txt")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("u1")
    u2 = sub.add_parser("u2")
    u2.add_argument("--u1-read", required=True, help='JSON of U1\'s category scores, e.g. {"S2": .8561, ...}')
    u3 = sub.add_parser("u3")
    u3.add_argument("--u2-read", required=True, help="JSON of U2's category scores")
    u4 = sub.add_parser("u4")
    u4.add_argument("--u2-read", required=True, help="JSON of U2's category scores (U3 is not uploaded, #163)")
    a = ap.parse_args()
    {"u1": cmd_u1, "u2": cmd_u2, "u3": cmd_u3, "u4": cmd_u4}[a.cmd](a)


if __name__ == "__main__":
    main()
