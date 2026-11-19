# Statement (Track B, team Cookie)

## Confirmation for the entry, submission `d1ac996d-62e0-4988-b79a-571c28ec92af`

We confirm that every prediction in this submission was produced independently from its own item's inputs, as
stated in the rules clarification of October 15. Each value comes from DeepSeek-V4.1-Flash-1017 sessions that were
given only the video, that question's text, its own prior, depth_info and question_fps, and a scene record of the same
video made by a session that saw no question. No session held more than one question, and no other question's prior,
answer or label entered an answer. Several sessions of the same question are combined by their median. The
deterministic factors are either constants that are the same for every question, fitted on the labelled validation
rows, or computed from the video's own SAM 3 object tracks and the row's own depth_info. Every model and tool used at
inference time has public weights (`MODELS.md`), and no closed model's output enters any row.

## What we disclose about the entry

1. **Constants fitted on validation labels.** The lab motion factors k = 1.25 and s = 1.5 were fitted on the 15
   labelled lab motion rows of the validation split.
2. **One model choice informed by the leaderboard.** Whether lab motion takes the direction model or the constant was
   chosen per category after one aggregate leaderboard read that compared the two on our Track A answers (our Track A
   upload of 2026-10-24 21:26 UTC): the direction model for D2 and S3, the constant for D3. No row was set from
   leaderboard feedback.
3. **Rules fixed without labels.** The repeat policy (which questions get a third to fifth run) was fixed from a
   simulation on labelled validation questions before any test score was read; the physical-scale rule was written and
   revised on the sessions' own answers and notes, without any test label or score.
4. **Closed models in development (the FAQ asks us to disclose these).** On the validation split: `gpt-5.1` and
   `gemini-3.1-pro-preview` (2026-09-14) and a Claude teacher pilot on six validation videos (2026-10-12/13). Our Track A
   pipeline (Claude Opus in Claude Code) answered the test questions for Track A; during Track B development we
   compared our open agent's answers with those answers on a handful of test videos and on aggregate agreement, to find
   where our code measured wrong. Every fix became a code rule or a question-agnostic sentence of the prompt applied to
   every question alike (the 2D method card in `scripts/dsh_scene.py`, `JUDGMENT_CARD`, is one); no Track A value, note,
   per-video setting or per-row choice enters a Track B row. OpenAI's Sol and our Claude Code agent also answered
   validation and test videos for Track A (2026-10-15/16); those answers were kept out of every Track B file.
5. **Hosted inference.** The public DeepSeek weights were served by DeepInfra (fp8) through OpenRouter, not on our own
   hardware; SAM 3 ran on our GPU box.

## The alternative, submission `bb9d428e-340a-47e0-b868-16e6797965b4`: what it adds, and our question

It differs from the entry in 717 rows. Its S3 rows are the medians of the runs that had finished on 2026-10-24 (the
same builder; `results/b9_runs.csv`), and 499 rows are changed by two lookups:

- **Validation catalog.** A catalog of "dimension of object = value" statements from the validation split (labels and
  priors). A scored test question asking for a static size of an object that reappears from the validation split
  (same object name, another clip of the same simulated scene or the same lab prop) takes the catalog value when our
  answer is already within a factor of 1.49 (clip in the same scene range), 1.13 (farther clip) or 1.28 (lab prop) of
  it (`scripts/s40_catalog_snap.py`).
- **The paper's prop table.** A lab question about a prop listed in appendix B of the QuantiPhy paper takes the listed
  size; where the name allows several listed values, the nearest one within a factor of 1.6 (`scripts/lab_props.py`).

Neither step reads another test question's prior, answer or label, and both are the same for every question. But the
first copies labels and priors of validation questions, which are questions of the same benchmark, and the second uses
the hand measurements the lab labels come from. We could not give the confirmation above for those rows without this
caveat, so we name the entry. **If you consider both steps allowed, please rank us on the alternative; otherwise on the
entry.** Everything else in the alternative is as disclosed for the entry.
