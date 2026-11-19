# q_2205: ball velocity at 0.3 s (captured_0010X, pendulum)

The question frame rate is 24 fps, the same as the file, so t = 0.3 s is frame 7. The camera is f = 0.5959 x 1280 = 762.75 px, cx,cy = (640, 360).
The ball track in scene/tracks/ball.csv was checked on frame 7 (zoomed crop). The centroid sits on the ball.

The ball is a pendulum swinging mostly along the line of sight. The given depths are at frames 7, 14, 22, 29, 36 and 43, never on
adjacent frames, so speed cannot be taken directly from back-projected depths.

## Route A (main): 3D damped-pendulum fit (pendfit.py)
- Model: pivot (pixel position and depth), length L, gravity direction (pitch and roll), swing azimuth, amplitude θ0, ω, phase and damping,
  plus the ball diameter.
- Data fitted: the pixel centroids of all 49 frames (σ 1.5 px), the 6 given depths (σ 2 cm) and the equivalent diameters.
- Result: L = 0.355 m, ω = 5.21 rad/s, so g/ω² = 0.360 m, consistent with L and with g = 9.8 (the prior).
  θ0 = 0.775 rad, ball D = 7.2 cm. Pixel RMS is 3.2 / 2.0 px; depth residuals are within ±4 cm.
- A fit with ω tied to sqrt(g/L) gives the same result.
- Speed at 0.3 s:
  - instantaneous: 1.14 m/s
  - forward difference at frame 7: 1.19 m/s
  - backward difference: 1.00 m/s
  - mean of the forward speeds over frames 5–9: 1.13 m/s
  - (p9 − p5)/4 frames: 1.06 m/s

## Checks
- Energy, with g: v = sqrt(2 g L (cos θ − cos θ0)) with θ(frame 7) = 0.49 rad gives 1.07 m/s.
- Route C (routeC.py): depth from apparent size, Z = f·D/diam, with D from the given depths. A quadratic fit to the 3D
  points over frames 3–11 gives 0.90–1.40 m/s depending on the window, centred near 1.1 m/s. It is noisy because the diameter is ±2 px.
- Sphere-about-pivot intersection (measure.py) gives 0.95–1.04 m/s. This route is less reliable: the root choice is ambiguous and the
  residual at frame 7 is 2.3 cm.

## Answer
1.13 m/s, which is the 5-frame-smoothed forward-difference convention. Confidence: moderate, about ±10%.
