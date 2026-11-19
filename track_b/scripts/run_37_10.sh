#!/bin/bash
# 37_10 (2026-10-24 ~10:20 UTC, session 05e6b3c8): catch-up r2 for the S3 / D3 questions left with one answered run when
# the forward and reverse r2 processes hit their spend caps (S3 17, D3 56 at 10:14 UTC; their failed r2 records are set
# aside first so the r2 slot is free). The guard floor drops to $5 (in-flight sessions are killed at once, so $5 covers
# the spend between the read and the stop). Same configuration and tiers as 37_6.
#   bash scripts/run_37_10.sh          # on the box
set -euo pipefail
cd "$(dirname "$0")/.."
PY="$HOME/qp_dsh_venv/bin/python"
tmux kill-session -t qp_37_guard 2>/dev/null || true
tmux new-session -d -s qp_37_guard "FLOOR=5 bash scripts/run_37_guard.sh > results/run37_guard.log 2>&1"
for f in results/s37_test_repeats/q/*/r2.json; do
  "$PY" - "$f" <<'PY'
import json, os, sys
f = sys.argv[1]
r = json.load(open(f))
if not (r.get("final") or {}).get("answers"):
    os.rename(f, f.replace("/r2.json", f"/failed_r2_{int(os.path.getmtime(f))}.json"))
PY
done
for G in S3 D3; do
  read -r IDS VIDEOS < <("$PY" - "$G" <<'PY'
import glob, json, sys
g = sys.argv[1]
rows = json.load(open("data/test/test_dataset_current_20261021.json"))
ans = {}
for p in glob.glob("results/s37_test_repeats/q/*/r*.json"):
    r = json.load(open(p))
    if (r.get("final") or {}).get("answers"):
        ans.setdefault(int(p.split("/")[-2].split("__")[-1]), set()).add(int(p.split("/")[-1][1:-5]))
left = [(r["video_id"], r["row_idx"] + 1) for r in rows if r["inference_type"][0] + r["video_type"][1] == g
        and len(ans.get(r["row_idx"] + 1, set())) <= 1]
print(",".join(str(i) for _, i in left), ",".join(sorted({v for v, _ in left})))
PY
)
  echo "$G catch-up: $(echo "$IDS" | tr ',' '\n' | grep -c .) questions"
  [ -n "$IDS" ] || continue
  tmux new-session -d -s "qp_37_10_$G" "TIERS=deepinfra/fp8/flex,deepinfra/fp8,deepinfra/fp8/priority QP_RETRY_429=1 GROUP=$G SAM3_URL=http://127.0.0.1:$([ "$G" = D3 ] && echo 8791 || echo 8790) IDS=$IDS VIDEOS=$VIDEOS WORKERS=8 QW=4 CAP=$([ "$G" = D3 ] && echo 3.5 || echo 1.2) bash scripts/run_37_1.sh --workdir /tmp/qp_blind/s37_test_repeats_${G}cu > results/run37_10_$G.log 2>&1"
done
tmux ls | grep qp_37
