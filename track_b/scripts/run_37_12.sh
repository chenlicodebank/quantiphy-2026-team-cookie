#!/bin/bash
# 37_12 (2026-10-24, session 05e6b3c8, GH200 lambda2): the final sweep of Series 37 once every earlier process has ended.
# Sets aside unanswered records (capped or failed sessions; s37_requeue_failed.py), then schedules from the question's
# own runs under the preregistered policy (POLICY a .05 / b .3): r2 where none answered, r3 where |ln r1/r2| > .05 and
# no r3, r4 + r5 where three runs spread > .3 in ln and no r4. One process per group and repeat window, own workspace
# roots, caps from the balance. Run it again until it schedules nothing (an r3 can call for an r4 + r5).
#   bash scripts/run_37_12.sh          # on the box, after `tmux ls | grep qp_37_` shows only the guard
#   SWEEP_GROUPS="S2 S3 D3" bash scripts/run_37_12.sh   # while the D2 pipeline still runs (2026-10-24 19:45 UTC)
set -euo pipefail
cd "$(dirname "$0")/.."
PY="$HOME/qp_dsh_venv/bin/python"
SWEEP_GROUPS="${SWEEP_GROUPS:-S2 S3 D3 D2}"   # (not GROUPS, a bash builtin) SWEEP_GROUPS="S2 S3 D3" sweeps those while another group's run still goes
for G in $SWEEP_GROUPS; do
  if ps -eo args | grep "[d]sh_scene.py" | grep s37_test_repeats | grep -q -- "--cats $G"; then echo "a Series 37 $G run is still going"; exit 1; fi
done
"$PY" scripts/s37_requeue_failed.py results/s37_test_repeats
T="TIERS=deepinfra/fp8/flex,deepinfra/fp8,deepinfra/fp8/priority QP_RETRY_429=1"
for G in $SWEEP_GROUPS; do
  for STAGE in 2 3 4; do
    read -r IDS VIDEOS < <("$PY" - "$G" "$STAGE" <<'PY'
import glob, json, math, sys
g, k = sys.argv[1], int(sys.argv[2])
rows = json.load(open("data/test/test_dataset_current_20261021.json"))
mine = {r["row_idx"] + 1: r["video_id"] for r in rows if r["inference_type"][0] + r["video_type"][1] == g}
ans = {}
for p in glob.glob("results/s37_test_repeats/q/*/r*.json"):
    r = json.load(open(p)); a = (r.get("final") or {}).get("answers") or []
    v = a[0].get("value") if a else None
    if isinstance(v, (int, float)) and v > 0:
        ans.setdefault(int(p.split("/")[-2].split("__")[-1]), {})[int(p.split("/")[-1][1:-5])] = float(v)
need = []
for i in mine:
    a = ans.get(i, {})
    if k == 2 and 2 not in a:
        need.append(i)
    elif k == 3 and 2 in a and 1 in a and 3 not in a and abs(math.log(a[1] / a[2])) > 0.05:
        need.append(i)
    elif k == 4 and 3 in a and 4 not in a:
        v = [a[j] for j in (1, 2, 3) if j in a]
        if math.log(max(v) / min(v)) > 0.3:
            need.append(i)
print(",".join(map(str, need)) or "-", ",".join(sorted({mine[i] for i in need})) or "-")
PY
)
    [ "$IDS" = "-" ] && continue
    N=$(echo "$IDS" | tr ',' '\n' | grep -c .)
    R=$([ "$STAGE" = 4 ] && echo 5 || echo "$STAGE")
    S=$([ "$G" = S2 ] || [ "$G" = S3 ] && echo 8790 || echo 8791)
    CAP=$("$PY" -c "print(round(max(1.0, $N * $([ "$STAGE" = 4 ] && echo 2 || echo 1) * 0.06), 1))")
    echo "$G r$STAGE..r$R: $N questions, cap \$$CAP"
    tmux new-session -d -s "qp_37_12_${G}r$STAGE" "$T GROUP=$G SAM3_URL=http://127.0.0.1:$S IDS=$IDS VIDEOS=$VIDEOS WORKERS=8 QW=4 REPEATS=$R FROM=$STAGE CAP=$CAP bash scripts/run_37_1.sh --workdir /tmp/qp_blind/s37_test_repeats_${G}s$STAGE > results/run37_12_${G}r$STAGE.log 2>&1"
    break   # one stage per group per sweep: the next sweep sees what this one adds
  done
done
tmux ls | grep qp_37 || true
