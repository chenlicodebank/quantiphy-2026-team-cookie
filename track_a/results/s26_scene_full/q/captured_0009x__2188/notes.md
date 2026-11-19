# q_2188 – maximum rebound height of the basketball (cm)

File fps 24 = question_fps 24. Pinhole f = 0.5959*1280 = 762.8 px, principal point (640,360).
Track: scene/tracks/basketball.csv (checked on frames 37, 38 and a contact sheet; bbox_w is the reliable diameter near the bounce).
Bounce between f37 and f38 (f37 still falling at ~59 px/frame; rebound ~38 px/frame); contact ≈ f37.15, centre px ≈ (546, 666).
Apex f46 (t=1.917 s = the stated 1.92 s), centre px (528, 481.5), depth 1.5795 m (given).

## Geometry
- Depths along the rebound from apparent size: R = k / bbox_w, k calibrated from given depths
  (f0: 181, f43: 171, f46: 175).
- Gravity direction in camera coordinates from a 3D parabola fit to frames 38-48 (or 39-48): camera pitched down 16-19°.
  (Fitted |a| ≈ 6.5 m/s², not 9.8: the clip's timing appears slowed by about 1.25x (30 fps recorded as 24 fps?). This does not matter for a height.)
- Ball radius ≈ k/f/2 ≈ 0.115 m.

## Route 1 (floor from the bounce: centre at contact minus radius)
Centre rise from bounce to apex = 0.44-0.53 m. Apex centre height above floor = 0.57-0.65 m. With k = 181 (the t=0 calibration), the predicted
floor contact point is 2.02 m from the camera, which matches the given floor distance of 2.0285 m. That route gives 0.64-0.65 m.

## Route 2 (given floor distance)
Floor contact point at pixel ≈ (552, 707) and distance 2.0285 m, compared with the apex centre (1.5795 m):
vertical separation 0.648-0.651 m, Euclidean 0.657-0.660 m.

## Answer
Height of the ball centre above the floor at the apex ≈ 0.65 m, so the answer is **65 cm**.
Other reading: the gap between the ball's bottom and the floor, which equals the rise of the centre from the bounce, is ≈ 0.53 m (65 cm minus the 11.5-12 cm radius).
Confidence: moderate. The geometry is consistent to ±2 cm; the main risk is which definition the reference used.
