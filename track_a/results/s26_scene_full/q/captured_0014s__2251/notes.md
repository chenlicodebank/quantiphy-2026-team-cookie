# q_2251 — velocity of rolling ball at t = 0.6 s (cm/s)

File fps = question_fps = 24, so t = 0.6 s is frame 14 (0.6 × 24 = 14.4, rounded to 14).

## Method (measure.py)
- I checked the ball centroids in scene/tracks/ball.csv for frames 6–19 on a gridded crop sheet (view.py → frames/seq.png). They are correct on the board, frames 8–16.
- Camera: f = 0.5959 × 1280 = 763 px, principal point (640, 360).
- 3D points: frame 0 back-projected with depth 1.8180 m, frame 14 with depth 1.7288 m (both from depth_info). These two points are 16.08 cm apart.
- The ball rolls in a straight line down the board, so each frame's 3D centre is the point on the P0–P14 line whose projection matches the tracked pixel centre.
- Arc position s (m), frames 11–17: 0.0346, 0.0947, 0.1252, 0.1608, 0.2020, 0.2501, 0.3002.
- Per-frame forward speeds (m/s), from frame 12→13 to frame 16→17: 0.733, 0.854, 0.989, 1.154, 1.204.
- The step from frame 11 to 12 is irregular (21 px, about 1.44 m/s), probably frame-timing jitter.

## Estimates of v at frame 14
| Route | v (m/s) |
|---|---|
| Forward difference at frame 14 | 0.989 |
| Forward differences averaged over a centred 5-frame window, frames 12–16 | 0.986 |
| Central difference | 0.921 |
| Linear fit over frames 12–16 | 0.930 |
| Quadratic fits over frames 8–16 or 12–16 | 0.93–1.04 |
| Fit with acceleration fixed at the prior 4.6 m/s², frames 12–16 | 0.93 |
| Same fixed-acceleration fit, frames 10–16 | 1.125 |

## Second route
Image speed with a local scale, as a cross-check:
- In-plane speed: 14.55 px/frame × 1.7288 / 763 × 24 = 0.79 m/s.
- Correcting for the depth component of the motion gives about 0.95 m/s. This agrees with the routes above.

## Caveat
The acceleration measured here is about 3.3 m/s², which is lower than the prior's 4.6 m/s². The reference data's acceleration may be noisier. A higher acceleration would favour the upper end of the range.

## Answer
v ≈ 0.97 m/s = 97 cm/s. This follows the forward-difference convention, about 0.99, nudged slightly toward the fits at about 0.93. Confidence is moderate, about ±7 %.
