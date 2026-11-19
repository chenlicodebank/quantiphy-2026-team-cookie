# Q2650 – soccer ball velocity at t = 1.4 s (cm/s)

The file and the question both run at 24 fps, so t = 1.4 s is frame 34.

## Data used
- The soccer ball's centres come from scene/tracks/soccer_ball.csv. I checked frame 34 by eye (f34.png): the centre is at about (690, 497) and the diameter is about 60 px. The track is correct.
- Camera: f = 763 px, principal point (640, 360). Each centre is back-projected as d * r/|r|.
- depth_info gives two "soccer ball" distances at 1.4 s: 2.602 m and 2.373 m. One of them is probably the basketball's.
  - From apparent size, the basketball should be at about 2.60 m: its diameter grows from 61.2 to 65.1 px compared with t = 0.9 s, when it was at 2.778 m.
  - From apparent size, the soccer ball should be at about 2.52–2.57 m: its diameter of about 60 px is similar to its size at 0.9 s, when it was at 2.477 m.
  - Neither given value fits cleanly, so I used the mean, 2.49 m. Using 2.373 m instead changes the result by about -5%; using 2.602 m changes it by about +5%.
- Depth trend after the collision at frame 25: from a linear fit of 1/radius over frames 28-47, the ball comes toward the camera by about 0.48% per frame, which is roughly -0.29 m/s.

## Results (vel.py)
With d34 = 2.49 m:

| Depth model | Smoothing | Speed (cm/s) |
|---|---|---|
| Constant depth | 5–10 frame windows / linear fit | 51–59 |
| Size-based depth trend | 5–10 frame windows / linear fit | 58–66 |

- Lateral component: about 6.6 px/frame, which is about 0.50 m/s.
- Frame 35→36 contains a dropped source frame, which inflates any window that includes it.
- Second route: a linear fit of the 3D positions over frames 29-39 gives 51.6 cm/s (constant depth) and 59.0 cm/s (size-based depth).

Answer: **58 cm/s**. Confidence is moderate (about ±10%). The main uncertainties are which of the two depths belongs to the soccer ball and how large the depth-rate component is.
