# q_688 – acceleration of moving red general at t = 1.5 s

- 2D scene (top-down xiangqi board), fps = question_fps = 24, so t = 1.5 s is frame 36.
- Track: scene/tracks/red_general.csv, mask_centroid_y (x constant). I dropped the first frame of each duplicated
  pair (9, 11, 18, 20, 28, 34), because each shows the next frame's position, and also frames ≥40 (piece over the tatami/off-frame).
- fit.py: per-frame speeds near frame 36 on clean frames: 33→35 36.31, 35→36 37.98, 36→37 39.01, 37→38 39.96 px/frame.
  Local acceleration ≈ 1.0–1.03 px/frame². Polynomial fits evaluated at frame 36 give: quadratic over frames 20–39 1.034,
  quadratic over 26–39 1.02, cubic 0.98–1.02. The acceleration falls a little over the clip (about 1.15 early, about 1.0 late).
  Value used: 1.01 px/frame² = 1.01 × 576 = 582 px/s².
- Scale: prior diameter 0.097 m over the general's own disc of 86–87 px (mask bbox) → 0.097/86.3 = 1.124e-3 m/px.
- a ≈ 582 × 1.124e-3 ≈ 0.65 m/s² (range 0.64–0.67 across the methods).
- Second route: the raw local difference (39.01 − 37.98) × 576 × 1.124e-3 = 0.667, which is consistent.
- Confidence: moderate-high (±4 %).
