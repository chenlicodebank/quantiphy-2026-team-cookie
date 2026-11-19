# q_325: height of the power outlet (m). Prior: cup diameter = 0.087 m

Answer: **0.0607 m**

## What is in the scene
- The "power outlet" is the black wall plate (2 sockets + switch). It is flat on the back wall.
- The "cup" is the navy, slightly tapered cup lying on its side on the counter. The rim (wide end) is away from the
  camera and the base faces the camera. The cup points almost straight at the camera the whole time. Frames 16-23 are
  end-on: the silhouette top is the rim top and the widest horizontal chord is the rim diameter.
- The camera is static (from the scene record). fps 24 = question_fps; time does not matter for this question.

## Why one flat 2D scale is wrong here
The cup stands near the front of the counter and the plate is on the wall, so they are at different depths. A single
scale (cup 168 px tall, which also includes the foreshortened cup length) would give about 0.040 m. That is wrong.
I used ground-plane perspective instead:
- Horizon: two edges that recede from the camera, the cooktop's left and right side edges (`edges.py`, read off
  the intensity profiles). The outer and inner edge pairs cross at (945, 531.7) and (957, 531.9). That is near the
  image centre, so the camera looks horizontally and straight at the wall. I used y_h = 533.
- On the counter plane, pixels per metre at depth Z = (y_ground - y_h) / h_cam. So the scale ratio between two depths
  is the ratio of (y_ground - y_h) at those depths.

## Measurements (all in code)
- Plate (`precise.py`, frame 0, 50% edge crossings over 19 columns): top 711.3, bottom 788.3, **height 77.0 px**
  (width 201.9 px).
- Wall–counter junction (back edge of the counter): **y = 891.5** (constant over x 560-1120).
- Cup, end-on frames 16-23 (`cupsub.py`; mask from the difference against empty frame 0; 50% local-contrast crossings):
  - rim width (widest chord, rows 885-891 on the wall background) = **131.2 px** (f18 131.4, f19 130.9; 130.9-133.4
    over frames 16-23);
  - rim top = **827.7 px**.
  - The rim's lowest point touches the counter, so the rim's ground row = 827.7 + 131.2 = 958.9.
- Rim scale s_r = 131.2 / 0.087 = 1508 px/m.
- Wall scale s_w = s_r × (891.5 - 533) / (958.9 - 533) = 1508 × 0.8417 = 1269 px/m.
- **Outlet height = 77.0 / 1269 = 0.0607 m.**

## Checks
- Horizon: y_h from 520 to 540 gives 0.0603 to 0.0609 m. Rim width from 130.9 to 132.4 px over the end-on frames
  gives 0.0608 to 0.0603 m.
- The rim chord widths at rows 13 px above the rim centre (about 128.8-129.2 px) match a 131 px circle, which confirms
  the widest chord is the rim.
- The near-base ground row (about 1002) gives a base-to-rim depth ratio of 1.10. That is consistent with a cup lying
  along the depth direction.
- The cooktop ring ellipses (minor/major about 0.15 at y≈948, about 0.13-0.15 at y≈910) are consistent with a camera
  that looks horizontally (horizon near the image centre).
- Small ignored effects: the plate's thickness in front of the wall, and the rim tilting by the cup's taper (cos β,
  about 0.99). Each is under 1%.

## Confidence
Moderate to good, about ±5%. The main assumption is that the plate sits on the wall plane, at the counter's back edge.
The prior is taken as the rim (maximum) diameter.
