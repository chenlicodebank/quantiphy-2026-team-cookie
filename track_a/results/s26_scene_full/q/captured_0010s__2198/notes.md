# q_2198 — ball diameter (cm)

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959*1280 = 762.8 px.
Prior (g = 9.8) is not needed for a size; scale comes from depth_info.
depth_info frames: t=0.3→f7 (1.706 m), 0.6→f14 (1.344), 0.9→f22 (1.4605), 1.2→f29 (1.784), 1.5→f36 (1.717), 1.8→f43 (1.350).

Method: D = d * pixel_diameter / f.

Route 1 (measure2.py): redness map R−G, sub-pixel half-max width of the ball through its centre,
perpendicular to the motion direction (motion blur elongates along motion), plus horizontal width.

| frame | blur px/f | perp px | x px | D_perp cm | D_x cm |
|---|---|---|---|---|---|
| 7  | 14.0 | 26.9 | 27.2 | 6.02 | 6.08 |
| 14 | 4.2  | 37.2 | 36.0 | 6.55 | 6.34 |
| 22 | 3.6  | 33.8 | 33.3 | 6.47 | 6.38 |
| 29 | 11.8 | 25.8 | 27.2 | 6.03 | 6.36 |
| 36 | 20.3 | 27.5 | 28.0 | 6.19 | 6.30 |
| 43 | 3.1  | 36.1 | 35.3 | 6.39 | 6.25 |

Fast frames (7, 29, 36) are biased low by a few % (half-max width of a motion-blurred disc shrinks
perpendicular to the blur by ~3–7 % for these blur lengths). Low-blur frames 14/22/43 average ≈ 6.40 cm.

Route 2 (measure.py): HSV mask, equivalent-area diameter (6.43–6.69 cm on low-blur frames, inflated by blur
on fast frames) and ellipse minor axis (5.9–6.3 cm, eroded edges). These bracket route 1.
Overlays frames/ov_XX.png checked: mask covers the ball; f7 visibly blurred vertically.

Answer: 6.4 cm. Confidence moderate (±4 %); spread mostly from depth_info vs apparent-size inconsistency between times.
