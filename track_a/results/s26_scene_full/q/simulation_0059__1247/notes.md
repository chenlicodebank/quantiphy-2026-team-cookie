# Q1247: length of the white car (the white cargo van)

The file rate and question_fps are both 24. The white car is the van in scene/tracks/van.csv. I checked this on frames 0, 40 and 63.

## Method (3D, pinhole)
- Prior: the van's acceleration is 4 m/s^2 along a straight line, so s(t) = 2 (t - t0)^2.
- Depths of the van's origin: 43.8120 m at f14 and 43.0028 m at f38.
- `fit3d.py` fits a single 3D line-motion model to the van's horizontal pixel track. It uses the patch_cx track
  plus the bbox-centre offset (27.9 px), and both depths are constraints. The free parameters are the focal
  length F, the start point X0 and Z0, the heading theta and the start time t0.
  - Result: F = 2212 px (horizontal FOV 52 deg), heading -4.5 deg (toward the camera), t0 = -0.035 s.
  - The rms residual is 0.09-0.28 px.
  - The fit is stable whether it uses frames >= 2, 10, 25 or 34: F ranges 2210-2216 and the length changes by
    less than 0.3 %.
- Length: the van is modelled as a box (length L, width W) on the fitted line. L is solved so that the projected
  box's horizontal extent equals the measured bbox length, on frames 34-47 and 62-71.
  - With W = 2.0 m, the median is 5.52 m (range 5.45-5.63).
  - With W = 2.2 m, the median is 5.50 m.
  - With no end-face correction (W = 0), it is 5.77 m. That is an upper bound: the front face is visible around
    f34-47 and the rear face from about f62 on, which the growing pixel length confirms.

## Checks
- `measure.py` is a simpler route: a quadratic pixel fit, then F solved from the displacement between f14 and
  f38. It gives 5.50 m with no end-face correction.
  - It differs from the full fit only through the motion start time t0: that route assumes the van starts at
    about f0.3, while the full fit finds about f-0.8.
  - The early per-frame displacements support the full fit's t0: dx from f1 to f2 is 0.8 px, which is consistent
    with motion already under way.
- Visual check at f40: the rear end is at about x 842 and the front bumper at about 1135-1143.

## Answer
5.52 m. Confidence: moderate-high, about ±4 %. The van's width (end-face correction) and the bbox end
precision (±3 px) are the main sources of uncertainty.
