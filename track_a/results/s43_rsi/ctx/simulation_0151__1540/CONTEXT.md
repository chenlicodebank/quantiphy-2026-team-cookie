# Context of question 1540 (organised record; every round adds to it)

## Question
- Text: What is the acceleration of the blue car at time 1s in m/s^2?
- Its own prior: diameter of the tire of the yellow car = 0.764m
diameter of the tire of the blue car = 0.369m
- Its own depth_info: t=0.5s, distance_yellowCarLeftFrontTire_camera = 11.38m
- question_fps: 24
- Video: simulation_0151.mp4 (simulation, S3MC)

## The answer currently submitted
1.64317 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 1.44 and an earlier DeepSeek median B = 1.875; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 1.44 | 0.876 |
| C2 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 2 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 1.2 | 0.730 |
| C3 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 3 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 1.15 | 0.700 |
| C4 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_6b S3 adjudication (DeepSeek differs >2x; Codex in the dossier) | 1.4 | 0.852 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 2.1 | 1.278 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 1.65 | 1.004 |
| C7 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 1.4 | 0.852 |
| C8 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 1.2 | 0.730 |
| C9 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 1.2 | 0.730 |
| C10 | OpenAI GPT-6 Astra (Codex agent) | 1.493 | 0.909 |

DeepSeek median over its 5 runs: 1.4.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 1.4 (switch, confidence high, follows C4)
- Where the answers part: pixel acceleration of the cart at frame 24: about 0.50 px/f^2 from clean template tracks vs 0.67-0.75 from the DeepSeek canopy-edge estimators behind blend component B; tyre px 74.5-77 is only a 3 pct spread
- Fault proven: the blend's component B (DeepSeek, 1.875) rests on pixel accelerations 0.67-0.75 px/f^2 from noisy point estimators; a 0.03 px-rms light-panel track and a clip-wide joint ease fit both give 0.50 px/f^2
- Closure on the prior: -3 pct

# Round 1 addendum: Q1540 (blue cart acceleration at t = 1 s, frame 24)

## Established
- **Motion model.** The cart's motion is a single Blender ease (smoothstep) from frame ≈0 to ≈59, with Δ ≈ 1330 px.
  - Light-panel template track, frames 23-41: rms 0.03 px to a cubic; i0 = -0.16, T = 59.2.
  - Joint fit with the scene record's frames 0-13: i0 = -0.2, T = 59.8.
- **Pixel acceleration at frame 24.** (x22 - 2 x23 + x24) = **0.50 px/f²**: lights 0.496, joint 0.504, windows 0.49-0.53.
- **Tracked plane vs wheel plane.** The body + wheels track moves 1.0017 x the lights track (frames 27→41), so no correction is needed.
- **Cart front tyre.** 77 px laterally (circle fits and horizontal extent, frames 31-41) and 74.5 px vertically (top and bottom touch the fender and the floor). The rear tyre is unusable (merged with its wheel arch).
- **Answer.** a = 0.501 x 576 x 0.369 / (74.5 to 77) = 1.38 to 1.43 m/s². Adopted **1.40** (= C4).
- **Checks.**
  - Closure on the yellow-tyre prior: -1.5 to -4 % (ground-row depth ratio 1.241).
  - Plausibility: cart 1.58 m tall, yellow car 4.5 m long, cart speed 3.8 m/s.

## Ruled out
- **Blend component B = 1.875 (DeepSeek).** It rests on pixel accelerations of 0.67-0.75 px/f² (C5, C6), which are 35-50 % too high, so the submitted blend of 1.643 is about 17 % high.
- **C6's 86 px tyre.**
- **C2 / C3 (1.15-1.2).** They read the curvature from the noisy record track, getting about 0.40 px/f².

## Open
- The tyre pixel diameter is 74.5 px (vertical) or 77 px (lateral), a ±1.6 % effect on the answer. Lateral is the more likely to be the true silhouette.

### Round 2 (harness v3; files in context/round2/)
- Answer: 1.4 (switch, confidence high, follows C4)
- Where the answers part: pixel acceleration of the cart at frame 24 (second difference centred on frame 23): 0.50-0.53 px/f^2 from clean tracks anchored by the clip-wide ease, versus 0.67-0.75 behind the DeepSeek component of the blend; the tyre spread of 76-78 px is only +-1.5 pct
- Fault proven: blend component B (1.875) needs about 0.68 px/f^2 at a 77 px tyre; LED-centroid, chained-velocity and joint-ease routes give 0.45-0.56 (anchored 0.50-0.53), so B and the submitted blend are about 30 and 17 pct high
- Closure on the prior: -3.5 pct

# Round 2 addendum: Q1540 (blue cart acceleration at t = 1 s)

## Established (round 2 verified round 1's switch with independent code)
- **Pixel acceleration at frame 24 (x22 - 2 x23 + x24): 0.51 px/f² (0.50-0.53).**
  - Template-free LED-blob centroid track: 0.47-0.50.
  - Linear trend of the clean LED second differences 28-40: 0.497 (a = 0 at frame 29.55, jerk -0.076).
  - Joint smoothstep of the record's early speeds plus LED 28-41: 0.50-0.53.
  - Late-only extrapolations bracket these at 0.45-0.56.
  - The motion is a single ease: start-up acceleration about 2.2 px/f², falling linearly to zero at frame 29.6.
- **Cart front tyre: 77 px (76-78).**
  - Dark-mask width 76; left-arc circle fit about 78.
  - The vertical top edge equals the circle fit, so the fender does not occlude it. The bottom is about 2 px short at ground contact.
  - LED edges show no horizontal motion blur.
- **Result: a = 0.51 × 576 × 0.369/77 = 1.41 m/s²** (range 1.36-1.46). Answer 1.40 (C4).
- **Closure on the yellow-tyre prior: -3.5 %.** Yellow tyre 188-189 px vertically, ground-row depth ratio 1.228-1.241. The depth_info route gives f ≈ 2720 px and reproduces the 189 px.

## Ruled out
- **Submitted blend 1.643.** Its component B (1.875) needs about 0.68 px/f², which no clean route gives.
- **C5, C6.** Pixel accelerations of 0.67-0.75 (C6 also used an 86 px tyre).
- **C2, C3, C8, C9 (1.15-1.2).** About 0.42 px/f², below the anchored range.

## Open
- The tyre pixel size (74.5 vertical vs 76-78 horizontal) is a ±2 % effect. The geometry from the yellow tyre predicts 74.4 px, which would give 1.45. Any answer between 1.38 and 1.46 is within 3 % of 1.40.
