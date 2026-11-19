# Changes from our code packages of 28 October 2026

`track_a/` and `track_b/` are our two code packages of 28 October 2026, unpacked: `cookie_track_a.zip` (sha256
`24717bf49857d847d5f518a725b08c8ca28c3832897c16a753cb7b5d834973a4`) and `cookie_track_b.zip` (sha256
`ec4f6c7e13b938982b8ec2cd079e0002131b764c46b14de6b4acbcc3389a9d33`). They differ from those packages in these ways only.

1. **Local paths.** The absolute path of our working copy is cut to a path relative to the package root, and our home
   directory is written `~`. The launch scripts take the Python interpreter from `QP_PYTHON` (default `python3`).
   `track_a/scripts/cc_agent_run.py` takes it from `QP_PYTHON` or the running interpreter, and
   `track_b/scripts/dsh_coder.py` from `QP_SANDBOX_PY` or the running interpreter. `track_b/scripts/api_clients.py`
   reads API keys from the environment or from a `config.yaml` at the package root.
2. **Login names.** Our two Claude Code logins are called `a` and `b`: in the `--account` flag, in the `account` field
   of the run records, in the `account` column of `track_a/results/s26_scene_full/ledger.csv`, and in file and folder
   names (`_a`, `_b`). Comments say "login A" and "login B" where they described the plans. `track_a/LINES.json`
   carries the ledger's new sha256.
3. **Internal references.** Comments that pointed at our internal notes now say "our run rules", and the OpenRouter
   `HTTP-Referer` header names no account (`OPENROUTER_REFERER`, default `https://github.com`). The scripts' check for
   leaked paths no longer lists one word and one environment-variable prefix that are specific to our machines.
4. **Archive owners.** `track_a/session_code.tar.xz` is repacked with neutral owner names, and the files in it carry
   changes 1 and 2. `track_b/records.tar.xz` is unchanged.
5. **Added.** `README.md`, this file, `LICENSE` and `.gitignore` at the top level.

No answer, prompt or build step changed. `reproduce.sh` in each folder still rebuilds every submission file byte for
byte.
