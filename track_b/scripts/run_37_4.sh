#!/bin/bash
# 37_4 (2026-10-24, Track B, session 05e6b3c8, GH200 lambda2): Codex's 36_1 projective calibration instrument + card in
# the r1 configuration with SAM 3 (scripts/s37_calib_agent.py), one run of 57 D3 simulation / segmentation test
# questions: 39 scored rows drawn before any read (2 per video from 20 videos, numpy seed 374) and the 18 labelled
# test-resolution D3 simulation rows (validation duplicates). Read against r1 / r2 of the same questions (37_1): row MRA
# on the labelled rows, agreement with E2 on the scored ones. Adopt for later repeats of D3 simulation rows only if the
# treatment beats the plain single runs on both reads. Tiers flex / standard, 429s waited out. ~$2.
#   STAGE=1 bash scripts/run_37_4.sh
#   tmux new-session -d -s qp_37_4 "SAM3_URL=http://127.0.0.1:8791 CAP=3 bash scripts/run_37_4.sh > results/run37_4.log 2>&1"
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="${OUT:-results/s37_calib}"
SRC=results/s29_pass_sam3
PY="$HOME/qp_dsh_venv/bin/python"
if [ "${STAGE:-0}" = 1 ]; then
  mkdir -p "$OUT/videos" "$OUT/q"
  "$PY" - "$OUT" <<'PY'
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
out = Path(sys.argv[1])
ds = pd.DataFrame(json.loads(Path("data/test/test_dataset_current_20261021.json").read_text()))
ds["id"] = ds.row_idx + 1
ds["cat"] = [("S" if it[0] == "S" else "D") + vt[1] for it, vt in zip(ds.inference_type, ds.video_type)]
scored = set(pd.read_csv("results/s26_scene_full/ledger.csv").id)
val = pd.read_csv("data/validation/validation_dataset.csv")
lab = ds.merge(val[["video_id", "question"]], on=["video_id", "question"])
labd3 = lab[(lab.cat == "D3") & lab.video_source.isin(["simulation", "segmentation"])]
pool = ds[(ds.cat == "D3") & ds.video_source.isin(["simulation", "segmentation"]) & ds.id.isin(scored)]
rng = np.random.default_rng(374)
vids = rng.choice(sorted(pool.video_id.unique()), 20, replace=False)
pick = []
for v in vids:
    t = pool[pool.video_id == v]
    pick += list(rng.choice(t.id.values, min(2, len(t)), replace=False))
ids = sorted(set(map(int, pick)) | set(map(int, labd3.id)))
vv = sorted(set(ds.set_index("id").loc[ids].video_id))
(out / "ids.txt").write_text(",".join(map(str, ids)) + "\n")
(out / "ids_random.txt").write_text(",".join(map(str, sorted(map(int, pick)))) + "\n")
(out / "videos.txt").write_text(",".join(vv) + "\n")
print(len(pick), "random +", len(labd3), "labelled =", len(ids), "questions on", len(vv), "videos")
PY
  for v in $(tr ',' ' ' < "$OUT/videos.txt"); do
    [ -f "$OUT/videos/$v/scene/scene.json" ] || cp -r "$SRC/videos/$v" "$OUT/videos/"
  done
  exit 0
fi
source ~/.qp_keys.sh
export PATH="$HOME/qp_tools/node/bin:$PATH" QP_LLM_ROUTE=openrouter QP_RETRY_429=1
TIERS="${TIERS:-deepinfra/fp8/flex,deepinfra/fp8}"
"$PY" scripts/s37_calib_agent.py \
  --runtime "${QP_DSH_RUNTIME:-$HOME/qp_dsh_runtime}" \
  --model deepseek/deepseek-v4.1-flash-1017 --provider "$TIERS" --provider-order "$TIERS" --reasoning medium \
  --split test --qsource current --videos "$(cat "$OUT/videos.txt")" --ids "$(cat "$OUT/ids.txt")" --cats D3 \
  --sam3-url "${SAM3_URL:?set SAM3_URL}" --out "$OUT" --workdir /tmp/qp_blind/s37_calib \
  --repeats "${REPEATS:-1}" --repeat-from "${FROM:-1}" --clip-usd 0.3 --budget-usd "${CAP:?set CAP}" \
  --workers "${WORKERS:-6}" --q-workers "${QW:-4}" --fail-fast 6 "$@"
