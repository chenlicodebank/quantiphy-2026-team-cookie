#!/bin/sh
# Rebuild our Track A uploads (#224, the entry, and #225, the alternative) from the answer lines, compare each file's
# sha256 with the upload, then trace every value of the answer lines to its per-question record.
# Python 3.13 with requirements-rebuild.txt; under a minute.
set -e
cd "$(dirname "$0")"
python3 build/replay.py
python3 build/check_leaves.py
