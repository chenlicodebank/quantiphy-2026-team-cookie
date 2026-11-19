# q_537 – speed of the magnifying glass at t = 0.25 s

- 2D simulation, 24 fps (file and question_fps agree); t = 0.25 s -> frame 6. Glass falls straight down in frames 0-10
  (impact between 10 and 11), so frame 6 is in free fall.
- Scale from the prior: pixel acceleration fitted (quadratic, frames 0-10) to my own difference-mask track
  (`measure.py`): bbox-mid a = 12.95 px/frame², mask centroid 12.95 px/frame² (bbox top/bottom 12.5/13.4, biased by the
  slow tilt of the glass). 9.8 m/s² = 12.95 px/frame² x 576 -> 1.313e-3 m/px.
- Speed (backward difference p6 - p5 = v(5.5) of the quadratic): 71.7-72.0 px/frame -> 2.26-2.28 m/s.
- Check: v/a = 5.55 frames, i.e. the fit says the glass started from rest at frame ~0, so the analytic value
  9.8 x 5.5/24 = 2.246 m/s agrees within 1 pct. Raw bbox-centre difference 440-367.5 = 72.5 px/f -> 2.28 m/s.
- Answer 2.26 m/s. Confidence high (±2 pct).
