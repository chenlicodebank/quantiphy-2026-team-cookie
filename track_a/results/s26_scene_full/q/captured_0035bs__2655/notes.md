# q2655 — soccer ball velocity at 1.3 s (cm/s)

- t = 1.3 s → frame 31 (question_fps 24 = file fps). This is after the ball collision at frame ~25; the soccer ball moves right/down in the image and slowly toward the camera.
- depth_info: the second "t=1.4 soccer" entry is presumably mislabelled. Apparent sizes show the basketball at 1.4 s is about 2.62 m away (2.7777 × 61.5/65.3), which matches 2.602, so the basketball is 2.602 and the soccer ball 2.373 at 1.4 s (frame 34). Soccer ball at 0.9 s (frame 22) = 2.477 m.
- Track checked: the scene track at frame 31 is (674, 490), diameter about 60 px, and matches the frame crop (f31.png). Frame 33 is about 3-4 px off and frame 36 follows a dropped frame, so the fit windows avoid relying on them.
- Method (vel.py): back-project the centres with f = 763 px and principal point (640, 360), depth linear in time from 2.477 (frame 22) to 2.373 (frame 34), then fit a linear least-squares slope of the 3D position over a window around frame 31.
  - Windows 27-35: 53.3; 28-34: 53.8; 30-32: 55.5; 29-33: 60.0 (frame 33 outlier); forward difference 57.2, backward 53.9 cm/s.
  - Components (27-35): about (44, 18, -25) cm/s.
- Second route: depth from the ball's apparent size instead of the given depths. The 1/radius trend over frames 25-48 gives dz/dt of about -0.06 to -0.11 per second relative (-0.15 to -0.26 m/s), close to the -0.25 m/s z-component of the linear model. With size depths the speed is 48-59 cm/s; with constant depth (no z motion) it is 50-52 cm/s.
- Answer: **54 cm/s**. Confidence moderate (±10%): the depth rate is the main uncertainty.
