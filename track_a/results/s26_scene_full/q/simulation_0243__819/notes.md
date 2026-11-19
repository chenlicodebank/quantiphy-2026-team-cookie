# Q819: height of the left tree (m)

The scene is 2D (static camera; the antelope walks across at constant depth). I used one m/px scale from the prior and 30 fps (file fps = question_fps).

## Scale
- Antelope pixel speed (speed.py on scene/tracks/creature.csv): chest_front_x net 195.0 px/s; the two halves give
  196.2 and 193.8. Mask centroid 194.6, nose 199.1, rump 187.3. Walking speed is constant.
- Scale = 1.277 / 195.0 = 0.006549 m/px. Antelope height 423 px gives 2.77 m.

## Tree
- Top (treetop.py, frame 72, luminance scan against the sky): tip at y = 362, x ≈ 120.
- Base: the trunk (x 60–95) is visible down to y ≈ 1370, then hidden by the roadside bushes. I took the ground line at
  the bushes' bottom and the antelope's hoof line, y ≈ 1545 (a plausible range is 1520–1560).
- Pixel height ≈ 1545 − 362 = 1183 px, giving 1183 × 0.006549 = 7.75 m.

## Check / confidence
- Using the other speed features (187–199 px/s) gives 7.6–8.1 m. A base anywhere in 1520–1560 gives 7.58–7.85 m.
- The main uncertainty is the hidden trunk base and whether the tree sits slightly deeper than the antelope.
  Confidence is moderate (about ±5–8 %).
