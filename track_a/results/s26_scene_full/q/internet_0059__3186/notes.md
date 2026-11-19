# q3186 – ball velocity at 3.00 s (internet_0059)

Time base: fps = question_fps = 30, so t = 3.00 s is frame 90 (the ball is falling and in clear view).

## Scale from the prior (g = 9.8 m/s^2)
- The track is scene/tracks/ball.csv, using the background-compensated centre (cx_bg, cy_bg); the camera drifts slowly.
  I checked it with my own red-mask bbox centres (check.py). Frames 84-90 and 94-97 agree within about 1-2 px. Frames 91-93
  touch the poster, so I kept the record's values there.
- A parabola fit of cy_bg against t over frames 66-97, leaving out 77-80 (apex frames where the top is cut off), gives
  a_px = 4956 px/s^2, so the scale is 9.8/4956 = 0.001977 m/px.
  - Rising part only (66-76): 5330 px/s^2. Falling part only (81-97): about 4750 px/s^2. The difference is probably
    perspective or rolling shutter.
  - Sanity check: ball diameter 121 px x 0.001977 = 0.239 m, the size of a real basketball. This supports the
    whole-flight scale.

## Velocity at frame 90
Velocity uses the forward difference (frame 90 to 91), lightly smoothed with the fits (fit.py).

| Route | px/s | m/s |
|---|---|---|
| Whole-flight fit, evaluated at the forward-difference midpoint t = 3.0167 (vx ≈ 1338, vy ≈ 1893) | ≈ 2318 | 4.58 |
| Local fit over frames 84-96 at t = 3.0167 | ≈ 2299 | 4.55 |
| Raw forward difference (90 to 91), raw positions | | 4.69 |
| Raw backward difference (89 to 90) | | 4.27 |
| Centred fit derivative at t = 3.000 | | 4.45 |

Answer: **4.58 m/s** (speed magnitude). Likely range 4.45-4.7. Medium-high confidence; the main uncertainty is the
scale choice (whole-flight or falling-only acceleration, about ±5%).
