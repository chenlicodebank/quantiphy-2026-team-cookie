# q_2624 — basketball displacement between 0.5 s and 0.6 s (cm)

- Frames at question_fps 24 (same as the file's rate): t=0.5 -> frame 12, t=0.6 -> frame round(14.4) = 14.
  The basketball is free and unoccluded in both (checked on 3x crops frames/f12.png, f14.png); the record's
  dropped frame (11->12) lies outside the interval.
- measure.py: HSV orange mask -> centroid, bbox, area-equivalent diameter, enclosing circle.
  Frame 12: centre (771.2, 552.7), d_eq 78.0 px. Frame 14: centre (737.3, 535.3), d_eq 77.1 px.
  These match scene/tracks/basketball.csv fit_cx/fit_cy to within 0.3 px.
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Depth: 2.270 m at t=0.6 s (given). Check: 23.2 cm prior with d_eq 77.1 px gives 2.296 m (1 % off), so the
  sizes agree. Depth at frame 12 comes from the diameter ratio (the ball is moving away; d_eq trend
  78.0 -> 75.4 over frames 12-16): Z12 ≈ 2.24 m.
- Back-projected along the unit ray x the Euclidean distance: displacement = 10.84-10.87 cm (area-eq diameter ratio),
  10.70-10.72 cm (bbox diameter ratio), 10.56-10.59 cm if the depth is held constant.
- Second route: the enclosing-circle centre instead of the centroid gives the same results to within 0.03 cm.
- Answer: 10.8 cm. Confidence: high (about ±3 %). The main uncertainty is the depth change between frames 12 and 14.
