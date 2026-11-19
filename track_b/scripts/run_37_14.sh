#!/bin/bash
# 37_14 (2026-10-24 ~20:20 UTC, session 05e6b3c8, GH200 lambda2; user: "wrap up when we got all remaining results"): the
# sweep driver. Round = wait until no Series 37 run session is left (qp_37_* other than the guard and this driver), then
# run_37_12.sh on every group; stop when a round schedules nothing or after 4 rounds. Writes
# results/s37_test_repeats/SWEEP_DONE when it ends.
#   tmux new-session -d -s qp_37_14_driver "bash scripts/run_37_14.sh > results/run37_14.log 2>&1"
set -uo pipefail
cd "$(dirname "$0")/.."
for round in 1 2 3 4; do
  while tmux ls -F '#S' 2>/dev/null | grep '^qp_37_' | grep -vqE '^qp_37_(guard|14_driver)$'; do sleep 60; done
  echo "$(date -u +%FT%TZ) round $round"
  out=$(bash scripts/run_37_12.sh 2>&1); echo "$out"
  if ! echo "$out" | grep -qE 'r[2-4]\.\.r[0-9]: [0-9]+ questions'; then
    echo "$(date -u +%FT%TZ) nothing left to schedule" | tee results/s37_test_repeats/SWEEP_DONE; exit 0
  fi
  sleep 30
done
while tmux ls -F '#S' 2>/dev/null | grep '^qp_37_' | grep -vqE '^qp_37_(guard|14_driver)$'; do sleep 60; done
echo "$(date -u +%FT%TZ) stopped after 4 rounds" | tee results/s37_test_repeats/SWEEP_DONE
