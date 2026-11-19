# q_1819 — boat length (m), prior: boat acceleration = 3 m/s^2

2D top-down Blender render, 24 fps (file fps = question_fps, no retiming). Boat moves left along a straight line, accelerating uniformly.

## Method (fit.py, uses scene/tracks/boat.csv mask centroids, checked)
- Pixel acceleration: quadratic fit of centroid x(t), frames 0–36: a = 138.5 px/s^2 (rms residual 0.4 px).
  Second route: linear fit of per-frame backward-difference speed vs t: slope 138.5 px/s^2. Left bbox edge: 136.4,
  right edge: 138.9. Half windows: 136.3 (f0–18), 130.7 (f18–36, noisier).
- Scale = 3 / 138.5 = 0.02166 m/px.
- Boat length (along its axis, rotation only −3°): 226 px at frame 0 (sharpest; later frames shrink to ~216 px from
  blurred pointed tip). Visually confirmed on zoomed frame 0: hull spans x ≈ 1340–1568.
- Length = 226 × 0.02166 = 4.90 m. (With a = 136.4: 4.97 m.)

Answer: 4.9 m. Confidence: good (~3%).
