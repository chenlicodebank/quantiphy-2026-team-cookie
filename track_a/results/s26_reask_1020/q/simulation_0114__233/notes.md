# q_233 — width of the plane (m)

2D top-down scene; yellow plane moves straight down the image (+y) from rest, uniformly accelerating.
Prior: acceleration = 18 m/s^2. question_fps = 24.0 (file fps 24.0024; frame indices used, t = frame/24).

## Method (fit.py)
- Quadratic fit of the plane's ref_y (blur-corrected centre, scene/tracks/plane.csv) vs frame, several windows:
  a = 343.57 (0-40), 343.79 (0-75), 343.64 (20-75), 343.81 (2-60) px/s^2 -> 343.7 px/s^2. Zero-velocity at frame ~0.
- Scale = 18 / 343.7 = 0.05237 m/px.
- Width = wingspan (across the direction of travel, image x). Re-measured at frame 0 with my own HSV mask:
  x 588-755 = 168 px (matches record). Width = 168 x 0.05237 = 8.80 m.
- Check: length 106-108 px -> 5.6 m; constant apparent width over clip (2D). Fit windows agree within 0.1%.
- Second route: mean second difference of ref_y (frames 2-74) = 0.620 px/frame^2 -> 357 px/s^2 (noisier, 0.5 px
  quantisation); gives 8.47 m. The quadratic fit is the more reliable estimate.

Answer: 8.80 m. Confidence: high (about +/-2%).
