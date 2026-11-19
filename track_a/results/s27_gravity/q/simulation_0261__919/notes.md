# q_919 – speed of the mug at t = 0.4 s

The video is 2D: the mug falls straight down. The question rate is 24 fps, the same as the file rate. t = 0.4 s is frame round(9.6) = 10.
Speed follows the convention: one-frame backward difference |p10 - p9| x 24.

## Method (measure.py)
- I re-measured the mug mask myself: max-channel difference above 14, using the last frame as background above row 1100 and frame 0 below it. This reproduces the scene record to within 1 px.
- Scale from the prior: g = 9.8 m/s^2 equals the pixel acceleration from a quadratic fit of the mask centroid y over frames 3-17. Frame 18 is excluded because the floor shadow touches the mask, and impact comes between frames 18 and 19. The fit gives a = 5084.5 px/s^2 with a residual of 0.10 px, so 1 px = 9.8/5084.5 = 1.927e-3 m.
- Centroid y is 443.2 at frame 9 and 528.1 at frame 10, so the step is 84.9 px, or 2037 px/s, which gives **3.93 m/s**.

## Checks
- Other reference points and fit windows all agree within about 1%: the body-only centroid gives 3.928, the bbox centre 3.98, and the centroid with fit windows 1-10 and 6-14 gives 3.90 and 3.93.
- The fitted velocity at the midpoint of frames 9 and 10 is 3.926 m/s, which matches the backward difference.
- The mug's instantaneous velocity at t = 10/24 s would be about 4.13 m/s. The answer uses the backward-difference convention instead.
- The top and bottom edges are noisier because the apparent height changes with perspective, so I did not use them.

Confidence: high, within about 2%.
