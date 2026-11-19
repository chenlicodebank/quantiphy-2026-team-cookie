# Q329 – speed of the cup at t = 1 s (simulation_0136, 2D, 24 fps)

- fps = question_fps = 24, so t = 1 s is frame 24; speed = |x(24) - x(23)| x 24 (motion is purely horizontal).
- Scale: prior cup diameter 0.087 m = rim width. Measured from the HSV mask (measure.py), the rim width is
  118-122 px (it is 120 px at frames 10-14 and 23-24), so I used 120 px -> 7.25e-4 m/px.
- Displacement from frame 23 to 24:
  - row-averaged mask centre: 33.09 px
  - column-profile cross-correlation: 32.50 px
  - quadratic fit to the per-frame shifts over frames 21-27, evaluated at frame 24: 32.87 px and 32.60 px.
  I used 32.8 px/frame. The scene record's cx_est gives 28.7 px, but that value is noisy because of the minAreaRect
  switch; its bbox centre gives 32.5 px, which agrees with my value.
- Speed = 32.8 x 24 x 0.087 / 120 = 0.571 m/s. Using a 121 px rim gives 0.566 m/s.
- Confidence: good, about ±3 %. The main uncertainty is the rim pixel width (±1-2 px).
