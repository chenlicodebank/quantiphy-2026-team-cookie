# q_928 — speed of the spacecraft (the only moving object, a car-shaped vehicle seen top-down) at 1.0 s

- 2D scene, fps 24 = question_fps, so t = 1.0 s is frame 24. Prior: acceleration = 4 m/s^2 (uniform).
- Scale comes from the prior acceleration: speed = 4 m/s^2 × (pixel speed / pixel acceleration).
- Route 1 (`fit.py`, scene track ref_x): per-frame steps are linear in frame number, step = 0.8994·i − 0.434 px
  (residual std 0.06 px). a_px = 0.8994 × 24² = 518 px/s² → 0.00772 m/px. Step at frame 24 = 21.15 px (fit), 21.18 raw
  → 508 px/s → **3.92 m/s**. A quadratic fit of position (frames 1-60) gives 3.93 m/s.
- Route 2 (`track.py`, own NCC re-track of consecutive frames 0-40): slope 0.888 px/frame², step(24) 20.85 px
  → 3.917 m/s.
- Motion begins about half a frame after t = 0 (the car is at rest in frames 0-1), so the backward-difference speed at
  frame 24 is ≈ 4 × 0.98 = 3.92 m/s rather than exactly 4.0.
- Answer 3.92 m/s. Confidence high (routes agree within 0.2 %; worst case reference = a·t = 4.0, 2 % off).
