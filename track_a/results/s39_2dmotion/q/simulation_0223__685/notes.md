# q_685 – speed of the moving red general at t = 1 s

2D scene (camera is static and looks almost straight down). question_fps = file fps = 24, so t = 1 s is frame 24.
Speed = |p(24) - p(23)| x 24 x (m/px).

## Position (measure.py)
Mask = difference to the per-pixel median of a column strip (x 840–1080), then the centroid. Motion is purely along +y (x = 959.15 ± 0.05).
- Frame 23: y = 437.07. Frame 24: y = 462.48. The step is **25.42 px**. Neither frame is part of a duplicated-frame pair.
  (Duplicated pairs: 18/19, 20/21, 28/29.)
- Neighbouring steps are 23.27, 24.31, 25.42, 26.56 and 27.57 px, which grow smoothly (constant acceleration, about 1.1 px/frame²).
  The mean of the two neighbouring steps is 25.44, which is consistent.
- scene/ record: 436.98 → 462.44, a step of 25.46 px. SAM 3 centroids: 437.6 → 463.2, a step of 25.6 px (+0.7 %).

## Scale (compare.py)
Prior: piece diameter = 0.097 m. I measured the moving general's own diameter across the motion direction (no blur in that direction):
- In the row-463 intensity profile of frame 24, the half-maximum edges are at x ≈ 915.5 and 1002.5, so the diameter is **87.0 px**.
  My difference mask is 87 px wide (cols 916–1002), and the scene record's bbox_w is 86–87.
- The SAM 3 mask (frame 24) is 92–94 px wide at the middle rows (box 913.5–1005.3). That is more than 3 % larger.
  On the zoomed overlay (frames/cmp24.png), SAM bulges left and right into the dark outline and shadow fringe on the board
  (sums of RGB of 48–67, darker than the board's 119) beyond the bright edge of the disc. My 87 px edge is the right one.
  The SAM area-equivalent diameter is 88.9 px.
- Scale = 0.097 / 87.0 = 1.1149e-3 m/px.

## Answer
v = 25.42 px x 24 /s x 1.1149e-3 m/px = **0.680 m/s**.
Second route: the mean of the neighbouring steps (25.44 px) gives 0.681. The SAM centroids give 0.685.
If SAM's 88.9 px equivalent diameter were used, the answer would be 0.666 (−2 %).
Confidence: high (about ±2 %).
