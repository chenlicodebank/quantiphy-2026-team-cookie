# Q98 — distance yellow car ↔ black/white car at t = 1.0 s

- 2D top-down simulation, fps 24 = question_fps, so t = 1.0 s is frame 24. The camera does not move.
- Scale comes from the prior: the yellow car is 270 px long (x extent, steady near the image centre) and 5.67 m, so 0.021 m/px.
- measure.py: per-pixel median background (frames 0/36/71). Mask = pixels differing from the background by more than 35,
  OR brighter than it by more than 12 (this catches the black car's white front), OR yellow. Each car is the largest
  connected part in its own lane band, and its bbox centre stands in for the car's origin.
  - Frame 24: yellow centre (632.5, 415.5), length 270 px; black centre (1105.0, 539.5), length 269 px.
  - dx = 472.5 px, dy = 124 px, so the distance is 488.5 px = **10.26 m**.
- The first try used a darker-only threshold. It lost the black car's white front (length 240 px), which proved the
  bright term is needed. With that term the result matches scene/tracks exactly.
- Second check: fit the constant velocities (yellow −10 px/frame; black +13.96 px/frame starting from 784.5 at
  frames 0–1). This puts black at x ≈ 1105.6 at frame 24. The distance changes by under 0.6 px, about 0.01 m.
- Confidence: high for the pixel measurement. The remaining risk is that a vehicle's root might not sit at its bbox centre.
