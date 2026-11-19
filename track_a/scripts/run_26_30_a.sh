#!/bin/bash
# 26_30 (2026-10-18; renumbered from 26_16, which the Track B session took for its per-question GLM run): the per-question Track A run over the whole scored test split (523 videos, 3,012 questions) with
# the lean two-phase agent (scripts/cc_agent_scene.py --lean), approved by the user 2026-10-18. One queue, one pool per
# account (claims/); this is pool A.
# Guard: results/s26_scene_full/guard_a.json (edit live). Drain: touch results/s26_scene_full/STOP_a.
# Build afterwards: scripts/build_s26_scene.py --runs results/s26_scene_full.
set -euo pipefail
TASK_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$TASK_REPO"
exec "${QP_PYTHON:-python3}" -u scripts/cc_agent_scene.py --account a \
  --guard results/s26_scene_full/guard_a.json --out results/s26_scene_full \
  --workdir /private/tmp/qp_blind/scene_full_a --lean --effort medium --max-turns 120 --max-turns-p2 80 \
  --workers 2 --q-workers 3 --max-sessions 5 "$@"
