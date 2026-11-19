# Q443: speed of the box (tool box / crate) at t = 1.5 s

- 2D scene, fps 24 (the same as question_fps). t = 1.5 s is frame 36, which is inside the steady slide down the ramp (frames 22–44).
- Track: scene/tracks/crate.csv, the rectangle centre from the template fit. Frame-to-frame motion is smooth, and a quadratic fit to path length leaves an rms residual of 0.2–0.3 px.
- Scale from the prior: the slide acceleration fitted over frames 22–44 is 0.697 px/frame² = 401.5 px/s². With a = 1.58 m/s², that gives 0.003935 m/px.
  Other fit windows (24–44, 26–42, 22–36, 30–44, 24–40) give 0.687–0.706 px/frame².
- Speed at frame 36 as a backward difference of the fitted path, s(36) − s(35): 28.79 px/frame = 691 px/s, so **v = 2.72 m/s**.
  Across the windows the result is 2.69–2.76 m/s.
- Second route (independent scale): the free fall in frames 0–7 has a step increase of about 4.33 px/frame² = 2494 px/s². Setting this equal to g = 9.81 m/s² gives 0.003933 m/px. That matches the prior-derived scale to within 0.1 %, and it gives v = 28.79 × 24 × 0.003933 = 2.717 m/s.
- Raw backward step 35→36 is 29.29 px/frame, which would give 2.77 m/s. That is within the ±1 px per-frame noise, so the fitted value is used.
- Confidence: high, within about 2 %.
- Script: fit.py.
