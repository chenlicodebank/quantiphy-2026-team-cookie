# q_1759 — length of the orange car (m)

Prior: acceleration of the orange car = -2.86 m/s^2. This is a 2D top-down clip at 30 fps (question_fps is also 30).
Scale = 2.86 / |pixel acceleration|.

## Measurements (fit.py, using scene/tracks/car.csv)
- Quadratic fit of the car's mask-centroid y against t, using only frames where the car is fully visible:
  - frames 16–90: a = -162.26 px/s^2 (residual 0.27 px)
  - frames 40–90: a = -162.11 px/s^2
  - front edge, frames 45–90: -162.21 px/s^2
  - The cubic term is negligible, so the deceleration is uniform.
  - Not used: the rear edge (-168) and the front edge in the early, motion-blurred frames (-147 to -156). Edge
    positions are integer pixels, and blur affects them.
- Car length in pixels (bumper to bumper, along y): the median bbox height over frames 40–90 is 289 px. I checked
  this by eye on frame 60 with a grid: the car runs from about y = 579 to y = 866.
- Scale = 2.86 / 162.2 = 0.01763 m/px. Length = 289 × 0.01763 = **5.09 m**.

## Check
Independent fits over different frame windows and reference points (centroid, front edge late) all agree within
0.1%. An uncertainty of ±2 px in the pixel length gives ±0.7%. A 5.1 m sports car is plausible.
Confidence: high.
