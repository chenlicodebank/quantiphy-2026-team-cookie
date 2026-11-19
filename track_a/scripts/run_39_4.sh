#!/bin/bash
# 39_4 (2026-10-24, Track A, session 28b2ba80, login A): a fresh
# Opus 5.5 per-question session with the SAM 3 mask as the REQUIRED second route (35_2: +.023 on 32 labelled 2D rows,
# method_queue 62) for every scored 2D simulation / segmentation speed and acceleration row (results/s39_third/ids_2dmotion.csv,
# written by scripts/s39_third_prep.py; special-reading re-ask rows and the audit's OUT rows left out). Phase 2 only: the
# 26_30 question-blind scene records are reused (--scene-from results/s26_scene_full); question data from the CURRENT rows.
# Same phase-2 settings as 26_30 (Opus 5.5, effort high, 80 turns, --size-names) + --sam3-url/--sam3-required.
# SAM 3: lambda2 scripts/sam3_server.py remote mode on :8791 through `ssh -N -L 8791:127.0.0.1:8791 lambda2`.
# Drain: touch results/s39_2dmotion/STOP_a.
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${QP_PYTHON:-python3}"
SAM3_URL="${SAM3_URL:-http://127.0.0.1:8791}"
curl -sf "$SAM3_URL/health" >/dev/null || { echo "SAM 3 server not reachable at $SAM3_URL"; exit 1; }
exec "$PY" -u scripts/cc_scene_ids.py --ids-file results/s39_third/ids_2dmotion.csv --out results/s39_2dmotion \
  --account a --guard results/s39_2dmotion/guard_a.json --scene-from results/s26_scene_full \
  --workdir /private/tmp/qp_blind/s39_2dmotion --size-names --max-turns-p2 80 \
  --sam3-url "$SAM3_URL" --sam3-required --workers "${WORKERS:-6}" --q-workers "${QW:-3}" --max-sessions "${MAXS:-12}" "$@"
