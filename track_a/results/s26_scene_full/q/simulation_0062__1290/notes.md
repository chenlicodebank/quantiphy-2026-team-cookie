# q1290 – average speed of walking pedestrian (whole clip), m/s

File fps = question fps = 24. t=0.58 s -> f14, t=1.58 s -> f38. Frames 0 and 1 are identical (duplicate first frame).

## Calibration (calib.py)
- White van (prior: a = 4 m/s^2) moves parallel to the image plane at constant depth. Quadratic fit of its x track: a_px = 307.2 px/s^2 (resid 0.5 px) -> Z/f = 0.01302 m/px.
- White-van depths (30.065 / 29.307 m at f14 / f38) with its pixel positions -> Z/f = 0.01293, Z = 29.17 m, f = 2256 px.
- Acceleration scale + each depth -> f = 2239–2240 px. Used f ≈ 2248 px (the routes agree within 0.7%).

## Pedestrian (ped.py, traj.py, traj2.py)
- Pelvis track from scene/tracks/pedestrian.csv, checked on zoomed frames f2 and f71.
- Back-projecting the pelvis with the given human depths: f14 (-5.88, 0.04, 16.25) m and f38 (-5.88, 0.04, 15.05) m. The pedestrian walks straight toward the camera at constant X. Displacement 1.202 m in 1.0 s -> **1.20 m/s** (main route).
- Consistency check: height_px*Z/f = 1.827 m at both anchors, and camera height = 1.00 m from ground_y at both.
- Whole-clip routes (f1–f71, linear fit of Z(t)): from apparent height 1.240; from ground row 1.226; from pelvis u with constant X 1.249 (windows: 1.33 early, which is likely biased by the clipped mask against the white van, then 1.23 and 1.20).
- The answer is the mean of per-frame pelvis speeds, which comes out slightly above the net speed because of gait sway.

Answer: 1.23 m/s. The routes span 1.20–1.25. Confidence: about ±4%.
