# q1227: height of the fire hydrant (m)

The video is a 3D Blender scene with a static camera, 2048x2048. The file runs at 29.9936 fps and question_fps is 30.
The hydrant is static, so the frame rate does not matter here. Inputs used: hydrant depth 4.721 m (camera to origin)
and the scene's depth_info. The prior (orange-car acceleration of -2.86 m/s^2) fixes motion along the line of sight,
which is nearly f-free, so it could not pin down the focal length (see below).

## Hydrant pixels (median of frames 0, 15, 30, 45, 60; scripts cap_edges.py, flange_bottom*.py, zoom.py)
- Dome top silhouette: y = 1377. The dome apex projects at about 1379: the dome sag was solved from the rim ellipse.
- Cap rim: x 724-867 (a = 71.5 px). Lower-edge front is at y 1418 and the ellipse centre at about 1408, so b is
  about 10-12 px (b/a about 0.15).
- Base flange: silhouette x 713-891 (a = 89). Top-surface front edge is at about 1779, b about 27 (b/a about 0.31).
  Bolt circle (6 bolts) gives b/a = 0.36.
- Ground contact: front at y 1815. The base-centre on the axis is 1815 - a x (b/a at f), which is about 1783.

## Focal length (the key unknown)
- Ellipses of horizontal circles give the view depression angle (ellipse_f.py, ellipse_f2.py: full pinhole model,
  horizon y = 1050 from the road vanishing point (923, 1050)):
  - cap rim: f ≈ 2300-2650
  - flange top: f ≈ 2290
  - bolt circle: f ≈ 1875
  - ground-contact outline: f ≈ 1500-1800. This one is biased because the contact shadow is off-centre.
  - Cap and flange read together (tilt-free difference): f ≈ 2100 with horizon about 1077.
- Cross-checks:
  - At f ≈ 2000-2100 the man (head-to-foot with his depth) is 1.78-1.85 m tall, and the camera height (from his
    feet) is above his head, as the image shows (his head is below the horizon).
  - At f ≈ 1000 the static objects would agree on a common ground plane (assuming base origins), but the man would
    then be 3.2 m tall. Also the flange and cap ellipses would have b/a 0.6 and 0.33, far from the measured 0.3 and 0.15.
    So I rejected f ≈ 1000.
  - The orange-car width and depth fit (car_f.py) gives f x W ≈ 2950-3150 px·m, with the widest part about 3 m in
    front of the origin. This does not discriminate f.
- Adopted: f = 2100 px (plausible range 1850-2300).

## Height (hyd_height.py)
I intersected the rays to the dome apex (1379) and to the base centre on the axis with the hydrant's vertical axis.
The axis is placed by back-projecting the origin (bbox centre, depth 4.721 m).

| f (px) | H, centre origin (m) | H, base origin (m) |
|---|---|---|
| 1900 | 0.948 | 0.919 |
| 2000 | 0.909 | 0.883 |
| 2100 | 0.872 | 0.850 |
| 2200 | 0.838 | 0.818 |
| 2300 | 0.807 | 0.789 |

Simple check: 4.721 x 405 px / |r| gives the same values to 0.3%.

Answer: 0.88 m. This is close to a real hydrant's height (0.75-0.9 m), which is consistent.

Confidence: moderate. The result scales as 1/f, and f is uncertain by about ±10% (the ellipse readings disagree), so
the answer is about ±10%. The scene/ record was used only as a starting point: hydrant bbox 707-936 x 1377-1811,
confirmed. The near-lamp base is not at y 1378 as recorded: the lamp continues behind the hydrant down to about y 1680.
