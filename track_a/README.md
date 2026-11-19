# Team Cookie: QuantiPhy Challenge 2026, Track A code

This package rebuilds our Track A entry and the alternative we ask you to consider (`SUBMISSION.md`) from the answer
lines they were built from, with our build scripts exactly as they ran, and traces every value of those lines to the
per-question session record it comes from. It also contains the code that produced the records. Model calls are not
deterministic, so running the agents again gives answers that differ slightly from the recorded ones; the recorded
answers are the exact inputs of the rebuild.

- `SUBMISSION.md`: the two submissions, their ids, timestamps and sha256.
- `METHOD.md`: the method on one page.
- `MODELS.md`: every model, with versions and generation settings.
- `STATEMENT.md`: our per-question confirmation for the entry, its exception, and what the alternative adds.

## Rebuild and trace (under a minute)

```sh
python3.13 -m venv .venv && . .venv/bin/activate
pip install -r requirements-rebuild.txt
./reproduce.sh
```

1. `build/replay.py` checks the answer lines against `LINES.json`, runs the build scripts in `scripts/` in the order
   below and prints, for each submission, the sha256 of the rebuilt file and `"byte_identical": true` when it equals
   the uploaded file's (and the same for every intermediate file).
   - `build_s39_fuse.py`, then `build_s39_stack.py` with `results/fulltest_s39_f2/spec.json` and
     `results/fulltest_s39_f3/spec.json`: the per-question combination of the Opus line E2 (and U1 on the S3 lab motion
     rows) with the DeepSeek medians B9lat / B9const;
   - `s43_strict_a.py`: **the entry**, `results/fulltest_s43_strict_rsi/track_a_s43_strict_rsi.csv`;
   - `build_s40_stack.py` with `results/fulltest_s40_c1/spec.json`, then `build/overlay_rsi.py`: **the alternative**,
     `results/fulltest_s43_gray_rsi/track_a_s43_gray_rsi.csv`.
2. `build/check_leaves.py` re-reads, for every value of the Opus answer lines (E2, its pre-table values, U1, the 39_4
   re-answers, the #200 line's human-check rows, the RSI answers), the raw answer from the per-question record that
   `answers/leaf_rows.csv` names, applies the listed rule (x1, a lab constant, the physical-scale factor, the lab
   direction factor, a rounding) and compares; it lists the rows no per-question record explains, by class.

The DeepSeek lines (`results/fulltest_s37_b9lat/`, `results/fulltest_s37_b9const/`) are rebuilt from their 8,275 run
records by our Track B package, whose replay checks the same sha256 as `LINES.json` here.

## Layout

| path | content |
|---|---|
| `results/fulltest_s27_e2/` | E2, the Opus line: one per-question answer per row, with the Series 27 re-asks and the deterministic factors; `combine_rows.csv` holds each re-ask and prop-table row's value before and after |
| `results/fulltest_s30_u1/` | U1: E2 with the lab direction factor (and other changes not used here) |
| `results/fulltest_s37_b9lat/`, `results/fulltest_s37_b9const/` | the DeepSeek medians per question, two lab models; `aggregate.csv` lists each question's runs |
| `results/s39_2dmotion/collected.csv` | 39_4 re-answers (they enter the intermediate F3 only) |
| `results/fulltest_s26_reask_full/` | the #200 line (the human-check rows go back to it) |
| `results/fulltest_s43_strict_rsi/apply_r123.csv`, `results/fulltest_s43_gray_rsi/apply_final.csv` | the RSI answers each file takes |
| `results/fulltest_s26_ccagent_full/` | our earlier per-video line (`STATEMENT.md`, the exception) |
| `results/<run>/q/<video>__<id>/` | per-question session records: `inputs.json` (exactly what the session was given), `answers.json`, `notes.md` (how it measured), `run.json` (model usage, timing) |
| `results/s43_rsi/ctx/<video>__<id>/` | a recheck's context (the question's own earlier answers and notes) and each round's record |
| `results/s26_scene_full/videos/<video>/scene/` | the question-blind scene records (object tracks for the lab videos) |
| `results/s26_scene_full/ledger.csv` | the 26_30 run ledger: one line per scored question (first answer, stated confidence) |
| `session_code.tar.xz` | each session's own measurement scripts (`tar -xJf session_code.tar.xz`) |
| `answers/leaf_rows.csv`, `answers/s31_factors.csv` | the provenance table and the lab direction factors |
| `data/` | the test split's rows (`PaulineLi/QuantiPhy`, revision of 2026-10-21) and the validation split |
| `scripts/` | the build scripts above and the pipeline that made the records, as they ran |

## The pipeline that made the records (`scripts/`)

| step | code | launchers |
|---|---|---|
| scene record per video, then one session per question (Claude Code) | `cc_agent_scene.py` (prompts `SCENE_PROMPT`, `LEAN_SCENE_PROMPT`, `ANSWER_PROMPT`; shared conventions in `cc_agent_run.py`); frame viewer `framekit2.py` | `run_26_30_a.sh`, `run_26_30_b.sh` |
| re-asks of chosen questions | `cc_scene_ids.py`; rows chosen by `s26_reask_prep.py`, `s27_plaus_screen.py` | `run_26_59.sh`, `run_27_3.sh`, `run_27_6.sh`, `run_27_9.sh` |
| the Opus line and its factors | `build_s26_scene.py`, `build_s26_physb_a.py`, `build_s26_labcal.py`, `build_s26_reask.py`, `build_s27_combine.py`, `s31_lablat.py`, `s32_d2lab.py`, `s30_reset_plan.py` | |
| the DeepSeek medians | in our Track B package | |
| per-question rechecks (Series 43) | `s43_rsi.py` (harness versions and lessons in `results/s43_rsi/harness/`, prompts `results/s43_rsi/prompt_round*.txt`, rule `results/s43_rsi/apply_rule.md`) | `run_43_1.sh` to `run_43_4.sh` |
| other models' one-question answers that some recheck contexts hold (`MODELS.md`) | Claude Sonnet repeats: `cc_agent_scene.py`, rows by `s26_repeat_prep.py`; OpenAI GPT-6 Astra: `s30_codex_perq.py`; Opus adjudications: `s30_dossier.py` | `run_26_80_a.sh`, `run_26_80_b.sh` |

These scripts ran on our machines (their local paths are relative here) and two Claude Code logins (`--account
a|b` sets `CLAUDE_CONFIG_DIR`); to answer one test video with the same prompts:

```sh
python scripts/cc_agent_scene.py --account a --guard <guard.json> --out results/rerun \
  --events simulation_0007 --lean --effort medium --max-turns 120 --max-turns-p2 80
```

with the QuantiPhy test videos from Hugging Face where `results/s26_test_prepared` points.

## Hardware and runtime

- **Rebuild and trace:** any machine with Python 3.13; under a minute.
- **Claude sessions** ran from a Mac (Apple M6, 24 GB, macOS 27.0.1, Python 3.13.16); inference ran on Anthropic's
  servers. The DeepSeek sessions and the SAM 3 server ran on Lambda GH200 boxes.
- **26_30:** 523 scene records (82.8 hours of session time, a median of 277 s a video) and 3,012 answer sessions (a
  median of 93 s a question, p90 396 s), about two days with parallel sessions on two logins. 413 re-asks; 225
  recheck sessions (a median of 266 s).

## Data versions

The 26_30 sessions took their questions from the test split as we downloaded it before 2026-09-08; the dataset
repository later corrected the wording or metadata of 172 scored rows (the videos are unchanged). Each record's
`inputs.json` shows exactly what its session was given. Re-asks from 2026-10-21 on read the revision of 2026-10-21.

## Not included (available on request)

The raw model transcripts (Claude Code stream-json, about 16 GB), the frame images the sessions rendered, and our full
git history.
