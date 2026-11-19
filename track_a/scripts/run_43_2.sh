#!/bin/bash
# Series 43 round 2 (2026-10-26, session 0c8cbddf, login A): harness v2 (provenance of the submitted answer in
# every context, verification of round-1 proposals, open points of low-confidence keeps, lessons v2 from round 1).
# First the 28 round-2 rows (14 proposals to verify, 14 low-confidence keeps), then the 23 D3 rows round 1 never
# reached, as their first round under v2. Physical-scale / Series 30 S2-adjudication clips stay out
# (results/s43_rsi/excluded_physscale.json).
cd "$(dirname "$0")/.." || exit 1
python3 scripts/s43_rsi.py run --round 2 --harness v2 --ids-file results/s43_rsi/ids_round2.csv \
  --out results/s43_rsi --account a --guard results/s43_rsi/guard_a.json --max-sessions 8 --timeout 45
exec python3 scripts/s43_rsi.py run --round 1 --harness v2 --ids-file results/s43_rsi/ids_round1_v2_d3.csv \
  --out results/s43_rsi --account a --guard results/s43_rsi/guard_a.json --max-sessions 8 --timeout 45
