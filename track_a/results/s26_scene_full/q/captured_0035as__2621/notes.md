# q_2621 — soccer ball velocity at 0.6 s (cm/s)

- t = 0.6 s -> frame round(0.6*24) = 14 (file fps = question fps = 24). Soccer ball in free flight frames 12-19
  (kick contact ends ~frame 9, collision with basketball at 19->20, a dropped capture frame at 11->12, so window 12-19).
- Centres from scene/tracks/soccer_ball.csv (automatic, ±1 px), checked visually at frame 14 (blob centre ~(524,410)).
- Camera: f = 0.5959*1280 = 762.8 px, principal point (640,360). Position = dist * unit ray, dist(14) = 2.758 m (depth_info).
- Depth at other frames: dist(i) = 2.758 * d(14)/d(i), d = linear fit of the blur-robust minor-axis diameter
  (52.6 px at frame 14, +0.4 px/frame -> ball approaching camera ~40 cm/s).
  Consistency: at 1.6 s (frame 38, d≈45.8) this gives ~3.17 m vs given 3.052 m (4% off; fine).
- Results (vel.py):
  * linear fit of 3D position over frames 12-19: 166.1 cm/s (with depth change), 160.4 cm/s (constant depth)
  * mean of forward-difference speeds frames 12-17: 167.5 cm/s; single forward diff at 14: 171.0 cm/s
  * pixel speed 450 px/s.
- Uncertainty mainly from radial (depth) component (0 to ~-60 cm/s) -> 160-172 cm/s.
- Answer: 166 cm/s. Confidence: moderate-good (~±5%).
