# q2079 — speed of the car before the motorcycle at 1.0 s (prior: lane width = 3.66 m)

Object: the car directly ahead of the red two-wheeler (motorcycle) in the upper lane = **white_hatchback**.
Top-down static drone view, 2D planar scene -> one m/px scale from the lane width.

## Scale (measure.py)
Brightness-peak centroids of the road lines at frame 30 (three column windows): upper edge line y≈521.4–521.6,
centre double line 566.4/574.3 (inner line 565.8–566.7), lower edge line 620.4–621.5.
Upper lane (the one the car drives in), line centre to line centre: 45.0 px (44.3–45.1).
Scale = 3.66 / 45.0 = 0.0813 m/px. (Alternative reading, half the edge-to-edge road 99.2/2 = 49.6 px -> 0.0738 m/px,
which would give 26.1 m/s; not used: the lane is bounded by edge line and centre line.)

## Speed at t = 1.0 s (frame 30)
- scene track (edge-profile, bg-compensated): dx 29->30 = -11.84, 30->31 = -11.72 px/frame, linear fit f20–40 -11.69.
- independent route (check.py): NCC template of the car from frame 30, matched f16–45 with subpixel peak:
  forward diff 30->31 = -11.79, backward 29->30 = -11.77, linear fit -11.76 px/frame (NCC ≥ 0.95).
- background drift < 0.07 px/frame (fence patch), negligible.
Adopted 11.77 px/frame.

## Time base
File fps 29.78 vs question_fps 30 — 0.7 % difference; both give frame 30 for t = 1.0 s. Used 30 fps
(question rate): 11.77 × 30 = 353 px/s. (With 29.78: 350.5 px/s, 28.5 m/s.)

Speed = 353.1 px/s × 0.0813 m/px = **28.7 m/s** (≈103 km/h, plausible for a rural road).
Confidence: the speed in pixels is solid (±1 %); the main uncertainty is how the lane width was defined in pixels (±5–10 %).
