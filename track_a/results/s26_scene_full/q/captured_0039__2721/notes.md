# q_2721 — speed of the white ball at t = 1.0 s (frame 24, question_fps = file fps = 24)

Lab video, f = 0.5959*1280 = 762.8 px, principal point (640, 360). Prior (card length) not needed: depth_info gives
the ball distance at f24 (1.014 m) and f36 (0.737 m).

## Method (scripts: vel.py, linefit.py, overlay.py)
- Ball centres from scene/tracks/ball.csv (upper-arc circle fit); overlay check on f20-36 (frames/overlay.png): circles sit
  on the ball within ~1-2 px.
- Back-projected anchors: P24 = (-0.127, 0.123, 0.998) m, P36 = (-0.133, 0.132, 0.713) m; chord 0.286 m in 12 frames
  = 57.2 cm/s average over f24-36. Motion is almost straight toward the camera.
- Route C (main, linefit.py): ball assumed on the straight 3D line P24-P36; each frame's position s along the line found
  by matching the projected point to the pixel centre (residual <1 px for f23-40). Per-frame steps (mm):
  f22-28: 32.6, 21.5, 25.6, 18.4, 21.6, 26.0; f28-35 ~24-20; f35->36 = 40 (double step: probably a dropped frame, as
  noted in scene/); f36-40 ~18-20. The ball decelerates slowly.
  Speed at f24: 5-frame smoothed forward differences (f22-27) 58.3 cm/s; local linear fits 56-60; quadratic fits over
  f20-40 59.9 (no drop) / 60.9 (one dropped frame at 36, better rms).
- Route A (vel.py, ball-centre-plane depth model Z = k/(v - y_h) fitted to the two given depths): windows around f24
  give 44-59 cm/s (noisy, depends on v only). Route B (depth from smoothed apparent diameter): 66 cm/s, but its depths
  disagree with the given ones (0.348 m vs 0.277 m depth change f24-36), so rejected.

## Answer
58.5 cm/s (range of credible estimates 56-61). Confidence moderate: ±5-8 %, mainly from ±1-2 px centre noise and the
deceleration/dropped-frame question.
