# q131: distance between the big bird (eagle) and small bird (crow) at t = 0.3 s

- fps 24 = question_fps; t = 0.3 s -> frame round(7.2) = 7. 2D video, both birds fly horizontally on the same line.
- measure.py (my own script: background-difference mask + connected components) reproduces the scene/ tracks exactly.
- Scale from the prior: the eagle moves 119.69 px/frame at a steady rate (tail end 1762 -> 206 over f1->f14; bbox centre gives 119.65).
  17.98 m/s / 24 = 0.74917 m/frame -> 0.0062594 m/px.
- Frame 7: eagle bbox centre x = 975.0, crow bbox centre x = 1343.5, body lines y ~554 / ~552 (vertical offset ~2 px, too small to matter).
  Gap = 368.5 px -> 2.307 m.
- Second route: the gap grows linearly by ~46.4 px/frame (f2: 136.5 + 5 x 46.4 = 368.5). Interpolating f6 and f8 (321.0, 414.5)
  gives 367.8 px, within 0.2 %. Using mask centroids instead gives 374 px (2.34 m); the centroid moves with wing flapping, so I used the bbox centre.
- Confidence: high. The remaining uncertainty is where each bird's origin sits relative to the bbox centre (about ±1-2 %).
