# Context of question 1389 (organised record; every round adds to it)

## Question
- Text: What is the acceleration of the ball at time 1s in m/s^2?
- Its own prior: diameter of the ball = 0.21m
- Its own depth_info: t=0.5s distance_bowling_ball_camera = 9.391m
- question_fps: 24
- Video: simulation_0164.mp4 (simulation, S3MC)

## The answer currently submitted
0.338821 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 0.41 and an earlier DeepSeek median B = 0.28; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 0.41 | 1.210 |
| C2 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 2 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 0.41 | 1.210 |
| C3 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 3 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 0.36 | 1.063 |
| C4 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_3 S3 adjudication (DeepSeek differs 25 pct to 2x) | 0.41 | 1.210 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 0.3 | 0.885 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 0.26 | 0.767 |
| C7 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 0.2 | 0.590 |
| C8 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 0.43 | 1.269 |
| C9 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 0.25 | 0.738 |

DeepSeek median over its 5 runs: 0.26.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v1; files in context/round1/)
- Answer: 0.41 (switch, confidence high, follows C1)
- Where the answers part: position of the ball's vanishing point on its image path: lane/floor lines (x~5643) vs ball apparent-diameter trend or mis-fitted lane edges (x~5240-5380)
- Fault proven: low answers used a VP from motion-blur/off-axis-biased ball diameters or mis-fitted lane edges; 8 sub-pixel floor/lane lines (rms <=0.11 px) all meet within 1 px of (5643.5,208.4) and the ball path passes through it, while the low-answer VPs lie where lane lines are 25-35 px apart; the submitted 0.339 is a blend with those
- Closure on the prior: 1.6 pct

# Round addendum, q1389 (ball acceleration at t = 1 s)

## Established
- **Lane VP = (5643.5, 208.4) ±~5 px.** Eight independent straight edges were fitted with sub-pixel precision on frame 0 (lines.py, lines2.py; rms 0.07–0.11 px):
  - 3 cyan floor lines;
  - the lane far and near edges;
  - the 2 gutter-cap edges;
  - the far-lane edge.

  All eight pass within 1 px of this point.
- **The ball moves parallel to the lane.** Its image path, y = −0.0832x + 678.6, passes through the VP (y = 209.1 at that x), and the ball rolls at constant height.
- **Reconstruction:** 3D line toward the VP, anchored at depth_info (9.391 m at frame 12), f ≈ 3670 px. Over frames 6–37 (before the impact at 37–38) it gives:
  - a = −0.411 m/s² from the quadratic fit;
  - −0.408 from the cubic fit at 1 s;
  - −0.410 from the slope of the per-frame speeds;
  - v(1 s) = 3.58 m/s;
  - residuals of 3.2 mm.

  Across fit windows a ranges from −0.38 to −0.42. f from 3400 to 3950 gives −0.43 to −0.39.
- **Closure:** the diameter re-derived over frames 6–36 has a mean of 0.2066 m (−1.6 %; worst −3 % in the late frames).

## Ruled out
- **VPs taken from the ball-diameter trend** (≈5240–5380; C3, C5's second route, C7, C9). The diameters are biased by motion blur (62 vs 32 px/frame) and by off-axis stretch (2.9 % at frame 6 vs 0.8 % at frame 36). At those x values the lane lines are 25–35 px apart, so they are not a lane vanishing point.
- **C6's lane edges with the VP at y = 242.** Its slopes are off by about 0.0006 from the sub-pixel fits.
- **The blended 0.339.** It is not a measurement.

## Answer now
0.41 (switch, following C1, C2 and C4).

## Open
- Whether the ground-truth per-frame speed difference at frame 24 has physics jitter. This cannot be known from the video; the smooth value is 0.41.
- The lane surface comes out about 1.85 m wide (the scene's modelling). It does not affect a.

### Round 2 (harness v2; files in context/round2/)
- Answer: 0.415 (switch, confidence high, follows C1)
- Where the answers part: vanishing point of the ball's straight image path (lane lines x~5648 vs ball-diameter trend x~5300), with f fixed by ball size and depth
- Fault proven: low answers used a diameter-trend VP (~5300) that is 25-35 px off three floor lines meeting within 5 px at (5648,208) and off the zero-roll horizon crossing (5656); that VP gives a=0.31; submitted 0.339 is a blend including them
- Closure on the prior: 1.0 pct

# Round 2 addendum, q1389

## Verified
- **Round 1's switch to 0.41 is confirmed.** It was reproduced with independent code (vp_mine.py, recon_mine.py).
- **Lane VP = (5648, 208) ± 3 px.** Three cyan floor lines were fitted at sub-pixel precision; they meet within 5 px.
- **Second route to the ball VP.** The camera roll is about 0: screen and pit edges near the centre column have a tilt of about 0. So the horizon is the row y = 208, and the ball path y = −0.0832x + 678.6 crosses it at x = 5656.
- **Line model anchored at 9.391 m at frame 12, frames 6–37:**
  - a = −0.412 at f = 3670;
  - a = −0.419 at f = 3573 (self-consistent with the late clean diameters, off-axis factor applied);
  - a cubic fit evaluated at 1 s gives −0.416;
  - v(1 s) = 3.6 m/s.
- **The answer is now 0.415.**

## New point settled
- **The vertical edges disagree with f, but this does not move the answer.** The "vertical" screen and pit edges tilt by up to 1.8°, and the pit top edge has slope 0.085. Together they imply f ≈ 2450 if the principal point is at the image centre. That is ruled out:
  - it makes the ball 0.30 m (prior 0.21, exact);
  - it makes the pins about 0.5 m tall.
- **A lens-shift explanation leaves a unchanged.** With the principal point at (950, 947), at f ≈ 3550, a = −0.422. Either way a is 0.41–0.42.
- **The diameter-trend VP is ruled out.** Taking the VP at 5300 gives a = −0.31, the low answers' value. That VP is off the lane lines and off the horizon crossing.

## Open
- Physics jitter in the ground-truth per-frame speed difference at frame 24 cannot be known from the video.
