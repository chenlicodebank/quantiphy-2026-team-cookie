# q_295 — diameter of the ball (m)

Prior: gravity 9.8 m/s^2 on the falling red ball; no depth_info. 2D scene → one metres-per-pixel scale from the ball's
pixel acceleration. File fps = question_fps = 24.

- measure.py: re-tracked the red ball (red-dominance mask, soft-weighted centroid) in all 38 frames → ball_track.csv.
  Quadratic fit of y(t) over frames 2–37: a = 608.8 px/s^2 (3–37: 608.8; 5–37: 609.4; 2–20: 600.6; 20–37: 610.3).
  x stays constant, no bounce or impact → a ≈ 609 px/s^2. Scale = 9.8/609 = 0.01609 m/px.
- Diameter in pixels: area-equivalent 22.6–22.9 px (mask), soft-weighted 22.5 px; edge profiles through the centre on
  the rest frame 0 with partial-pixel coverage give about 23.5 px horizontally and about 23.5 px vertically (the dark
  shaded lower rim lowers the mask-based values). Adopted 23.0 ± 0.5 px.
- Diameter = 23.0 × 0.01609 = 0.370 m (range 0.36–0.38).
- Check: the first and second halves of the fall give the same acceleration within 1.5 pct, so the scale is consistent.
  With this scale the back-wall window comes out at 547 px ≈ 8.8 m, which is plausible for a hall. The forklift is in
  the nearer foreground, at a different depth, so it is not used for the scale.
Confidence: good (about ±4 pct).
