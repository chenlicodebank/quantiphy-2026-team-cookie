# Q2725 — distance white cup ↔ pink bottle (cm)

Static objects, camera static; measured on frame 48 (t=2.0 s at question_fps 24 = file fps).
Lab card: f = 0.5959·1280 = 762.8 px, principal point (640,360).

Pixel extents (measure.py masks + zoomed grid crop frames/f.png):
- Pink bottle: x 640–688, y ≈330 (lid top) – ≈480 (bottom) → centre (664, 405). Colour mask leaks into the
  pink-backed card tent below y≈420 and misses the lid, so the box was read from the grid crop.
- White cup: mask x 725–794, y 378–497 (rim ~375) → centre (759.5, 436).

Back-projection with depth_info as Euclidean camera→centre distance (bottle 0.9998 m, cup 0.8740 m):
distance = 17.46 cm. Centre perturbations of ±5 px → 17.40–17.56 cm.
If depths were treated as z-depth: 16.66 cm (≈5% lower); Euclidean reading used per the stated convention.

Sanity: implied sizes bottle ≈19.7 × 6.3 cm, cup ≈14.0 cm tall, 8.0 cm rim — realistic.

Answer: 17.5 cm. Confidence: moderate-high (dominated by the given depths; ±0.5 cm from centre picking).
