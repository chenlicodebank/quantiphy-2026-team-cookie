#!/bin/bash
# 26_59 (2026-10-20, user go "do all"): the --real-scale re-ask of the compliant Track A rows the 26_30 traces point at
# (method_queue item 38; selection and stages by scripts/s26_reask_prep.py; gate preregistered in scripts/gate_26_59.py).
# pool B, started from a session opened on login B (run rule 3); own guard; phase 2 only (the 26_30
# scene records are copied in, results/s26_scene_full stays untouched). Same phase-2 settings as 26_30 (Opus 5.5 high,
# 80 turns, --size-names) plus --real-scale. Usage: run_26_59.sh stage1 | stage2. Drain: touch results/s26_reask_1020/STOP_b.
set -euo pipefail
TASK_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$TASK_REPO"
STAGE="${1:?stage1 or stage2}"; shift
exec "${QP_PYTHON:-python3}" -u scripts/cc_agent_scene.py --account b \
  --guard results/s26_reask_1020/guard_b.json --out results/s26_reask_1020 \
  --workdir /private/tmp/qp_blind/reask_1020 --size-names --real-scale --max-turns-p2 80 \
  --events "$(cat results/s26_reask_1020/events.txt)" --rerun "results/s26_reask_1020/rerun_${STAGE}.json" \
  --workers 4 --q-workers 4 --max-sessions 10 "$@"
