# Team Cookie: QuantiPhy Challenge 2026, Track B code

This package rebuilds our Track B entry and the alternative we ask you to consider (`SUBMISSION.md`) from the
per-question model outputs, with our build scripts exactly as they ran, and contains the code that produced those
outputs. Model calls are not deterministic, so running the agent again gives answers that differ slightly from the
recorded ones; the recorded answers are the exact inputs of the rebuild.

- `SUBMISSION.md`: the two submissions, their ids, timestamps and sha256.
- `METHOD.md`: the method on one page.
- `MODELS.md`: the models, their public weights and the generation settings.
- `STATEMENT.md`: our per-question confirmation for the entry, what we disclose, and what the alternative adds.

## Rebuild both files (about 2 minutes)

```sh
python3.13 -m venv .venv && . .venv/bin/activate
pip install -r requirements-rebuild.txt
./reproduce.sh
```

`build/replay.py` unpacks `records.tar.xz`, runs the build scripts in `scripts/` in the order below and prints, for each
submission, the sha256 of the rebuilt file and `"byte_identical": true` when it equals the uploaded file's.

1. `s37_final_b.py` collects every run of each question, takes the median (and applies the physical-scale rule), then
   runs `s33_final_b.py`, which applies the lab factors: once with the direction model (`fulltest_s37_b10lat`), once
   with the constant (`fulltest_s37_b10const`).
2. `s37_mix.py` takes D3 from the constant build and the other categories from the direction build: **the entry**,
   `results/fulltest_s37_b10mix/track_b_s37_b10mix.csv`.
3. For the alternative, the same `s37_final_b.py` build on the runs listed in `results/b9_runs.csv` (those finished on
   2026-10-24, hard-linked into `results/b9_runs/`), then `build_s40_stack.py` with `results/fulltest_s43_k3/spec.json`:
   `results/fulltest_s43_k3/track_b_s43_k3.csv`.

## Layout

| path | content |
|---|---|
| `records.tar.xz` | `results/s37_test_repeats/q/<video>__<id>/r<k>.json`: every DeepSeek session of every test question (8,380), and `results/s37_physcheck/q/...`: the 420 physical-scale sessions. Each record is compacted to what the session was given (`inputs`), its `notes.md`, its final answer (`final`, `final_text`), the model, provider pin, providers that answered, finish reason, cost and wall time. Also the question-blind scene record of every video (`results/*/videos/<video>/scene/scene.json`). |
| `results/fulltest_s33_l5lat/`, `results/fulltest_s33_l5const/` | the files `s33_final_b.py` starts from. They give the template's row order and columns; every row's value is then set from the DeepSeek medians (where the new value equals the old one, the old string is kept). |
| `results/s33_lablat_open/factors.csv` | the per-row lab direction factors, from SAM 3 tracks and the row's own depth_info |
| `results/fulltest_s18_tracks24/`, `results/s33_sam3_tracks/` | SAM 3 tracks of the lab videos (question-agnostic) |
| `results/s26_scene_full/ledger.csv` | the 3,012 test rows we treated as scored (the rows outside the validation videos): id, video, source, category, question |
| `results/b9_runs.csv` | the runs behind the alternative's S3 rows |
| `results/fulltest_s43_k3/spec.json` | the alternative's build spec (per-category base files, catalog snap, prop table) |
| `data/test/test_dataset_current_20261021.json` | the test split's rows (`PaulineLi/QuantiPhy`, revision of 2026-10-21), which the sessions and builds read |
| `data/validation/validation_dataset.csv` | the validation split (`PaulineLi/QuantiPhy-validation`) |
| `scripts/` | the build scripts above and the pipeline that made the records, as they ran |
| `build/replay.py` | the rebuild |

## The pipeline that made the records (`scripts/`)

| step | code | launchers |
|---|---|---|
| scene record per video, then one session per question | `dsh_scene.py` (prompts, the 2D method card `JUDGMENT_CARD`), `dsh_scene_tools.mjs` (harness tools), `dsh_coder.py`, `api_clients.py` (OpenRouter provider pin) | `run_29_5.sh` (first run of every question), `run_37_1.sh`, `run_37_1b.sh` (second run) |
| further runs where runs disagree | `s35_repeat_ids.py`, `s37_next_ids.py` | `run_37_2.sh`, `run_37_2b.sh`, `run_37_5.sh`, `run_37_10.sh` to `run_37_14.sh` |
| physical-scale sessions (internet questions) | `s37_scale_check.py` | `run_37_3.sh`, `run_37_3b.sh` |
| SAM 3 server | `sam3_server.py` | |
| audit of each build before upload | `s37_audit.py` | |

These scripts assume our machines: a Lambda GH200 box with the DeepSeek Harness runtime and the SAM 3 server, and an
OpenRouter key in an environment file there. To answer one test question the same way, run `dsh_scene.py` with the
flags in `run_37_1.sh` (`--model deepseek/deepseek-v4.1-flash-1017 --provider deepinfra/fp8 --reasoning medium
--split test --qsource current`, plus `--judgment-card` for S2 / D2) on the test videos from Hugging Face.

## Hardware and runtime

- **Rebuild:** any machine with Python 3.13; about 2 minutes, most of it unpacking the records.
- **Sessions:** the harness and the SAM 3 server ran on Lambda GH200 boxes; the model ran on DeepInfra through
  OpenRouter.
- **Volume:** 568 scene records, 8,800 per-question sessions (a median of 914 s each, p90 2,175 s; about 2,690
  session-hours, run in parallel between 2026-10-22 and 2026-10-25).
- **Cost:** $262 of OpenRouter credit for the 8,800 sessions (the sum of the records' `cost_usd`).

## Not included (available on request)

The raw event streams (about 12 GB), the code each session wrote, the frame images, the scripts and tracks of the
scene records, and our git history.
