#!/bin/bash
# 27_6 (2026-10-21, session 6e6e97e4): --real-scale --size-names re-asks (26_59's answering prompt) of 41 rows the 27_4
# plausibility screen called implausible, kept only where the named thing has a standard real size (cars, doors, cart and
# bicycle wheels, bicycles, walking people, forklift, helicopter, teacup, toothbrush, beach chairs, birds, deer /
# antelope, a football, lettering vs its stated width; two internet cars under a lane-width prior). Not re-asked: rows
# 26_59 already re-asked, lanes (validation: 11.8 m curb to curb), TV-stand widths (--size-names), non-standard things
# (acorns, billboard, wallet, canoe, rocks, boats with masts). Selection used only each row's own question, prior and
# answer (27_4 judged one line at a time). Opus 5.5 high; scene records from 26_30.
set -euo pipefail
cd "$(dirname "$0")/.."
"${QP_PYTHON:-python3}" scripts/cc_scene_ids.py --ids-file results/s27_plaus_reask/ids.csv \
  --out results/s27_plaus_reask --account b --guard results/s27_plaus_reask/guard_b.json \
  --scene-from results/s26_scene_full --real-scale --size-names \
  --workers 6 --q-workers 4 --max-sessions 8 --workdir /private/tmp/qp_blind/s27_plaus_reask "$@"
