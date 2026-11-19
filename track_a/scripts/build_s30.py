"""Series 30 builds (2026-10-22, session 625fd803): the Track A entry E2 with the per-question adjudicated answers of
one or more `s30_dossier.py adjudicate` runs on top, one category per run, so a board read splits exactly by category.

Each replaced row takes its own adjudicator session's answer (that session held only that question and its dossier);
lab rows keep the entry's class transforms (the adjudicator answers the raw quantity: lab motion x1.215 in S3 / x1.19 in
D3 and the S3 lab size x1.03 are re-applied, the prop table is re-applied by the caller if needed). Rows whose answer
moves by less than --min-move stay at the entry value, so the read counts real changes only. Every row is filled.

    python scripts/build_s30.py --run results/s30_adj_s3 --out results/fulltest_s30_a1 --name track_a_s30_a1.csv
"""
import argparse
import csv
import hashlib
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import s30_dossier as D  # noqa: E402

ROOT = D.ROOT


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default=str(D.BASE.relative_to(ROOT)))
    ap.add_argument("--run", action="append", default=[], help="an adjudication out dir (repeatable; none = a copy)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--min-move", type=float, default=0.02, help="relative change below which the entry value stays")
    ap.add_argument("--exclude", default="", help="comma ids kept at the entry value (human-check fixes)")
    ap.add_argument("--support-veto", type=float, default=0.0,
                    help="a change larger than this relative step is kept only when another answer in the question's "
                         "dossier (not the entry's own) lies within --support-tol of the new value (0 = off)")
    ap.add_argument("--support-tol", type=float, default=0.15)
    ap.add_argument("--dossier", default="results/s30_dossier")
    ap.add_argument("--codex-veto", type=float, default=0.0,
                    help="a change larger than this relative step is kept only when the question's independent Codex "
                         "answer is nearer to the new value than to the entry's (0 = off)")
    a = ap.parse_args()
    led = D.ledger()
    excl = {int(x) for x in a.exclude.split(",") if x}
    with open(ROOT / a.base, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys())
    byid = {int(r["id"]): r for r in rows}
    changes, latest, vetoed = [], {}, []
    codex = {}  # independent Codex answers of the same questions (30_4 / 30_8), for the --codex-veto rule
    for qd in (ROOT / "results/s30_codex_test/q").glob("*__*") if (ROOT / "results/s30_codex_test/q").exists() else []:
        qid = int(qd.name.rsplit("__", 1)[1])
        if (qd / "answers.json").exists():
            codex[qid] = D.fnum(json.loads((qd / "answers.json").read_text()).get(str(qid)))
    for run in a.run:  # a later --run overrides an earlier one on the same question (a re-adjudication)
        for qd in sorted((ROOT / run / "q").glob("*__*")):
            qid = int(qd.name.rsplit("__", 1)[1])
            if qid not in excl and (qd / "answers.json").exists():
                latest[qid] = (run, D.fnum(json.loads((qd / "answers.json").read_text()).get(str(qid))))
    for qid, (run, new) in sorted(latest.items()):
        old = D.fnum(byid[qid]["parsed_value"])
        if not new or not old:
            continue
        lr = led.get(qid, {})
        cat, src, kind = lr.get("category", ""), lr.get("source", ""), lr.get("kind", "")
        if src == "lab":
            # The entry's lab class transforms (motion x1.215 / x1.19 by quantity, sizes x1.03 in S3, the prop
            # table) depend on the quantity named in the question, which the ledger's `kind` (SS / SD / DS / DD)
            # does not carry: refuse rather than guess until a lab run needs it.
            sys.exit(f"q{qid} is a lab row: build_s30.py does not re-apply the lab transforms yet")
        factor = 1.0
        val = round(new * factor, 6)
        if abs(math.log(val / old)) < math.log(1 + a.min_move):
            continue
        cx = codex.get(qid)
        if a.codex_veto and cx and abs(math.log(val / old)) > math.log(1 + a.codex_veto) and \
                abs(math.log(cx / val)) >= abs(math.log(cx / old)):
            vetoed.append({"id": qid, "before": old, "after": val, "codex": cx})
            continue
        if a.support_veto and abs(math.log(val / old)) > math.log(1 + a.support_veto):
            # a big change needs an independent voice: some earlier answer in the question's own dossier, other than
            # the one the entry carries, within --support-tol of the new value (used where no Codex answer exists)
            cj = ROOT / a.dossier / "q" / f"{byid[qid]['video_id'].strip()}__{qid}" / "candidates.json"
            others = [c["answer"] for c in json.loads(cj.read_text())["candidates"]] if cj.exists() else []
            others = [x for x in others if x and abs(math.log(x / old)) > math.log(1.01)]
            if not any(abs(math.log(x / val)) <= math.log(1 + a.support_tol) for x in others):
                vetoed.append({"id": qid, "before": old, "after": val, "codex": ""})
                continue
        changes.append({"id": qid, "cat": cat, "source": src, "kind": kind, "before": old, "after": val,
                        "raw": new, "factor": factor, "run": run, "codex": cx or ""})
        byid[qid]["parsed_value"] = repr(val)
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    with open(out / a.name, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    with open(out / "changes.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(changes[0]) if changes else ["id"])
        w.writeheader()
        w.writerows(changes)
    by = {}
    for c in changes:
        by[c["cat"]] = by.get(c["cat"], 0) + 1
    with open(out / "vetoed.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "before", "after", "codex"])
        w.writeheader()
        w.writerows(vetoed)
    man = {"base": a.base, "codex_veto": a.codex_veto, "support_veto": a.support_veto, "support_tol": a.support_tol,
           "vetoed": len(vetoed), "base_sha256": hashlib.sha256((ROOT / a.base).read_bytes()).hexdigest(), "runs": a.run,
           "min_move": a.min_move, "exclude": sorted(excl), "changed": len(changes), "by_cat": by,
           "sha256": hashlib.sha256((out / a.name).read_bytes()).hexdigest()}
    (out / "manifest.json").write_text(json.dumps(man, indent=1) + "\n")
    assert len(rows) == 3289 and all(D.fnum(r["parsed_value"]) for r in rows), "every row must be filled and positive"
    print(json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
