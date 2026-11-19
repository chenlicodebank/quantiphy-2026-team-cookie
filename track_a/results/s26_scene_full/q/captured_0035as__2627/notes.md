# q_2627 — basketball velocity at 1.5 s (cm/s)

File fps = question fps = 24, so t=1.5 s is frame 36.
depth_info: the last line says "soccer_ball" a second time at t=1.6 s (2.412 m). Read as the basketball (it is
nearer than the soccer ball's 3.052 m, and 2.27 m at 0.6 s fits).

Method (vel.py): basketball centres = scene/tracks/basketball.csv fit_cx/fit_cy (checked; the ball is free and
rolling slowly left after the collision at frame 19-20). f = 0.5959*1280 = 762.8 px, principal point (640,360).
Back-projection ((u-cx)/f, (v-cy)/f, 1)*Z.
- Route A: depth from the pixel diameter (linear fit over frames 23-48), anchored at Z=2.412 m at frame 38.
  Per-frame speeds near frame 36 are about 36-40 cm/s. Forward difference 36->37 gives 39.9.
- Route B: depth interpolated linearly between the given depths (frames 14 and 38). Speeds are about 37-42 cm/s,
  and the forward difference 36->37 gives 42.5.
- Steps 34-37, leaving out the gap: 38.9 (A) / 41.5 (B).
Caveat: frame step 35->36 is doubled (about 76 cm/s), which suggests a dropped capture frame. A 5-frame centred
window that includes it gives 46-50 cm/s. A forward window over 36-41 gives 37.
Pixel diameter is about 69.4 px. The given depth predicts 73.4 px (5% smaller than predicted, OK).

Answer: 42 cm/s. This sits between the physical value (about 39-42) and window smoothings that include the gap
(about 46-48). Confidence moderate: about ±10%.
