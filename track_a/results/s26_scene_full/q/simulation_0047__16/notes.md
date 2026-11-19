# q16 – length of the planter between the two staircases (top building)

2D near-nadir render, static camera, fps = question_fps = 33.

Scale (prior: walking person speed 1.236 m/s), pedestrian track from scene/tracks/pedestrian.csv (checked: 99 frames, smooth):
- mean per-frame step 3.350 px (includes ±jitter), 5-frame-smoothed mean step 3.339 px, net/98 frames 3.333 px,
  linear fit 3.326 px -> use 3.338 px/frame = 110.2 px/s -> 0.01122 m/px.

Planter (measure.py, frame 0, rows y 215–245, greenness + brightness column profile):
- hedge starts at x≈1127 (right edge of left staircase railing, bright → green transition) and ends at x≈1396–1400
  (dark side wall of the right staircase). Stone border below the hedge spans the same x range.
- length ≈ 270 px (±3) along the street (its long horizontal extent).

Answer: 270 × 0.01122 ≈ 3.03 m.
Check: the range of speed estimates (3.326–3.350 px/frame) gives 3.01–3.03 m; edge uncertainty ±3 px ≈ ±1 %.
Sanity: sidewalk tiles ~120 px ≈ 1.35 m, plausible. Confidence: moderate-high (main risk: which edges the
reference used for the planter box).
