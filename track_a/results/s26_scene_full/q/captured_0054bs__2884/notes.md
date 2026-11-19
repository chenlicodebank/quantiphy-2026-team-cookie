# Q2884: velocity of the green ball at 1.0 s

**Answer: 2.1 m/s**

## Identification
At t = 1.0 s (frame 24, at 24 fps for both the file and the question), the green ball is the yellow-green tennis ball, called `yellow_object` in scene/. The "white ball" is `grey_object`. I checked this on a zoomed crop (frames/f24.png).

The size check is consistent: the green ball's width across the motion is 39.6 px. At 1.331 m with f = 763 px, that gives 6.9 cm, which matches a tennis ball.

## Method
- **Track** (`measure.py`, output in `green_track.json`): the ball is segmented by colour (G−B>40, R−G<50, R−B>30). This excludes the orange basketball, which the first, looser mask had picked up. For each frame I took:
  - the mask centroid;
  - the width across the motion: the 90th percentile of the cross-sections near the middle of the blur streak.
- **Depth** (`velocity.py`): from apparent size, Z(f) = 1.331 · w24 / w(f). A straight line is fitted to 1/w over the window, because a thrown ball's depth changes at a roughly constant rate. The depth is anchored to the given 1.331 m at frame 24.
- **Velocity:** each frame is back-projected to X = (u−640)/f·Z and Y = (v−360)/f·Z. I fitted a quadratic to each coordinate and took its derivative at frame 24. I also computed the mean of the 5 forward differences from frame 22 to frame 26.

## Results
| Window | Velocity (m/s) | 5-frame forward-diff mean (m/s) | Velocity, capsule widths (m/s) |
|---|---|---|---|
| 20–28 | 2.06 | 2.09 | 2.02 |
| 21–27 | 2.14 | 2.14 | 2.12 |
| 19–29 | 1.98 | | 1.97 |
| 20–32 | 2.17 | | 2.36 |

- At frame 24 the velocity components are about (vx, vy, vz) = (1.33, −1.02, 1.2) m/s.
- If the depth did not change at all, the in-plane speed alone would be 2.07 m/s.
- The rate of depth change is the main uncertainty, at roughly ±10%.

## Second route: capsule model (`capsule.py`)
Here the width comes from area and length, treating the blurred ball as a capsule: A = wL − (1−π/4)w². This gives the same trend, with velocities of 1.97–2.12 m/s for the central windows.

## Prior check (`bball_check.py`)
The basketball (orange ball) at frame 12, measured the same way, gives about 1.80 m/s. The prior is 2.21 m/s.

The gap is explained by the dropped source frame between frames 11 and 12: that step is doubled (53 px against about 24 px). A 5-frame smoothed forward difference that includes this step is inflated by about 1.23×, and 1.80 × 1.23 ≈ 2.2. This supports the size-and-depth method.

There are no timing anomalies near frame 24. The nearest is at 35→36, which is outside the windows used.

The given depth of 1.81 m for the orange ball at 1.0 s conflicts with its apparent size: by size it would be about 2.7 m. That value was not used.

## Caveat
The vertical acceleration of the green and white balls comes out at about 6.2–6.8 m/s² at 24 fps, not 9.8. This points to a time-base quirk in the recording, and I kept the benchmark's 24 fps convention.

**Confidence:** moderate. I expect the answer to be within about 10%.
