# Q1219 – distance between the right and left streetlights (m)

The file runs at 30.0033 fps and the question at 30 fps; all frame/time conversions use 30 fps.
Each lamp's distance from the camera is given (L 17.706 m, R 17.594 m). So the answer is
|d_L·ray_L − d_R·ray_R|, which needs only the focal length f (and a small camera yaw).

## Measurements
- Lamp poles, measured in code on frame 0 (`lamps.py`, rows 500-550): left x ≈ 201, right x ≈ 896.
  The base is at y 757 and the top at y 366, which matches the scene record.
- Orange car reference (wheelbase centre) comes from scene/tracks: f0 1343.7 (extrapolated) and f30 621.3.
  A quadratic fit over frames f6-79 (leaving out the occluded f35-45) gives a pixel acceleration of 301.1 px/s².
- Black car: constant −69.84 px/frame. At t=2 (f60) it is off-screen, so its position there is extrapolated.

## Focal length (`geom.py`, `fit.py`)
- Route A, no yaw, orange car's two depths alone: f ≈ 1585 with Z = 15.29 m.
- Route B, the prior: a = 2.86 m/s² = 301.1 px/s² × Z/f, so Z/f = 0.009498. With d(t=1) = 15.436 this gives
  f ≈ 1610, Z = 15.30. Feeding that back predicts d(t=0) = 17.21 m against the given 17.26.
- Route C, solving f, yaw and Z together from the orange depths and the prior: f = 1626, yaw 0.6°.
  This gives a lamp distance of 7.32 m.
- Global least squares over all 7 constraints (car depths, lamp depths with both lamps at the same depth, and the prior):
  f ≈ 1630, yaw 0.8°, with residuals of a few cm. Lamp distance 7.29-7.35 depending on the assumed origin heights.
- Lamp-depth consistency together with the orange car: f ≈ 1605, lamp distance 7.40-7.47.
- The black car's depths fit on their own pull f to about 1790-1940, which contradicts both the orange car and the prior.
  This is probably because its t=2 position is far off-screen and extrapolated, so it gets low weight (it is still
  included in the global fit).

## Answer
Taking the lamp origin at the base (y 757), the answer is about **7.33 m**; across the models the spread is 7.28-7.47.
If the origin is at mid-pole, the value is about 0.06 m higher.
Confidence: good, about ±2%.
