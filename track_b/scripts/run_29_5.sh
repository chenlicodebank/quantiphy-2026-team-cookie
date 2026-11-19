#!/bin/bash
# 29_5 (2026-10-22, Track B, session 432d3a13, GH200): DeepSeek-1017 two-phase per question on the test questions Track A
# asked second opinions on (run channel #121 / #122): D3 on 3D simulation + segmentation videos first, then S2 (PASS_GROUPS; not GROUPS, a bash builtin);
# the answers are Track B's own per-question line too. 28_3 configuration (DeepInfra fp8, reasoning medium) on DSH 0.2.1.
# The user topped up OpenRouter for it (balance $51.64 at 10:55 UTC). Phase 1 (question-blind scene records) runs first:
#   PHASE=1 CAP=8 bash scripts/run_29_5.sh
# then phase 2, with the SAM 3 tools only if the 29_4 A/B says so (SAM3_URL=http://127.0.0.1:8790 OUT=..._sam3; the
# scene records are copied over so both arms start from the same record):
#   CAP=40 bash scripts/run_29_5.sh
set -euo pipefail
cd "$(dirname "$0")/.."
source ~/.qp_keys.sh
export PATH="$HOME/qp_tools/node/bin:$PATH" QP_LLM_ROUTE=openrouter
PY="$HOME/qp_dsh_venv/bin/python"
PASS_GROUPS="${PASS_GROUPS:-d3sim,s2}"
VIDEOS="${VIDEOS:-$($PY scripts/s29_pass_videos.py videos "$PASS_GROUPS")}"
CATS="$($PY scripts/s29_pass_videos.py cats "$PASS_GROUPS")"
OUT="${OUT:-results/s29_test_dsf1017}"
EXTRA=()
if [ -n "${SAM3_URL:-}" ]; then
  EXTRA+=(--sam3-url "$SAM3_URL")
  for v in ${VIDEOS//,/ }; do  # the same question-blind record as the no-tools arm
    if [ -f "results/s29_test_dsf1017/videos/$v/scene/scene.json" ] && [ ! -f "$OUT/videos/$v/scene/scene.json" ]; then
      mkdir -p "$OUT/videos/$v" && cp -r "results/s29_test_dsf1017/videos/$v/scene" "$OUT/videos/$v/scene"
    fi
  done
fi
"$PY" scripts/dsh_scene.py \
  --runtime "${QP_DSH_RUNTIME:-$HOME/qp_dsh_runtime}" \
  --model deepseek/deepseek-v4.1-flash-1017 --provider "${PROVIDER:-deepinfra/fp8}" --reasoning medium \
  --split test --qsource current --phase "${PHASE:-both}" --videos "$VIDEOS" --cats "$CATS" \
  --out "$OUT" --workdir "/tmp/qp_blind/$(basename "$OUT")" "${EXTRA[@]}" \
  --clip-usd 0.3 --budget-usd "${CAP:?set CAP}" --workers "${WORKERS:-20}" --q-workers "${QW:-6}" --fail-fast 6 "$@"
