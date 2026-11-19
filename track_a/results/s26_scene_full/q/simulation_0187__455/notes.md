# q_455 – speed of the truck at t = 1.5 s (m/s)

Prior: acceleration = 10.757 m/s^2 (exact). 2D simulation, 30 fps (file and question rates are the same), t = 1.5 s -> frame 45.
The camera is static, and the truck moves left to right in a straight horizontal line.

## Method
- Track: scene/tracks/truck.csv ref_x_px (side-plane template track, rigid translation). fit.py fits a quadratic
  x(frame) over several frame windows:
  | window | a (px/frame^2) | dx45 (px) | rest frame | v(1.5) m/s |
  |---|---|---|---|---|
  | 14-54 | 2.0415 | 90.77 | 0.04 | 15.94 |
  | 20-50 | 2.0364 | 90.70 | -0.04 | 15.97 |
  | 30-50 | 2.0569 | 90.77 | 0.37 | 15.82 |
  | 36-50 | 2.0416 | 90.76 | 0.04 | 15.94 |
  The fit residuals are 0.2-0.6 px, so the acceleration is constant and the truck starts from rest at frame 0.
- Scale: m/px = 10.757 / (a_px x 30^2). Speed = dx45 x 30 x m/px = 10.757 x dx45 / (30 a_px).
  The answer depends only on dx45 / a_px. For a start from rest at frame 0 this ratio is 44.5 frames, so
  v = 10.757 x 44.5 / 30 = 15.96 m/s.
- Second route (check.py): my own template matching on frames 30-55. I took the central 300 px of the truck in
  frame k and matched it horizontally in frame k+1, then rejected false matches caused by repeating texture.
  The per-frame shift grows linearly with a slope of 1.97 px/frame^2, and extrapolates to rest at frame 0.66.
  This gives v(1.5) = 16.08 m/s, 0.8 % from the main route.

## Answer
15.95 m/s. Confidence is high: the routes agree within 1 %.
