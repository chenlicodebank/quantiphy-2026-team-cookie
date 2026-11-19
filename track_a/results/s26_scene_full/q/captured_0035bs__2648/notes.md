# q_2648 — soccer ball velocity at t = 0.9 s (cm/s)

- t = 0.9 s -> frame round(0.9*24) = 22 (file fps = question_fps = 24).
- Lab camera: f = 0.5959*1280 = 763 px, principal point (640, 360).
- Track: scene/tracks/soccer_ball.csv circle fits; overlays on frames 16-25 (frames/ov.png) show the circles on the
  right ball and its outline. The ball is kicked at frame 11-12 and hits/crosses the basketball at frames 24-26, so
  the velocity window is limited to frames 16-24 (free flight).
- Depth per frame: given 2.477 m at frame 22, scaled by apparent size, d_i = 2.477 * R(22)/R(i), with R from a
  linear fit of the circle radius over frames 14-24 (slope -0.424 px/frame, R22 = 29.93 px). Independent check with
  the background-difference mask area: equivalent radius 32.98 -> 30.44 px over frames 17-23, also -0.42 px/frame.
  So the ball moves away from the camera at ~0.95 m/s, which is a large part of the speed.
- 3D centre = d * r/|r|, r = ((u-640)/763, (v-360)/763, 1); velocity = slope of a linear fit (smoothing >= 5 frames).
  - frames 18-24: v = (65, -49, 95) cm/s, |v| = 125.2
  - 19-24: 124.0; 17-23: 128.1; 16-24: 130.3; 20-24: 126.5
  - Unsmoothed forward difference 22->23: 137 cm/s (noisy, 110-155 per frame).
  - Without the depth change (constant depth) it would be only ~93-106 cm/s; the size shrinkage confirmed by two
    methods shows the depth motion is real.
- The second 1.4 s depth line appears to be a mislabelled basketball depth; not needed here.
- Answer: 126 cm/s. Confidence moderate (±10 %), mostly from the depth-rate (radius-slope) uncertainty.
