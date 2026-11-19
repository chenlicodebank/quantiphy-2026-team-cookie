# q_964 – speed of the phoenix at 1.0 s

Prior: acceleration at 2.0 s = 2 m/s^2. 2D top-down clip, 24 fps (file fps = question fps). Camera static.

## Method
- Used scene/tracks/bird.csv (beak_x, body_cx, bbox_cx, cx), all frames. fit.py fits x(t) with a quadratic.
- Every tracked point fits a quadratic from rest: a ≈ 239–242 px/s^2, v(0) ≈ 0 to 5 px/s (≈0), and
  v(1.0)/a = 0.98–1.03. The residual rms is about 12 px, and it pulses with the wingbeat (the animation moves the
  body around the origin). The underlying origin motion is therefore uniform acceleration from rest at t = 0.
  Frames 0 and 1 look the same because the expected move by frame 1 is only 0.2 px.
- With constant a = 2 m/s^2 (the prior), the scale cancels: v(1 s) = a·1 s = 2.0 m/s. The benchmark speed is a
  one-frame backward difference at frame 24: 0.5·a·(24²−23²)/24² · 24 = 1.958 m/s.
- Scale for reference: 2 / 240 px/s^2 ≈ 0.0083 m/px.

## Check
- A cubic fit (frames ≥1) gives velocity at 1 s of about 237 px/s and acceleration of about 240 px/s^2 near
  1–2 s, which agrees.
- The fit is the same whichever tracked point is used (beak, body, bbox centre).
- If the motion started at frame 1 instead, the answer would be 1.875 m/s. The fit's v(0) ≈ 0 favours a start
  at t = 0.

Answer: 1.96 m/s. Confidence: high.
