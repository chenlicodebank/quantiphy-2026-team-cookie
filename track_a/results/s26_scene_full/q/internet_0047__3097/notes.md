# q3097: distance between the two vertical red lines (m)

The prior is "ball velocity at 0.5 s = 2.94 m/s". The file and the question both use 30 fps, so t = 0.5 s is frame 15.

**Scale (internet convention: one planar scale from the prior).**
- Ball centre track from scene/tracks/basketball.csv. I checked it against frame 15: the ball centre is at about (1240, 512).
- Speed per frame (measure.py):
  - forward difference at frame 15: 78.7 px/frame stabilised, 79.0 px raw;
  - backward difference: 77.3 px;
  - mean over frames 13–17: 78.1 px;
  - median over the whole track: 77.9 px.
- Adopted 78.3 px/frame = 2350 px/s, so the scale is 2.94 / 2350 = 1.251e-3 m/px.
- The camera drift is about 1 px/frame, which is negligible.

**Line spacing.** Maroon colour mask on frame 15, measured on image rows:

| row y | between centrelines (px) | inner edges (px) | outer edges (px) |
|---|---|---|---|
| 530–550 (ball level) | 1497–1499 | 1457–1461 | 1536–1537 |
| 700 | 1512 | | |
| 1000 | 1560 | | |

The spacing widens toward the bottom of the frame (keystone).

I used the centreline spacing at the height of the ball's path: about 1500 px × 1.251e-3 = **1.88 m**.

**Other readings** (same scale):
- inner edges: 1.83 m
- outer edges: 1.92 m
- centrelines at mid-image: 1.89 m

**Second route.** Using the forward-difference-only speed (79.0 px, scale 1.241e-3) gives 1.86 m. Using the whole-track mean speed gives 1.89 m.

**Confidence.** Moderate, about ±4 %. The main uncertainty is which line edges the annotator measured between.
