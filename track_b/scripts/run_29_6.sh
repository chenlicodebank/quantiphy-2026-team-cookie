#!/bin/bash
# 29_6 (2026-10-22, Track B, session 432d3a13, GH200): 29_4's A/B again with the judgment levers on top of the SAM 3 tools
# - the method card in the answering prompt (--judgment-card) and one forced self-check before an answer counts
# (--self-audit) - on the same questions and the same 28_x scene records, so 28_x (no tools), 29_4 (tools) and 29_6
# (tools + card + audit) are three arms of one comparison. LEG=val or LEG=test as in run_29_4.sh.
set -euo pipefail
cd "$(dirname "$0")/.."
LEG="${LEG:?set LEG=val or LEG=test}"
if [ "$LEG" = val ]; then OUT="${OUT:-results/s29_val_dsf1017_card}"; else OUT="${OUT:-results/s29_test_dsf1017_card}"; fi
OUT="$OUT" LEG="$LEG" bash scripts/run_29_4.sh --judgment-card --self-audit "$@"
