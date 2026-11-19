# q471: speed of the box at t=0.2 s (frame 24 at question_fps 120; file is also 120 fps)
2D scene: the box falls straight down from rest and hits the truck roof at frame 61.
Prior: acceleration 9.8 m/s^2 before 0.6 s -> scale = 9.8 / pixel acceleration.
- I tracked the box myself in measure.py (template from the lower front face at frame 120, sub-pixel NCC, scores >= 0.95).
  It agrees with scene/tracks/box.csv to about 0.1 px.
- A quadratic fit of y(t) over frames 2-60 gives a_px = 1975 px/s^2, so the scale is 0.004962 m/px. The fall starts at
  frame -0.2, which is essentially frame 0.
- Speed at frame 24, backward difference (y24 - y23) x 120 x scale: 1.934 from the fitted curve, 1.928-1.935 from raw
  positions (my track and the record). Fit windows 5-60 and 10-50 agree within 0.1 pct; window 2-40 gives 1.925.
- Check: g x (24 - 0.5 + 0.2)/120 = 1.935 m/s.
- Scale sanity: the truck is about 8.4 m long, which is plausible. The box is 2.0 m long, which is large but possible.
Answer 1.934 m/s. Confidence high (about 1 pct).
