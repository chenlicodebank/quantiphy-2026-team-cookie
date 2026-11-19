# Method (Track B, team Cookie)

**Idea.** A vision-language model answering from the frames alone mostly recalls typical values; it does far better
when it measures. Every answer is a measurement made in code by an open-weight coding agent, DeepSeek-V4.1-Flash-1017
in the DeepSeek Harness, with SAM 3 segmentation and tracking as tools, one question per session, and the median of
several such sessions of the same question.

**1. A question-blind scene record per video.** One session per video sees the video and its basic metadata, no
question. It writes Python (OpenCV, NumPy, SciPy) and calls SAM 3 to inventory the objects a question could name, track
the moving ones, measure static ones, time events and note camera motion and perspective cues (`scene.json`). 568
records.

**2. One session per question.** A fresh session gets the video, a read-only copy of the scene record and one question
with its own prior, depth_info and question_fps (its `inputs` field in the run records). It finds the asked object and
the prior's object, measures in code, converts pixels to metres (2D: the prior's scale; 3D: pinhole geometry with
depth_info) and returns one number. The answering prompt states the dataset's conventions once for all questions; on
2D questions it adds a short method card (masks, extents, motion fits, scale checks; `scripts/dsh_scene.py`,
`JUDGMENT_CARD`), the same text for every question.

**3. Repeated runs, median (Series 37).** Every question was answered at least twice in the same configuration; a third
run where the first two differ by more than 0.05 in |ln|, a fourth and fifth where three runs spread more than 0.3 in
ln(max/min). The policy was fixed before any test read, from a simulation on labelled validation questions. The row is the median of the
question's runs: 8,800 sessions over the 3,289 questions, 2 to 6 each.

**4. Physical-scale check on internet clips.** One more session per internet question (420) measures a standard
object in view (an adult, a ball) under the question's own prior and records the implied scale k. When the session
calls the clip self-filmed, the prior is a speed or acceleration, k is beyond 15 percent and within 1/3 to 3, the
question's runs are brought to the physical scale (113 rows; `scripts/s37_final_b.py`, function `physical`).

**5. Lab factors.** Lab labels come from a sensor process that inflates motion. Lab motion answers are multiplied by
k = 1.25, or by a per-row factor from the direction of motion (lateral x1.5, along the line of sight x1), computed from
SAM 3 tracks of the video and the row's own depth_info. Both constants are fitted on the 15 labelled validation lab
motion rows. The entry takes the direction model for the lab rows of D2 and S3 and k for those of D3; that split followed one leaderboard read
of the two models on our Track A answers (disclosed in `STATEMENT.md`).

**6. The alternative (#222) only.** Two lookups on top: a test answer about an object that reappears from the
validation split takes that validation label or prior when the answer is already close to it; a lab size answer
about a prop listed in the QuantiPhy paper's appendix B takes the listed size.

**What did not help** (measured on labelled rows): other open models as the agent or as a vote (DeepSeek-V4-Flash-Vision-Exp,
GLM-5.3-Flash, MiMo-V2.6, MiniMax-M3.1 and Qwen3.8-Flash were below DeepSeek-1017 or level at several times the cost,
and missed the same rows), temperature
1.0, high reasoning effort instead of more runs, and a 3D depth tool. Most of the remaining error is per-question bias
that every open model shares.
