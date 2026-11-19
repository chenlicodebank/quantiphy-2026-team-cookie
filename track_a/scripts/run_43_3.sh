#!/bin/bash
# Series 43 round 3 (2026-10-26, session 0c8cbddf, login A): harness v3 (v2 + lesson 15 on re-ask conventions)
# verifies the 7 open proposals (results/s43_rsi/ids_round3.csv). Round number 3 for every row keeps the history
# uniform: the D3 rows' first investigation is in round1 (harness v2), round2 is empty for them.
cd "$(dirname "$0")/.." || exit 1
exec python3 scripts/s43_rsi.py run --round 3 --harness v3 --ids-file results/s43_rsi/ids_round3.csv \
  --out results/s43_rsi --account a --guard results/s43_rsi/guard_a.json --max-sessions 7 --timeout 45
