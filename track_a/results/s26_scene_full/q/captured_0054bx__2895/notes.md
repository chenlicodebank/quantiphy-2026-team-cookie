# q_2895: soccer ball velocity at t = 0.5 s (frame 12, question_fps 24 = file fps)

## Situation
At f12 the soccer ball is still **held** (released only at f23-24). The hand was removed by segmentation and
something in front (the throwing arm) hides the lower part of the ball in f10-f15. Only a small top patch is
visible at f12 (area 583 px, versus about 1600 px in f4-9). See frames/soccer_crops.png (crops.py).

## Depth / scale
f = 0.5959*1280 = 763 px. Soccer ball size from the given depth at t=2.0: 3.254 m * 47.2 px / 763 = 0.201 m.
The held ball's apparent diameter (RANSAC f18-22 64-72 px, f26 70 px) gives Z ≈ 2.1-2.3 m. Used Z = 2.2 m
(close to the orange ball's 2.24 m at t=0.5; the two balls touch in the image at the start).

## Measurements (measure.py)
- Route A, visible-mask centroid: f10 (912.8,602.4), f11 (915.1,599.3), f12 (917.4,596.0), f13 (915.9,594.6),
  f14 (916.2,595.9), f15 (914.8,599.4). The visible part shifts up and back down as the occluder passes.
  - central differences over 4-6 frames (f10→f14, f9→f15): 1.84-2.04 px/frame -> 0.127-0.141 m/s
  - single steps f11→12: 0.275 m/s, f12→13: 0.142 m/s; mean of |step| over f10-15: 3.0 px/frame -> 0.21 m/s
- Route B, texture template (top patch with pentagon) tracked by NCC: the ball itself moves ≤1 px/frame around f12,
  which is ≈0.03-0.07 m/s. The ball barely moves in the hand. The centroid motion is mostly the occluder.

## Answer
The reference positions are clicked centres, smoothed over at least 5 frames. I answer with the smoothed
visible-centre value, 0.13 m/s (Route A, about a 5-frame window). This is uncertain. If the reference followed
the true (hidden) centre, the value would be lower, about 0.03-0.07 m/s. If it averaged per-step speeds, about
0.2 m/s. Confidence: low.
