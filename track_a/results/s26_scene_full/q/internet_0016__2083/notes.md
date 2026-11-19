# q_2083 – distance basket ↔ player in black at t = 0.5 s

- Time: t = 0.5 s → frame 15 at both rates (29.9 fps and 30 fps).
- Scale: prior "inner court width = 4.88 m" = the lane (paint) width (16 ft). Bottom lane measured 639.5 px
  (lines at x 750.5 and 1390, scene record; I checked it on frame 15: about 750 and 1390).
  So 4.88 / 639.5 = 0.007631 m/px.
- Basket: bottom rim ring centre (1062, 3568) px, read from a 3x zoom of frame 15 (ring x 1028-1097, y 3537-3600).
- Player B (black shirt) at frame 15: arms are raised up-left. Torso and head blob centre is about (1065, 3293) px,
  read from 2x and 3x zooms (frames/p15.png, frames/b_sheet.png). The record's mask centroid (1049.5, 3262.5) is pulled up
  by the raised arms, so I did not use it as the body position.
- Distance = sqrt(3² + 275²) ≈ 275 px × 0.007631 = 2.10 m. Answer: 2.11 m.
- Check: with the record's mask centroid instead, 306 px → 2.33 m (+11%). That is the upper bound if the annotator
  clicked the whole silhouette including the arms. Rim and head are both raised above the floor, so their parallax
  shifts partly cancel. I used the planar convention with no correction.
- Confidence: moderate, about ±8%. The main uncertainty is which point counts as the player's position.
