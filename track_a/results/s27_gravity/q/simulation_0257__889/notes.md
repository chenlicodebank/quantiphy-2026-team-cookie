# Q889 – speed of the plant at t = 0.4 s

- 2D scene, static camera. The pot falls straight down from rest at frame 0 and lands at frame 15.
- The file runs at 24 fps but question_fps is 30, so all timing uses 30 fps: t = 0.4 s → frame 12.
  Speed = (y12 − y11) × 30 px/s.
- Scale comes from the prior (a = 9.8 m/s² before 0.5 s): I fitted a quadratic over frames 0–14 to get the pixel
  acceleration a_px (px/frame²). Then m/px = 9.8 / (a_px × 30²). The speed in m/s then works out as
  9.8 × Δy / (a_px × 30), so it does not depend on the absolute pixel scale.
- Mask centroid (scene track): a_px = 6.93, rest at t0 = −0.01 frame, rms 0.29 px. Speed 3.760 (fit) / 3.747 (raw diff).
- bbox centre: 3.75. Bottom edge (scene track and my own subpixel re-measurement): 3.68–3.75. That edge is noisier
  (rms ≈ 1 px).
- Analytic check: uniform acceleration from rest at frame 0 gives v = 9.8 × (12 − 0.5) / 30 = 3.757 m/s.
- Answer: 3.75 m/s. Confidence high (spread about ±1%).
