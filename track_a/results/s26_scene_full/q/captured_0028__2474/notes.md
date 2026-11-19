# q2474 – ping pong ball velocity at t = 1.0 s (frame 24, question_fps = file fps = 24)

Method (lab card): f = 0.5959*1280 = 763 px, principal point (640,360). Ball centres from scene/tracks/ball.csv
(checked on a zoomed montage of frames 20-33, frames/montage.png). Back-projected with depth 1.805 m (given at t=1.0).

Depth during the fall: half-max horizontal ball width (width.py) stays ~15.5-16 px in frames 22-27 (constant), then
grows 16.7 -> 20.8 px over frames 28-31 (0.04*763/21 ≈ 1.45 m, which agrees with the given 1.4115 m at the apex). So
the ball moves toward the camera only after the first bounce (frame 26, near the table's back edge); during the
fall the depth is ≈ constant, and I used 1.805 m for frames 21-25. The given 1.557 m at t=1.1 does not match the
ball's apparent size at frame 26 (bounce/blur frame), so I did not use it for the velocity.

Results (vel.py, 3D):
- forward differences: 23->24 1.28, 24->25 1.83 m/s
- central difference at frame 24: 1.55 m/s; quadratic fit over frames 21-25: instantaneous 1.55, forward-diff 1.79 m/s
- fitted acceleration 11.6 m/s² (a bit above g; it could be a slight downward push or a small error in the scale)

The forward-difference convention gives ~1.80 m/s and the instantaneous value is 1.55 m/s. The reference's 5-frame
smoothing would cross the bounce at frame 26, so I can't reproduce it exactly. Answer: 1.68 m/s = 168 cm/s, between
the two (within ~8 % of each).
Confidence: moderate.
