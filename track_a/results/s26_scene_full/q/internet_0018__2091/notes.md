# Q2091: tennis ball velocity at 1.5 s (m/s)

**Time base:** the file runs at 29.97 fps and the question at 30 fps; that is not a re-time. t = 1.5 s gives frame 45 either way. I used 30 fps (it changes the result by 0.1 %).

**Scale (prior: singles court width = 8.23 m):** the drone looks almost straight down. I measured the singles sideline separation at frame 0 with vertical intensity profiles (`measure.py`):
- x = 1200: 1515 − 593 = 922 px
- x = 2600 (near the ball): 1509 − 585 = 924 px
- x = 3200: 1507 − 580 = 927 px

The record gives 924.7 px. Scale = 8.23 / 924.7 = 0.008900 m/px.

**Ball:** the ball is in free flight after the serve (contact is between frames 36 and 37, and it hits the net at frame 48). Camera drift is about 0.3 px/frame, which is negligible. Centroids:

| Source | Frame 44 | Frame 45 | Frame 46 | Frame 47 |
|---|---|---|---|---|
| Record | (2648.0, 1026.6) | (2522.9, 1011.5) | (2403.7, 997.8) | (2289.0, 985.8) |
| My re-measurement (G−B weighted, slightly pulled to the green fringe) | (2648.1, 1026.2) | (2523.3, 1011.6) | (2405.2, 996.3) | (2290.4, 986.6) |

Steps from those positions:

| Step | Record (px) | Mine (px) |
|---|---|---|
| 44→45 | 126.0 | 125.7 |
| 45→46 | 120.0 | 119.1 |
| 46→47 | 115.3 | 115.1 |

**Velocity:** I followed the annotator convention, a forward difference at frame 45: 120.0 px/frame × 30 = 3600 px/s, × 0.00890 = **32.0 m/s**.

**Checks:**
- Central difference over frames 44–46: 123 px/frame, which gives 32.8 m/s.
- Backward difference: 33.6 m/s.
- My own centroids with a forward difference give 31.8 m/s.

A serve speed of about 115 km/h is plausible. Confidence: good. The spread across difference schemes is about ±3 %.
