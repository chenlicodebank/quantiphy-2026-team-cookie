# Q2051: velocity of the ball at 2.00 s (cm/s)

## Scale
The prior says the basketball diameter is 24 cm. The ball's full outline is about 45 px across: the scene record measured 45.1–45.9 px against the sky, and I checked it on my own crop at f59 (frames/crop59.png, about 45 px). This gives **0.533 cm/px**, used as a single planar scale.

## Time base
- 2.00 s is frame 60 at question_fps = 30, or frame 59 at the file's 29.66 fps.
- Gravity check: a parabola fit to the flight (f48–80, background coordinates) gives a_y = 2.064 px/frame².
  - At 30 fps this is 9.91 m/s².
  - At 29.66 fps it is 9.69 m/s².
  - Both rates are plausible. 30 fps is slightly closer to g, so I used 30 fps and frame 60.

## Track
- I used the ball centres in scene/tracks/ball.csv, mapped to background coordinates (x_bg, y_bg) so the camera pan is removed.
- The ball is in free flight over f47–81, and f60 is just before the apex (f65).
- Over f54–73 the ball is seen against palm fronds. The colour mask from my own re-measurement (measure.py) fails there, but the recorded centre sits on the ball in crop59.png.
- The parabola residual is about 2.2 px rms, which matches the record's stated jitter.

## Velocity (velocity.py), at 30 fps
| Frame | Raw forward diff | Backward diff | Central diff | Parabola derivative | 6-frame linear fit |
|---|---|---|---|---|---|
| f60 | 587 | 546 | 562 | 556 (at f) / 549 (at f+0.5) | 538 |
| f59 | — | — | 565 | 570 | — |

The raw single-frame differences are noisy (±25 cm/s from 2–3 px centre jitter). The smoothed estimates agree at about 550–565 cm/s.

**Answer: 555 cm/s.**

## Second-route check
- Using 29.66 fps and frame 59 instead gives 556–564 cm/s (parabola or central difference), which is consistent.
- The speed is dominated by the horizontal component, about 33.5 px/frame, or about 535 cm/s.

## Confidence
Moderate to good. The main uncertainty is the ball diameter (±1.5 px, about 3%) and the smoothing choice (about 3%). The planar-scale convention ignores the ball's motion in depth, as the reference annotators also did.
