#!/bin/bash
# 37_3 (2026-10-24, Track B, session 05e6b3c8, GH200 lambda2): the physical-scale check on every internet question
# (S2 203 + D2 217 = 420; scripts/s37_scale_check.py): one more session per question in r1's configuration (DeepSeek-1017
# on DeepInfra fp8, reasoning medium, SAM 3 tools, the 29_6 method card - every
# internet question is S2 or D2) plus the scale_check card. Its answer stays on the prior's scale; the recorded check
# feeds s37_final_b.py's rule. Same question-blind scene records as r1 (copied from results/s29_pass_sam3). Price tiers
# as 37_1b: flex then standard, no priority, 429s waited out (QP_RETRY_429).
#   STAGE=1 bash scripts/run_37_3.sh     # copy the internet scene records, write ids.txt / videos.txt (no spend)
#   tmux new-session -d -s qp_37_3 "SAM3_URL=http://127.0.0.1:8790 CAP=8 bash scripts/run_37_3.sh > results/run37_3.log 2>&1"
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="${OUT:-results/s37_physcheck}"
SRC=results/s29_pass_sam3
PY="$HOME/qp_dsh_venv/bin/python"
if [ "${STAGE:-0}" = 1 ]; then
  mkdir -p "$OUT/videos" "$OUT/q"
  "$PY" - "$OUT" <<'PY'
import json, sys
from pathlib import Path
out = Path(sys.argv[1])
rows = json.loads(Path("data/test/test_dataset_current_20261021.json").read_text())
ids = [r["row_idx"] + 1 for r in rows if r["video_source"] == "internet"]
vids = sorted({r["video_id"] for r in rows if r["video_source"] == "internet"})
(out / "ids.txt").write_text(",".join(map(str, ids)) + "\n")
(out / "videos.txt").write_text(",".join(vids) + "\n")
print(len(ids), "internet questions on", len(vids), "videos")
PY
  for v in $(tr ',' ' ' < "$OUT/videos.txt"); do
    [ -f "$OUT/videos/$v/scene/scene.json" ] || cp -r "$SRC/videos/$v" "$OUT/videos/"
  done
  exit 0
fi
source ~/.qp_keys.sh
export PATH="$HOME/qp_tools/node/bin:$PATH" QP_LLM_ROUTE=openrouter QP_RETRY_429=1
TIERS="${TIERS:-deepinfra/fp8/flex,deepinfra/fp8}"
"$PY" scripts/s37_scale_check.py \
  --runtime "${QP_DSH_RUNTIME:-$HOME/qp_dsh_runtime}" \
  --model deepseek/deepseek-v4.1-flash-1017 --provider "$TIERS" --provider-order "$TIERS" --reasoning medium \
  --split test --qsource current --videos "$(cat "$OUT/videos.txt")" --ids "${IDS:-$(cat "$OUT/ids.txt")}" \
  --cats S2,D2 --judgment-card --sam3-url "${SAM3_URL:?set SAM3_URL}" --out "$OUT" \
  --workdir /tmp/qp_blind/s37_physcheck --repeats "${REPEATS:-1}" --repeat-from "${FROM:-1}" \
  --clip-usd 0.3 --budget-usd "${CAP:?set CAP}" --workers "${WORKERS:-8}" --q-workers "${QW:-6}" --fail-fast 6 "$@"
