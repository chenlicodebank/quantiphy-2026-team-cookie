# q_2149 – ball velocity at t = 1.3 s (cm/s)

File fps = question_fps = 24, so t = 1.3 s is frame 31. Lab video: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## What happens
The "slope" is the white board leaning on the table. The ball sits on its top edge until about frame 27, then
rolls down the board's face from frame 30 to frame 35, reaching the table at about frame 36. Over the board the
ball shows only as a faint yellow ghost (a segmentation artefact), so the scene record's diff-mask centres for
frames 30–31 were biased. I re-tracked frames 27–36 with a yellowness-change centroid against frame 48, where
the ball is gone (`track2.py`), and checked them on 4x zooms (`frames/zoom.png`).

Ball centre v (px): 27: 283.5, 28: 285, 29: 292, 30: 305.9, 31: 317.8, 32: 336.1, 33: 354.8, 34: 378.0, 35: 405.8
(u stays at 615–620).

## 3D
- Depth is linear in image v, set by the given ball depths (frame 24 at 1.779 m, frame 31 at 1.736 m): -1.21 mm/px.
- Each centre is back-projected along the ray ((u-cx)/f, (v-cy)/f, 1) and scaled to that depth (`velocity.py`).
- Second route for depth: use the gradient from the slope's two end distances, -1.12 mm/px. Results change by
  less than 2 %.

## Velocity at frame 31
| method | ball-depth gradient (m/s) | slope-end gradient (m/s) |
|---|---|---|
| 5-frame smoothed forward difference, (X34 - X29)/5 | 1.053 | 1.036 |
| 3-frame, (X33 - X30)/3 | 1.001 | 0.985 |
| raw forward difference 31→32 | 1.126 | 1.107 |
| quadratic fit over frames 30–35, at frame 31.5 (forward-difference time) | 1.010 | 0.994 |
| quadratic fit over frames 30–35, at frame 31 | 0.909 | 0.894 |

The reference convention is a forward difference smoothed over at least 5 frames, which gives about 1.04–1.05 m/s.
The quadratic fit at the forward-difference time gives about 1.00 m/s. **Answer: 103 cm/s.**

## Prior check
Accelerations from the measured track are about 4.8 m/s² (quadratic fit) and about 5.4 m/s² (mean of the
frame-to-frame differences). The prior gives 4.05 m/s². Both are somewhat higher than the prior, but the track is
noisy and the ball is faint over the board. If the whole scale were corrected to match the prior, the answer would
be about 0.85 m/s. I did not apply that correction: the scale from the given depths is consistent with the board's
own depth gradient, so I trust it. Confidence: moderate, about ±10 %.
