# Context of question 1970 (organised record; every round adds to it)

## Question
- Text: What is the width of the house in meters?
- Its own prior: speed of the brown horse = 0.874m/s
- Its own depth_info: none
- question_fps: 24
- Video: simulation_0237_segmented.mp4 (segmentation, V2MX)

## The answer currently submitted
8.8728 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 8.1 and an earlier DeepSeek median B = 10.975; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 8.1 | 0.913 |
| C2 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 10.95 | 1.234 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 11.0 | 1.240 |

DeepSeek median over its 2 runs: 10.975.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 8.1 (switch, confidence medium, follows C1)
- Where the answers part: Top-down roof view (C1: shorter eave-level Y extent 617-618 px, eave-height-corrected) vs side-view box reading (C2/C3: full horizontal mask extent 800 px at gable-peak depth, uncorrected)
- Fault proven: C2/C3 measured the longer axis at ridge level (803 px, perspective-inflated) under a side-view reading refuted by the top-down horse; the width is 618 eave-px, so even uncorrected the width is <= 8.47 m, below the submitted 8.87 blend
- Closure on the prior: 1.5 pct

# Round 1 addendum (q1970, house width)

## Established
- The camera is top-down (measure.py, frames/overlay.png).
  - The horse is seen from above: 148 x 42 px, no legs, white muzzle at its leading end.
  - The building is a cross-gabled roof: main ridge vertical at x = 1018, eaves at x = 662 / 1361; cross ridge at
    y ~ 383, gable peaks at x = 620 / 1423.
  - The ridge/eave ratio about the image centre is 1.165 at the top gable and 1.170 at the bottom, so the principal point
    is at the centre and the ridge is about 17 pct closer than the eaves.
- Horse pixel speed is 63.8 px/s (centroid and right-edge fits agree; left edge 62.0), so the scale is 0.013699 m/px at
  the horse.
- House width = shorter horizontal extent = main-wing gable-to-gable Y extent at eave level = 618 px. It reads 616 / 620
  at the two eave lines, and 721 / 1.167 = 618 from the ridge. Length (X) is about 700-715 eave-px.
- Uncorrected width is 8.47 m. This is an upper bound, because the eaves are above the horse's back.

## Ruled out
- The side-view box-corner reading (scene/ record, C2, C3), and the 800 px horizontal extent at gable-peak depth
  (10.95-11.0 m). That extent is the longer axis and inflated by perspective.
- The submitted 8.87 is above the 8.47 upper bound.

## Open
- Eave height above the horse's back is not observable (no walls or ground). The depth factor Ze/Dh is 0.94-0.97 for a
  single storey (7.95-8.2 m) and 0.77-0.88 for two storeys (6.5-7.4 m), using tan(pitch) = 0.0299 Dh and a pitch of
  30-48 deg.
- New answer: 8.1 (switch to C1), medium confidence.
- A route to settle it would be sun-shadow geometry: the cross wing casts a shadow on the main roof, with its edge from
  (1018, 415) to (1210, 605) and then along y ~ 605.

### Round 2 (harness v3; files in context/round2/)
- Answer: 8.1 (switch, confidence medium, follows C1)
- Where the answers part: Shorter horizontal (Y, gable-to-gable) extent at eave level, 618 px with small eave-height correction (C1), vs the whole-mask X extent at gable-peak level, 800 px uncorrected (C2/C3)
- Fault proven: C2/C3 measured the longer axis (X: 700 eave-px / 803 ridge-px) instead of the width (Y: 618 eave-px) and at ridge level; the submitted 8.87 blend exceeds the uncorrected 8.47 m upper bound
- Closure on the prior: 0.3 pct

# Round 2 addendum (q1970, house width)

## Verified (own code: measure.py, overlay.py)
- Horse pixel speed fits (px/s), giving 0.013699 m/px at the horse:
  - centroid 63.97;
  - muzzle tip 63.84;
  - brown-only centroid 63.84;
  - brown left edge 63.43.
- Closure on the prior: 0.3 pct.
- House Y extent at eave corners: 615 / 619 / 617 / 625 px (x = 664 / 670 / 1358 / 1350).
  - At the ridge it is 721 px. The ridge/eave ratio about the image centre is 1.164 (top) and 1.172 (bottom).
  - Width = 618 eave-px, so 8.47 m uncorrected.
- X extent: 700 px at eave level, 803 px at the gable peaks. So X is the length.
- The C2/C3 fault (longer axis at ridge level) is real. Round 1's switch to 8.1 is confirmed.
- New top-down cue: grey hooves peek out only on the horse's edge facing the image centre, and stay put while planted.
  This is consistent with a perspective view from above, with a ground depth of roughly 30-45 m (rough).

## Ruled out
- 10.95-11.0 m: this is the length at ridge level.
- 8.87 m (blend): above the 8.47 m upper bound.

## Still open
- Eave height above the horse cannot be observed.
  - Single storey: factor 0.93-0.96, giving 7.85-8.15 m.
  - Two storeys: about 7.2 m.
- The tile-period route (tiles.py) is inconclusive. The main-wing foreshortening is about 0.82, but the tile aspect is
  unknown and the cross-wing spectra are harmonic-dominated.
- Answer 8.1, medium confidence.
