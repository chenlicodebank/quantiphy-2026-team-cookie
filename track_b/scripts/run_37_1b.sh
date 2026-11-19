#!/bin/bash
# 37_1b (2026-10-24, session 05e6b3c8): run_37_1.sh (r2 in r1's configuration) without DeepInfra's 1.5x priority tier.
# 37_1's first S2 / D3 sessions fell through flex -> standard -> priority on 62 pct of their calls under ~190 concurrent
# sessions; here the provider list is flex then standard only and a 429 is waited out in dsh_measurement.forward
# (QP_RETRY_429, up to ~6 min a call) instead. Same model, quantization, prompt and tools; only the price tier differs.
# provider.only "deepinfra/fp8" also matches deepinfra/fp8/priority (35_5), so the priority tier is excluded by name.
#   tmux new-session -d -s qp_37_1_S3 "GROUP=S3 SAM3_URL=http://127.0.0.1:8790 CAP=18 bash scripts/run_37_1b.sh > results/run37_1_S3.log 2>&1"
export TIERS="${TIERS:-deepinfra/fp8/flex,deepinfra/fp8}" QP_RETRY_429=1
exec bash "$(dirname "$0")/run_37_1.sh" --provider-ignore deepinfra/fp8/priority "$@"
