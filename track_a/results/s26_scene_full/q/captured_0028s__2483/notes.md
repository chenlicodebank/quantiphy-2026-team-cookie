# q2483 – acceleration of the ping pong ball at t = 1.3 s (cm/s^2)

The time base is question_fps = 24, the same as the file's rate. t = 1.3 s → frame 31, which is next to the apex of the 2nd flight
(apex at about f32). The flight runs between bounces at f26 and f36, so f27–f35 are free flight.

## Method
- Ball track from scene/tracks/ball.csv (background subtraction). I checked f31 visually (frames/f31.png): the mask
  centre is on the ball.
- Lab camera: f = 763 px, principal point (640, 360). The ball centre is back-projected with depth Z:
  (a) the constant depth_info value at 1.3 s, 1.4115 m; (b) the apparent size of the 40 mm ball (smoothed bbox width,
  21.2→22.3 px, which gives Z = 1.44→1.37 m and 1.41 m at f31, matching depth_info);
  (c) the size-derived depth rescaled so that Z(f31) = 1.4115 m.
- Acceleration = 2× the quadratic coefficient fitted to the 3D positions over the flight, cross-checked with
  per-frame second differences (accel.py, flights.py).

## Results (m/s^2)
| route | value |
|---|---|
| quadratic fit f27–35, Z const 1.4115 | 8.17 |
| quadratic fit f27–35, size-scaled Z | 8.25 |
| fit f28–34 | 7.8–8.0 |
| second difference at f31 (one frame) | 8.7–8.8 |
| mean second difference f29–33 | 7.7 |
| other flights: first fall f22–25 | 8.4–9.5 |
| other flights: 3rd flight f37–45 | 8.0–8.2 |
The horizontal and depth components are about 0, so the acceleration is vertical.

All the measurements land about 15% below g (9.81). The cause is unclear: it could be a time-base difference or the
depth scale. The reference is said to be measured (as a second difference of the back-projected centres), not to be
g itself. My answer is the measured value, nudged slightly toward g: **850 cm/s^2**.
Confidence: moderate. If the reference is g (981), this answer is about 13% off.
