# q1419 – height of the trolley (shopping cart), simulation_0180

Question fps = file fps = 24. Prior: trolley acceleration 1.507 m/s^2. Depth: 12.589 m at t=0 (frame 0), 12.513 m at t=0.5 (frame 12).
Height = vertical extent of the world AABB = top of the handle bar to the bottom of the wheels (floor).

## 1. Focal length (fit_f.py)
Constant acceleration from rest along a straight 3D line, P(t) = P0 + d * 0.5*1.507*t^2, projected with a pinhole (principal
point 960,540), fitted to the scene/ track (bbox centre, 60 frames) with |P(0)| = 12.589 and |P(12)| = 12.513 as constraints.
f = 2694 px (rms 0.5 px). Variants: free start time 2705, wheel-bottom track 2675-2684, first 45 frames only 2683-2697, so f ≈ 2690 ± 15.
Both given depths are reproduced (12.590 / 12.512). Fitted direction d = (0.976, 0.028, -0.215), so the cart moves right and slightly toward the camera.

## 2. Camera up direction (lines2.py)
Vanishing direction of near-vertical lines (door frame, vent edges) gives up = (0.018, -0.988, -0.156), i.e. pitch ≈ 9° down and roll ≈ 1°
(an earlier set of lines gave pitch 7.8°; H changes by < 0.5 % between the two).

## 3. Height (height.py, run_h.py, profile.py)
Cart mask = |frame - frame without the cart| > 30. From the column profiles of the mask I read:
- the wheel-bottom contact points (near/far, rear/front);
- the top of the handle bar's near end and far end. Their midpoint is taken to lie in the cart's central vertical plane.

Reconstruction: the floor plane comes from the up vector. The wheel contacts are back-projected onto the floor, giving the cart axis (through the rear and front
wheel-pair midpoints) and the vertical plane through it. The handle-midpoint ray is intersected with that plane, and its height above the floor
gives H. The metric scale comes from the fitted origin range at that frame (origin = AABB centre ≈ footprint centre at H/2, which projects
onto the bbox-centre row as expected; an origin at floor level would give about 1.3 % less).

| frame | H (origin mid-height) | H (origin at floor) |
|---|---|---|
| 12 | 1.172 / 1.168 | 1.157 / 1.154 |
| 30 | 1.174 / 1.169 | 1.158 / 1.155 |
| 59 | 1.147 / 1.143 (wheel readings poor: overlapping front wheels, track widths inconsistent) | 1.130 |

By-products (sanity): wheelbase ≈ 0.75 m, rear track ≈ 0.44 m, front track ≈ 0.31 m, handle ≈ 0.22 m behind the rear axle,
camera ≈ 3.7 m above the floor.

## Second-route check
Frames 12 and 30 were read independently (different background, different position in the image) and agree within 0.3 %.
Frame 59 is 2 % lower, which is consistent with its poorer wheel readings. The result is insensitive to f (±15 px → ±0.5 %) and to the up vector (±0.4 %).

## Answer
H ≈ 1.165 m (frames 12 and 30, origin at mid-height). Confidence: about ±4 %. The main uncertainties are reading the handle-top pixels (±2 px ≈ ±1 %)
and the origin convention (≈1.3 %).

Record check: scene/ tracks cover the right object for all frames. The bbox height (283 px at frame 0) includes the depth offset across the cart's width,
so it is not a direct height measure.
