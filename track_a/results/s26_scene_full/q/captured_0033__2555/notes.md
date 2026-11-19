# q 2555 — ping pong ball velocity at 0.5 s (cm/s)

t = 0.5 s -> frame 12 (question_fps 24 = file fps). Ball is falling (released ~frame 9, bounce 1 between frames 14 and 15), motion-blurred.

## Measurements (streak.py, background-difference blob, centroid of blur streak = mid-exposure position)
frame: v (px) — 10: 190.0, 11: 211.3, 12: 287.4, 13: 340.6, 14: 404.1; u drifts only ~-0.8 px/frame.
Frame 11 looks off (ball still near the fingers; its increments 21 / 76 px do not fit a parabola), frames 12-14 do
(increments 53.2, 63.5 px -> 10.3 px/frame^2).

## Scale
Lab card: f = 0.5959 x 1280 = 763 px. Depth = 1.457 m (depth_info at t = 0.9 s, frame 22: the ball is at the same
back-of-table spot, it falls straight down and bounces in place, so the depth at frame 12 is about the same).
Back-projected 3D centres, constant Z.

## Results
- forward difference 12->13: 244 cm/s (reference convention)
- 5-frame smoothed (frames 10->14): 245 cm/s (second route, agrees)
- parabola instantaneous at frame 12: 220 cm/s; central diff 11->13: 296 (inflated by bad frame 11)
Answer: 244 cm/s.

Check: the pixel acceleration 10.3 px/frame^2 implies depth 1.26 m if it is g (noisy from 3 points), and the ball width
26-29 px implies ~1.1-1.2 m, so the given 1.457 m could be a little large; the answer follows depth_info as the
reference does. Confidence moderate (±10 %).
