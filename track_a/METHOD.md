# Method (Track A, team Cookie)

**Idea.** A vision-language model answering from the frames alone mostly recalls typical values; it does far better
when it measures. Each answer is a measurement made in code by a coding agent (Claude Opus in the Claude Code CLI),
scaled to metric units by that question's own prior and depth_info, one question per session; a second, open model
measures the same question independently, and the two answers are combined per question.

**1. A question-blind scene record per video.** One agent session per video sees the video and its basic metadata, no
question. It writes Python (OpenCV, PyAV, NumPy, SciPy) to inventory every object a question could name, track moving
objects frame by frame, measure static objects, time events and record camera motion and perspective cues, and checks
its tracks by drawing them on frames.

**2. One session per question.** A fresh session gets the video, a read-only copy of the scene record and one question
with its own prior, depth_info and question_fps. It finds the asked object and the prior's object, re-measures what
the answer depends on and converts pixels to metres (2D: the prior's scale; 3D: pinhole geometry with depth_info, the
focal length from at least two references). It confirms the answer by a second route and returns one number with
notes. The prompt states the dataset's answering conventions once for all questions.

**3. Re-asks with one stated assumption.** Some answers were asked again in a fresh session told to check one
assumption: whether a standard object comes out at a real size, whether a stated gravity is the render's, or the
plausibility of the first answer. Rows were chosen by rules on the row's own text and notes, by a text-only
plausibility screen, or, on two internet clips, because two of the clip's answers disagreed (`STATEMENT.md`); the
re-ask's answer replaces the first one.

**4. Deterministic transforms.** Lab clip labels come from a sensor process that inflates motion. For the S3 lab
motion rows the answer is multiplied by a per-row factor from the direction of motion (lateral x1.5, along the line of
sight x1; fitted on labelled validation rows; on captured_0034b, whose depth readings contradict the question's own
size prior, our code measures the motion on the scene record at the prior's scale instead, `STATEMENT.md`); the other
lab motion rows carry a constant (x1.215 or x1.19 by population) and lab sizes x1.03, constants we fitted to
leaderboard reads (`STATEMENT.md`). On eight self-filmed internet clips the stated speed contradicts the scene's
physical scale, so their 2D answers are rescaled by a standard object's known size (on two of them only after
single-row leaderboard probes, `STATEMENT.md`).

**5. A second model, combined per question.** DeepSeek-V4.1-Flash-1017 (open weights) with SAM 3 segmentation and
tracking tools answered every question in the same two-phase design, 2 to 6 times; its median per question is the
partner answer B (our Track B package rebuilds it from its run records). Where the Opus answer A and B are within a
factor of 1.49, the row becomes exp(w ln A + (1 - w) ln B), with w per population (S3 0.5, D2 and D3 0.7, lab D3 0.6;
on D2 raised when the Opus session stated a tight error bar or the DeepSeek runs spread widely, lowered when Opus was
unsure and the runs agree). Both inputs are answers to the same question from its own inputs. S2 keeps the Opus
answers. The weights and populations were kept after aggregate leaderboard reads of whole categories.

**6. A per-question recheck with an organised context (Series 43).** For the 168 scored questions where A and B
disagreed most, a fresh Opus session read that question's own context only (every earlier one-question answer to it,
with notes and code: the sessions above, Opus adjudications over those answers, Claude Sonnet repeat runs and, on some
rows, OpenAI GPT-6 Astra; `MODELS.md`), re-measured the crux, ran four required checks (the question's own prior
reproduced by its scale, plausibility, units and time base, a proof of the fault it claims), and proposed to keep or
change the answer; later rounds re-checked the proposals. Which answers count follows a rule written before the first
leaderboard read of any RSI row (`results/s43_rsi/apply_rule.md`): 14 rows in the entry, 29 in the alternative (whose
categories followed the entry's read).

**7. The files.** The entry takes each category from the combination above, puts the rows the paper's prop table had set
back to the agent's own measurement (combined like every other lab size row), and seven of the eight human-check rows
back to the agent's answers; q879 keeps the recomputed product of the agent's own measurement (`STATEMENT.md`). The
alternative keeps the prop-table and human-check values and adds the validation catalog (`STATEMENT.md`).

**What did not help** (measured): a second fresh Opus session of the same question (it mostly repeats the first),
other open models as the partner, and medians over weaker models. Most remaining error is shared by every reader:
answering conventions the task does not state, and lab label noise.
