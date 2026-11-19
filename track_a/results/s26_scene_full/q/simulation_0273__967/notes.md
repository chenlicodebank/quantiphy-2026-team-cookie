# q_967: phoenix speed at 1.0 s

Prior: acceleration at 2.0 s = 2 m/s^2. 2D video, 24 fps (file rate equals question_fps). Only the ratio v(1)/a is needed, so no pixel scale is required.

## Method
I took the x tracks from scene/tracks/phoenix.csv (head_x, bbox_cx, cx_mask, cx_green, bbox_x1). The y motion is negligible.
- fit.py: quadratic fit of x(t) over all frames (and over frames 2 onward). a is about -275 to -294 px/s^2, v0 is about 0 (-19 to +14 px/s), and v(1)/a = 0.95-1.07 depending on the reference point.
- fit2.py: quadratic plus wing-beat harmonics (period about 12.5 frames). v(1)/a = 0.965 (head), 0.991 (bbox centre), 1.023 (green body), 1.023 (tail end), 1.037 (mask centroid).
- Frames 0 and 1 are identical, which fits a start from rest at t = 0 (expected shift 0.5·a/24^2 ≈ 0.25 px).

The motion is consistent with uniform acceleration from rest at t = 0, so v(1) = a·1 s = 2.0 m/s. The backward-difference convention would give a·47/48 = 1.96 m/s.
The mean v(1)/a across the reference points is about 1.00.

## Confidence
Good: a ±5% spread between reference points, caused by the wing beat moving each reference point back and forth.
