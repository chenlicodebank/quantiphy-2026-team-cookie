"""Series 27 (2026-10-21, session 6e6e97e4): overlay new per-question answers on a standing file, with the per-question
transforms #199 applies to raw session answers (scripts/run_26_57.sh):

- lab motion rows (build_s26_labcal.MOTION on a lab S3 / D3 / D2 row): x1.215 (S3), x1.19 (D3), x1.19 (D2);
- lab size rows (labcal SIZE, not MOTION, not NOT_SIZE, lab S3 / D3): x1.03 (S3), x1.0 (D3);
- rows on the physical-scale internet clips (build_s26_physb_a ANCHORS / WEAK) are refused: their k needs the clip's
  anchor rule, so they keep the base value (reported).

Each new answer is the CURRENT answer of its own question folder (<run>/q/<video>__<id>/answers.json, the folder that
held only that question); a later --runs entry wins over an earlier one for the same id. Every other row is the base
byte for byte. Never overwrites an existing build directory.

    python scripts/build_s27_entry.py --base results/fulltest_s26_clean_fixes/track_a_s26_clean_fixes.csv \\
        --runs results/s27_valfam --out results/fulltest_s27_valfam --name track_a_s27_valfam.csv
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

from build_s26_labcal import MOTION, NOT_SIZE, SIZE
from build_s26_physb_a import ANCHORS, WEAK

ROOT = Path(__file__).resolve().parents[1]
FACTOR_MOTION = {"S3": 1.215, "D3": 1.19, "D2": 1.19}
FACTOR_SIZE = {"S3": 1.03, "D3": 1.0}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def answers(run, only=None):
    out = {}
    for f in sorted((ROOT / run / "q").glob("*/answers.json")):
        vid, ids = f.parent.name.split("__", 1)
        for k, v in json.loads(f.read_text()).items():
            qid = int(k)
            if only is not None and qid not in only:
                continue
            v = float(v)
            if np.isfinite(v) and v > 0:
                out[qid] = (v, vid, str(f.parent.relative_to(ROOT)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True)
    ap.add_argument("--runs", required=True, help="comma list of run dirs, later wins")
    ap.add_argument("--ids-file", help="CSV with an id column: only these ids take a new answer")
    ap.add_argument("--cats", default="S2,D2,S3,D3", help="categories that take changes; the others stay the base")
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--fixes", help="CSV id,value,kind,source: final values applied after the runs (a session's own "
                    "alternative reading under a convention the board confirmed); no transform is applied to them")
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    dest = ROOT / a.out
    if dest.exists():
        raise SystemExit("Use a new build directory; never overwrite an evaluated artifact")
    base = pd.read_csv(ROOT / a.base, dtype={"parsed_value": float})
    cur = pd.DataFrame(json.load(open(ROOT / "data/test/test_dataset_current_20261021.json")))
    cur["id"] = cur.row_idx + 1
    cur = cur.set_index("id").loc[base.id]
    cat = dict(zip(base.id, (cur.inference_type.str[0] + cur.video_type.str[1]).values))
    src = dict(zip(base.id, cur.video_source.values))
    vid_of = dict(zip(base.id, cur.video_id.values))
    q_of = dict(zip(base.id, cur.question.values))
    only = set(pd.read_csv(ROOT / a.ids_file).id.astype(int)) if a.ids_file else None
    cats = set(a.cats.split(","))
    new = {}
    for run in a.runs.split(","):
        new.update(answers(run.strip(), only))
    physb = set(ANCHORS) | set(WEAK)
    out = base.copy()
    pos = {int(i): k for k, i in enumerate(base.id)}
    rows, refused = [], []
    for qid, (v, vid, folder) in sorted(new.items()):
        if qid not in pos:
            refused.append((qid, "not in base"))
            continue
        c = cat[qid]
        if c not in cats:
            refused.append((qid, f"category {c} held"))
            continue
        if vid_of[qid] != vid:
            refused.append((qid, f"folder video {vid} != {vid_of[qid]}"))
            continue
        if vid in physb:
            refused.append((qid, "physical-scale clip"))
            continue
        q = q_of[qid]
        f, how = 1.0, "raw"
        if src[qid] == "lab" and c in FACTOR_MOTION and MOTION.search(q):
            f, how = FACTOR_MOTION[c], "lab motion"
        elif (src[qid] == "lab" and c in FACTOR_SIZE and SIZE.search(q) and not MOTION.search(q)
              and not NOT_SIZE.search(q)):
            f, how = FACTOR_SIZE[c], "lab size"
        before = float(out.parsed_value.iloc[pos[qid]])
        after = v * f
        out.iloc[pos[qid], out.columns.get_loc("parsed_value")] = after
        rows.append(dict(id=qid, video=vid, cat=c, raw=v, factor=f, transform=how, before=before, after=after,
                         ratio=after / before if before > 0 else np.nan, folder=folder))
    if a.fixes:
        for fx in pd.read_csv(ROOT / a.fixes).itertuples():
            qid = int(fx.id)
            before = float(out.parsed_value.iloc[pos[qid]])
            out.iloc[pos[qid], out.columns.get_loc("parsed_value")] = float(fx.value)
            rows.append(dict(id=qid, video=vid_of[qid], cat=cat[qid], raw=float(fx.value), factor=1.0,
                             transform=f"fix:{fx.kind}", before=before, after=float(fx.value),
                             ratio=float(fx.value) / before, folder=str(fx.source)))
    assert np.isfinite(out.parsed_value).all() and (out.parsed_value > 0).all()
    dest.mkdir(parents=True)
    out.to_csv(dest / a.name, index=False)
    ch = pd.DataFrame(rows)
    ch.to_csv(dest / "changes.csv", index=False)
    moved = ch[(ch.ratio - 1).abs() > 1e-9] if len(ch) else ch
    man = {"run": a.out, "base": a.base, "base_sha256": sha(ROOT / a.base), "runs": a.runs, "ids_file": a.ids_file,
           "cats": a.cats, "note": a.note, "taken": len(ch), "moved": len(moved),
           "moved_by_cat": moved.groupby("cat").size().to_dict() if len(moved) else {},
           "refused": refused, "sha256": sha(dest / a.name)}
    (dest / "manifest.json").write_text(json.dumps(man, indent=1) + "\n")
    print(json.dumps({k: man[k] for k in ("taken", "moved", "moved_by_cat")}), "refused", len(refused))


if __name__ == "__main__":
    main()
