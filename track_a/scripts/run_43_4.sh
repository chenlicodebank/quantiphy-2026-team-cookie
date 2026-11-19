#!/bin/bash
# Series 43 round 4 (2026-10-26, session 0c8cbddf, login A): the RSI loop extended to the categories where
# rounds 1-3 read positive on #224 (D2 exactly +.0004, S3 about +.002): every scored non-lab S3 row and the 30 largest
# D2 rows with 10-25 pct between the gray file and the DeepSeek median (results/s43_rsi/ids_round4.csv), excluded clips
# and rows of rounds 1-3 left out. First investigation under harness v3, then a verification round on every proposal
# the apply rule would consider. The guard holds the pool until login A's five-hour window resets (06:30 UTC).
cd "$(dirname "$0")/.." || exit 1
python3 scripts/s43_rsi.py build --ids-file results/s43_rsi/ids_round4.csv --out results/s43_rsi
python3 scripts/s43_rsi.py annotate --out results/s43_rsi
python3 scripts/s43_rsi.py run --round 1 --harness v3 --ids-file results/s43_rsi/ids_round4.csv \
  --out results/s43_rsi --account a --guard results/s43_rsi/guard_a.json --max-sessions 8 --timeout 40
python3 scripts/s43_rsi.py collect --round 1 --out results/s43_rsi
python3 scripts/s43_rsi.py proposals --ids-file results/s43_rsi/ids_round4.csv --out results/s43_rsi \
  --write results/s43_rsi/ids_round4_verify.csv
python3 scripts/s43_rsi.py run --round 2 --harness v3 --ids-file results/s43_rsi/ids_round4_verify.csv \
  --out results/s43_rsi --account a --guard results/s43_rsi/guard_a.json --max-sessions 8 --timeout 40
python3 scripts/s43_rsi.py collect --round 2 --out results/s43_rsi
echo "round 4 done $(date -u +%H:%M)"
