# q_112 — width of the car (m); prior: car acceleration = 4.03 m/s^2

2D top-down render, static camera, 24 fps (file and question agree; one time base).

## Scale from the prior (accel.py, fit.py)
- Car per-frame speed from integer bbox edges (front edge to frame 63, rear edge 64–71), checked against my own
  re-segmentation (track.py: same edges ±1 px).
- The car starts from rest at frame ~2 and speeds up to a plateau of ~62 px/frame by frame ~67. The acceleration is
  not perfectly uniform: ~0.87 px/frame^2 over frames 3–30, ~1.06 over 30–63, easing off over 61–67.
- Linear fit of speed vs frame over 3–63: 0.950 px/f^2 (3–65: 0.954, 5–60: 0.942). Second route: net
  Δv/Δt = 62 px/f over ~64 frames = 0.97. Used 0.95 px/f^2 = 547 px/s^2 → 4.03/547 = 0.00736 m/px.

## Width
- Across the direction of motion (y), at frames 10, 30 and 50: body + tyres span y 589–858 = 270 px
  (column-wise p90 269); with side mirrors 570–885 = 316 px.
- Wheel-to-wheel width (the requested reading): 269.5 px × 0.00736 = **1.98 m**.
- Alternative reading (AABB including mirrors): 316 px → 2.33 m.
- Sanity check: length 727 px → 5.35 m; ratios match a Cybertruck (5.68 × 2.03 m, 2.41 m with mirrors).

Confidence: moderate-high. The main uncertainty is the non-uniform acceleration (±5–8 % depending on window).
