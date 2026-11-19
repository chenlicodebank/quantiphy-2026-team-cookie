#!/bin/bash
# 37_11 (2026-10-24 ~12:50 UTC, session 05e6b3c8, GH200 lambda2; user: "topuped 100 already ... continue to run", balance
# $112.33): back to the policy fixed before any read (r3 where |ln r1/r2| > .05, r4 + r5 where three runs spread > .3;
# POLICY.json rewritten) and the runs the budget had cut: (1) D2 simulation (758 questions, r1 only so far) through the
# whole pipeline; (2) r3 for every S2 / S3 / D3 / D2 question in the .05-.1 band the tightened policy skipped, plus any
# question still without an answered r2, in their own workspace roots (the running 37_6 / 37_7 D3 / S3 r3 stages hold
# the > .1 lists; the bands are disjoint from them). A final r4-r5 sweep follows once every r3 has landed (37_12).
#   bash scripts/run_37_11.sh          # on the box
set -euo pipefail
cd "$(dirname "$0")/.."
PY="$HOME/qp_dsh_venv/bin/python"
OUT=results/s37_test_repeats
echo '{"a": 0.05, "b": 0.3, "why": "2026-10-24 12:50 UTC: back to the policy fixed before any read after the user topped up $100"}' > "$OUT/POLICY.json"
T="TIERS=deepinfra/fp8/flex,deepinfra/fp8,deepinfra/fp8/priority QP_RETRY_429=1"
D2SIM="$("$PY" - <<'PY'
import json
rows = json.load(open("data/test/test_dataset_current_20261021.json"))
print(",".join(str(r["row_idx"] + 1) for r in rows
               if r["inference_type"][0] == "D" and r["video_type"][1] == "2" and r["video_source"] == "simulation"))
PY
)"
tmux new-session -d -s qp_37_11_D2sim "$T IDS=$D2SIM WORKERS=10 QW=4 GROUP=D2 SAM3_URL=http://127.0.0.1:8791 CAP_R2=13 CAP_R3=4 CAP_R45=3 bash scripts/run_37_2b.sh > results/run37_11_D2sim.log 2>&1"
for G in S2 S3 D3 D2; do
  read -r IDS2 IDS3 VIDEOS < <("$PY" - "$G" <<'PY'
import glob, json, math, sys
g = sys.argv[1]
out = "results/s37_test_repeats"
rows = json.load(open("data/test/test_dataset_current_20261021.json"))
mine = {r["row_idx"] + 1: r["video_id"] for r in rows if r["inference_type"][0] + r["video_type"][1] == g
        and not (g == "D2" and r["video_source"] == "simulation")}
held = set()   # the r3 ids the running dsh_scene processes of this group hold, read from their own command lines
for c in glob.glob("/proc/[0-9]*/cmdline"):
    try:
        a = open(c, "rb").read().decode(errors="replace").split("\0")
    except OSError:
        continue
    if not any(x.endswith("dsh_scene.py") for x in a) or "--ids" not in a or "--cats" not in a:
        continue
    if a[a.index("--cats") + 1] == g and "--repeats" in a and int(a[a.index("--repeats") + 1]) >= 3:
        held |= {int(x) for x in a[a.index("--ids") + 1].split(",") if x}
ans = {}
for p in glob.glob(f"{out}/q/*/r*.json"):
    r = json.load(open(p)); a = (r.get("final") or {}).get("answers") or []
    v = a[0].get("value") if a else None
    if isinstance(v, (int, float)) and v > 0:
        ans.setdefault(int(p.split("/")[-2].split("__")[-1]), {})[int(p.split("/")[-1][1:-5])] = float(v)
need2, need3 = [], []
for i in mine:
    a = ans.get(i, {})
    if 2 not in a:
        need2.append(i)
    elif 3 not in a and i not in held and 1 in a and abs(math.log(a[1] / a[2])) > 0.05:
        need3.append(i)
vids = sorted({mine[i] for i in need2 + need3})
print(",".join(map(str, need2)) or "-", ",".join(map(str, need3)) or "-", ",".join(vids) or "-")
PY
)
  S=$([ "$G" = S2 ] || [ "$G" = S3 ] && echo 8790 || echo 8791)
  echo "$G: r2 catch-up $(echo "$IDS2" | tr ',' '\n' | grep -vc '^-$'), r3 band $(echo "$IDS3" | tr ',' '\n' | grep -vc '^-$')"
  if [ "$IDS2" != "-" ]; then
    tmux new-session -d -s "qp_37_11_${G}r2" "$T GROUP=$G SAM3_URL=http://127.0.0.1:$S IDS=$IDS2 VIDEOS=$VIDEOS WORKERS=6 QW=4 CAP=3 bash scripts/run_37_1.sh --workdir /tmp/qp_blind/s37_test_repeats_${G}c2 > results/run37_11_${G}r2.log 2>&1"
  fi
  if [ "$IDS3" != "-" ]; then
    tmux new-session -d -s "qp_37_11_${G}r3" "$T GROUP=$G SAM3_URL=http://127.0.0.1:$S IDS=$IDS3 VIDEOS=$VIDEOS WORKERS=8 QW=4 REPEATS=3 FROM=3 CAP=12 bash scripts/run_37_1.sh --workdir /tmp/qp_blind/s37_test_repeats_${G}c3 > results/run37_11_${G}r3.log 2>&1"
  fi
done
tmux ls | grep qp_37
