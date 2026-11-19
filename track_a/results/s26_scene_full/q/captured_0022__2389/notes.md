# Q2389 – ping pong ball velocity at 0.8 s (cm/s)

- The file and the question both use 24 fps. t = 0.8 s is frame 19. The depths are given at frames 14 (1.751 m), 19 (1.687 m) and 29 (1.526 m).
- **Camera:** the lab camera, f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- **Ball centre:**
  - Route 1 is the record track (scene/tracks/ball.csv). I checked it on a zoomed frame 19, where the ball is at about (432, 412).
  - Route 2 is my own template-matching re-track (track2.py). It has a constant offset of about 2.5 px in y, but the per-frame steps are the same: about 3.7 px/frame over frames 16-22 in both.
- **3D:** P = r x unit ray(u, v). r is the depth at each frame, interpolated from the three given depths in three ways: piecewise linear, a quadratic through the three points, or a straight-line fit (vel.py).
- **Speed near frame 19** (cm/s):

  | Depth interpolation | Centred 5-frame | Forward 5-frame (19→23) | Linear fit over 16-22 |
  |---|---|---|---|
  | Piecewise linear | 39.9 | 43.6 | 39.8 |
  | Quadratic | 38.7 | 40.9 | 38.7 |
  | Straight line | 41.3 | 41.6 | 41.3 |

  Both tracks give the same numbers to within about 0.5.
- The depth rate (about 1.3-1.6 cm/frame) is the largest part of the motion. The lateral part is about 0.82 cm/frame.
- **Answer:** about 40 cm/s. The methods spread from 38.7 to 41.6, so I expect the answer to be within about 5%. The main uncertainty is how the depth varies between the three given values.
