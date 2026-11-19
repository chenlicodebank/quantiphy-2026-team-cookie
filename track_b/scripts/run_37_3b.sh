#!/bin/bash
# 37_3b (2026-10-24 23:46 UTC, session 05e6b3c8): run_37_3.sh with the priority tier excluded by name. provider.only
# "deepinfra/fp8" also matches deepinfra/fp8/priority (35_5), and 37_3's first sessions were billed at 1.5x; the same
# out folder resumes (finished records keep their tier in their own requests).
exec bash "$(dirname "$0")/run_37_3.sh" --provider-ignore deepinfra/fp8/priority "$@"
