# q_3173: ball velocity at 1.00 s (prior g = 9.8 m/s^2)

Time base: file fps = question_fps = 30, so t = 1.00 s is frame 30. The ball is in free flight there, rising: it is released at frame 22 and reaches its apex at frame 42.

Method (`fit.py`): I used the ball centre track from scene/tracks/ball.csv (edge circle fit, about ±0.5 px in flight).
- Scale: I fitted a parabola to the vertical centre position over free-flight windows. Pixel gravity is about 2004-2018 px/s^2 in every window that includes the rising phase. Scale = 9.8 / 2010 ≈ 0.00487 m/px.
- At frame 30 (camera-drift-stabilised track):
  - Parabola-fit instantaneous velocity: vy = -4.01 m/s, vx = +0.20 m/s, |v| = 4.01-4.03 m/s.
  - Forward difference (annotator convention): |v| = 3.86 m/s. Backward difference: 4.17 m/s. Their mean (central difference) is 4.01 m/s.
- Raw track (no drift correction, which is probably what the annotators used): the fit gives 4.10 m/s and the forward difference gives 3.96 m/s.

Second-route check: fit windows 23-42, 25-40, 24-62 and 26-60 all give 4.01-4.03 m/s (stabilised track) at the same scale. The descending half alone gives a lower pixel g (about 1925 px/s^2), but the speed it implies changes by only about 3%.

Answer: 4.0 m/s, the centre of the plausible range 3.9-4.1. Confidence: high, within about 4%.
