# q_678 — acceleration of the robot vacuum at t = 1 s

- 2D top-down render, 24 fps (file fps = question_fps = 24, so no re-timing). t = 1 s -> frame 24.
  Acceleration = (speed(24) - speed(23)) x fps, with speed(i) = |p(i) - p(i-1)| x fps.
- Track: scene/tracks/robot_vacuum.csv, circle-fit centre (x, y). Frames 8-36 are not occluded, centre good to ~0.3 px.
- Scale: the prior diameter 0.438 m over the fitted circle diameter 117.9 px (median 117.75 over all frames,
  118.0 over frames 10-34) gives 3.715e-3 m/px. One scale holds because the robot moves on the floor.
- The raw difference s24 - s23 = 0.097 px/frame^2 is noise-dominated: the step noise is about 0.1-0.2 px.
- Route 1 (fit.py): polynomial fits of degree 3-5 to x(f) and y(f) over windows from 8-36 to 15-33, then the
  one-frame difference of the fitted speed. Result 0.197-0.222 px/frame^2, mostly 0.20-0.21.
- Route 2 (route2.py): quadratic or cubic fits to the per-frame speed series over windows 14-34 to 20-28,
  slope at 23.5. Result 0.192-0.218. Linear fits give 0.16-0.18 and are biased low, because the speed curve
  flattens toward its peak near frame 25-27.
- Adopted 0.205 px/frame^2 x 576 x 3.715e-3 = 0.439 m/s^2.
- Confidence: moderate. The px/frame^2 value is good to about ±5-8 %. The acceleration is falling toward zero here,
  so the reference's exact value depends on the true curve.
