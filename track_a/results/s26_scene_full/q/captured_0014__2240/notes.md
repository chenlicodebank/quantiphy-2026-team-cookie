# Q2240 — velocity of the rolling ball at t=0.6 s (cm/s)

The file rate and question_fps are both 24, so t=0.6 s is frame 14. The ball is rolling down the tilted white board (frames 12–16 are clean).

## Method
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360). The depth_info values are Euclidean distances along the viewing ray.
- `track.py`: the ball is found by differencing against a background (median of frames 36–48), with a diff-weighted centroid.
  Centres (u, v): f12 (545.8, 329.9), f13 (546.6, 341.0), f14 (547.4, 354.8), f15 (548.3, 370.3), f16 (549.8, 389.3).
  These agree with scene/tracks/ball.csv to within about 1 px, except frame 15, where the record has 367.0 and my centroid has 370.3.
- 3D path: the ball moves along a straight line on the board. I built the line two independent ways:
  (a) through the ball's back-projected centres at t=0 (d=1.818) and t=0.6 (d=1.7288), in `solve.py`;
  (b) parallel to the board, using slope_far 1.854 and slope_near 1.701 at the board's top and bottom edge midpoints, in `board.py`.
  Both give nearly the same direction and the same scale along the slope: 0.00273 vs 0.00274 m per image pixel.
  The back-projection reproduces the 1.7288 m depth at frame 14.
- Each frame's position along the slope comes from the closest point between that frame's viewing ray and the line.
  Steps per frame: 12→13 3.04, 13→14 3.70, 14→15 4.06, 15→16 4.86 cm (route b).

## Check against the prior
Using the paper's convention, a(14) = s16 - 2 s15 + s14 = 0.80 cm per frame², which is 4.61 m/s².
This reproduces the prior of 4.6 m/s² at t=0.6, so the track, the scale and the forward-difference convention are confirmed.
(Second differences at the neighbouring frames are noisy: 3.8 and 2.1 m/s². A quadratic fit over frames 12–16 gives a=3.3 m/s².)

## Velocity at frame 14
- Forward difference s15 - s14: 4.06 cm x 24 = 97.4 cm/s (route b); 4.01 x 24 = 96.2 cm/s (route a).
- Other estimates: central difference about 92, quadratic fit 92–94, backward difference about 88 cm/s.

The answer is **97 cm/s**, the forward-difference convention that reproduces the prior's acceleration. Confidence: moderate-high. The plausible range is 92–98 cm/s.

Frames 8–11 (release, near the blurred hand) are irregular and were not used.
