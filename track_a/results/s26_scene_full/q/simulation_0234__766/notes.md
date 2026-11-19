# Q766 – speed of basketball at t = 1.5 s

- 2D simulation, static camera, fps = question_fps = 24 → t = 1.5 s is frame 36 (ascent after the bounce at frame 24).
- measure.py: my own HSV mask + least-squares circle fit for frames 28-45 (it agrees with scene/tracks/ball.csv). The overlay
  frames/ov36.png shows the fit sitting on the ball edge.
- Ball diameter in pixels: circle fit 74.6, area-equivalent 75.6, bbox about 74-76 → used 75.3 px (±0.5). Scale = 0.282 / 75.3 =
  0.003745 m/px.
- Motion is purely vertical (x is constant to ±0.2 px).
- Route 1, raw backward difference: |y36 - y35| = 823.95 - 812.23 = 11.71 px → 281.1 px/s.
- Route 2, parabola fit over frames 28-45 (no bounce inside that window), difference between frames 35 and 36 → 282.35 px/s.
  This is used because it averages out the ~0.15 px centre noise.
- Speed = 282.35 × 0.003745 = 1.057 m/s. The range over the diameter choices (74.6-75.6 px) and both routes is 1.049-1.067.
- Confidence: high, about ±1.5 %.
