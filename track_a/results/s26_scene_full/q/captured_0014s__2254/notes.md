# q_2254 — displacement of the rolling ball, 0 s → 0.6 s (cm)

- Time base: question_fps = 24 = file fps. t=0 → frame 0, t=0.6 → frame round(14.4) = 14.
- Ball centre (measure.py: |frame − frame 48| > 30 mask, largest blob; overlays frames/ov_0.png, ov_14.png checked):
  - frame 0: centroid (544.7, 296.0), enclosing-circle centre (543.9, 295.8), r ≈ 16 px
  - frame 14: centroid (547.7, 353.9), circle centre (547.5, 354.5)
  - These agree with scene/tracks/ball.csv (±0.5 px).
- Camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- Back-projection along unit ray × depth_info (1.8180 m at t=0, 1.7288 m at t=0.6):
  - centroid → 16.05 cm, circle centre → 16.21 cm. If the depth is treated as z instead, the result is 16.6 cm.
- Second route (physics): the ball starts moving at about frame 8 (t ≈ 0.333 s). With the prior a = 4.6 m/s² from rest,
  s = ½ · 4.6 · (0.267 s)² ≈ 16.4 cm. This is consistent.
- Answer: 16.1 cm. Confidence: good (±5 %).
