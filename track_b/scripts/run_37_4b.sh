#!/bin/bash
# 37_4b (2026-10-24 23:46 UTC, session 05e6b3c8): run_37_4.sh with the priority tier excluded by name (as 37_3b).
exec bash "$(dirname "$0")/run_37_4.sh" --provider-ignore deepinfra/fp8/priority "$@"
