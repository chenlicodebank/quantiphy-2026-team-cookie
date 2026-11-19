#!/bin/bash
# 26_30 (2026-10-18; renumbered from 26_16, which the Track B session took for its per-question GLM run): the per-question Track A run over the whole scored test split (523 videos, 3,012 questions) with
# the lean two-phase agent (scripts/cc_agent_scene.py --lean), approved by the user 2026-10-18. One queue, one pool per
# account (claims/); this is pool B: start it from a session opened on login B (run rule 3).
# Guard: results/s26_scene_full/guard_b.json (edit live). Drain: touch results/s26_scene_full/STOP_b.
# Build afterwards: scripts/build_s26_scene.py --runs results/s26_scene_full.
set -euo pipefail
TASK_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$TASK_REPO"
exec "${QP_PYTHON:-python3}" -u scripts/cc_agent_scene.py --account b \
  --guard results/s26_scene_full/guard_b.json --out results/s26_scene_full \
  --workdir /private/tmp/qp_blind/scene_full_b --lean --effort medium --max-turns 120 --max-turns-p2 80 \
  --workers 8 --q-workers 4 --max-sessions 16 "$@"
