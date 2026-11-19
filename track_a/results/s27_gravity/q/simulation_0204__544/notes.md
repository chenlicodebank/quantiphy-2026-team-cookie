# Q544 – speed of the magnifying glass at t = 0.25 s

- question_fps = file fps = 24 -> t = 0.25 s is frame 6. Speed = backward difference (frame 5 -> 6) x 24.
- Scale from the prior (g = 9.8 m/s^2 before 0.5 s; the clip shows free fall on frames 0-11, impact ~f11.2).
  Pure vertical fall at constant depth, so one metres-per-pixel scale (2D convention).
- fit.py: quadratic fit y(t) to the scene/ track (bbox-centre y and mask-centroid y), several frame windows
  (0-11, 1-11, 0-8, 2-10). Pixel acceleration 7387-7469 px/s^2 -> 0.001312-0.001327 m/px. Fitted
  vertex t0 ≈ -0.003 s (released from rest at frame 0).
- Speed at frame 6: from the fit 2.266-2.289 m/s; from the raw frame 5->6 drop (72.5 / 71.8 px) 2.261-2.308 m/s.
- Second route: ideal free fall from rest at t=0, backward difference 0.5 g (2*6-1)/24 = 2.246 m/s; g*t = 2.45
  (instantaneous, not the convention). Measured value (2.27) agrees with the backward-difference ideal within 1 pct.
- Sanity: magnifier length 162 px x 0.00132 = 0.21 m, lens 103 px = 0.136 m – realistic.
- Answer: 2.27 m/s. Confidence high (±2 pct).
