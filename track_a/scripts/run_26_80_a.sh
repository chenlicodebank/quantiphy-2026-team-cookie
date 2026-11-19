#!/bin/bash
# 26_80 (2026-10-21): repeat runs for a per-question median of three on the noisy 3D Track A questions (selection by
# question type only: lab S3/D3 speeds, accelerations, path lengths; simulation/segmentation S3/D3 accelerations; a
# 30-row seeded pilot of simulation/segmentation D3 sizes). Prepared by scripts/s26_repeat_prep.py. pool A; its own out dir (split by video, so no question folder is written by two pools) and guard (max_5h
# 0.80 leaves room for other use of the login). Phase 2 only, on copies of the 26_30 scene records
# (results/s26_scene_full untouched); phase-2 model Sonnet 5.5 at effort high (set explicitly: the level 26_81 validated and the level of the 26_30 Opus
# first runs; user 2026-10-21: "run now, but use correct thinking level"), 80 turns, --size-names. Repeat 2
# for every selected question, then repeat 3. Drain: touch results/s26_repeat_1021_a/STOP_a. Build
# afterwards: scripts/build_s26_median3.py.
set -euo pipefail
TASK_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$TASK_REPO"
OUT=results/s26_repeat_1021_a
for R in r2 r3; do
  "${QP_PYTHON:-python3}" -u scripts/cc_agent_scene.py --account a \
    --guard "$OUT/guard_a.json" --out "$OUT" --workdir /private/tmp/qp_blind/repeat_1021_a --size-names \
    --model-p2 claude-sonnet-5-5 --effort-p2 high --max-turns-p2 80 --events "$(cat "$OUT/events.txt")" --rerun "$OUT/rerun_$R.json" \
    --workers 4 --q-workers 4 --max-sessions 6 "$@"
  [ -e "$OUT/STOP_a" ] && break
done
