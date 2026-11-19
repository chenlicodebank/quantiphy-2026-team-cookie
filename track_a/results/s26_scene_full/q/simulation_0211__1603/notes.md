# Q1603 — black cat to camera distance at t = 0.5 s (frame 12 at 24 fps; file fps is also 24)

Given: d(0) = 4.199 m, d(1.0) = 4.481 m, cat speed 0.94 m/s (prior).
The track (scene/tracks/cat.csv) shows steady walking with no stops, turns or occlusion over frames 0-24.

Route 1 (closed form): for a straight path at constant speed, d(t)^2 = d0^2 + 2 b t + v^2 t^2.
Solving with d(1) gives b = 0.782, so d(0.5) = 4.3168 m. Simple linear interpolation would give 4.340.

Route 2 (pinhole, measure.py): I solved for the focal length that makes |P(0) - P(24)| = 0.94 m
(back-projected with the given depths), then intersected the frame-12 ray with the P0-P1 line.
- Torso centre: f = 2099 px (HFOV 49 deg), depth at frame 12 = 4.313 m; the frame-12 point sits at
  0.49 of the way along the segment, which fits constant speed.
- Mask centroid: f = 2161 px, depth = 4.320 m.

Answer: 4.317 m. Confidence is high; the routes agree within about 0.2 %.
