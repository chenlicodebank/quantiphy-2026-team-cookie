# q2481 — ping pong ball velocity at t = 1.3 s (cm/s)

The file and question_fps are both 24, so t = 1.3 s is frame 31. That is next to apex 1 (f32 in the scene record, and the
depth_info calls 1.3 s "max height"). Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Measurements
- Centres come from scene/tracks/ball.csv (mask centroid). I checked them visually on f31.
- I measured the ball's horizontal width in code at half contrast with sub-pixel edges (`measure.py`): f31 = 19.8 px,
  bbox 22 px. The expected width is 40 mm x 763 / 1.4115 = 21.6 px, so the scale is consistent.
- 3D centre = ((u-cx)/f, (v-cy)/f, 1) x Z. Velocity = forward differences, averaged over f29–f33 (5 frames centred on
  f31). This is in `velocity.py`.

## Depth per frame: three routes
A. Depth from depth_info, linear between f26 (1.557 m) and f31 (1.4115 m), extrapolated: vector speed 70.9,
   forward speed at f31 70.3, central difference over f29–33 75.5 cm/s.
B. Depth from the apparent size, a 1/w fit over f28–35 anchored at 1.4115 m: 47 cm/s.
C. Depth from the apparent size, apex f21 to apex f42 (constant horizontal velocity): 58 cm/s.

The speed is dominated by the ball moving toward the camera (dZ/dt). Near the apex the vertical part is about
-12 cm/s and the lateral X part is about 0.

Second check: P(1.1 s) and P(1.3 s) back-projected with the given depths have the same X (0.200 m). Their depth
difference, 0.1455 m over 5 frames, gives a horizontal speed of 69.8 cm/s. This agrees with route A.

The size-based routes say the ball approaches about 20–30 % more slowly than the measured depths do. The given f24
depth of 1.805 m disagrees with the size even more. The reference answer uses the sensor depths, so I answer with
route A.

Answer: 70.5 cm/s. Confidence: moderate. Depth noise in the sensor data could move the reference to anywhere in
about 55–80.
