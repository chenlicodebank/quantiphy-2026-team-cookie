# q_2191 – length of the string (cm)

File fps = question fps = 24. Lab convention f = 0.5959*1280 = 762.75 px, c = (640,360).

## Route 1 – 3D geometry (geo.py)
Back-projected the ball centre (scene/tracks/ball.csv centroids; ball and string position checked by eye on f14 only) at the six depth_info frames
(f7, f14, f22, f29, f36, f43) with the given distances. Pivot = hand pinch at image (636.5, 228) (string top,
confirmed on a 4x crop of f14); its depth was fitted so that the pivot-to-ball distances are as equal as possible:
pivot depth 1.489 m, distances 0.309-0.355 m, mean **0.331 m** (std 1.35 cm). Pivot y ±4 px changes it by ±0.6 cm.
Ball diameter from depth x pixel size: 0.062-0.068 m → radius ≈ 3.2 cm.

## Route 2 – pendulum period with g = 9.8 (period.py)
Turning points f3→f32.5 and f17→f46.5: T = 29.5 frames = 1.229 s. Swing amplitude from the 3D geometry
≈ ±47-49°, large-amplitude factor ≈1.045 → equivalent length ≈ 0.34 m (small-angle formula would give 0.375 m;
sinusoid fits give T 1.19-1.26 s, i.e. 0.32-0.35 m). Physical-pendulum correction for the ball is ~+0.1 cm.
Agrees with route 1 within ~3%.

## Answer
Pivot to ball centre ≈ 33.5 cm; string itself (pivot to top of ball) ≈ 33.5 - 3.2 ≈ 30.3 cm.
The ruler-measured "string length" is most likely the string from the hand to the ball (≈30 cm), but it could be
read as pivot to ball centre (≈33.5 cm). Answer 31.5 cm, between the two (within ~5% of either).
Confidence: moderate (mainly because of the definition of the length; measurement itself is ±1.5 cm).
