# q_1737: average speed of the person (m/s)

The file is 25 fps with duplicate frames 1, 26 and 51. The source is a 24 fps render, so I used question_fps = 24 and
render frame r = video frame with the duplicates dropped (72 render frames).

## Scale (geom.py)
- Prior: boat speed = 4 m/s. Boat depths: 177.21 m at t=1 s and 178.00 m at t=2 s. Boat reference point is the
  template-tracked `ref_x/ref_y` from scene/ (8.40 px per render step, steady).
- Back-projecting the boat at render frames 24 and 48 with the given depths and requiring a 4 m displacement gives
  f = 9070 px (horizontal FOV 9.7 deg).
- Checks:
  - The boat's main-axis length (512 px) comes out at 10.0 m, a realistic fishing boat.
  - The boat moves horizontally, which with no camera roll puts the camera pitch at 54 deg down.
  - The person's bbox height (64 px, 1.28 m across the line of sight) fits a person of about 1.75 m seen from 54 deg above.

## Person (measure.py)
- I tracked the filled-mask centroid as the pelvis proxy. It moves 2.15 px per render step (51.5 px/s) toward the image
  bottom, with gait jitter of about 1.8 px.
- Route A, perpendicular motion only, using the person's depths (182.92 to 183.02 m, only +0.09 m/s): 1.04 m/s
  (0.99 m/s from the t=1 to t=2 positions).
- Route B, walking on horizontal ground (plane normal from the boat-derived pitch): the person moves toward the camera
  and the depth falls by about 2.3 m over the clip. Speed from the linear-fit endpoints is 1.284 m/s; the mean of the
  smoothed per-frame speeds is 1.269 m/s.
- I chose route B. The given person depths barely change (under 0.1 m/s) although the body clearly walks toward the
  image bottom. Following the benchmark rule, that distance is the character's near-static object origin, not the
  pelvis. On a horizontal ground plane, motion toward the image bottom must include an approach toward the camera, so the
  speed perpendicular to the line of sight underestimates the true speed.
- The apparent-size change this predicts (about 1.2 pct) is too small to measure against the gait changes in the
  64 px mask.

Answer: 1.28 m/s. It is a plausible walking speed.

Confidence: medium. The main risk is the reading of the depths: if the reference used them as real, the answer would
be about 1.0 m/s.
