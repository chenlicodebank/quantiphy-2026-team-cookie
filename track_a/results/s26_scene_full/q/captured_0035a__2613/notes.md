# q_2613: basketball velocity at t = 0.6 s (cm/s)

t = 0.6 s → frame 14 (question_fps 24, which is also the file's fps). Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Centres
- I re-measured the basketball centre (orange HSV mask centroid, `measure.py`) for frames 8–26. It matches
  scene/tracks/basketball.csv within about 1 px. Frame 14: (737.0, 533.3). The ball is moving freely (kick released by frame 11,
  collision at frame 19–20). There is a suspected dropped frame between 11 and 12, so all windows use frames 12–18.

## Depth along the path (`plane.py`)
- depth_info gives the basketball at 2.270 m at frame 14. The 4th line, labelled "soccer_ball" at t = 1.6 s with 2.412 m, is
  taken to be the basketball, because the soccer ball already has 3.052 m at that time. The soccer ball is at 2.758 m (frame 14)
  and 3.052 m (frame 38).
- The balls roll on the floor, so I fitted the plane of the ball centres through these 4 back-projected points. Residuals are
  ≤1.6 cm. The fit gives a camera about 1.69 m above the floor, pitched down about 32°, which is plausible. Each frame's centre
  is the ray–plane intersection. Depth goes from 2.236 m (frame 12) to 2.343 m (frame 18), and the plane reproduces 2.269 m at
  frame 14 (given: 2.270).
- Velocity: a linear fit of the 3D positions over frames 12–17 gives **131.7 cm/s**. Other windows: 12–18 gives 131.5, 13–17
  gives 131.1, 12–16 gives 132.1. Centred differences give 132.0–132.1. Per-frame forward speeds are 124–140.

## Cross-checks
- Constant depth of 2.27 m (ignores motion in depth): 124 cm/s. This is a lower bound.
- Depth from pixel diameter (2.27 x d14 / d): 145 cm/s. The diameter is inflated by motion blur and noisy by about ±2%. It also
  rises again after the collision even though the ball keeps moving away, so I trust it less than the plane.
- The plane-based value lies between these two. Both the recorded track and my own centroids give 131–132.

Answer: 131.7 cm/s. Confidence: moderate, about ±7%. The main uncertainty is the depth-rate model.
