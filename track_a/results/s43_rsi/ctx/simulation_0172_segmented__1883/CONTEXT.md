# Context of question 1883 (organised record; every round adds to it)

## Question
- Text: What is the acceleration of the astronaut at time 0.5s in m/s^2?
- Its own prior: height of the astronaut = 2.2m
- Its own depth_info: t=1s, distance_astronaut_camera = 18.147m
- question_fps: 24
- Video: simulation_0172_segmented.mp4 (segmentation, S3SX)

## The answer currently submitted
0.25 - the Claude line's answer 0.25, unchanged.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 0.25 | 1.000 |
| C2 | Claude Opus 5.5 (Claude Code agent), 26_36 second run, spread test: a second independent answer on the kept scene record (26_36) | 0.35 | 1.400 |
| C3 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 2 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 2.2 | 8.800 |
| C4 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 3 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 6.5 | 26.000 |
| C5 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_6b S3 adjudication (DeepSeek differs >2x; Codex in the dossier) | 0.28 | 1.120 |
| C6 | Claude Opus 5.5 (Claude Code agent), 40_5 fresh per-question run | 0.4 | 1.600 |
| C7 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 0.42 | 1.680 |
| C8 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 0.5 | 2.000 |
| C9 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 2.6 | 10.400 |
| C10 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 0.5 | 2.000 |
| C11 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 1.5 | 6.000 |
| C12 | OpenAI GPT-6 Astra (Codex agent) | 0.574 | 2.296 |

DeepSeek median over its 5 runs: 0.5.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v1; files in context/round1/)
- Answer: 0.25 (keep, confidence low, follows C1)
- Where the answers part: whether the derivative window at f12 stays inside the first smooth root-motion segment (f0-14, before the abrupt 11->20.6 px/frame step at 14->15) and whether depth comes from pose-dependent silhouette size
- Fault proven: none in C1; C3/C4/C11 fit across the f14->15 step and C9 uses silhouette depth implying ~8% size growth over f0-13 that bbox_h and backpack size do not show
- Closure on the prior: None pct

# Round 1 addendum: Q1883

## Established
- Time base: f12 is t = 0.5 s (file and question are both 24 fps). The scale is f ≈ 3134 px (bbox 380 px at f24,
  2.2 m, 18.147 m); C12's standing-pose correction to 3290 px changes the result by only 5 %.
- The root motion is piecewise. Frame-to-frame upper-body ECC gives smooth image steps of 12.7 to 11.0 px/frame over
  f0→14. At 14→15 the step jumps to 20.6, rises to 33 and drops to 18 at 29→30. The torso shows no gait bob.
  f12 lies in the first smooth segment, so any derivative fit must end at f14.
- The depth is nearly constant near f12: bbox_h is 338-342 px over f0-14, and the backpack is 168 px against 171 px at
  f24, giving Z12 ≈ 18.47 m. The depth-rate variants (0 to -0.027 m/frame) change the answer by less than 10 %.
- Speed at f12 is 1.5-1.6 m/s, a plausible walk.
- Own fits in segment f0-14 (accel.py), signed scalar acceleration in m/s^2:
  - ECC point: quadratic -0.28 to -0.33, cubic -0.33 to -0.39, raw -0.40 to -0.45.
  - Centroid: quadratic -0.31 to -0.53, cubic -0.21 to -0.48.
  - Central magnitude about 0.32, range 0.21-0.53.

## Ruled out
- C3 (2.2), C4 (6.5) and C11 (1.5) fit or smooth across the f14→15 step.
- C9 (2.6) uses a silhouette-size depth with vz ≈ -2.7 m/s, which bbox_h and the backpack size contradict.

## Open
- Inside the plausible cluster (C1 0.25, C5 0.28, C2 0.35, C6 0.40, C7 0.42, C8/C10 0.5, C12 0.574), the choice is
  limited by noise in a second derivative. No concrete fault was shown in C1, so 0.25 is kept. My central value of
  0.32 is about 25 % higher.
- A better rigid depth/scale track (an anchored backpack patch) did not converge far from f12. A segment-wise model of
  the root path (e.g. an exact circular arc or Bezier) could pin the value down.

### Round 2 (harness v2; files in context/round2/)
- Answer: 0.4 (switch, confidence medium, follows C6)
- Where the answers part: which image track supplies the curvature of the root path inside segment f0-14: C1's integer silhouette-edge landmarks vs sub-pixel rigid-patch (upper body, backpack, rear hip) chained ECC; same scale (~0.0059 m/px) for all plausible candidates
- Fault proven: C1's rear-edge x-landmark drifts 9 px against the rigid backpack over f0-14 and its y is an integer row; with C1's own quadratic windows it gives -0.24/-0.26/-0.06 while the identical fits on sub-pixel patch tracks give -0.30 to -0.44 (central -0.39)
- Closure on the prior: 0.0 pct

# Round 2 addendum: Q1883 (answer 0.40, switch to C6, confidence medium)

## Established
- New route: chained frame-to-frame ECC (euclidean and affine) on three patches f0-16: the upper body, the backpack,
  and the rear hip band under the backpack (closest to the pelvis, free of arms). cc is at least 0.96.
- The image velocity in segment f0-14 is smooth:
  - dx rises from 9.6 to 10.8 px/frame (+0.06 to +0.11 px/f²).
  - dy falls from 8.2 to 2.2 px/frame, and the fall speeds up: about -0.6 px/f² near f12.
  - The cubic term in y is significant over f0/2-14 (p < 0.001); a quadratic over f6-14 is adequate.
- At f = 3134 px and Z12 = 18.47 m with constant depth, the acceleration at f12 in m/s^2 is:
  - quadratic fits (6 tracks x 5 windows): median -0.365;
  - cubic fits: median -0.403;
  - speed-series fits: -0.37 to -0.48.
  Central value -0.39. Speed at f12 is 1.53-1.60 m/s. The focal (+5 % standing) and Z12/Z24 (1.018-1.05) variants
  move the result by -5 % and +3 %.
- C1's fault (reproduced in c1repro.py): its rear-edge x-landmark drifts 9 px against the rigid backpack over f0-14
  (spurious +x curvature), and its y is an integer row. With C1's own quadratic windows 2/4/6-14 its landmarks give
  -0.24, -0.26 and -0.06; the same fits on the patch tracks give -0.30 to -0.44.

## Ruled out
- C1 (0.25): landmark artefact, as above. C3, C4, C9 and C11: as in round 1.
- Depth trends from the chained affine scale (5-9 % growth over f0-14, giving 0.6-1.1 m/s^2): bbox_h (340-348 px)
  and the backpack height are flat, so this growth is pose bias. That is probably the source of C12's higher 0.574.

## Open
- The real pelvis may carry gait oscillation invisible to smooth fits. Segment 2 (f15-29) implies 4-5 m/s, so either
  the camera moves or the root is keyframed oddly; this cannot be checked on a white background and does not affect
  f12.
- The remaining spread of 0.36-0.43 comes from the choice of patch and window.

### Round 3 (harness v3; files in context/round3/)
- Answer: 0.4 (switch, confidence medium, follows C6)
- Where the answers part: which image track supplies the curvature of the root path at f12 inside segment f0-14: C1's silhouette-edge landmarks vs sub-pixel rigid/waist tracks; same scale (~0.0059 m/px) for all plausible candidates
- Fault proven: C1's rear-edge x-landmark drifts 9.5 px against the rigid backpack flow track over f0-14 (spurious x curvature 0.11-0.16 vs 0.06-0.10 px/f^2); C1's own quadratic fits reproduce -0.24/-0.26/-0.06 on its landmarks but give -0.41 to -0.47 on dense-flow waist-band tracks
- Closure on the prior: 0.0 pct

# Round 3 addendum: Q1883 (answer 0.40, switch to C6, verified round 2; confidence medium)

## Established
- Round 2's fault proof was reproduced with a different tracker: dense DIS and Farneback flow, not chained ECC
  (`c1check.py`).
  - C1's landmark x drifts 9.5 px against the rigid backpack track over f0-14.
  - C1's own fits (quadratic, windows 2/4/6-14) on its landmarks give exactly -0.24/-0.26/-0.06.
  - The same fits give -0.31 to -0.36 on the backpack flow and -0.41 to -0.47 on the waist-band flow.
- The derivative depends on the body part tracked, because the torso turns about 0.7 deg/frame in the image:
  - head: -0.10 to -0.26
  - upper body / backpack: median -0.28
  - waist band at pelvis level: median -0.43, range -0.25 to -0.51 over quadratic/cubic/speed-series fits in
    f0-14
  - all-track median: -0.36
  Value for the pelvis origin: about 0.42.
- Scale confirmed:
  - The rigid helmet-top to backpack-bottom size is 176.8 px at f12 and 180.4 at f24, so Z12 = 18.5 m and
    m/px = 0.0059 (f = 3134).
  - Speed at f12 is 1.45-1.65 m/s.
- The flow-divergence vertical scale grows 0.5-0.9 %/frame in both segments. bbox_h and the backpack height are flat,
  so this is an estimator bias, not approach. Size-scale depth trends (C12, C9) are rejected again.

## Ruled out
- C1 (0.25): landmark drift (reproduced twice now, ECC and flow).
- C3, C4, C11: fits cross the f14→15 step.
- C9, C12: biased depth trends.

## Open
- Which body point the true origin follows: the upper body gives about 0.28, the waist about 0.43. The answer 0.40
  assumes the waist and pelvis.
- Gait oscillation of the true pelvis, and camera motion, cannot be checked on the white background.
