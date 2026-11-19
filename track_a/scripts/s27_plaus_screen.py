"""27_4 (2026-10-21, session 6e6e97e4): a world-knowledge plausibility screen of the standing answers, to choose rows
for a --real-scale re-ask (26_59's prompt). The 26_59 re-asks (rows picked by trace signals) read D3 +.022 on 70 rows:
a session that keeps a stated scale under which a standard object is implausible is usually wrong. This screen looks for
more such rows with a cheap text-only judge instead of trace signals.

Each judge request holds up to --batch questions from DIFFERENT videos (never two questions of one video), and each line
carries only that question's own text, prior and depth_info and our own answer to it; the judge is told to judge every
line alone. The screen only SELECTS rows; any new answer comes from a fresh per-question session. Output:
results/s27_plaus/verdicts.jsonl (one line per row: typical range in the question's unit, verdict, reason).

    python scripts/s27_plaus_screen.py --base results/fulltest_s26_clean_fixes/track_a_s26_clean_fixes.csv \\
        --out results/s27_plaus --model claude-sonnet-5-5 --account b
"""
import argparse
import json
import os
import random
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
ACCOUNTS = {"a": str(Path.home() / ".claude-a"), "b": str(Path.home() / ".claude-b")}
CLAUDE = os.environ.get("CLAUDE_BIN", "claude")

PROMPT = """You are checking answers to a physics-measurement benchmark for gross errors, using world knowledge only.
Each line below is ONE independent question about a different short video (Blender renders at real-world scale unless
the reference fact itself is unrealistic, lab recordings of everyday objects, or internet footage). Judge every line
ALONE: lines come from unrelated videos, so never compare or combine them.

For each line you get: the question (with its unit), the reference fact given with the question (the prior; an exact
fact about that video), and the answer our system gave. Decide whether the answer is physically plausible for the
named object or motion, in the question's unit:
- "implausible" only when the answer is far outside what the named thing can be under the prior (an adult person
  3.5 m tall, a car 9 m long or 1 m wide, a walking person at 4 m/s, a tennis ball 15 cm wide, a door 6 m high), or the
  answer contradicts the prior itself (a size far from a size the prior states for the same object).
- "plausible" when it is within a generous typical range, and "unknown" when the thing has no typical size or speed
  (rocks, buildings, distances between arbitrary objects, toys, abstract shapes, planets' models, priors that are
  clearly unrealistic like a 30 cm ice cube or a 0.05 m/s toy car - then the scene is scaled and anything goes).
Accelerations of walking characters, timed kinematics, and lab bounce / path / displacement questions are "unknown".

Do not use any tool. Reply directly with ONLY a JSON array, one object per line, in input order:
[{"id": <id>, "lo": <typical low in the question's unit or null>, "hi": <typical high or null>,
  "verdict": "plausible" | "implausible" | "unknown", "reason": "<= 15 words"}]

Lines:
"""


def judge(batch, a, k):
    lines = "\n".join(json.dumps({"id": int(r.id), "question": r.question.strip(), "prior": str(r.prior).strip(),
                                  "answer": float(r.parsed_value)}, ensure_ascii=False) for r in batch.itertuples())
    env = os.environ.copy()
    for key in list(env):
        if key.startswith(("CLAUDE_CODE_", "CLAUDECODE", "ANTHROPIC_")):
            env.pop(key)
    env["CLAUDE_CONFIG_DIR"] = ACCOUNTS[a.account]
    cmd = [CLAUDE, "-p", "--output-format", "json", "--no-session-persistence", "--model", a.model,
           "--max-turns", "3", "--permission-mode", "dontAsk", "--allowedTools", "",
           "--disallowedTools", "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,Task,Agent,TodoWrite,ToolSearch"]
    for attempt in range(3):
        p = subprocess.run(cmd, input=PROMPT + lines, capture_output=True, text=True, env=env, cwd="/tmp",
                           timeout=600)
        try:
            res = json.loads(p.stdout)
            txt = res.get("result", "")
            arr = json.loads(re.search(r"\[.*\]", txt, re.S).group(0))
            return arr, res.get("total_cost_usd", 0.0)
        except Exception as exc:  # retry a malformed reply
            print(f"batch {k} attempt {attempt + 1} failed: {exc}; stderr {p.stderr[:200]}", flush=True)
            time.sleep(5)
    return [], 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="claude-sonnet-5-5")
    ap.add_argument("--account", required=True, choices=sorted(ACCOUNTS))
    ap.add_argument("--batch", type=int, default=40)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0, help="first N batches only (smoke)")
    a = ap.parse_args()
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    t = pd.DataFrame(json.load(open(ROOT / "data/test/test_dataset_current_20261021.json")))
    t["id"] = t.row_idx + 1
    led = pd.read_csv(ROOT / "results/s26_scene_full/ledger.csv")[["id"]]
    base = pd.read_csv(ROOT / a.base)[["id", "parsed_value"]]
    t = t[t.id.isin(led.id)].merge(base, on="id")
    done = set()
    vf = out / "verdicts.jsonl"
    if vf.exists():
        done = {json.loads(l)["id"] for l in vf.read_text().splitlines() if l.strip()}
    t = t[~t.id.isin(done)]
    # batches with distinct videos: round-robin over videos in a seeded random order
    rng = random.Random(0)
    groups = {v: list(g.index) for v, g in t.groupby("video_id")}
    vids = list(groups)
    rng.shuffle(vids)
    batches, cur, used = [], [], set()
    while any(groups.values()):
        for v in vids:
            if groups[v] and v not in used:
                cur.append(groups[v].pop(0))
                used.add(v)
                if len(cur) == a.batch:
                    batches.append(cur)
                    cur, used = [], set()
        if cur and not any(groups[v] and v not in used for v in vids):
            batches.append(cur)
            cur, used = [], set()
    if cur:
        batches.append(cur)
    for b in batches:
        assert t.loc[b, "video_id"].is_unique
    if a.limit:
        batches = batches[:a.limit]
    print(f"{len(t)} rows in {len(batches)} batches", flush=True)
    cost = [0.0]

    def run(k):
        arr, c = judge(t.loc[batches[k]], a, k)
        cost[0] += c or 0.0
        with open(vf, "a") as f:
            for x in arr:
                f.write(json.dumps(x) + "\n")
        print(f"batch {k}: {len(arr)} verdicts, ${c:.3f}", flush=True)

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        list(ex.map(run, range(len(batches))))
    print(f"done, ${cost[0]:.2f}", flush=True)


if __name__ == "__main__":
    main()
