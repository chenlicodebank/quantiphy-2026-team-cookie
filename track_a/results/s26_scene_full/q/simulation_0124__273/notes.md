# q_273 – width of the grey (silver) and red-striped car

2D top-down video at 24 fps (question_fps is also 24). One metres-per-pixel scale for the whole image.

## Scale
- Prior: the black (dark) car moves at 26.085 m/s. I computed its per-frame steps from scene/tracks/dark_car.csv (frames 3–45):
  26.97 px/frame (median; mean 27.01) = 647.3 px/s. This gives **0.04030 m/px**.

## Width of the silver car
- The record gives a body width of 47 px (±2), or 51–53 px measured across the door mirrors.
- My own check (prof.py) at frames 17–19, where the car points straight down, comparing each frame with the empty last frame:
  - row-by-row extent of the difference mask over the body rows: median 48.5–50 px
  - half-maximum extent of the column profile: 36–39 px (the dim body edges fall below half-max, so this underestimates)
  - the 5x crop (frames/s18raw.png) shows the body spanning about x 732–779, i.e. about 47 px
- I used a body width of **48 px**, taking width as wheel to wheel per the guidance.
- 48 × 0.04030 = **1.93 m**. With 47 px it would be 1.89 m.
- Other reading: across the mirrors (52 px) the width would be about 2.10 m.

## Cross-check
- The silver car's length is 122 px × 0.0403 = 4.92 m, so its length/width ratio is 2.6. Both values are plausible for a sports car.

## Confidence
- Moderate. The scale is good to within 1 %. The width is uncertain by ±1–2 px (about 3 %), plus the question of whether the mirrors count.
