#!/bin/bash
# 37_5 (2026-10-24 ~00:20 UTC, session 05e6b3c8, GH200 lambda2): the relaunch of 37_2 (four group pipelines), 37_3 and
# 37_4 after two failure modes at the price tiers. (1) ~360 concurrent sessions without priority: 429s past the retry
# schedule. (2) at ~110 sessions, flex / standard fail inside 200 streams (an SSE error event, no usage), which DSH ends
# as "Provider returned error" after three quick re-sends (37_4 stopped at fail-fast). dsh_measurement.forward now waits
# both out (QP_RETRY_429, ~15 min jittered) and lets one request use the priority tier after QP_PRIORITY_AFTER=3 failed
# attempts. Order: stop every Series 37 session, set unanswered records aside (s37_requeue_failed.py), clear the
# read-only workspaces, start again (finished r<k>.json are kept and skipped).
#   bash scripts/run_37_5.sh          # on the box
set -euo pipefail
cd "$(dirname "$0")/.."
for s in qp_37_2_S2 qp_37_2_S2S3 qp_37_2_S3 qp_37_2_D3 qp_37_2_D2 qp_37_3 qp_37_4; do tmux kill-session -t "$s" 2>/dev/null || true; done
sleep 5
if ps -eo args | grep -E "[d]sh_scene.py|[s]37_scale_check.py|[s]37_calib_agent.py" | grep -q s37; then
  echo "a Series 37 process is still running"; exit 1
fi
"$HOME/qp_dsh_venv/bin/python" scripts/s37_requeue_failed.py results/s37_test_repeats results/s37_physcheck results/s37_calib
for d in /tmp/qp_blind/s37_*; do [ -e "$d" ] && chmod -R u+w "$d" && rm -rf "$d"; done
E="QP_PRIORITY_AFTER=3"
tmux new-session -d -s qp_37_2_S2 "$E WORKERS=6 QW=3 GROUP=S2 SAM3_URL=http://127.0.0.1:8790 CAP_R2=10 CAP_R3=5 CAP_R45=5 bash scripts/run_37_2.sh > results/run37_5_S2.log 2>&1"
tmux new-session -d -s qp_37_2_S3 "$E WORKERS=6 QW=3 GROUP=S3 SAM3_URL=http://127.0.0.1:8790 CAP_R2=13 CAP_R3=7 CAP_R45=6 bash scripts/run_37_2.sh > results/run37_5_S3.log 2>&1"
tmux new-session -d -s qp_37_2_D3 "$E WORKERS=8 QW=4 GROUP=D3 SAM3_URL=http://127.0.0.1:8791 CAP_R2=24 CAP_R3=12 CAP_R45=8 bash scripts/run_37_2.sh > results/run37_5_D3.log 2>&1"
tmux new-session -d -s qp_37_2_D2 "$E WORKERS=8 QW=3 GROUP=D2 SAM3_URL=http://127.0.0.1:8791 CAP_R2=12 CAP_R3=6 CAP_R45=5 bash scripts/run_37_2.sh > results/run37_5_D2.log 2>&1"
tmux new-session -d -s qp_37_3 "$E WORKERS=4 QW=3 SAM3_URL=http://127.0.0.1:8790 CAP=8 bash scripts/run_37_3b.sh > results/run37_5_phys.log 2>&1"
tmux new-session -d -s qp_37_4 "$E WORKERS=3 QW=3 SAM3_URL=http://127.0.0.1:8791 CAP=3 bash scripts/run_37_4b.sh > results/run37_5_calib.log 2>&1"
tmux ls | grep qp_37
