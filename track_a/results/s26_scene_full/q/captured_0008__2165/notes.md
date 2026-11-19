# q_2165 — basketball distance from camera at t = 1.2 s

Question fps 24 = file fps 24; t = 1.2 s -> frame 29 (falling, just before the first impact at frame 30).

## Answer
depth_info states directly: t=1.2s, distance_ball_camera = 1.5640 m. Answer **1.564 m**.

## Consistency check (check.py)
Focal f = 0.5959 x 1280 = 763 px. Ball diameters from scene/tracks/ball.csv:
- frame 24 (t=1.0, Z=1.401 m): 114.5 px -> implied D = 0.2102 m
- frame 29 (t=1.2, Z=1.564 m): 102.5 px -> implied D = 0.2101 m
- frame 36 (bounce apex, Z=1.5225 m): 107.7 px -> implied D = 0.2149 m
The implied sizes agree (≈0.21 m, about right for a basketball), so the given depth at 1.2 s matches the image.
Size-based route: depth(frame 29) = 763 x 0.210 / 102.5 ≈ 1.56 m, which agrees.

Confidence: high (the value is given in depth_info).
