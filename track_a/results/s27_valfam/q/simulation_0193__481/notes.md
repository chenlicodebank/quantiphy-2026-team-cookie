# q481 — Europa speed at 1 s (simulation_0193)

- 2D scene (Jupiter system seen pole-on, static camera). File fps = question fps = 30; t = 1 s → frame 30.
- Frame 30 checked: labels match the record (Europa = 2nd orbit, R≈205 px; Callisto = outermost, R≈414 px).
- Scale from prior: Callisto speed 0.627 m/s. Both moons move in uniform circular motion (record residuals tiny), so
  speed at any frame = model speed.
- measure.py:
  - uniform-circle chord speed (R·ω fit to the tracks): Europa 120.82 px/s, Callisto 60.96 px/s → ratio 1.982
  - mean of the raw one-frame speeds: 120.85 / 61.09 → ratio 1.978
  - second route: my own centroids (green excess, frames 20–40), quadratic fit, derivative at 1 s: 120.28 / 60.02 → 2.004
    (a local window, so noisier)
- Answer: 0.627 × 1.981 = **1.243 m/s**. Confidence is high (the routes agree within about 1 %).
