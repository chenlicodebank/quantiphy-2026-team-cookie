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
