# Q2502: distance travelled by the tennis ball until it hits the whiteboard (cm)

The file rate and question_fps are both 24. The whiteboard hit is at t = 1.24 s, which is frame 30. That matches the direction change and the farthest point in scene/ (frame 30). The ball is held still in frames 0 to 12, creeps in frames 13 to 17, then rolls almost straight across the table to the board.

## Method (lab card)
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Ball centre: the colour-mask centroid from scene/tracks/ball.csv. I checked frame 5 by eye: the ball is visible, and its tangential (roughly vertical) extent is about 97 px.
- Depth along the ray:
  - Where depth_info gives it, I used the given value: frame 24 = 0.901 m, frame 30 = 1.144 m (and frame 38 = 1.027 m).
  - At the start, depth_info gives nothing, so I used the size: R = f x 0.067 / d_tan / cos(theta).
  - Check against the given depths: the size depth comes out 2 to 6 pct too far (given/size ratios 0.94, 0.96, 0.98). So I applied a correction factor between 0.94 and 1.0 to the start depth. Start R is about 0.64 to 0.67 m.
- The path is nearly straight, so path length is about the same as the net 3D displacement.

## Results
| Route | Value (cm) |
|---|---|
| Start (mean of frames 0 to 12) to P30, given depth | 65.7 (no correction) to 67.8 (corr 0.94); 67.1 at corr 0.96 |
| Start to P24 to P30, both given depths | the same to within 0.1 |
| Per-frame size-depth path, 3- to 5-frame smoothing (path.py) | 63 to 69 |

Unsmoothed per-frame size depth gives 82 to 86 cm. That number is inflated by depth noise and blur, so I did not use it.

**Answer: 66.5 cm.** Confidence: moderate, about ±5 pct. The start depth is not given, and it is the main uncertainty.
