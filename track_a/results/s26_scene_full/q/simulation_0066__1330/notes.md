# q1330: speed of the yellow car (taxi) at t = 2.5 s, which is frame 60 at 24 fps (the file is also 24 fps)

## Calibration (3D pinhole, principal point at the image centre)
- Vanishing points from Hough curb lines on scene/bg.png (`edges.py`, `vp.py`): road A at (622, 77) and road B at
  (3137, 76). Line pairs agree within a few px. If the roads are perpendicular, f = 853 px (pair range 851–857).
  The horizon is the line through the two vanishing points, which fixes the ground normal.
- Checks with depth_info (`speed.py`): at f = 853 the 3D displacements of the depth points from f14 to f38 are
  - white van: 4.24 m, almost purely along road A. With the prior a = 4 m/s² from rest at t = 0, the expected
    value is 2·(38² − 14²)/576 = 4.33 m, a 2% match.
  - cyclist: along road A.
  - pedestrian: 1.19 m along road B, so 1.19 m/s, a plausible walk.
  These direction checks favour f between 853 and 900. Other constraints, such as constant reference height, are flat in f.
- Ground plane: the pedestrian's pelvis point comes from its depth (interpolated or extrapolated). Its feet lie
  vertically below it, so the feet ray gives the camera height above the ground, 6.98 m at f = 853. The pelvis comes
  out 0.92–1.04 m above the ground, which is consistent with a person.

## Taxi speed
- Route 1 (main, `wheels.py`): template-track the taxi's near front and near rear wheels over f50–70 (correlation
  above 0.94), project the tyre contact points onto the ground plane, and take the speed.
  - f = 853: front wheel 4.38, rear wheel 4.36 m/s (linear fit f54–66). The f57–63 means are 4.40 and 4.36.
    The raw backward difference at f60 is 4.52 and 4.41.
  - f = 880: 4.32 / 4.31. f = 900: 4.28 / 4.27.
- Route 2 (`speed.py`): the record's mask centroid intersected with a plane at the height that depth_info gives for
  the taxi at f14 and f38. This gives 4.22 (f = 853). It is lower because the side-on body centroid at f60 sits
  higher above the ground than the origin height derived from the f14/f38 centroids. Using the record's
  bottom-of-box point gives 3.93; that point is not a fixed ground point, so it is less reliable.
- Answer: 4.35 m/s. This is the wheel route with f ≈ 853–880, and the taxi moves at a nearly constant speed around f60.

## Confidence
Moderate, about ±5%. The main uncertainties are the focal length (853 to 900 changes the answer by about 2%)
and the camera height taken from the pedestrian (about 1–2%).
