# Context of question 1365 (organised record; every round adds to it)

## Question
- Text: What is the average speed of the turing yellow car from the beginning to the end in m/s?
- Its own prior: length of the white car = 6m
- Its own depth_info: t=0.58s, distance_human_camera = 37.0747m
t=1.58s, distance_human_camera = 37.8958m
t=0.58s, distance_yellow_car_camera = 31.0495m
t=1.58s, distance_yellow_car_camera = 30.4267m
t=0.58s, distance_white_car_camera = 31.2826m
t=1.58s, distance_white_car_camera = 27.7202m
t=0.58s, distance_bike_camera = 28.6001m
t=1.58s, distance_bike_camera = 24.5118m
- question_fps: 24
- Video: simulation_0074.mp4 (simulation, S3MS)

## The answer currently submitted
3.69621 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 4.14 and an earlier DeepSeek median B = 3.3; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 4.14 | 1.120 |
| C2 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_3 S3 adjudication (DeepSeek differs 25 pct to 2x) | 4.1 | 1.109 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 3.9 | 1.055 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 3.3 | 0.893 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 3.2 | 0.866 |

DeepSeek median over its 3 runs: 3.3.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 4.1 (switch, confidence high, follows C2)
- Where the answers part: 3D reconstruction of the taxi path: ground-parallel plane through the two given depths with f~1790 (4.1) vs depth linearly extrapolated from the two given values along each ray with f 1850-1930 (3.2-3.3)
- Fault proven: DeepSeek runs (B=3.3 in the blend) extrapolated the taxi depth linearly to 29.6 m at the last frame while ground-plane geometry gives 33.9 m (taxi approaches then recedes); reproducing that method gives 3.33 (f=1790) / 3.20 (f=1930), matching C4/C5, and their f is ~5% too long against two independent vanishing-point routes (1785-1794)
- Closure on the prior: 3 pct

# Round 1 addendum (Q1365, yellow-taxi average speed)

## Established, and by which measurement
- **Focal length f = 1790 ± 10 px, from two independent routes:**
  - Kerb-line VPs, assuming orthogonal roads: vA = (-1301,-260), vB = (2686,-258), f = 1783-1787.
  - Vertical VP from 7 pole centre lines (rms ≤ 0.15 px): vz = (1072, 4566). f = 1787/1794 with vA/vB, with no
    orthogonality assumption.
  - One short right-hand signal pole is an outlier: exclude it.
- **Camera height ≈ 9.5 m.** The pedestrian pelvis at its given depth and the taxi sign plane agree on it.
- **Frame 0 is a duplicate of frame 1** (zero motion step).
- **Taxi path:**
  - The roof sign is tracked in all 72 frames. Each sign ray is intersected with a ground-parallel plane solved from the
    depths at frames 14 and 38; the two frames agree to 0.01 m.
  - Mean per-frame speed = 4.08 (steps 1..71) / 4.14 (steps 2..71) at δ = 0.8 m. The range is 4.05-4.17 over δ 0-1.6 m,
    f 1785-1795 and smoothing.
  - The per-frame speed is constant at about 4.1 m/s. There is no deceleration.
- **The taxi's depth is not linear in time.** Plane-model origin depth is 32.2, 31.0, 30.3, 30.5, 31.3, 33.9 m at frames
  0, 14, 26, 38, 50, 71. The taxi's image row goes 239 → 263 → 219: it approaches, then recedes.
- **Closure on the van:**
  - Wheelbase 3.77-3.89 m from hub points on the plane at hub height. With Express length/wheelbase ratios (1.57-1.66)
    that is 6.0-6.3 m against the 6 m prior, about 3 %.
  - The silhouette box fit gives 5.0-5.3 m, which underestimates because of the sloped hood.
- **Plausibility at f = 1790:**
  - Pedestrian about 1.82 m. The scene bbox height of 98 px includes about 8 px of shadow below the feet; the real
    extent is about 90 px.
  - Taxi broadside about 5.4 m (Crown Victoria 5.39 m).

## Ruled out
- **C4 (3.3) and C5 (3.2), and so the DeepSeek median B = 3.3:**
  - Linear depth extrapolation along bbox-centre or centroid rays. Reproduced: 3.33-3.44 at f=1790 and 3.10-3.21 at
    f=1930.
  - Their "deceleration" is an artefact of that model.
  - Their f of 1850-1930 is too long.
- **C3 (3.9):**
  - f = 1659 contradicts both VP routes.
  - Its average includes the mask-centroid track, which is biased low (3.86 even at f=1790). Its own tyre-contact route
    (4.12) agrees with mine.

## Decision this round
Switch from 3.696 (the blend) to 4.1, following C2. C1's 4.14 is equally supported.

## Open
- Whether the reference includes the duplicated frame-0 zero step: 4.08 if it does, 4.14 if not. That is a ±1.5 %
  effect.
- The exact origin height relative to the roof sign (δ): ±0.03 m/s.

### Round 2 (harness v3; files in context/round2/)
- Answer: 4.1 (switch, confidence high, follows C2)
- Where the answers part: 3D taxi path: ground-parallel plane through the two given depths with VP focal length (~4.1) vs depth extrapolated linearly in time with a long focal length (3.2-3.3)
- Fault proven: DeepSeek runs (B=3.3 in the blend) extrapolated depth linearly (31.4->29.6 m) although the plane-consistent depth is 32.2->30.3->33.9 m; reproduced 3.25-3.50, and their f 1850-1930 exceeds the VP value 1782
- Closure on the prior: 3 pct

# Round 2 addendum (Q1365, yellow-taxi average speed)

## Verified (independent code, round 2)
- **Focal length: f = 1782.**
  - Measured from Hough-fitted kerb and sidewalk lines on a median background, 8 + 7 lines.
  - vA = (-1294,-258), vB = (2686,-259). Leave-one-out gives 1779-1783.
  - This agrees with round 1's 1783-1794.
- **Ground-parallel plane model is consistent with the depths.** The sign-plane offset solved at frame 14 and at
  frame 38 agrees to 0.01 m (7.951 / 7.943).
- **Taxi speed from the roof-sign track on the plane:**
  - Mean per-frame speed is 4.12-4.18 raw and 4.02-4.07 smoothed. The lower value of each pair includes the
    duplicated frame-0 zero step.
  - f 1775-1800 and δ 0-1.5 give 4.06-4.22. The per-frame speed stays flat at about 4.1-4.2.
- **Independent chord check:** the given depths alone, placed on the frame-14 and frame-38 rays, give a 3D chord of
  4.099 m over 1 s. The plane model gives 4.094.
- **Fault reproduced:** linear-in-time depth extrapolation gives 3.50 at f 1782, 3.38 at f 1850 and 3.25 at f 1930.
  This matches C4 and C5, so B = 3.3 in the blend is faulty.
- **Closure:**
  - Van wheelbase from tyre contacts at frame 66 is 3.86-3.94 m (H 9.5-9.7 m), which fits an extended Express.
  - Scaled by length/wheelbase, that gives about 6.0-6.2 m against 6 m, about +2-3 %.
- **Plausibility:** taxi length along its heading is 5.43-5.47 m (Crown Victoria 5.39 m).

## Decision
4.1 (switch from the blend 3.696, following C2). Round 1's proposal is verified.

## Ruled out
- The KLT body-feature median-flow track drifts 91 px over the clip and is not usable.
- The van's bottom-contour length is contaminated by its shadow.

## Open
- Whether the reference counts the duplicated frame-0 zero step: about 1.5 %.
- Raw versus smoothed track: about 2 %.
- The full range is 4.02-4.18, all within 2.5 % of 4.1.
