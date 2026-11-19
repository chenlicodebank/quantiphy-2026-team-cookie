# Context of question 1409 (organised record; every round adds to it)

## Question
- Text: What is the speed of the astronaut at time 1s in m/s?
- Its own prior: height of the astronaut = 2.2m
- Its own depth_info: t=1s, distance_astronaut_camera = 18.147m
- question_fps: 24
- Video: simulation_0172.mp4 (simulation, S3SS)

## The answer currently submitted
4.66498 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 5.2 and an earlier DeepSeek median B = 4.185; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 5.2 | 1.115 |
| C2 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_3 S3 adjudication (DeepSeek differs 25 pct to 2x) | 5.15 | 1.104 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 4.12 | 0.883 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 4.25 | 0.911 |

DeepSeek median over its 2 runs: 4.1845.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 4.95 (new, confidence medium, follows None)
- Where the answers part: whether the astronaut approaches the camera: depth term dZ (~-2.3 m/s) and depth-correction of the rest pixel height (C3/C4 assume constant depth, C1/C2 do not)
- Fault proven: C3/C4 (DeepSeek half of the blend) assume constant depth, but rigid upper-body template scale grows 1.052 by f42 and ~1.11 by f60; they omit dZ (~+11%) and use uncorrected f42 height 418-420 px (~-5%)
- Closure on the prior: 0.0 pct

# Round addendum, Q1409 (astronaut speed at t = 1 s)

## Established
- **The astronaut approaches the camera.** An affine ECC track of the rigid upper body (backpack + helmet + torso; `track_scale.py`) gives a scale relative to frame 24 of:
  - 0.9931 at f23, 1.041 at f36, 1.052 at f42 (cc ≥ 0.90);
  - 1.10-1.13 at f60, from a frame-60 template linked over f30-52 (cc 0.96-0.99).
  - The foot/shadow ground rows move down from 1023 to 1060, which agrees.
  - The constant-depth premise of C3/C4 is therefore false.
- **Pelvis step f23 to f24:** (+30.1, -14.3) px = 33.3 px. Independent tracks give 32.6-33.9 px.
- **Depth step at f24:** about 0.095 ± 0.02 m per frame (raw backward 0.11-0.12; central and constant-heading 0.08-0.09).
- **Rest height at frame 24's depth:**
  - At f42: bbox 418 px, segment sum about 421-425 px. Divided by 1.052 this gives H ≈ 400 px (range 397-410).
  - So f ≈ 3300 px.
- **Speed:** sqrt(0.183² + 0.095²) × 24 = **4.95 m/s** (range 4.7-5.25).

## Ruled out
- **C3/C4 values (4.12 / 4.25):** they omit the depth term (about 11 %) and do not depth-correct the frame-42 height (about 5 %).
- **Submitted blend 4.665:** it inherits half of that bias.

## Open
- **Exact dZ for the one-frame backward step:** the template scale is noisy at the 0.001/frame level, which moves the answer by ±4 %.
- **Rest height:** this round uses 400 px; C1 used 388 px. A better segment-sum or skeleton measurement would settle about ±3 %.
- **C1 (5.2) and C2 (5.15)** are consistent with this round within uncertainty.

### Round 2 (harness v3; files in context/round2/)
- Answer: 5.15 (switch, confidence medium, follows C2)
- Where the answers part: approach toward camera (depth term and depth-corrected rest pixel height), then rest height in px at frame 24 depth (388-390 vs 400)
- Fault proven: C3/C4 (DeepSeek half of the blend) assume constant depth although the rigid upper-body scale grows 1.07 by f42 and 1.16 by f79 (ground-contact rows agree): they omit dz ~0.098 m/frame and use an uncorrected 418-420 px height
- Closure on the prior: 2.0 pct

# Round 2 addendum, Q1409 (astronaut speed at t = 1 s)

**Answer: 5.15 m/s** (switch, following C2). Confidence medium, about ±4 %.

## Round 1 verification
- **Its fault claim holds.** SIFT + RANSAC similarity tracking of the upper body (a route independent of round 1's ECC) gives a scale relative to frame 24 of:

  | Frame | Scale |
  |---|---|
  | 0 | 0.925 |
  | 17 | 0.96 |
  | 42 | 1.07 |
  | 60 | 1.13-1.14 |
  | 79 | 1.16 |

  - Foot-contact rows check this. Rows 1023 at frame 17 and 1060 at frame 79 put the horizon at about row 842, and that predicts a row of 1054 at frame 60; the observed row is 1053.
  - So C3/C4's constant-depth premise is false.
- **Round 1's value (4.95) is about 4 % low, but within tolerance.**

## Established
- **Pelvis image step, frames 23 to 24:** (+29.7, -14.3) px = 32.9 px (round 1: 33.3).
- **Depth step:** s24/s23 = 1.0054 from templates at frames 21 and 27, so dZ ≈ 0.098 m per frame.
  - With the template at frame 23 or 24 the result is biased: about 1.0058-1.0065 backward, with the forward step correspondingly low.
- **Rest height at frame 24's depth:**
  - Upright walking frames 74-79: bbox / scale = 377-380 px, about 383-387 px after correcting for lean and knee bend.
  - Flight frames 34-40 with a pointed toe: 393-394 px (chained scale) or about 399 px (ECC scale). This overstates the rest height.
  - Adopted H = 390 ± 8 px, so f ≈ 3217 px.
- **Speed:** at H = 390 it is 5.14 m/s, with per-frame components dx 0.170, dy -0.085, dz -0.098 m.
  - Over H 388-400 and the scale choices, the range is 5.0-5.25.

## Ruled out
- **C3/C4 (4.12 / 4.25):** they assume constant depth.
- **Submitted blend 4.665:** it inherits that bias.
- **Hop gravity as a focal-length route:** the parabola gives about 2.4 m/s² rather than the lunar 1.62, so the animation is not ballistic.

## Open
- **Rest pixel height, ±2 %:** a skeleton or segment-length fit would settle it.
- **The frame 42 scale:** chained/direct SIFT gives 1.068-1.072 and ECC gives 1.052. This affects only the flight-pose height route.
