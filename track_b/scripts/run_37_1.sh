#!/bin/bash
# 37_1 (2026-10-24, Track B, session 05e6b3c8, GH200 lambda2; user: "work on quantiphy track B ... you can run exps,
# including full test run ... when running deepseek, note the use correct settings"): the second run (r2) of every test
# question, in exactly r1's configuration (DeepSeek-1017 on DeepInfra fp8, reasoning medium, temperature 0.3, the SAM 3
# tools, the 29_6 method card on S2 / D2 only - read per question from r1's recorded prompt by s35_repeat_ids.py), so
# r1 / r2 / later repeats are exchangeable runs of the same question (method_queue 59; 35_1 gate +.022 a row for the
# median of three). It is the first stage of an adaptive repeat policy: r3 (37_2) only where r1 and r2 disagree.
# Validation simulation on the 63 questions with seven runs (2026-10-24, zero API): one run .775, geomean of two .788,
# median of three .791, adaptive (r3 when |ln(r1/r2)| > .05, r4-r5 when the three spread > .3) .797 at 2.6 runs.
# Price tiers: DeepInfra fp8 flex (0.8x) first, standard on 429, priority (1.5x) last (35_5).
# New folder: results/s29_pass_sam3 (the declared B7 answers) is never written.
#   STAGE=1 bash scripts/run_37_1.sh       # on the box: copy r1 + the 568 scene records, write the id lists (no spend)
#   tmux new-session -d -s qp_37_1_S2 "GROUP=S2 SAM3_URL=http://127.0.0.1:8790 CAP=12 bash scripts/run_37_1.sh > results/run37_1_S2.log 2>&1"
#   ... GROUP=D3 (SAM3_URL :8791, CAP=30), S3 (CAP=18), D2 (CAP=17) the same way.
# IDS=<comma list> overrides the group's id list; REPEATS / FROM set the repeat window (default r2 only).
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="${OUT:-results/s37_test_repeats}"
SRC=results/s29_pass_sam3
PY="$HOME/qp_dsh_venv/bin/python"
if [ "${STAGE:-0}" = 1 ]; then
  mkdir -p "$OUT/videos" "$OUT/q"
  for v in $(ls "$SRC/videos"); do
    [ -f "$OUT/videos/$v/scene/scene.json" ] || cp -r "$SRC/videos/$v" "$OUT/videos/"
  done
  for d in "$SRC"/q/*; do
    b=$(basename "$d"); mkdir -p "$OUT/q/$b"; [ -f "$OUT/q/$b/r1.json" ] || cp "$d/r1.json" "$OUT/q/$b/"
  done
  "$PY" scripts/s35_repeat_ids.py --src "$SRC" --out "$OUT"
  exit 0
fi
source ~/.qp_keys.sh
export PATH="$HOME/qp_tools/node/bin:$PATH" QP_LLM_ROUTE=openrouter
GROUP="${GROUP:?set GROUP=S2, D3, S3 or D2}"
case "$GROUP" in S2|D2) FLAG=card; CARD=(--judgment-card) ;; *) FLAG=nocard; CARD=() ;; esac
IDS="${IDS:-$(cat "$OUT/ids_${FLAG}_${GROUP}.txt")}"
VIDEOS="${VIDEOS:-$(cat "$OUT/videos_${FLAG}_${GROUP}.txt")}"
TIERS="${TIERS:-deepinfra/fp8/flex,deepinfra/fp8,deepinfra/fp8/priority}"
"$PY" scripts/dsh_scene.py \
  --runtime "${QP_DSH_RUNTIME:-$HOME/qp_dsh_runtime}" \
  --model deepseek/deepseek-v4.1-flash-1017 --provider "$TIERS" --provider-order "$TIERS" --reasoning medium \
  --split test --qsource current --videos "$VIDEOS" --ids "$IDS" --cats "$GROUP" ${CARD[@]+"${CARD[@]}"} \
  --sam3-url "${SAM3_URL:?set SAM3_URL}" --out "$OUT" --workdir "/tmp/qp_blind/s37_test_repeats_$GROUP" \
  --repeats "${REPEATS:-2}" --repeat-from "${FROM:-2}" --clip-usd 0.3 --budget-usd "${CAP:?set CAP}" \
  --workers "${WORKERS:-12}" --q-workers "${QW:-6}" --fail-fast 6 "$@"
