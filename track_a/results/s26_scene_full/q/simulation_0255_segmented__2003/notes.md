# q_2003 — acceleration of the tennis ball at t = 0.5 s

- 2D video, 24 fps (file and question rates match), static camera. There is one ball, which moves right in a straight horizontal line (y std 0.08 px) and slows down steadily.
- Tracking (measure.py): mask where darkness > 60, intensity-weighted centroid in all 41 frames. The result matches scene/tracks.
- Pixel acceleration:
  - Quadratic fit over all frames: −153.6 px/s² (residual rms 0.18 px).
  - Cubic fit, evaluated at 0.5 s: −155.0 px/s².
  - Local quadratic fits centred on frame 12 (±4, ±6, ±8 frames): −151.1, −154.6, −155.0 px/s².
  - Mean of the speed differences: −158.3 px/s².
  - The deceleration is uniform, so I take −154 px/s².
- Diameter:
  - The bounding box is 25 px vertically. It is 26 px horizontally because of motion blur.
  - The soft-area equivalent diameter is 24.2–25.3 px (diam.py).
  - Visual check on a zoomed crop at t = 0.5 s: about 25 px. I use 25 px.
- Scale: 0.17 m / 25 px = 0.0068 m/px.
- Acceleration = 154 × 0.0068 = 1.047 m/s², answered as the magnitude 1.05 m/s². The ball is decelerating.
- Second route: the speed-difference mean gives 1.077 m/s², which is within 3%.
- Confidence: good. The main uncertainty is the diameter in pixels (±1 px, about 4%).
