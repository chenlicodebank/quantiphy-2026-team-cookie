# q_2002: tennis ball speed at t = 1.5 s

- 2D video, 24 fps (file fps and question_fps match, so no re-timing). t = 1.5 s is frame 36. One ball moves horizontally to the right at y ≈ 564 and slows down steadily (no bounces).
- Tracking (measure.py): intensity-weighted centroid in every frame, which agrees with scene/tracks/ball.csv to within about 0.2 px.
- Speed at frame 36, backward difference (pixels per frame):
  - raw x36 − x35 = 33.98
  - quadratic fit over all 41 frames, slope at 35.5 = 34.71 (residual std 0.19 px)
  - cubic fit = 34.74
  - Mean of the neighbouring raw steps (frames 34–38): about 34.5

  I use 34.71 px/frame = 833 px/s.
- Diameter in pixels: the vertical bbox extent is a median of 25, the soft-area equivalent diameter is 24.99, and the half-max vertical profile (diam.py) gives 24.75. The horizontal extent of 26–27 px is inflated by motion blur. I use 25 px, so the scale is 0.17/25 = 0.0068 m/px.
- Speed = 833 px/s × 0.0068 = 5.66 m/s. If the diameter were 24.75 px, it would be 5.72 m/s. Answer: 5.67 m/s.
- Second route: the raw single-frame difference gives 5.55 m/s, about 2% lower, which is within the centroid noise.
- Confidence: about 3%, limited mainly by the pixel diameter.
