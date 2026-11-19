# q_1389 – ball acceleration at t=1 s (frame 24, fps 24 = question fps)
Method: ball centre track from scene/tracks/ball.csv (frames 6-37, before pin impact). Depth Z ∝ 1/(u_vp - u) (ball moves along lane toward vanishing point);
scale and focal length from the prior (diameter 0.21 m) and depth_info (9.391 m at frame 12): f ≈ 3600-3850 px.
3D positions -> per-frame speed; linear/quadratic fit of speed over frames 7-37.
Result: speed ≈ 3.6-4.0 m/s, decreasing (rolling deceleration). Accel = -0.33 (u_vp fitted 5377) to -0.41 (u_vp 5680) m/s^2; quadratic fit at frame 24: -0.32 / -0.40.
Answer magnitude 0.36 m/s^2 (deceleration). Confidence moderate (~±15%), sensitive to vanishing-point estimate.
