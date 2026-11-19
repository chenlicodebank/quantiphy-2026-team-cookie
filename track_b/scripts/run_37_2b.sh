#!/bin/bash
# 37_2b (2026-10-24 ~01:40 UTC, session 05e6b3c8): run_37_2.sh calling run_37_1.sh (tiers flex -> standard -> priority
# with OpenRouter's own fallback) instead of run_37_1b.sh. 37_5's hybrid (priority excluded, failures waited out,
# priority after 3 failed attempts) still sent 44 pct of calls to priority and ran ~3.5 sessions a minute (median request
# 41 s, 57 pct of requests retried); OpenRouter's fallback answered every session of 37_1's first half hour.
# Original header:
# 37_2 (2026-10-24, Track B, session 05e6b3c8, GH200 lambda2): the adaptive repeat pipeline of one category group in
# results/s37_test_repeats, all in r1's configuration (run_37_1b.sh: flex / standard tiers, priority excluded, 429s
# waited out). Stage r2 (skipped with WAIT_SESSION=<tmux session of a running r2>, which is waited for instead), then
# r3 for the group's questions whose r1 and r2 differ by more than .05 in |ln|, then r4 + r5 where the three runs spread
# more than .3 in ln(max / min) (s37_next_ids.py; policy fixed before any test read, simulated on validation .797 at
# 2.6 runs a question against .775 for one run and .791 for three). The build takes the median of every run.
#   tmux new-session -d -s qp_37_2_S2 "GROUP=S2 SAM3_URL=http://127.0.0.1:8790 WAIT_SESSION=qp_37_1_S2 CAP_R3=5 CAP_R45=5 bash scripts/run_37_2.sh > results/run37_2_S2.log 2>&1"
#   tmux new-session -d -s qp_37_2_S3 "GROUP=S3 SAM3_URL=http://127.0.0.1:8790 AFTER_SESSION=qp_37_1_S2 CAP_R2=15 CAP_R3=7 CAP_R45=6 bash scripts/run_37_2.sh > results/run37_2_S3.log 2>&1"
set -euo pipefail
cd "$(dirname "$0")/.."
OUT=results/s37_test_repeats
PY="$HOME/qp_dsh_venv/bin/python"
GROUP="${GROUP:?set GROUP}"
: "${SAM3_URL:?set SAM3_URL}"
case "$GROUP" in S2|D2) FLAG=card ;; *) FLAG=nocard ;; esac
if [ -n "${AFTER_SESSION:-}" ]; then  # start this group's r2 only once that tmux session (another group's r2) has ended
  while tmux has-session -t "$AFTER_SESSION" 2>/dev/null; do sleep 60; done
  echo "$(date -u +%FT%TZ) $AFTER_SESSION ended, starting $GROUP"
fi
if [ -n "${WAIT_SESSION:-}" ]; then
  while tmux has-session -t "$WAIT_SESSION" 2>/dev/null; do sleep 60; done
  echo "$(date -u +%FT%TZ) $WAIT_SESSION ended"
else
  GROUP="$GROUP" SAM3_URL="$SAM3_URL" CAP="${CAP_R2:?set CAP_R2}" bash scripts/run_37_1.sh
fi
"$PY" scripts/s37_next_ids.py "$OUT" --k 3 --a "${A:-0.05}"
L="$OUT/ids_${FLAG}_${GROUP}_r3.txt"
if [ -s "$L" ]; then
  echo "$(date -u +%FT%TZ) r3: $(tr ',' '\n' < "$L" | grep -c .) questions"
  GROUP="$GROUP" SAM3_URL="$SAM3_URL" IDS="$(cat "$L")" REPEATS=3 FROM=3 CAP="${CAP_R3:?set CAP_R3}" bash scripts/run_37_1.sh
fi
"$PY" scripts/s37_next_ids.py "$OUT" --k 4 --b "${B:-0.3}"
L="$OUT/ids_${FLAG}_${GROUP}_r4.txt"
if [ -s "$L" ]; then
  echo "$(date -u +%FT%TZ) r4-r5: $(tr ',' '\n' < "$L" | grep -c .) questions"
  GROUP="$GROUP" SAM3_URL="$SAM3_URL" IDS="$(cat "$L")" REPEATS=5 FROM=4 CAP="${CAP_R45:?set CAP_R45}" bash scripts/run_37_1.sh
fi
echo "$(date -u +%FT%TZ) $GROUP pipeline done"
