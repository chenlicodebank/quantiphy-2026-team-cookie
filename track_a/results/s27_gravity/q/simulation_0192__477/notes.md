# Q477: speed of the box at t = 0.4 s (2D sim, 120 fps, so question_fps = file fps)

Prior: the box falls with a = 9.8 m/s^2 before 0.6 s. Track: scene/tracks/cardboard_box.csv (cy_ref_px, the template-matched
front-face centre). The motion is purely vertical and the face width stays 281.6 px, so there is no depth change.

- fit.py: quadratic fits of y(t) over frames 0-57 (and sub-windows) give a_px of about 2030-2056 px/s^2 and v0 of about 0
  (start time t0 within ±3 ms of 0). The window starting at frame 20 drifts the most (1928), because its lever arm is short.
- steps.py: the per-frame steps come in three kinds: zero (frozen frames), double (the next frame catches up) and single.
  The single steps follow step = k*(i-0.5) with k = 0.1415 px/frame^2, which is a_px = 2037 px/s^2, with a near-zero
  intercept. So the box is in free fall from rest at t = 0.
- Scale = 9.8/2037 = 0.00481 m/px. Check: box face 1.36 m x 0.95 m, which is plausible for a large box on a truck roof.
- Speed at frame 48 (one-frame backward difference for an ideal fall from rest) = g*(47.5/120) = 3.879 m/s.
  Second route: the measured single step at frame 48 is 6.90 px, which gives 3.98 m/s. g*t = 3.92.
  The frozen and double frames look like render jitter, so I answer with the ideal backward difference.

Answer: 3.88 m/s. Confidence: high (all routes fall within 3 pct).
