# Q487: Europa orbital diameter (m)

2D pole-on Jupiter system; one m/px scale from prior (Callisto speed 0.627 m/s). File fps = question fps = 30.

- Callisto pixel speed: mean per-frame backward-difference speed 61.09 px/s; angular-rate model 60.97 px/s
  (scene record 60.96). Scale = 0.627/61.0 ≈ 0.01028 m/px.
- Europa orbit radius (moon centre path): 204.73 px about common centre (scene record), 205.26 px free circle fit
  to the track, 205.18 px from my own re-detection on raw frames (every 11th frame). Drawn red line 205.94 px.
- Diameter = 2R × scale: 4.211–4.222 m across routes. (measure.py)
- Second route: independent centroid re-detection from decoded frames → 4.222 m.

Answer: 4.215 m. Confidence high (±0.5 %).
