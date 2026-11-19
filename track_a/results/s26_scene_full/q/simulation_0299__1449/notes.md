# Q1449: speed of the forklift at 2.0 s (m/s)

The prior says the acceleration is 2 m/s^2. The question rate and the file rate are both 24 fps, so t = 2.0 s is frame 48.

## Method (fit.py)
- If an object moves along a straight line with constant acceleration from rest starting at frame n0, its image coordinate follows u(n) = (A + B s)/(1 + C s), with s = (n - n0)^2. I fitted this model to the scene track's bbox_x0, bbox_x1 and bbox_y0 over frames 0-71, and to the mask centroid over frames 15-71.
  - Every fit has rms 0.1-0.45 px, and the track has no departure from constant acceleration. Fitting only frames 0-50 or 0-30 gives the same result.
  - The fitted start is n0 ≈ 0 (between -0.1 and +0.2 frames for the x-edges and the centroid). The motion starts at frame 0 from rest.
- So the travelled distance is s(t) = 0.5·2·t^2 = t^2 m, with t = frame/24.
- Speed by the benchmark convention (one-frame backward difference at frame 48): (s(48) - s(47))·24 = (4 - (47/24)^2)·24 = **3.958 m/s**. The continuous value a·t = 4.0 m/s differs by 1%.

## Check against depth_info
- The fitted denominator 1 + C·s is proportional to depth along the line. For the centroid, C = 0.0089 per (n^2/100). This predicts a depth ratio z(48)/z(24) of 1.146.
- The given ratio is 19.098/16.795 = 1.137. The small difference comes from using the centroid rather than the origin.
- The given depths therefore agree with uniform acceleration from t = 0. Between 1 s and 2 s the forklift travels 3 m, of which 2.3 m is radial.

## Confidence
High. The only open choice is the speed convention: the backward difference gives 3.958 m/s and the continuous value gives 4.0 m/s.
