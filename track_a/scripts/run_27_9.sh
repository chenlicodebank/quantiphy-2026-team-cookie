#!/bin/bash
# 27_9 (2026-10-21, session 6e6e97e4): --real-scale --size-names re-asks of every scored simulation / segmentation row
# whose own prior is gravity (9.8 m/s^2), except the 11 already re-asked in 27_6. Why: in the farmhouse clips
# (simulation_0011 / 0013 / 0014) the stated gravity does not match the rendered fall (slow motion or a damped soft body;
# file fps = question_fps = 24), so the gravity route sets every size about 3x too large - the 26_30 sessions noticed it
# ("the scene is about 3x real-world scale") and kept it under the old "the prior is exact" wording, while the 27_6
# re-asks moved doors / wheels / birds to real size. The selection reads only each row's own prior (no other row's
# answer); each re-ask is a fresh per-question session that checks the gravity scale against standard objects and keeps
# it when they agree. Opus 5.5 high; scene records from 26_30.
set -euo pipefail
cd "$(dirname "$0")/.."
"${QP_PYTHON:-python3}" scripts/cc_scene_ids.py --ids-file results/s27_gravity/ids.csv \
  --out results/s27_gravity --account b --guard results/s27_gravity/guard_b.json \
  --scene-from results/s26_scene_full --real-scale --size-names \
  --workers 6 --q-workers 4 --max-sessions 10 --workdir /private/tmp/qp_blind/s27_gravity "$@"
