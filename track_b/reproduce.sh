#!/bin/sh
# Rebuild our Track B uploads (#221, the entry, and #222, the alternative) from the per-question DeepSeek run records
# and compare each file's sha256 with the upload. Python 3.13 with requirements-rebuild.txt; about 2 minutes.
set -e
cd "$(dirname "$0")"
python3 build/replay.py
