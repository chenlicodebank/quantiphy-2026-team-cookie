# q_526: diameter of the bottle's body (m)

Prior: drop acceleration = 9.7 m/s². The scene is 2D, so I used one metres-per-pixel scale. fps = question_fps = 60.

- Drop acceleration (fit.py, track from scene/tracks/drop.csv, checked against the sheet): quadratic fits of cy over
  frames 1–11, 2–11, 2–9, 3–11 and 0–11 give 28.78–29.09 px/frame². I took 28.9 px/frame² = 104,040 px/s².
  Second differences are 27.3–30.2.
- Scale: 9.7 / 104,040 = 9.32e-5 m/px.
- Bottle body width (bottle_width.py, intensity profiles of frame 13 over rows 600–1000): the left silhouette edge
  starts at x ≈ 702–704 (half-level ≈ 711). The right edge has a rim highlight at about 1064, then background from about 1071–1073.
  Outer width ≈ 368 px (the record says 703–1072 = 369, which agrees). Half-level widths come out lower at about 355.
- Diameter = 368 × 9.32e-5 = 0.0343 m (3.4 cm, a plausible dropper bottle).
- Second check: using the half-level width of 357 px gives 0.0333 m. The acceleration fits all stay within ±0.6%.
- Confidence: moderate. The edges are soft frosted glass (±5 px), and the bottle may not be at exactly the same depth as the drop.
