#!/usr/bin/env python
"""Shared helpers for the QuantiPhy board-probe programs.

A probe is one deliberate edit to a slice of the standing submission whose only
purpose is the number that comes back. The board returns four independent
scalars per upload (mra_s2 / mra_d2 / mra_s3 / mra_d3), so a batch carries at
most one probe per category and every probe in a batch is read independently.

Metric (official, Equation 2 on the competition site, mirrored by the devkit):

    row score  s_i = |{ theta in C : |pred_i - gt_i| / gt_i < 1 - theta }| / |C|
    C = {0.10, 0.20, ..., 0.90, 0.95}   ->   cutoffs {0.90, 0.80, ..., 0.10, 0.05}

so s_i lands on one of eleven levels 0, 0.1, ..., 1.0, and a category score is
the plain mean of its rows. That makes one row worth 1/N_c of its category
(S2 1/581, S3 1/576, D3 1/972, D2 1/1160) and one level worth a tenth of that.

Decoding a zero probe (slice S set to a value that cannot score):

    delta = m_c(base) - m_c(probe) = (sum of s_i over S) / N_c
    slice mean score under the base = delta * N_c / |S|

delta * N_c * 10 must come out an integer (the number of tenth-of-a-row steps);
the residual from the nearest integer is the decoder's self-test.
"""
import csv
import io
import json
import os
import random
import re

CATS = ["S2", "D2", "S3", "D3"]
THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
# questions that ask for a quantity AT a time (build_tool_first.py's rule)
TIMED = r"\bat\s*(?:t\s*=\s*)?\d|between\s+\d|from\s+\d.*to\s+\d|at time|initial|final|when t"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def row_mra(pred, gt):
    """The official per-row score, for local self-tests against validation."""
    try:
        pred = float(pred)
        gt = float(gt)
    except (TypeError, ValueError):
        return 0.0
    if pred == 0 or gt == 0:
        return 0.0
    rel = abs(abs(pred) - gt) / gt
    return sum(rel < (1 - t) for t in THRESHOLDS) / len(THRESHOLDS)


def gt_window(c, level):
    """GT interval implied by reading `level` on a row predicted at `c`.

    level is a multiple of 0.1. Returns (lo, hi) for the *outermost* cutoff the
    row passed; the row failed the next one in, so the true interval is that
    annulus. A level of 1.0 means the row is inside +/-5%.
    """
    k = int(round(level * 10))
    if k <= 0:
        return None
    gamma = (1 - THRESHOLDS[len(THRESHOLDS) - k])  # k=10 -> 0.05, k=1 -> 0.90
    return (c / (1 + gamma), c / (1 - gamma)) if gamma < 1 else (c / (1 + gamma), None)


QTYPE = [("accel", r"acceler"),
         ("speed", r"speed|velocit"),
         ("dist", r"distance|displac|how far"),
         ("size", r"length|width|height|diameter|radius|size|thick")]


def qtype(question):
    """Coarse quantity class of a question - the axis the map slices along,
    after cell and video_source. Order matters: an acceleration question often
    also says "speed"."""
    for name, rx in QTYPE:
        if re.search(rx, question, re.I):
            return name
    return "other"


# ---------------------------------------------------------------- csv I/O
def read_csv(path):
    raw = open(path, "rb").read()
    term = "\r\n" if b"\r\n" in raw else "\n"
    rows = list(csv.reader(io.StringIO(raw.decode("utf-8"))))
    return rows[0], rows[1:], term


def write_csv(path, header, rows, term):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator=term)
    w.writerow(header)
    w.writerows(rows)
    with open(path, "wb") as f:
        f.write(buf.getvalue().encode("utf-8"))


def col(header, name):
    return header.index(name)


def category(header, row):
    """S/D from inference_type, 2/3 from video_type — the devkit's own rule."""
    return row[col(header, "inference_type")][0] + row[col(header, "video_type")][1]


def cell(header, row):
    return category(header, row) + "/" + row[col(header, "inference_type")]


def category_sizes(header, rows):
    n = dict.fromkeys(CATS, 0)
    for r in rows:
        n[category(header, r)] += 1
    return n


# ---------------------------------------------------------------- selection
def select(header, rows, sel):
    """Indices of the rows a probe spec's `select` block picks out.

    Keys: cell, category, inference_type, video_source (str|list), video_type_prefix,
    question_regex, timed (bool), ids (list, wins outright), exclude_ids,
    limit + seed (stratified-free random sample, seeded so a replay is identical).
    """
    i_src, i_q, i_id = col(header, "video_source"), col(header, "question"), col(header, "id")
    if sel.get("ids"):
        want = {str(x) for x in sel["ids"]}
        return [i for i, r in enumerate(rows) if r[i_id] in want]
    out = []
    for i, r in enumerate(rows):
        if sel.get("category") and category(header, r) != sel["category"]:
            continue
        if sel.get("cell") and cell(header, r) != sel["cell"]:
            continue
        if sel.get("inference_type") and r[col(header, "inference_type")] != sel["inference_type"]:
            continue
        src = sel.get("video_source")
        if src:
            src = [src] if isinstance(src, str) else src
            if r[i_src] not in src:
                continue
        vtp = sel.get("video_type_prefix")
        if vtp and not r[col(header, "video_type")].startswith(vtp):
            continue
        if sel.get("question_regex") and not re.search(sel["question_regex"], r[i_q], re.I):
            continue
        if "timed" in sel and bool(re.search(TIMED, r[i_q], re.I)) != bool(sel["timed"]):
            continue
        if sel.get("qtype") and qtype(r[i_q]) != sel["qtype"]:
            continue
        out.append(i)
    if sel.get("exclude_ids"):
        bad = {str(x) for x in sel["exclude_ids"]}
        out = [i for i in out if rows[i][i_id] not in bad]
    if sel.get("limit") and len(out) > sel["limit"]:
        rnd = random.Random(sel.get("seed", 0))
        out = sorted(rnd.sample(out, sel["limit"]))
    return out


# ---------------------------------------------------------------- ledger
def ledger(path=None):
    path = path or os.path.join(ROOT, "results", "submissions.tsv")
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def standing(path=None, track="B"):
    """The newest winning deployment within a track; harvest defaults to B.

    A probe upload is never the standing, even one that scores above it: its file is
    a deliberately damaged copy, and the next probes would be built on it."""
    if track not in ("A", "B"):
        raise ValueError("Standing requires an explicit A or B track")
    best = [r for r in ledger(path) if r.get("verdict") == "new_best"
            and (r.get("track") or "B") == track
            and not (r.get("filename") or "").startswith("probe_")]
    return best[-1] if best else None


def base_scores(cfg_dir=None):
    """Per-category base scores, full precision where a probe has re-read them.

    Every probe upload leaves three categories bit-identical to the base, so it
    re-reads those three at whatever precision the API stores. probe_run folds
    those observations in here; the ledger's 4-decimal copies are the seed.
    """
    p = os.path.join(cfg_dir or os.path.join(ROOT, "probes"), "base_scores.json")
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    st = standing()
    return {"base_eval": st["eval"],
            "scores": {c: float(st[c]) for c in CATS},
            "precision": {c: "ledger-4dp" for c in CATS}}


def save_base_scores(d, cfg_dir=None):
    p = os.path.join(cfg_dir or os.path.join(ROOT, "probes"), "base_scores.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(d, open(p, "w", encoding="utf-8"), indent=2)


def decode_zero(delta, n_cat, n_slice):
    """Zero probe -> (slice mean score, integer tenth-steps, residual)."""
    steps = delta * n_cat * 10
    k = round(steps)
    return (delta * n_cat / n_slice if n_slice else 0.0), k, abs(steps - k)
