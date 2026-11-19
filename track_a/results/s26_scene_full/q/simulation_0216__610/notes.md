# q_610 — height of the black cat (incl. tail)

2D video, fps 24 (= question_fps), static camera; cat walks left→right parallel to the image plane at one depth.

Scale (from prior, speed 0.94 m/s):
- Matched upper-body track (scene/tracks/cat.csv, body_x_matched): mean 17.73 px/frame (median 17.70) → 425.6 px/s.
- Second route: torso centroid net 863 px / 49 frames = 17.61 px/frame (0.7 % lower).
- Scale = 0.94 / 425.6 = 0.002209 m/px.

Height (height.py): background-difference mask (85th-percentile bg) per frame; tail tip = top of mask,
paw bottom = lowest bright (white sock) mask row. Tail tip y = 796–808 (mean ≈ 801); ground contact of the paws
y ≈ 1020–1022 in every frame where the paws are detected (dips in some frames are paw-detection misses in shadow,
checked visually at frame 30: paws at y≈1020). Height ≈ 1021 − 801 = 220 px (median of per-frame 220; range 213–225).
Visual check on 2× gridded crops at frames 0 and 30: 796→1017 (221) and 806→1020 (214).

Answer: 220 px × 0.002209 m/px = 0.486 m (range over gait 0.47–0.50 m).
Confidence: moderate-high; main uncertainty is which frame the reference AABB used (±3 %).
