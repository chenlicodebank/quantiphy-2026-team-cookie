# Q1485 – whale displacement 0.5 s → 1.0 s

Prior: whale speed = 1.67 m/s (constant). question_fps = file fps = 24 → frames 12 → 24.

Method: check that the whale moves uniformly in a straight line over the interval, then displacement = v × Δt.
- head_top track (scene/tracks/whale.csv, ana.py): f0→12 34.5 px, f12→24 34.9 px, f24→36 27 px, f36→48 40 px
  (±3 px row-mean jitter) → steady ~2.9 px/frame. Direction is constant (f0–24: (-64,-30) px; f24–48: (-60,-32) px),
  so the path is straight and chord ≈ path length.
- Displacement = 1.67 × 0.5 = 0.835 m.

Second route / consistency check: depth_info gives a 1.43 m range increase over 1 s, i.e. most of the 1.67 m/s goes
away from the camera; the remaining lateral ~0.86 m/s at 33.7 m against ~70 px/s on screen implies f ≈ 2700 px
(HFOV ≈ 50°), which is plausible. That confirms uniform motion at the prior speed but is not precise enough
to beat v × Δt.

Answer: 0.835 m. Confidence: high (relies on the constant speed shown by the track).
