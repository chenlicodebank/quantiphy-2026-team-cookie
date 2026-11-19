#!/bin/bash
# 37_13 (2026-10-24 ~15:25 UTC, session 05e6b3c8): a reverse-order r2 process for the D2 simulation questions (461 of 758
# still without r2 at 15:19 UTC, ~110 an hour from the 37_11 pipeline alone), as 37_9 did for D3 / S3: the questions
# without an r2 record in reverse video order, own workspace root; the later record stays where both meet.
#   bash scripts/run_37_13.sh          # on the box
set -euo pipefail
cd "$(dirname "$0")/.."
PY="$HOME/qp_dsh_venv/bin/python"
read -r IDS VIDEOS < <("$PY" - <<'PY'
import glob, json
rows = json.load(open("data/test/test_dataset_current_20261021.json"))
have = {int(p.split("/")[-2].split("__")[-1]) for p in glob.glob("results/s37_test_repeats/q/*/r2.json")}
left = [(r["video_id"], r["row_idx"] + 1) for r in rows if r["inference_type"][0] == "D" and r["video_type"][1] == "2"
        and r["video_source"] == "simulation" and r["row_idx"] + 1 not in have]
print(",".join(str(i) for _, i in left), ",".join(sorted({v for v, _ in left}, reverse=True)))
PY
)
echo "D2 simulation reverse r2: $(echo "$IDS" | tr ',' '\n' | grep -c .) questions"
tmux new-session -d -s qp_37_13_D2rev "TIERS=deepinfra/fp8/flex,deepinfra/fp8,deepinfra/fp8/priority QP_RETRY_429=1 GROUP=D2 SAM3_URL=http://127.0.0.1:8790 IDS=$IDS VIDEOS=$VIDEOS WORKERS=12 QW=4 CAP=9 bash scripts/run_37_1.sh --workdir /tmp/qp_blind/s37_test_repeats_D2rev > results/run37_13_D2rev.log 2>&1"
tmux ls | grep qp_37
