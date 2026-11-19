# Q940: speed of the spacecraft at 1.0 s (m/s)

Prior: acceleration at 1.0 s = 4 m/s^2. 2D top-down render, 24 fps (file fps = question fps), static camera.
The single moving object (the black vehicle the scene record calls a "snowmobile"; it looks like a
spacecraft/hover-vehicle) speeds up in a straight line toward -x.

## Method (fit.py)
- I fitted a quadratic x(t) to the record's per-frame positions (cx_est = bbox centre, plus the rear edge x1 and the
  front edge x0 as independent reference points), using several frame windows (1-60, 4-60, 10-50, 1-30, 1-40).
- Residuals were 0.3-1 px RMS, so the acceleration is constant: a_px ≈ 513 px/s^2 (centre), 520 (rear), 505 (front).
  Start time t0 ≈ 0.000-0.017 s, so the vehicle starts from rest at frame 0.
- Scale = 4 / a_px m/px. Speed at frame 24 is the one-frame backward difference of the fit,
  |x(24) - x(23)| * 24 ≈ 500.5 px/s (centre).
  Answer = 4 * v_px / a_px ≈ 3.90 (centre), 3.89-3.91 (rear), 3.89-3.92 (front).
- Analytic check: for uniform acceleration from rest at t = 0, the backward difference at frame 24 gives
  a * (1 - 1/48) = 3.917 m/s. The instantaneous value would be 4.0 m/s.

## Answer
3.91 m/s. Confidence: high. The ratio does not depend on the scale, and all routes agree within ±0.5 %.
The largest possible gap is the convention: an instantaneous-speed reference would give 4.0 m/s, about 2 % higher.
