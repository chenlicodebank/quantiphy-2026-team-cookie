# q_659: speed of the vacuum cleaner at t = 0.5 s

- 2D top-down render, static camera, file fps 24 = question_fps 24, so t = 0.5 s is frame 12.
  Speed = |p(12) - p(11)| x 24 x (m/px).
- Scale from the prior: vacuum diameter 0.438 m.

## Measurements (measure.py, check.py)
- Own circle fit (360 rays, outermost half-max crossing between disc and floor, least-squares circle with outlier rejection)
  on frames 9-15: diameter 121.98-122.19 px, mean 122.09 px -> 0.003587 m/px. Scene record gives 122.5-123.2 px (0.6% larger);
  the difference changes the answer by <1%.
- Centres: f11 (1611.63, 410.09), f12 (1599.54, 407.91) -> step 12.28 px -> **1.057 m/s**.
  Neighbouring steps 11.17 (f10->11) and 13.25 (f12->13) px show smooth acceleration; quadratic fit of positions over f9-15
  gives a smoothed step of 12.21 px -> 1.051 m/s. Scene track: step 12.46 px with d = 122.8 px -> 1.067 m/s.
- SAM 3 (box-prompted "white round object", frames 11 and 12): centroids (1611.3, 410.7) and (1599.2, 408.5) -> step 12.3 px,
  agreeing with the circle fit. SAM extents are 129-133 px (about 6% larger than the fit). Checked on raw intensity profiles
  through the centre at frame 12 (check.py) and a 4x zoomed crop: the SAM mask also includes the dark contact/shadow ring
  (grey 84-100, darker than floor 88-105) 3-4 px outside the white rim on each side. The disc's own half-max edge gives
  124.2 px horizontally and 120.2 px vertically (mean 122.2), which matches the circle fit. So the circle fit is right and SAM
  overestimates the size; the SAM centre is still usable for motion.

## Answer
Speed at 0.5 s = 12.28 px x 24 x 0.438 / 122.09 = 1.057 m/s (routes: 1.051 smoothed, 1.067 scene record, ~1.06 SAM centroid).
Answer 1.056 m/s. Confidence: high (about ±2%).
