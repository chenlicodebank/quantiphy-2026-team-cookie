# q1389 acceleration of ball at t=1 s (frame 24, fps 24 = question_fps)
Method: used scene/tracks/ball.csv ball centres (frames 6-37, before impact). f ~ 3660 px from
diam fit (82 px at frame 12) x 9.391 m / 0.21 m. Depth along the ball's straight path Z ∝ 1/(vpx - u) with the
vanishing point x ~5400-5750 (scene notes 5680), scaled to 9.391 m at frame 12; 3D path length = Z * sqrt(1+a^2+b^2).
Speed falls from ~3.9 m/s (frame 7) to ~3.5 m/s (frame 37): slowing down. Quadratic fit of path position
gives a = -0.34 (vp 5405) ... -0.45 (vp 5750); -0.43 at vp 5680; per-frame speed slope gives -0.40..-0.43.
Answer magnitude 0.41 m/s^2 (deceleration, ball slowing). Confidence moderate (~15%).
