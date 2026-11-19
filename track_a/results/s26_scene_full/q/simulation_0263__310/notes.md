# Q310 – length of the spacecraft (m)

Prior: acceleration = 4 m/s^2. 2D top-down render, static camera, 24 fps (file fps = question fps).
The "spacecraft" is the single dark vehicle (scene/ calls it a car) moving left along y ≈ 718 from rest.

## Scale (fit.py)
Quadratic fit of the template-tracked position `ref_x` (scene/tracks/car.csv, sub-pixel, rms residual 0.04-0.14 px)
vs time: acceleration = 517.0-518.0 px/s^2 for windows f2-71, f5-60, f10-40, f30-71, f2-35 (cubic term negligible).
Per-frame second difference: mean 517.5, median 515.5 px/s^2. Use 517.5 px/s^2
-> scale = 4 / 517.5 = 0.007729 m/px.

## Length in px (length2.py)
Mask = frame / background < 0.45 (body ratio 0.30-0.37; cast shadow ratio ~0.50, lies upper-left and ~15-20 px ahead
of the nose, so it is excluded; thresholds 0.55-0.75 include the shadow and give ~788 at f40).
Body extent along x: f0 789, f20 783, f30 777, f40 768, f50 759, f58 746 px — linear in position (mild perspective:
rear fins higher than nose). At the image centre (f40, centre x ≈ 1282 = image centre) the length is 768 px, where
perspective effects of the fins/nose heights cancel to first order.

## Answer
L = 768 px × 0.007729 m/px = 5.94 m.

Check: scene/ record's independent body mask gives 767 px at f40 (-> 5.93 m); the acceleration from several
independent frame windows agrees within 0.2 %. Using the frame-0..60 median length 776 px would give 6.00 m
(+1 %). Confidence: good, ~±2 %.
