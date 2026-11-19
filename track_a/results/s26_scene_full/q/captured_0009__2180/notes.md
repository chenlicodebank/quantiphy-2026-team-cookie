# q_2180 — basketball distance from camera at 1.8 s

Question: the basketball's distance from the camera at t = 1.8 s (frame round(1.8 x 24) = 43; file fps = question_fps = 24).

## Answer
depth_info gives this value directly: "t=1.8s, distance_ball_camera = 1.5835m". These are measured camera distances to the
ball centre, which is how the reference values were made. **Answer: 1.5835 m.**

## Sanity check (check.py)
I compared depths from the ball's apparent size (Z ∝ 1/D) against the held frame (Z0 = 1.321 m, D0 = 145.5 px from scene/tracks/ball.csv):
- frame 43: D = 108 px -> Z ≈ 1.78 m; frame 46 (apex): D = 112 px -> 1.72 m (given value at 1.92 s: 1.5795 m).
- Both size-based values come out about 12% above the given depths. Two things make the size check unreliable: the held
  diameter was fitted while the hands hid part of the ball, and the mask edges are soft/blurred. Either way it confirms the
  direction (the ball is farther than at t = 0, and 1.8 s is near the apex, close to the given 1.5795 m at 1.92 s).
- The given 1.5835 m at 1.8 s matches the given 1.5795 m at 1.92 s (the ball moves only a little near the apex). So the depth_info is
  self-consistent, and I used it as given.

Confidence: high (the question's own depth_info states the value).
