# Context of question 1522 (organised record; every round adds to it)

## Question
- Text: What is the speed of the car at time 0.5s in m/s?
- Its own prior: diameter of the tire = 0.764m
- Its own depth_info: t=0s, distance_yellowCarRightFrontTire_camera = 14.244m
- question_fps: 24
- Video: simulation_0149.mp4 (simulation, S3MC)

## The answer currently submitted
7.2336 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 6.5 and an earlier DeepSeek median B = 8.05; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 6.5 | 0.899 |
| C2 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 7.1 | 0.982 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 9.0 | 1.244 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 8.2 | 1.134 |

DeepSeek median over its 3 runs: 8.2.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 6.8 (switch, confidence medium, follows C1)
- Where the answers part: how the frame-12 derivative of the near-front-wheel track (rim-size depth + depth_info) is taken: local fit (C1/C2, 6.5-7.1) vs a constant-velocity straight-line fit over an accelerating window (C4 8.2) or a value chosen above its own fits (C3 9.0); f secondary
- Fault proven: the DeepSeek half of the blend rests on C4's constant-rate 1/h fit over frames 8-31 (+15% depth rate at f12 on the same data) and on C3 choosing 9.0 above its own 7.5-8.5 frame-12 fits; local cubic fits with VP-calibrated f=2353 give 6.75-6.84
- Closure on the prior: 1.6 pct

# Round 1 addendum – Q1522 (speed of the car at t = 0.5 s)

Proposed: **switch to 6.8 m/s** (from submitted 7.2336), following C1's method with refinements. Confidence: medium.

## Established (with the measurement)
- The asked wheel/depth object is the near-side front wheel (the car's right-front), seen at image left at f0. This was checked on zoomed frames.
- Focal length f = 2353 px from two orthogonal ceiling-grid vanishing points in frame 49 ((4021,824) and (-875,820); bootstrap
  2322-2379). This agrees with the tyre-size route (2346-2380). It rules out C4's 1924 and C3's 1500-2000.
- Rim vertical extent (half-max): f0 87.21, f11 97.88, f12 99.68 px. f9 is an outlier. Rim heights need a cubic fit
  (a quadratic leaves systematic residuals).
- Pinhole reconstruction calibrated to |P0| = 14.244 m: speed at f12 = 6.75 m/s (windows 0-24/2-22/0-20, cubic+). Components dX 3.99,
  dZ -5.44. Speed vs f is weak: 7.3 at f=1700, 6.66 at f=2500.
- Second depth route: affine ECC of the yellow body (template f12) gives scale 11->12 = 1.0184, the same as the rim. Its log-rate over
  11-13 is 0.0200 vs the rim's 0.0197 -> 6.84 m/s.
- Yaw rate at f12 is about 0.1 rad/s (car axis and velocity heading change about 5 deg over f4-24), so wheel speed = origin speed within 1%.
- Closure: tyre 136-138 px at f0 -> 0.765-0.776 m vs prior 0.764 (0.1-1.6%). Wheelbase 2.6-2.9 m (plausible).

## Ruled out
- C4 8.2: straight-line 1/h model over an accelerating window inflates the f12 depth rate by about 15% (linear slope 8-24
  -2.24e-4 vs local -1.95e-4 per frame).
- C3 9.0: chosen above its own frame-12 fits, with a speed-limit-sign argument.
- C1's down-weighting to 6.5 via fascia ECC (6.25): the body ECC agrees with the rim at the neighbouring frames, and only drifts farther away.

## Open
- Derivative noise: shorter windows give 6.3-7.0. The raw backward difference 11->12 is 6.49. The central estimate 6.75-6.84 is
  about ±4%.

### Round 2 (harness v3; files in context/round2/)
- Answer: 6.8 (switch, confidence medium, follows C1 (round-1 refinement, 6.8))
- Where the answers part: how the frame-12 derivative of the near-front-rim depth track (rim height + depth_info) is taken: local fits (6.5-7.0) vs a straight-line 1/h fit over an accelerating window (8.2) or a value chosen above its own fits (9.0)
- Fault proven: the DeepSeek half of the blend rests on a constant-rate 1/h line over f8-23+ that inflates the f12 depth rate by 13-15 pct (7.8 vs 6.8 on my data), plus a far-tyre depth offset, and on a 9.0 chosen above its own 7.5-8.5 fits
- Closure on the prior: 2.0 pct

# Round 2 addendum – Q1522 (speed of the car at t = 0.5 s)

Round 1's switch to **6.8 m/s** was verified with independent code. Decision: switch (to 6.8), confidence medium.

## Newly established
- Camera geometry: the vertical lines in f49 have zero tilt up to |u−cx| = 500 px. So there is no pitch, and the horizon v≈829 comes from a lens shift (principal point ≈ (960, 829)). With this principal point the VPs give f = 2370 (round 1 had 2353 with the image centre). The effect on speed is about 1%.
- Rim vertical extent, from two of my own estimators:
  - Column half-max: f0 87.25, f11 97.25, f12 99.29.
  - Radial-edge conic fit: f0 86.35, f11 97.03, f12 99.47.
  - Both agree with round 1 within about 0.6 px.
- Speed at f12 with long-window local fits (cubic to quintic or quadratic, windows 0-23, 0-20, 2-22, 6-18): 6.50–6.97, centre ≈ 6.8. Short windows (8-16, 6-18 cubic) give 5.95–6.35 and are noise-dominated. Raw single-frame differences (6.3–8.3) are unusable.
- C4's fault reproduced: a linear 1/H fit over f8-23 gives a rate −2.27e-4 vs −2.0e-4 locally (+13%), which gives 7.8 m/s.
- Closure: tyre about 137–140 px at f0 (top edge about 759, floor contact about 899) → 0.771–0.788 m vs 0.764 (+1 to +3%).

## Ruled out
- 8.2 (constant-rate fit plus far-tyre offset) and 9.0 (a guess from the speed-limit sign).
- A pitched-camera model is not needed. It also does not change the result materially.

## Open
- Derivative noise of about ±4% (6.5–7.0). The tyre-size closure being +1 to 3% high hints that f might be slightly larger (about 2450). That would lower the speed by about 0.1 m/s. This is within the noise.
