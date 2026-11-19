#!/bin/bash
# Series 43 round 1 (2026-10-26, session 0c8cbddf, login A): RSI harness v1 over the per-question contexts of the
# 118 scored non-lab rows where the gray Track A upload (#223 = C1) and the DeepSeek median differ by > 25 pct
# (no catalog-snap rows, no physical-scale clips). One fresh Opus 5.5 session per question, effort high.
cd "$(dirname "$0")/.." || exit 1
python3 scripts/s43_rsi.py build --ids-file results/s43_rsi/ids_round1.csv --out results/s43_rsi
exec python3 scripts/s43_rsi.py run --round 1 --harness v1 --ids-file results/s43_rsi/ids_round1.csv \
  --out results/s43_rsi --account a --guard results/s43_rsi/guard_a.json --max-sessions 8 --timeout 50
