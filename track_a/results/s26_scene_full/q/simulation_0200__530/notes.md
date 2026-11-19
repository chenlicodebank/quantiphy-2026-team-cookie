# q_530 — speed of droplet at t = 0.1 s (frame 6, fps 60 = question_fps)

Method (2D, scale from the prior a = 9.7 m/s^2):
- measure.py: background subtraction against frame 13, largest component = drop; tracked the sharp top tip and the
  top-45-row centroid in frames 0–11. Quadratic fit over frames 2–11: a = 29.39 px/frame^2 (tip) / 29.29 (centroid);
  the scene record's track gives about 28.8–29.1. Scale = 9.7 / (a·3600) m/px.
- Speed at frame 6 = (y6 − y5)·60·scale = (y6 − y5)/a_px · 9.7/60.
  - tip, fitted: 159.98/29.39 → 0.880 m/s; raw: 162/29.39 → 0.891
  - centroid, fitted: 0.883; raw: 0.894
  - scene record dy 161.2 px → ~0.90
- Second route / model: the fit vertex is at t ≈ 0.04 frame, so the drop falls from rest at frame 0. Then
  y6 − y5 = 5.5·a (frame units) and v = 5.5·9.7/60 = 0.889 m/s, which sits in the middle of the measured 0.88–0.90.

Answer: 0.889 m/s. Confidence high (±2%).
