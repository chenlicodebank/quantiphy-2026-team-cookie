#!/bin/bash
# 27_3 (2026-10-21, session 6e6e97e4, login B): per-question 26_30-harness answers for the 30 validation-family rows
# with no same-wording validation question (results/s27_valfam/ids.csv) - the 20 rows #201 exposed as scored are among
# them, and #203 still answers them with #186-line per-video answers (method_queue 45, narrowed). Opus 5.5 high, the
# 26_30 prompts (no --real-scale, as #199's first answers), current dataset rows, scene records reused where an earlier
# validation run made one.
set -euo pipefail
cd "$(dirname "$0")/.."
"${QP_PYTHON:-python3}" scripts/cc_scene_ids.py --ids-file results/s27_valfam/ids.csv \
  --out results/s27_valfam --account b --guard results/s27_valfam/guard_b.json \
  --scene-from results/s26_scene_val,results/s26_scene_val_lean,results/s26_reask_1020_val \
  --workers 4 --q-workers 3 --max-sessions 6 "$@"
