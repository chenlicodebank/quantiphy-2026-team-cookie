# q_2780 – yoga ball diameter (cm)

File fps = question_fps = 24. Lab clip, f = 0.5959*1280 = 762.75 px, principal point (640, 360).
Only one ball is visible (the dark-grey yoga ball); the "soccer ball" depth in depth_info has no visible object.

## Measurement (frame 24 = t 1.0 s, depth 2.4985 m)
- scene/ circle fit at frame 24: diameter 149.5 px, centre (516.6, 543.4); overlay frames/f24.png confirms the fit.
- My own green-key mask (width.py): horizontal extent x 444–589 → 146 px (frames 23/24/25: 140/146/150, smooth growth).
- Ellipse fit minor axis 144.4 px.
- Method-card size (Z·px/f): 146 px → 0.478 m; 149.5 px → 0.490 m.
- Off-axis correction: ball is 16.2° off-axis, so the sphere's image is stretched by 1/cosθ (tangential) and
  1/cos²θ (radial). Horizontal extent 146 px ↔ tangential minor axis ≈144 px (agrees with ellipse minor 144.4).
  True diameter = 2·Z·sinα with sinα = b·cosθ/f/√(1+b²/f²): 0.452 m (from minor 144.4) – 0.468 m (from circle 149.5).

## Check
- Depth-from-apparent-size track (dist ∝ 1/diam, anchored at 2.4985 m at frame 24) gives speed at 1.0 s
  = 2.155 m/s (5-frame mean), vs prior 2.1464 m/s → depth_info and size track are consistent.
- Person depth 3.83 m, squat height 196 px → 0.98 m (plausible).

## Answer
Physically corrected value ≈ 0.45–0.47 m; plain method-card value ≈ 0.48–0.49 m. Answer 46 cm
(the reference is ruler-measured, so the off-axis-corrected value is preferred; likely a 45 cm ball).
Confidence: moderate, ±5 %.
