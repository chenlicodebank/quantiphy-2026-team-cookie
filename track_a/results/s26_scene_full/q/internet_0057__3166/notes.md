# q_3166: distance between the basket and the ball at t = 3.00 s

- Time base: file fps = question_fps = 30, so t = 3.00 s is frame 90. The ball is falling after missing the hoop.
- Scale from the prior (g = 9.8 m/s^2): I fitted a quadratic to the ball's vertical position (scene/tracks/ball.csv,
  bg-fixed y) over the free flight of the shot, frames 54–96, leaving out the degraded frames 73–77 (`fit.py`).
  This gives a = 2.063 px/frame^2 = 1856 px/s^2, so the scale is 9.8 / 1856 = 0.005280 m/px.
  The other windows give 2.06 (frames 55–95 and 58–93), 2.13 (rise, 54–72), 2.01 (fall, 78–96), 2.09 (bounce arc 1)
  and 2.03 (bounce arc 2), which is about ±3 %.
- Sanity check: ball diameter 43 px → 0.23 m (a real ball is 0.24 m); rim 90 px → 0.48 m (real outer rim ≈ 0.46 m). Both are plausible.
- Ball at frame 90: (1183.0, 557.0) in frame pixels, or (1194.3, 561.8) bg-fixed. I checked it on a zoomed crop
  (frames/f90.png).
- Basket = rim centre: (967, 316) in frame-0 coordinates. On frame 90 by eye it is about (960, 307–311), which
  matches the camera drift.
- Pixel distance: bg-fixed route sqrt(227.3^2 + 245.8^2) = 334.8 px; frame-90 visual route ≈ 334 px.
- Distance = 334.5 px × 0.00528 m/px = **1.77 m**. Using the net centre (≈ y 360) instead of the rim centre would give about 1.6 m.
  I kept the rim centre.
- Confidence: moderate to good. The scale is uncertain by about ±3 %, and the "basket" reference point is somewhat ambiguous.
