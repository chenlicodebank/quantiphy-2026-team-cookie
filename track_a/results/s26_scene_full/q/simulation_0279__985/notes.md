# q_985 – whale displacement 0.5 s → 1.0 s

- 2D render, 24 fps (file fps = question_fps). Frames 12 → 24.
- Prior: whale speed 1.67 m/s. Whale translates uniformly left: head chain track (scene/tracks/whale.csv)
  gives 8.02 px/frame (std 0.12) from frame 1→2 to the end, y constant; frame 1 duplicates frame 0, which
  doesn't matter for frames 12–24.
- Scale = 1.67 / (8.02 px × 24) = 0.008676 m/px.
- Displacement frames 12→24: head chain 95.97 px → 0.833 m; independent sub-pixel snout edge 95.65 px → 0.830 m.
- Analytic check: the motion is uniform, so displacement = 1.67 m/s × 0.5 s = 0.835 m (the same value up to measurement noise).
- Answer: 0.835 m. Confidence high (within ~1%).
- Script: measure.py
