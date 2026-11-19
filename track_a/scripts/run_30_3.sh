#!/bin/bash
# 30_3 (2026-10-22, session 625fd803): Opus 5.5 adjudicator over the per-question dossiers of the 41 S3 3D simulation /
# segmentation rows where DeepSeek-1017 (28_3) differs from E2 by 25 pct to 2x (results/s30_flags/s3_rest41.csv; the
# 14 rows beyond 2x wait for a Codex third opinion, 30_4). Login A with admission control (guard). User approved
# ~$300 of Claude plan for Series 30 (2026-10-22). Validation gate 30_2 passed (7 rows: .957 vs Opus first .950).
cd "$(dirname "$0")/.."
python3 scripts/s30_dossier.py adjudicate --ids-file results/s30_flags/s3_rest41.csv --dossier results/s30_dossier \
    --out results/s30_adj_s3 --account a --guard results/s30_adj_s3/guard_a.json --max-sessions 8 \
    --workdir /private/tmp/qp_blind/s30_adj_s3 --trigger "30_3 S3 adjudication (DeepSeek differs 25 pct to 2x)"
