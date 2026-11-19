# Q872: speed of the tennis ball at t = 1 s (m/s)

2D render, 24 fps (file and question agree), so t = 1 s is frame 24. There is one ball, rolling right along y ≈ 562 and slowing down steadily. The camera is static.

## Speed in pixels (measure.py)
- I tracked the background-difference centroid in all 41 frames. A quadratic fit leaves 0.13 px of residual.
- Raw backward difference x24 − x23 = 37.89 px/frame. The fit gives 37.95, and the mean of dx over frames 22–26 is 37.93.
- The scene/ record gives the same: 1052.74 − 1014.83 = 37.91.
- Result: 37.93 px/frame × 24 = 910.3 px/s.

## Scale from the prior (diameter 0.17 m), using diam.py and profile.py
- On frame 24 the horizontal half-max edges are at about 1041.2 and 1064.4, so the width is 23.2 px. Blur would widen this, not narrow it.
- The vertical extent runs from 551.5 to about 575.5 px, so the height is about 24 px. Below it, at 576–577, there is a faint contact shadow, which I excluded.
- The colour-difference half-max height over all frames is about 24.2 px, but it includes a little shadow. The chroma-only mask gives 20–21.5 px, which is too small because it misses the dark rim.
- The scene/ record's estimate is 24.5 px, but it includes shadow and blur.
- Adopted diameter: 23.7 px (range 23.2–24.5). Scale = 0.17 / 23.7 = 0.00717 m/px.

## Answer
910.3 px/s × 0.00717 m/px = **6.53 m/s**. Across the diameter range 23.2–24.5 px the result runs from 6.67 to 6.32 m/s, which is ±3%.

Second-route check: the per-frame speed from the quadratic fit and the raw difference agree within 0.2%. Nearly all the uncertainty comes from the ball's pixel diameter.

Confidence: moderate to high, within about 4%.
