# q_730: acceleration of the paper airplane at t = 1 s (m/s^2)

Prior: the chalkboard is 5 m long. 2D scene, static camera. question_fps = file fps = 24, so t = 1 s is frame 24.
Convention: a(t) = (speed(24) - speed(23)) x fps, where speed is the backward difference of the origin.

## Scale (board.py, board_outer.py, SAM 3)
- Outer wooden frame, from colour profiles at frame 45: left edge about x 322.5 (the transition runs from 318 to 326), right edge
  about x 1690.5 (1688 to 1694). That gives **1368 px**. The inner green surface spans x 341.5 to 1670, so 1329 px.
- SAM 3 "chalkboard" mask at f24: box x 324.2 to 1690.0, so 1366 px. This matches my outer frame within 0.2 %. The record said
  1372 (320 to 1692), which is 0.3 % off. All three agree.
- I took the board length to be the whole object including its frame: 5 m / 1368 px = 3.655e-3 m/px. With the green
  surface only (1329 px) the scale would be 3.762e-3 m/px, 2.9 % larger.

## Plane motion (measure_plane.py, analyze.py, speedfit.py, combine.py)
- I segmented the plane against a median background for frames 14 to 33, where it is clear over the board. My
  reference points are the mask centroid, the midpoint of nose and tail along the main axis, and the bbox centre. They
  agree with the record's ref_x/ref_y within about 1 to 2 px.
- The SAM 3 track of "paper airplane" (box prompt at f24) is a fourth reference. The SAM mask at f24 has centroid
  (1092.7, 343.2) and length 137 px, against my centroid (1091.1, 342.7) and length 134 px. Both differ by less than 3 %.
- Speeds are about 1840 px/s at f17, falling to about 1680 at f23/24 and about 1410 at f32. Through t = 1 s the plane
  is slowing steadily.
- A raw single-frame difference at f24 is too noisy: it ranges from +112 to -882 px/s^2 depending on the reference,
  because ±1 px of position jitter is worth ±800 px/s^2. So I fitted the slope smoothly in two ways:
  - Route A: fit a polynomial of degree 3 or 4 to x(t) and y(t), sample it at frames 23 and 24, and take the backward
    differences. Results: -615 to -873 px/s^2.
  - Route B: fit a straight line to the per-frame speeds over windows 18-30, 19-29 and 20-28, centred on f23.5.
    Results: -755 to -866 px/s^2.
  - Across 4 references x 5 fits: mean -777, median -784, std 72 px/s^2.
- Result: a = -780 px/s^2 x 3.655e-3 m/px = **-2.85 m/s^2**, a deceleration. I report the magnitude, **2.85**.
  - With the green-surface scale it would be 2.94.
  - The fit spread is about ±0.25 m/s^2 (roughly ±9 %).

Confidence: moderate. The scale is solid. The acceleration is limited by position noise, so the smoothed slope is uncertain by
about ±10 %.
