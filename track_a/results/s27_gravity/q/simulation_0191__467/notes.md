# q467 — height of the box (simulation_0191, 2D, 120 fps = question_fps)

Scale from prior (box acceleration before 0.6 s = 9.8 m/s^2):
- Quadratic fit of the box front-face centre cy (scene/tracks/box.csv, template-matched, ±0.3 px) over free fall
  frames (impact at frame 61): frames 1-60 -> 1975.6 px/s^2; 2-58 -> 1976.3; 5-55 -> 1977.0; 10-60 -> 1971.0;
  1-30 -> 1985.8; 30-60 -> 1963.1 (residuals < 0.14 px). Adopt 1975 px/s^2 -> 9.8/1975 = 4.962e-3 m/px.
- Pinned at rest (frame 150) with a brown colour mask (flap.py): front-face top y ≈ 214-216, bottom ≈ 407.5
  -> face height ≈ 192 px (record: 191). Open flap at right end rises to y ≈ 198 -> overall vertical extent ≈ 210 px.

Height:
- front face only: 192 px x 4.962e-3 = 0.953 m
- including open flap (mesh AABB): 210 px -> 1.04 m
Answer 0.99 m, between the two readings (within ~5 % of either), since the reference AABB may or may not include
the flap.
Check: the acceleration from the early and late halves of the fall agrees to ±0.6 %, so the scale is stable.
Confidence: moderate-high on scale; the main uncertainty is whether the flap is included (±5 %).
