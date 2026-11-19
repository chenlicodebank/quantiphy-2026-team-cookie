# q3164 – ball velocity at t = 2.00 s (frame 60, 30 fps; file fps = question fps)

Method (fit.py): used scene/tracks/ball.csv bg-fixed centres (camera drift removed) in free flight, frames 54–96
(release to before the first bounce, frames flagged as degraded excluded). Frame 60 was checked on a zoomed crop:
the ball centre is about (730, 327) px, which agrees with the track (729.5, 329).
- Quadratic fit of y(t): pixel acceleration 1856 px/s² (rms residual 1.8 px). Scale = 9.8 / 1856 = 0.00528 m/px.
  Sanity check: ball diameter 43 px × 0.00528 = 0.227 m, close to a real basketball (0.24 m).
- At t = 2.0 the fit gives vx = 456 px/s and vy = −699 px/s, so |v| = 835 px/s = **4.41 m/s**.

Second route: raw frame differences at frame 60. Forward (60→61) gives 4.34 m/s, backward 4.75, and
central 4.55. Fits over sub-windows give ay from 1804 to 1897 px/s², which shifts the answer by about ±3 %.
Answer: 4.4 m/s. Confidence: moderate-high (about ±5 %).
