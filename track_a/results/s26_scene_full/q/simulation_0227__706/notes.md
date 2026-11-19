# q_706: width of the pool tiles (horizontal side)

- 2D render, static camera, fps 24 (same as question_fps). Prior: black cat speed = 1.041 m/s.
- "Pool tiles" = the coping stones along the pool edge (row of tiles at y≈926–975). They sit directly in front of
  the deck where the cat walks (paws y≈918), so they are at about the cat's depth. One scale is valid here.
- Cat pixel speed (measure.py, scene/tracks/cat.csv): the torso centroid's linear fit gives 5.389 px/frame, and its net
  displacement over 49 frames gives 5.378 px/frame. The mean of the per-frame steps is 5.51, which is inflated by
  ±2 px gait jitter, so I did not use it. Full-mask centroid: 5.48–5.50. Value used: 5.39 px/frame = 129.3 px/s, giving
  1.041/129.3 = 0.00805 m/px.
- Tile joints, measured in code from column-intensity minima on the coping band at frame 0: x = 482, 633, 931, 1082,
  1232, 1382, 1533, 1681, 1831. These match the scene record. Mean spacing = (1831−482)/9 = 149.9 px, and each
  spacing lies between 148 and 151 px.
- Width = 149.9 × 0.00805 = **1.206 m**.
- Check: the full-mask centroid speed (5.50 px/frame) would give 1.18 m, about 2% lower. The torso centroid is the
  better proxy for the pelvis, so I kept it. Confidence: moderate-high. The main risk is the reading of "pool tiles":
  if it means the deck slabs instead, the answer would differ.
