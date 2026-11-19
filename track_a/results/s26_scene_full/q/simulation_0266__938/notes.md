# Q938 — width of the spacecraft (snowmobile-like black vehicle), metres

Prior: acceleration at 1.0 s = 4 m/s^2 (uniform acceleration from rest). 2D top-down video, static camera, fps 24 = question_fps.

## Method
- Track from scene/tracks/snowmobile.csv (frames 0-60 fully visible). Quadratic fit of x(t) (fit.py):
  - bbox centre (origin proxy): a = 513.0 px/s^2 (frames 2-60), 511.8 (10-40), 502.8 (14-34); rms 0.5 px
  - rear edge: 521 px/s^2; front edge: 505 px/s^2 (length shrinks ~0.75 px/frame, slight perspective)
  - Per-frame finite differences around frame 24 average ~550 px/s^2 but are noisy (±600).
  - Adopted pixel acceleration of the origin = 513 px/s^2 -> scale = 4/513 = 0.00780 m/px.
- Width = shorter horizontal extent across the vehicle = image-y extent of the mask (top-down view):
  366 px at frames 20-30 (mean 365.4 over 0-60; bbox y 536-902, confirmed on frame 24 with a grid).
- Width = 366 x 0.00780 = 2.85 m.

## Check
- Using rear-edge acceleration (521) -> 2.81 m; front-edge (505) -> 2.90 m. Spread ±2 %.
- Length 785 px -> 6.1 m; the length/width ratio ~2.1 is plausible for this vehicle.

Confidence: good (~3 %).
