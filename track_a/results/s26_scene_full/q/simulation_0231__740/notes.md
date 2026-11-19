# q740 – paper airplane speed at t = 1 s

2D scene (wall parallel to image, static camera), fps 24 = question_fps, so t = 1 s → frame 24.

Scale (prior: cat speed 0.714 m/s, treated as the cat's steady walking speed):
- cat mean pixel speed over f0–49 from scene tracks: torso_cx 433.5/49 = 8.85 px/f, cx_dark 8.96, bbox 8.86
  (my band cross-correlation in measure.py gave 86–90 px / 10 f for the first windows, then locked onto the static
  background at its 60 px search limit, so only the early values mean anything) → 8.89 px/f = 213.4 px/s
- scale = 0.714 / 213.4 = 0.003346 m/px

Airplane (frame 24, backward difference from 23), measured again in measure.py (background difference on the board):
- bbox centre x 1028.0 → 1097.5 (69.5 px), mask centroid 1020.5 → 1090.1 (69.6 px), dy ≈ 1–2 px
  → step 69.5 px; matches the scene record (cx_best 1028 → 1097.5). Next/previous steps are 69–70 / 67, so it's smooth.
- speed = 69.5 × 24 × 0.003346 = 5.58 m/s

Second route: ratio of pixel speeds 69.5 / 8.89 × 0.714 = 5.58 m/s (same thing, no extra scale step); using the
mask centroid gives 5.59. The cat-speed definition (stride gait, ±3 %) is the main uncertainty.
Confidence: good (~±4 %).
