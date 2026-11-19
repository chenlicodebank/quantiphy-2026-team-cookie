# q956 — speed of the phoenix at 1.0 s (prior: acceleration at 2.0 s = 2 m/s^2)

2D clip, 24 fps (file fps = question_fps, no re-timing). The scale comes from the prior's acceleration in pixels.

## Method
- Track: scene/tracks/phoenix.csv (I checked it: the record covers the phoenix in all 72 frames). x positions of
  body_s (smoothed torso), whole-mask centroid and head NCC (head_ok frames only), frames 0-66.
- fit.py: plain quadratic fit of x(t) over frames 2-66. a_px is 283-294 px/s^2, v(1.0) is 282-285 px/s and the start
  time t0 is about 0.00-0.04 s. A cubic term changes little, so the acceleration is constant.
- fit2.py (second route): quadratic plus wingbeat harmonics (best period 1.04 s) to remove the flap wobble.
  body_s gives a residual of only 1.5 px with a_px = 284.6 px/s^2 and t0 = 0.000. So the phoenix starts from rest at
  t = 0 with constant acceleration. Centroid and head give the same result within 1%.
- Scale: 2 m/s^2 / ~285 px/s^2. Because the acceleration is constant, v(t) = a * t, giving 2.00 m/s from the
  continuous fit. The benchmark convention (one-frame backward difference at frame 24) gives
  a * (1 - 1/48) = 1.958 m/s. The three tracks give 1.947-1.981 m/s.
- The vertical bobbing is assumed to belong to the body animation, not to the root. Since the prior's acceleration
  is exactly 2, the root moves horizontally with constant acceleration.

## Answer
1.96 m/s (backward-difference convention; the continuous value 2.00 is 2% higher). Confidence: high.
