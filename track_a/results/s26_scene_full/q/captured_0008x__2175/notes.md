# q_2175 — basketball distance from camera at t = 1.2 s

Question fps 24, same as the file's fps; t = 1.2 s → frame round(28.8) = 29 (ball falling, one frame before first impact at frame 30).

## Answer
depth_info states the measured value directly: "t=1.2s, distance_ball_camera = 1.5640m". Answer = **1.564 m**.

## Check (check.py)
Using the apparent-size ratio from scene/tracks/ball.csv (circle-fit radius), with t=1.0 s (frame 24, r = 56.03 px, Z = 1.401 m) as reference:
- frame 29 (r = 50.99 px) → Z ≈ 1.401·56.03/50.99 = 1.540 m, 1.6 % from the given 1.564 (motion blur at frame 29 makes the fit slightly uncertain).
- frame 36 apex (r = 53.57 px) → 1.465 m vs given 1.5225 m (3.8 %).
Implied ball diameter 2·56.03·1.401/763 = 0.206 m, which is plausible for a small basketball. The given depth is consistent with the video.

Confidence: high, since the answer is the given measured depth.
