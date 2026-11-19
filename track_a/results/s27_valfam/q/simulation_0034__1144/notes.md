# q_1144 — eagle average speed, whole clip (m/s)

File fps = question_fps = 24, so frame i is at t = i/24. Camera is static (scene record), and the bird track (body point, scene/tracks/bird.csv) is the right object. I checked this on frame 24.

## Scale
Person height prior 1.75 m. Person bbox height is 67 px (median), at depth 92.19 m, so f ≈ 67·92.19/1.75 ≈ 3530 px. The principal point is assumed at (540,540).
The answer barely depends on f, because the motion is mostly along the line of sight: depth goes 91.69 → 103.43 m between t=1 and t=2. With f scaled ×0.8 or ×1.2 the answer changes by less than 0.5 %.

## Method (fit.py)
1. Two-point route: back-project the body pixel at f24 and f48 using the given depths. |P2−P1| over 1 s = 11.83 m/s.
2. Constant-velocity 3D line fitted to all 72 body pixels plus both depth constraints. RMS 1.1 px. |V| = 11.82 m/s, mostly along Z (11.73). Depth runs from 80.0 m at f0 to 114.7 m at f71.
3. Constant-acceleration fit (check): RMS 1.06 px, which is barely better. Mean of the per-frame speeds = 11.80 m/s.

All routes agree to within 0.3 %. Answer: 11.82 m/s.
Confidence: good. The main assumption is roughly uniform motion in 3D, since depths are given only at t=1 and t=2. The image slowdown and the shrinking wingspan are consistent with the bird receding.
