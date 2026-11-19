# Q1246: width of the lane (main road, curb to curb)

The video file and question_fps are both 24 fps. t=0.58 s is frame 14 and t=1.58 s is frame 38.
The "white car" is the white cargo van in the scene record. It accelerates along the cross street.

## Method
- `curbs.py` and `width.py`: I found the road/curb boundary of the main road in `scene/bg_full.png` using a warm-colour test
  (R-B > 10) and fitted lines with RANSAC. Left edge: x = -3.752 y + 3907.6. Right edge: x = 2.574 y - 555.6.
  The overlay is in `frames/curbs.png` and follows both curb edges.
  The two lines meet at the vanishing point (1260, 705.4), which I use as the horizon row.
- Camera model (`solve.py`): pinhole camera with the principal point at the image centre and no roll. The pitch comes from the horizon row.
  Unknowns are the focal length f and the camera height h. The van's ground track is the ray through (patch_cx, tyre row 799)
  intersected with the ground. Its scalar per-frame speed must rise at 4 m/s² (the prior), and its distances at f14 and f38
  must match depth_info (43.81 and 43.00 m). Result: f ≈ 2297 px, h ≈ 1.74 m (with horizon 705.4).
  The two distances alone give f ≈ 1655, but that route is ill-conditioned: it would make the van 7.9 m long, so I rejected it.
- Road width (`width2.py`): I back-projected both curb lines onto the ground and took the distance perpendicular to the road
  direction. With horizon 705.4 the result is **11.02 m** at every row from 830 to 1040, so the two lines are parallel on the ground.
  With the scene record's horizon of 702 the width is 11.1–11.3 m.

## Checks
- Van length: about 300 px at 43.4 m gives 5.67 m, which fits a full-size cargo van.
- Second route: the parked maroon sedan (seen from the rear, 142 px wide, ground row 849) comes out 1.74 m wide, a realistic car width.
  Using a 1.75–1.8 m car width directly as the scale gives a road width of about 11.1–11.4 m.
- The pedestrian's given distance (31 m) does not match the feet row: the ground-plane depth is about 36–37 m.
  The character's origin is probably not at its body, so I did not use it. From the ground-plane depth the pedestrian is about 1.7 m tall, which is plausible.
  The taxi's distances are also only roughly consistent with its tyre row, because it is turning.

## Answer
11.0 m. Confidence is fairly high (about ±4%). The answer depends mainly on the f set by the acceleration prior and on the horizon row.
