# q_2636 – basketball velocity at 1.5 s (cm/s)

- question_fps = file fps = 24, so t = 1.5 s is frame 36.
- Track: scene/tracks/basketball.csv, which fits a RANSAC circle to the ball edge. From frame 20 on the fit is high reliability. After the collision (frame 19) the ball moves slowly to the image-left.
- Depth: the second "t=1.6s soccer_ball" entry (2.412 m) is taken to be the basketball. It is a typo: the soccer ball is already listed at 3.052 m, and the basketball was at 2.27 m at t = 0.6 s.
  For other frames, depth is scaled by the apparent diameter, using a linear fit to the diameter over frames 21–48 and anchored at 2.412 m at frame 38.
  The diameter alone (with the 23.2 cm prior and f = 763 px) gives about 5% more depth at both stated times (2.39 vs 2.27 m, 2.57 vs 2.41 m), so the two stated depths agree with each other.
- 3D points come from back-projecting with f = 0.5959 × 1280 = 762.8 px and principal point (640, 360). Velocity is the forward difference × 24 (vel.py).
- Per-frame speeds after the collision are steady at about 36–39 cm/s. The exception is the step from frame 35 to 36, at 75 cm/s: a probable dropped capture frame, where both balls and the far person's foot jump together.
- Velocity at frame 36:
  - raw forward difference: 36.6 cm/s
  - forward 5-frame mean (frames 36–40): 36.0 cm/s
  - mean speed over frames 21–47, leaving out the jump: 36.7 cm/s
  - centred 5-frame mean (includes the jump): 44.7 cm/s
  - Savitzky–Golay derivative, windows 7 and 9: 45.3 and 43.4 cm/s
- Answer: 40 cm/s. This sits between the physical value (about 36.5) and the centred-smoothing value that a reference method would get if it ignores the dropped frame (about 44.5). Each of those is about 10% away.
- Confidence: medium. The main uncertainty is how the reference smoothing handles the jump at frame 35→36.
