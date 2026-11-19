# Q15 – width of the telephone booth (m)

- Object: the light-grey box on the upper-left sidewalk (called "utility box" in scene/) is the telephone booth
  (glazed side panels are visible on its right side). Static, frames 0–98.
- fps 33 = question_fps; no re-timing.
- Scale from prior: pedestrian speed 1.236 m/s. Pedestrian track (scene/tracks/pedestrian.csv, checked): mean of
  per-frame speeds 110.54 px/s (net over whole gait cycles 110.0–110.9 px/s) -> 0.011182 m/px at the height of the
  tracked head/shoulder point.
- Booth pixel size (measure.py, frame 50 edge profiles + zoomed crops): roof/top face x 346.5–461 (≈115 px),
  y 250.5–363 (≈113 px). Nearly square footprint; width = shorter horizontal extent ≈113 px.
- Perspective correction: the camera is a near-nadir perspective camera (booth sides visible, leaning toward the
  image centre). Base corners are displaced from the roof corners by ≈8.3–8.6 % of their distance to the image
  centre -> roof/ground scale ratio s ≈ 1.09 (h/H ≈ 0.083; for a ~2.4 m booth H ≈ 29 m). Tracked pedestrian point
  at ≈1.4 m -> ground scale = 0.011182 / (1-1.4/29) ≈ 0.011182 × 1.051 m/px, so
  W = 113 px × 0.011182 × (1/1.09) × 1.051 ≈ 1.218 m.
- Second route: base footprint read from the visible base corners (x ≈ 395–503 -> ~104–108 px at ground scale),
  × ground scale 0.011182×1.051 = 0.01175 m/px -> 1.22–1.27 m. Consistent.
- Readings: shorter extent (y, 113 px) 1.22 m; longer (x, 115 px) 1.24 m. Answer with width = shorter: 1.22 m.
- Uncertainty: camera height H (factor 1.16–1.25 m for H from infinity to 20 m), edge reading ±2 px. Confidence moderate (~±5 %).
