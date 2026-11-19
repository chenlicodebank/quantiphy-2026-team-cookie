# Q9: velocity of the ball at t = 0.0 s (m/s)

Time base: question_fps = 30 (the file rate is 29.997709 fps). t = 0 is frame 0.

## Scale
The prior is "gravity = 9.8 m/s^2", but the ball's motion in this clip is animated and does not follow one gravity.
In the record, the flight has about 0.17 px/frame^2 and the drop below the net about 0.65 px/frame^2. Those give
15.6 px/m and 60 px/m, which would make the ball 1.9 m or 0.50 m across and the player 14 m or 3.7 m tall. Both
are impossible, so the prior gives no usable scale. I took the scale from objects of known real size instead:
- basketball diameter 0.24 m / 29.6 px = 0.0081 m/px
- standing player about 1.85 m / 224 px = 0.0083 m/px

I used 0.0082 m/px. At frame 0 the ball is in the player's hands, so it is at the player's depth.

## Ball motion at the start (early.py, template matching plus orange-blob centroid)
| Frame step | Template step (px) | Centroid step (px) |
|---|---|---|
| 0 → 1 | 0.02 (frames 0 and 1 are identical; diff01.py shows only 16 changed pixels, none on the ball) | 0.0 |
| 1 → 2 | 1.08 | 0.7 |
| 2 → 3 | 3.0 | |
| 3 → 4 | 6.3 | |
| 4 → 5 | 9.1 | |

The ball is still at t = 0 and starts to move as the player lifts it.

The convention's backward difference cannot be taken at frame 0, and the forward difference is 0. The answer has
to be positive, so I assume that frame 0 duplicates the first rendered frame and take the first real step instead
(frame 1 → 2): about 1.0 px/frame × 0.0082 m/px × 30 = 0.25–0.27 m/s.

As a second route, the centroid step (0.7 px/frame) gives 0.17 m/s.

Answer: 0.26 m/s. Confidence is low: the true answer may be about 0 (the ball is held still), and it depends on how
frame 0 is handled.
