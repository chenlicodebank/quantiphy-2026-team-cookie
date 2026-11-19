# Context of question 811 (organised record; every round adds to it)

## Question
- Text: What is the width of the house in meters?
- Its own prior: speed of the horse at the back = 0.874m/s
- Its own depth_info: none
- question_fps: 24
- Video: simulation_0241.mp4 (simulation, V2MC)

## The answer currently submitted
9.15342 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 8.25 and an earlier DeepSeek median B = 11.665; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 8.25 | 0.901 |
| C2 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 10.93 | 1.194 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 12.4 | 1.355 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 11.1 | 1.213 |

DeepSeek median over its 3 runs: 11.1.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 8.2 (switch, confidence medium, follows C1)
- Where the answers part: which pixel extent is the width and at which depth it is converted: main-block gable-to-gable span at eave depth (C1) vs the silhouette's image-x extent 806 px at horse scale (DeepSeek runs, blend component B)
- Fault proven: the 806 px image-x extent is the cross wing's ridge-height ends (nearer the camera) and the house's longer dimension; the world X extent is the main eave span (705 px vs Y 625 px at the same depth), so width = Y = 8.2 m, not 10.9-12.4
- Closure on the prior: 1.3 pct

# Round 1 addendum (q811)

## Established
- The view is nadir/top-down: the gable-rake depth ratios are symmetric about the principal point (main 1.167 N / 1.165 S,
  wing 1.108 L / 1.106 R). C3's oblique-view premise (house farther than the horse) is wrong.
- Horse at the back = brown trailing animal. Pixel speed 2.632 px/frame (template 2.62-2.64, mask centroid 2.667,
  rear edge 2.613; frames 0-48, frame 49 is a loop reset), giving 0.013836 m/px at horse-back height.
- House world extents (pinhole solve; the main-ridge/wing junctions at y=352.5 and 416 give a consistent main-ridge
  depth, 0.9267 / 0.9258):
  - Y (main block gable to gable) = 624.7 px at main-eave depth.
  - X = main eave span, 705 px at the same depth.
  - X/Y = 1.13, so **width = Y**.
  - The wing's image extent (806-811 px) is due to its higher roof. It is not the world X extent (the wing is 4% shorter
    than the main eaves in world).
- Width = 8.644 m × factor (eave nearer the camera than the horse's back). For a one-storey eave and a 30-45° pitch the
  factor is 0.91-0.97, giving **8.2 m** (range 7.9-8.4). Length (X) under the same assumptions ≈ 9.2 m.

## Ruled out
- 806 px × horse scale (C2/C4, the DeepSeek blend component): wrong extent (the longer one) at the wrong depth (roof ridge).
- The ×1.139 oblique depth correction (C3).

## Open
- Focal length / eave height: the roof gives only f = 2478·tan(pitch). Tile texture was inconsistent; the ground shadow
  is obscured by trees. A two-storey main eave would lower the width to 6.8-7.6 m (judged unlikely).
- Naming: the "width = X extent" reading gives ≈9.2 m (≈ the submitted blend). The convention (width = shorter) excludes it.

Decision this round: switch to the C1 reading, answer 8.2 (confidence medium).

### Round 2 (harness v3; files in context/round2/)
- Answer: 8.2 (switch, confidence medium, follows C1)
- Where the answers part: which pixel extent is the width and at which depth: main-block gable-to-gable span at eave depth (C1, 624 px) vs the silhouette's image-x extent 806 px (cross-wing ridge ends) at horse scale (DeepSeek runs, blend component B)
- Fault proven: component B measured the longer horizontal dimension (main eave X span 703 px > Y 624 px at the same eave depth) and took it at ridge height; width = shorter = Y = 623.9 px x 0.013847 m/px x ~0.95 eave-depth factor = 8.2 m
- Closure on the prior: 1.0 pct

# Round 2 addendum (q811)

## Verified (own code: speed_me.py, roof_me.py)
- Round 1's switch to 8.2 is reproduced.
- Horse at the back: 2.63 px/frame.
  - Template matching: 2.605 / 2.631 / 2.644 at lags 24 / 36 / 48.
  - Rear edge 2.612; centroid 2.693.
  - Scale: 0.013847 m/px at horse-back depth.
- Main-block Y span (gable to gable):
  - Eave level: 623.9 px.
  - Ridge level: 727.9 px; divided by the eave/ridge depth ratio 1.1663 this gives 624.1 eave-px. The two routes agree to 0.03%.
- X span (main eaves) is 703.2 px at the same depth, so width = Y.
- Round 1 measured 624.7 / 705 / 2.632, all within 0.3% of these.
- Width:
  - Uncorrected: 8.64 m.
  - With the eave nearer the camera (one-storey eave, pitch 30-45°): 7.8-8.3 m, central 8.1-8.25.
  - **Answer 8.2** (switch; follows C1).

## Ruled out
- 806 px × horse scale (C2, C4, blend component B): this is the longer dimension, taken at ridge height.
- The oblique ×1.139 correction (C3): the eave/ridge depth ratios are symmetric (1.167 / 1.165).

## Open
- f / eave height is still unmeasured; the animals walk in shadow, so no shadow-length route works.
- A two-storey main eave would give about 7.0 m (judged unlikely).
- Under the reading "width = X extent", the answer would be about 9.15 m. The stated convention excludes that reading.
