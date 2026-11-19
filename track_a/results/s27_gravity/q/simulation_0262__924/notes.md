# q_924 – speed of red cup at t = 0.625 s (frame 15 at question_fps 24; file fps also 24)

Method (2D, scale from prior g = 9.8 m/s^2): `measure.py` re-measures the red body (HSV S>90) per frame;
quadratic fits of the body bottom and body top over frames 6–18 (free fall, unclipped, before the f19 impact).
- bottom: a = 11.36 px/frame^2 -> 0.001497 m/px; backward diff f14->f15: raw 163 px -> 5.86 m/s, fit 5.81 m/s
- body top: a = 11.03 px/frame^2 -> 0.001542 m/px; raw -> 6.14 m/s, fit 6.04 m/s
- Origin is about midway between these, so the mean of the two is ≈ 5.93 m/s.
Second route: both fits put zero velocity at frame ≈ 0 (−0.27 and +0.30 frames), so the cup was released at t ≈ 0.
Backward difference at frame 15 = g·(0.625 − 1/48) = 5.92 m/s, which agrees.
Scene record matches my re-measurement within 1 px.
Answer 5.92 m/s. Confidence: high (about ±3%).
