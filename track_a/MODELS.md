# Models, versions and generation settings (Track A, team Cookie)

Every value in both files is an answer of a session of one of the first two models below, or a per-question combination
of the two, possibly times a deterministic factor computed without a model, except 12 lab values that our code measured
on a scene record at the question's own prior scale. The values that are not plain model answers (from leaderboard
probes, a review of individual answers, our code's measurement, the paper's table or the validation catalog) are
listed in `STATEMENT.md`. No value is an answer of the last two models: Claude Sonnet chose rows to be asked again, and
answers of Claude Sonnet and OpenAI GPT-6 Astra to the same question were among the earlier answers that some
per-question rechecks read in their context.

| model | how it was called | role | sessions |
|---|---|---|---|
| `claude-opus-5-5` (Anthropic) | Claude Code CLI, headless `claude -p` (2.1.302 to 2.1.308; 2.1.310 for the rechecks) | scene records, per-question answers, re-asks, per-question rechecks (Series 43) | 4,173: 523 scene records, 3,012 answers, 413 re-asks, 225 rechecks |
| `deepseek/deepseek-v4.1-flash-1017` (open weights `deepseek-ai/DeepSeek-V4.1-Flash-1017`, MIT) with `facebook/sam3` tools | DeepSeek Harness 0.2.1 through OpenRouter, pinned to DeepInfra fp8 | the per-question median that is combined with the Opus answer (`METHOD.md` §5) | 8,275 runs, those finished on 2026-10-24 (records in our Track B package) |
| `claude-sonnet-5-5` (Anthropic) | Claude Code CLI 2.1.306 | plausibility screen that picked 37 rows for a re-ask; one-question repeat answers (26_80) that 4 of the entry's 14 rechecks (5 of the alternative's 29) read in their context | the screen; 598 repeats of 299 3D questions |
| `gpt-6-astra` (OpenAI) | Codex CLI 0.163.0, headless `codex exec` (`scripts/s30_codex_perq.py`) | one-question answers (Series 30) that 5 of the entry's 14 rechecks (6 of the alternative's 29) read in their context | 21 test questions |

## Claude Code sessions

- Command: `claude -p --verbose --output-format stream-json --safe-mode --no-session-persistence --permission-mode
  dontAsk --max-turns N --model M --effort E` (`scripts/cc_agent_scene.py`, function `claude`).
- Tools: `Read, Write, Edit, Glob, Grep` and `Bash` restricted to the Python interpreter; `WebFetch, WebSearch, Task,
  Agent` disallowed. Each session runs in its own empty workspace (the video, the scene record, one `inputs.json`;
  for a recheck, the question's own context folder).
- Environment: `CLAUDE_CODE_SAFE_MODE=1`, no CLAUDE.md, no memory; two Claude subscription logins, no API key.
- Temperature and maximum output tokens are the CLI defaults: Claude Code exposes neither, and no script sets them.
  Reasoning is set by `--effort`; each session's usage is in its `run.json`.

| run (records in `results/`) | effort | max turns | timeout |
|---|---|---|---|
| 26_30 scene records, one per video (`s26_scene_full/videos/`) | medium (`--lean` prompt) | 120 | 90 min |
| 26_30 answers, one per question (`s26_scene_full/q/`) | high | 80 | 45 min |
| 26_59 real-scale re-asks (`s26_reask_1020/`) | high | 80 | 45 min |
| 27_3, 27_6, 27_9 re-asks (`s27_valfam/`, `s27_plaus_reask/`, `s27_gravity/`) | high | 150 | 45 min |
| Series 43 rechecks (`s43_rsi/ctx/<question>/round<k>/`) | high | 150 | 40-50 min |
| 26_80 Sonnet repeats, phase 2 only on the 26_30 scene records (`scripts/run_26_80_a.sh`, `_personal.sh`) | high | 80 | 45 min |

## Codex sessions (GPT-6 Astra)

- Command: `codex exec --json --ephemeral --skip-git-repo-check --ignore-user-config -s workspace-write -C <folder>
  -m gpt-6-astra -c model_reasoning_effort="high" -c approval_policy="never" -o last_message.txt -`
  (`scripts/s30_codex_perq.py`), one session per question, 40 minutes, through a ChatGPT Plus subscription login.
- Each session's folder holds the video, an `inputs.json` with that one question and the frame viewer; no scene
  record, no other question, no network (workspace-write sandbox), the user's Codex configuration ignored. The prompt is
  the Track A answering prompt without the scene-record lines. No script sets a temperature or an output limit (CLI
  defaults).

## DeepSeek sessions

As in our Track B package (`MODELS.md` there): reasoning effort `medium`, temperature 0.3, `max_tokens` 16,384 a
request, at most 60 calls, 200,000 output tokens, 30 images, 40 minutes and $0.30 a session; OpenRouter with
`provider.only` DeepInfra fp8; SAM 3 `segment` / `track` from our GH200 server (`transformers` 5.14.1).

## Where to check

Each Claude session's model and CLI version are in the init line of its stream (kept on our side, about 16 GB) and its
usage in `run.json`; the DeepSeek run records are in the Track B package. The Sonnet and GPT-6 Astra answers a
recheck read are listed in its `CONTEXT.md`, with their notes in `results/s43_rsi/ctx/<question>/C<k>/notes.md`.
