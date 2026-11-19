# q_2207 — acceleration of the pendulum ball at t = 0.3 s (frame 7)

Clip: lab pendulum, 24 fps (file and question fps are the same), f = 0.5959*1280 = 763 px, principal point (640, 360).
The ball track in scene/tracks/ball.csv (mask centroids) was checked on frame 7: the centroid sits on the ball, which is motion-blurred.

## 3D reconstruction (fit3d.py)
- Model: a pendulum with its pivot on the ray of pivot pixel (637, 229), pivot depth Zp, and length L. Each frame's ball
  depth is where the ball's pixel ray meets the sphere of radius L. The root is chosen using the size depth f*D/diam_px.
  Zp, L and D were fitted to the 6 given camera distances and to the size depths.
- Fit: Zp = 1.456 m, L = 0.320 m, D = 0.072 m. Model distances at the given times: 1.716 / 1.363 / 1.488 / 1.737 / 1.701 / 1.366
  against the given 1.706 / 1.344 / 1.4605 / 1.784 / 1.717 / 1.350. All are within 3 %.
- Direct back-projection at frame 7: Z = 1.705 m, and the implied diameter D is 0.077 m.
- Period check: L = 0.32 m with a ±47° amplitude gives T ≈ 1.19 s (28.5 frames). The observed far turning points are at frames 3 and ~32.5,
  which is 29.5 frames. That agrees within 3 %.

## Acceleration at frame 7 (accel.py)
- Route B (physics on the fitted geometry): vertical = the bisector of the far and near extreme directions. The half-amplitude is 46.9°, and θ(frame 7) is 31.5°.
  a_t = g sinθ = 5.12 m/s², a_c = 2g(cosθ − cosθ0) = 3.31 m/s², so **|a| = 6.10 m/s²** (v = 1.03 m/s).
- Route A (finite differences of the reconstructed 3D track):
  - raw second difference: |a| = 6.5 m/s²
  - with 5-frame smoothing: |a| ≈ 4.6–5.5 (frames 6–7)
  - d(speed)/dt ≈ 3.9–5.3
  Smoothing slightly attenuates the curvature.
- The gravity prior (9.8) is the scale of the physics. The ball is a pendulum bob, not in free fall, so its acceleration is below g.

Answer: the magnitude of the acceleration vector, ≈ 6.0 m/s². The physics value is 6.1; the finite-difference routes give 4.6–6.5.
If the asked quantity is the tangential acceleration (rate of change of speed), it is ≈ 5.1 m/s².
Confidence: moderate. The convention (vector magnitude vs tangential) and the noise in the reference's clicked points are the main uncertainties.
