# Q947 — speed of the spacecraft at 0.5 s (prior: acceleration at 1.0 s = 4 m/s^2)

2D video, fps 24 (file and question_fps agree). The spacecraft is the single vehicle; it moves horizontally to the left,
accelerating uniformly from rest.

## Method
- Scale comes from the prior: pixel acceleration = slope of the per-frame pixel step vs frame (k px/frame^2), times 24^2.
  Speed at 0.5 s = frame 12 backward step x 24. So answer = 4 * step(12) / (24 k), and the m/px factor cancels.
  This also cancels any constant factor from which point of the 3D vehicle is tracked.
- fit.py (scene record tracks): x_body_texture gives k = 1.251 and step12 = 14.33 (raw) / 14.37 (fit), so answer = 1.909–1.917.
  x_ref gives the same ratio. Fitting frames 2-30, 8-50 or 30-65 gives 1.91–1.93, so the acceleration is constant.
- The line fit is step ≈ k (i − 0.51). So the motion starts at t ≈ 0, v = 4t, and the backward difference at frame 12
  is 4 × 11.5/24 = 1.917 m/s.

## Second route
- check.py: my own NCC template match of the rear part (fins) from frame 12, over frames 4-48. It gives k = 1.202 and
  step12 = 14.07, so answer = 1.95. A quadratic fit of position puts the start of motion (vertex) at t = −0.01 s,
  which confirms the vehicle starts from rest at t = 0.
- The routes agree within 2%.

## Answer
1.92 m/s (backward-difference convention; a·t at t = 0.5 would give 2.0). Confidence: high.
