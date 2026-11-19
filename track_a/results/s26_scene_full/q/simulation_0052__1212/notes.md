# q1212 – height of the streetlight (m)

File fps 30.003297, question_fps 30.0 (frame indices used; times via question_fps). 3D render, 1080x1080,
principal point assumed at image centre (539.5, 539.5).

## Pixel height of the lamps (base.py, measure.py)
Two identical lamps (record: x 201 and 897). Vertical gray profiles at the pole column, left lamp on f0 and right
lamp on f90 (the car is not in front of them in those frames): top finial edge y≈365.3/365.8, bottom of base
y≈757.3/757.0, so **391.5 px** for both (record said 366→757, 391 px – confirmed). Below 757 is curb/road, not lamp.

## Focal length / scale (from the orange car, the prior's object)
- Orange car ref (wheelbase midpoint) from scene/tracks/orange_car.csv, hub-tracked frames. Quadratic fit
  f6-75: pixel accel 0.3346 px/frame² = 301.1 px/s² (f6-34: 297.6, f46-80: 303.8).
  Route A (prior): k = 2.86 / 301.1 = 0.009504 m/px at the car's depth.
- Route B (depth_info): motion is parallel to the image x-axis, so r0²−r1² = k²[(u0−cx)²−(u30−cx)²] with
  u0 = 1344.9 (fit extrapolation), u30 = 621.2 → k = 0.009639 m/px. Agrees with route A within 1.4 %.
- f from r1 = 15.436 = k·sqrt(f² + du² + dv²): f = 1579–1612 px (route/origin row 720 or 794); Z_car ≈ 15.2–15.3 m.
- Green (black) car check: its t=2 depth needs extrapolation far off-screen (u≈−984) and gives an inconsistent k;
  with f≈1595 its predicted r(t=2) is 13.3 vs given 12.77 (4 %), ground rows are consistent with a ~3° upward
  pitch. Not used for the scale.

## Height
Z_lamp = r_lamp·f / sqrt(f² + du² + dv²) ≈ 17.0–17.3 m (lamps ~1.8 m behind the car, consistent with sidewalk
by the wall); h = 391.5 px · Z/f. Over both lamps, both k routes, lamp origin at base or mid, car origin row
720/794: 4.13–4.30 m, median **4.21 m**. Left and right lamp differ ~1 % (small cx / depth inconsistency).

Second route: route A vs route B scale differ by 1.4 %, lamps L vs R by 1 %; all within ±2 % of 4.21.
Confidence: good (~±3 %).
