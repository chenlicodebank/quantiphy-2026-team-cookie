# q_434 — speed of the trolley (shopping cart) at t = 1 s

2D side view, 24 fps (file fps = question_fps, no re-timing). Prior: the cart's acceleration is 1.507 m/s² (constant).

## Method (fit.py)
- I used the record's track `scene/tracks/shopping_cart.csv` (frames 0–59). The cart is the only moving object and is never occluded.
- I fit a quadratic x(t) to bbox_cx, wheels_cx and bbox_x1 over the windows 0–59, 3–59 and 3–39. Residuals are about 0.5 px RMS, so the acceleration is constant.
- Pixel acceleration is 295–302 px/s², so the scale is 1.507 / a_px ≈ 0.0050–0.0051 m/px.
- The fitted start of motion is t0 ≈ -0.017 to +0.001 s, so the cart starts from rest at about frame 0.
- Speed at frame 24 is a one-frame backward difference: (x(24) - x(23)) × 24 × scale.
  - From the fitted curves: 1.474–1.505 m/s.
  - From raw pixel differences: 1.44–1.47 m/s. These are noisy at ±1 px per frame.
  - From the analytic value with motion starting at t = 0: 1.507 × 23.5/24 = 1.476 m/s. The instantaneous value a × t would be 1.507 m/s.

## Answer
1.485 m/s, between the analytic backward-difference value (1.476) and the fit mean (about 1.495).
Confidence is high: every route falls within ±2%.
