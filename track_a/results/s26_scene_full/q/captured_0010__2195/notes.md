# q_2195 – ball (pendulum bob) acceleration at t = 0.3 s

t = 0.3 s -> frame round(0.3 x 24) = 7. File fps = question fps = 24.
Lab camera: f = 0.5959 x 1280 = 762.75 px, principal point (640, 360).

## What the ball does
It is a pendulum on a string pinched at image (≈638, 226), swinging mostly towards and away from the camera.
Far turning points are at f3.0 and f32.6, near turning points at f17.0 and f46.4, so the period T ≈ 1.21-1.23 s.
At f7 the ball is 4 frames past the far turning point and swinging down and towards the camera.

## Measurements (geom.py, geom2.py)
- I back-projected the six given depths (f7, 14, 22, 29, 36, 43) using the ball centroids from scene/tracks/ball.csv.
  I then fitted the pivot depth along the pinch-point ray, and L, as a sphere through those points:
  pivot depth 1.488 m, **L = 0.334 m**, residuals ≤ 2.3 cm.
- Check of L against the period: T0 = 2π√(L/g) = 1.160 s. The large-amplitude factor at 48° is 1.046, giving 1.213 s.
  The measured period is 1.21-1.23 s, so they agree.
- Amplitude: I put the ball on that sphere along its pixel ray at each turning frame (the root agrees with the depth from apparent size).
  The angle between the string directions at the far and near extremes is 95-96° (f3-f17, f32-f17, f32-f46, f3-f46), so **θ0 ≈ 48°**.
- Phase: f7 is 4 frames (0.167 s) after the far turn, so θ(f7) ≈ 33° (from integrating the nonlinear pendulum ODE, pend.py).

## Answer
Pendulum acceleration vector at f7: tangential g·sinθ ≈ 5.3 m/s² and centripetal v²/L ≈ 3.3 m/s² (v ≈ 1.06 m/s).
That gives **|a| ≈ 6.3 m/s²** (the range is 5.8-6.6 for θ0 between 45° and 50°, and T from 1.20 to 1.23 s).
A 5-frame smoothing like the reference's lowers the oscillation by about 5%, so the answer is **6.2 m/s²**.
Under the other reading (rate of change of scalar speed = tangential only), the value is about 5.2-5.4 m/s².

## Second route (route2.py)
I took the sphere-constrained 3D positions from the image centroids and differenced them directly. A raw second difference gives |a| = 4.5 (f7) and 6.2 (f8).
Savitzky-Golay with a 5-frame window gives 5.7 (f7) and 6.25 (f8), and the speed at f7 is about 1.1 m/s (the model gives 1.06).
Wider windows are corrupted: the sphere root flips near the bottom of the arc (f9-13), so those results were discarded.
Differencing positions whose depth comes from apparent size alone (measure.py) gives 10-15 m/s². That is noise, because a 3% error in size is a 5 cm error in depth, and those values were rejected.

Confidence: moderate. The physics model is self-consistent (L, period, speed), and the main uncertainty is θ0 (±3°, about ±0.4 m/s²).
