# Q2677: ping pong ball velocity at t=1.4 s (cm/s)

- Lab video, 24 fps (file and question), so t=1.4 s is frame round(33.6) = 34. The depth_info is at t=0.9 (frame 22, 1.010 m) and t=1.4 (frame 34, 0.716 m).
- Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).
- Centres come from scene/tracks/ball.csv. I checked them against zoomed crops of frames 28-37 (frames/crops.png). The ball rolls across the table top until frame 35 and falls off the right edge from frame 36.
- 3D positions: P = unit ray(u, v) x distance. The distance was linearly interpolated in frame between the two given depths (model A, in vel.py).
  Check: model A gives a camera-Y slope against Z of about 2.6 deg, which matches the camera pitch from the horizon at y≈330 (2.25 deg). So the ball moves on the horizontal table plane, and model A is consistent.
- Per-frame forward speeds for frames 30-34: 88, 81, 87, 90, 92 cm/s. Smoothed velocities: frames 31→35 give 87.1, 32→35 give 89.2, 33→35 give 90.5, and 30→35 give 87.3 cm/s.
  Windows that run into frame 36, where the ball is falling and blurred, give 99-104 cm/s. I excluded them because the motion changes there.
- Plane-fit model B (Z from v) is noisy because the cy values are poor at frames 34-35 (a segmentation halo and a missed underside). Over the windows that end at frame 35 it gives 74-77 cm/s, and it is unreliable.
- Second route: lateral pixel speed of about 31 px/frame at Z=0.68 m gives 66 cm/s in X. The depth rate of 0.0245 m/frame gives 59 cm/s. Combined, that is about 89 cm/s.
- The average from frame 22 to 34 is 83 cm/s, so the ball speeds up slightly over this stretch.
- Answer: 88.5 cm/s. Confidence: moderate, about ±8%.
