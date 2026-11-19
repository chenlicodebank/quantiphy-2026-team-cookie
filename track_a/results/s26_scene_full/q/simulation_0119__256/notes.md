# q_256 — distance moved by the chess piece

2D top-down render. One dark glass piece slides straight down the image, moving uniformly from frame 0 and stopping at frame 36.
After that it stays still through frame 47. Prior: speed = 0.04 m/s.

Measurements (check.py, using the circle-fit centre from scene/tracks/dark_piece.csv, which I re-checked):
- Linear fit over frames 0–35: 1.398 px/frame, residual 0.18 px. The quadratic term is negligible, so the speed is constant.
- The fitted line reaches the rest position at frame 35.97, which confirms the stop at frame 36. Net displacement 0→36 = 50.29 px, purely vertical.
- Mask-centroid route over frames 18–35: 1.388 px/frame, which agrees.

Scale: 1.398 px/frame × 24.012 fps = 33.58 px/s ↔ 0.04 m/s → 1.191e-3 m/px.
Distance = 50.29 px × 1.191e-3 = 0.0599 m.
Second route, time-based: 36 frames / 24 fps = 1.5 s × 0.04 m/s = 0.060 m. Both fps values (24 and 24.012) give the same result to within 0.05 %.

The path is straight, so path length equals net displacement. Answer: 0.06 m. Confidence: high.
