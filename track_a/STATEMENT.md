# Statement (Track A, team Cookie)

## Confirmation for the entry, submission `9de2b974-6be8-4c1a-938d-c9acc93ccc47`, with one exception

Apart from the rows listed under "Exception", every prediction in this submission was produced independently from its
own item's inputs, as stated in the rules clarification of October 15. Each value comes from sessions that were given
only the video, that question's text, its own prior, depth_info and question_fps, plus a scene record of the same video
made by a session that saw no question (on 12 lab rows, from our code's measurement on that scene record at the scale
of the question's own prior; see below). No such session held more than one question, and no other question's prior,
answer or label entered a session. Answers of different sessions of the same question (Claude Opus and the open
DeepSeek model, `METHOD.md` §5) are combined per question; a per-question recheck session (§6) read only earlier
answers and notes of the same question, from sessions that each held only that question (Claude Opus and DeepSeek, on
some rows also Claude Sonnet and OpenAI GPT-6 Astra; `MODELS.md`). Deterministic factors are the same for every
question of a population; the factors and conventions that were fitted or read on labelled rows or on the leaderboard,
and the rows chosen for a re-ask or rebuilt because of what other answers of the same clip showed, are listed under
"Choices we disclose". `answers/leaf_rows.csv` names the per-question record behind every value of the answer lines
the file is built from.

## Exception in the entry

We found this while preparing this package. `answers/leaf_rows.csv` marks each row by class.

**The 277 questions on the clips of the 24 validation scene families.** We treated them as unscored, because we
understood the scored split to leave out the questions on the validation videos and their variants, so to save tokens
we answered only 30 of them again, per question. The other 247 keep the values of our earlier line
`results/fulltest_s26_ccagent_full/` (27 of them then combined with the DeepSeek median of the same question; class
`per_video_186`); on these clips that line carries values from our submissions of 2026-10-17 and before, which were not
produced per question. A read on 2026-10-21 with these rows blank showed that 20 of the 277 are scored; we could not
tell which. **For up to 20 scored rows the per-question confirmation does not hold.**

## Choices we disclose

- Population-level choices were kept after aggregate leaderboard reads of whole categories: the weights and
  populations of the combination with DeepSeek, the lab model per population, the lab constants (lab motion x1.215 /
  x1.19, 359 rows; lab sizes x1.03, 115 rows) and (alternative only) the categories that take RSI answers.
- 17 values follow a convention or a rescaling chosen on single-row leaderboard probes: q244, q1020 and q1023 take the
  horizontal extent of an upright object as its "length" (class `board_probe`), and 14 rows on two self-filmed clips
  (internet_0045, internet_0069) take the physical-scale rescaling of `METHOD.md` §4.
- q879: after a review flagged the row, Claude Code redid the arithmetic of the agent's own measurement from that
  question's notes (50.3 px/frame x 24 fps x 0.004722 m/px = 5.70 m/s, where it had written 57.0), and the user
  approved the result (class `human_check`).
- The lateral lab factor x1.5 was fitted on labelled validation rows; validation labels were also used in development.
- 37 rows were picked for a re-ask by a text-only plausibility screen (Claude Sonnet) that judged each question on its
  own line, several unrelated questions to a request; the re-ask answers came from per-question sessions.
- Two choices of which rows to redo compared answers of different questions of one clip; every value still comes from
  its own question's inputs. (a) internet_0065's displacement answers (about 15 m over 0.1 s) disagreed with its speed
  answers (about 2.7 m/s), which showed that the gravity prior of this clip and of internet_0066 falls on a ball that
  only rolls; the 18 questions of the two clips were asked again, each alone (26_59, `scripts/s26_reask_prep.py`,
  `DEGENERATE`), and 14 of the re-asked answers differ from the first ones. (b) On captured_0034b and its renders
  bs / bx the depth readings contradict the question's own 6.7 cm size prior by about 2.4x (they repeat captured_0034a's
  to the fourth digit), which we noticed because the clip's sessions split between the two scales; its 12 S3 values are
  our code's measurement on the question-blind scene record's track at the scale of the question's own prior, times
  s = 1.5, not a model's answer (`scripts/s31_lablat.py`, `prior_scale_0034b`; class `code_measurement`).
- Two small tables were transcribed by hand into the code: the pixel sizes and motions of standard objects on 8
  self-filmed internet clips, read from the question-blind scene records, for the physical-scale rule
  (`scripts/build_s26_physb_a.py`, `ANCHORS` and `WEAK`), and the event times of 11 lab rows whose question names an
  event instead of a time, copied from each row's own session notes (`scripts/s31_lablat.py`, `EVENT_T`).
- The recheck contexts hold every earlier one-question answer to the question (`results/s43_rsi/ctx/`): besides Claude
  Opus and DeepSeek, Claude Sonnet repeat runs (4 of the entry's 14 rechecked rows, 5 of the alternative's 29) and
  OpenAI GPT-6 Astra through the Codex CLI (5 of the 14, 6 of the 29), each session holding only that question.
- The recheck sessions' prompt carries a short library of general lessons that earlier recheck sessions wrote
  (measurement procedures, no values; `results/s43_rsi/harness/`), the same for every question.
- During development some answering conventions in the prompts (real-scale checks, a character's rig origin, the time
  base, which side of an object is its length) were found by comparing our answers across questions and with facts
  stated in other questions' priors, and the 26_59 re-ask gate was checked against such facts in aggregate; they became
  prompt text or rules applied to every question alike, never an individual answer.
- A public competitor repository first suggested the physical-scale convention on self-filmed internet clips; our rule
  and its factors use only each question's own inputs.

## The alternative, submission `5978cdf6-3fcf-4594-8f1f-2d1867bd8f4b`: what it adds, and our question

It is built from the same answer lines and differs from the entry in 478 rows (451 of them in our scored set):

- **Validation catalog** (245 rows): a scored test question asking for a static size of an object that reappears from
  the validation split (same object, another clip of the same simulated scene or the same lab prop) takes that
  validation label (231) or prior (14) when our answer is already within a factor of 1.49 (clip in the same scene
  range), 1.13 (farther clip) or 1.28 (lab prop) (`scripts/s40_catalog_snap.py`).
- **The paper's prop table** (197 lab rows): the listed size of a prop named in appendix B of the QuantiPhy paper.
- **Seven more answers changed in the review of 2026-10-21** that also gave q879 (class `human_check`; the user flagged
  rows while watching the videos, Claude Code proposed each change from that question's own notes, and the user approved
  it): q248, q282 and q3051, one of the agent's own alternative readings or measurements; q618 and q1934, the agent's
  own horizontal reading of an upright object (read on the leaderboard as a probe of the length convention); q1668 (1.4
  m/s, a typical walking speed: no person is in the clip and the agent had substituted a boat's speed); q1670 (18 m, the
  agent's own alternative reading with the rock at the boat's depth, where it had answered 168 m). The docstring of
  `scripts/s43_strict_a.py`, written on 2026-10-26, calls these "a person chose among the agent's readings"; the review
  record says Claude Code proposed each change and the user approved it.
- 29 RSI answers instead of 14.

The first two read labels or priors of other benchmark items or the hand measurements the lab labels come from, and the
third rests on a review of individual answers, so we cannot give the confirmation for those rows. **If you consider
these steps allowed, please rank us on the alternative; otherwise on the entry.** The entry's exception and choices
apply to it as well.
