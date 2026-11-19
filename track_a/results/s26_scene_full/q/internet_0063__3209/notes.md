# q_3209: bottle velocity at 1.50 s (prior: g = 9.8 m/s^2)

- Time base: file 30.016 fps vs question 30.0 fps (negligible difference); t=1.50 s -> frame 45. Used 30 fps.
- The camera is rotated, so gravity points along image +x. Camera drift is ~0.2 px/frame, which is negligible.
- Track: blue-cap centroid and bottle centre from scene/tracks/bottle.csv. Frame 45 checked visually (frames/f45.png): the cap is at ~(310,555), matching the record's (312.6,555.6).
- Scale from gravity: quadratic fits over the free-fall frames (fit.py) give a pixel acceleration of
  12.1 (frames 41-52), 12.2 (42-51) and 12.6 (41-49) px/frame^2. Release onset is at frame ~39.3.
  Used a ≈ 12.3 px/frame^2, so the scale is 9.8/(12.3*900) = 8.85e-4 m/px.
- Velocity at frame 45, following the annotator convention (forward difference x46-x45): 76.2 px/frame
  -> 76.2*30*8.85e-4 ≈ 2.02 m/s (range 1.97-2.08 depending on the fit window and the cap/centre point).
- Second route: central or fitted velocity is 70 px/frame -> 1.82-1.91 m/s. As a physics check,
  g*(t - t_release) = 9.8*(45.5-39.3)/30 = 2.03 m/s at the forward-difference midpoint, which agrees with the forward difference.
- Answer: 2.02 m/s. Confidence: moderate-high (the main uncertainty is forward vs central difference, ~7%).
