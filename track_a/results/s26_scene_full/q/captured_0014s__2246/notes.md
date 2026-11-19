# q_2246 — height of the cup (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959 x 1280 = 763 px, principal point (640,360).
Scale from depth_info: cup centre at 1.7270 m (t=0). The cup is static, so I used a per-pixel median of frames
0,10,20,30,40,48 (scripts: cupmask.py, cupzoom.py, edges.py, pitch.py, height.py).

## Pixel measurements (white tumbler, back-left of the table; the cookie hides its lower-right part)
- Rim (outer ellipse): top 335.5, front 353.5, left 450.5, right 489 -> centre (470, 344.5), 38.5 x 18 px,
  minor/major 0.47.
- Base: the left silhouette is a straight line (x = 455 at y=360 to 465 at y=396). It turns into the base ellipse at
  y ~ 399, and the lowest visible cup pixel is (471, 402.5); the rest is hidden by the cookie. Fitting an ellipse arc
  (semi-axis 10–16 px, b/a = 0.51 from the camera geometry) through these points puts the base-ellipse centre at
  y = 397.5–398.5.
- Axis length in the image is about 53.5 px (rim centre to base centre). The scene record's bbox (336–400, 64 px)
  runs from the back of the rim to the front of the base, so it overstates the axis.

## Geometry (the camera looks down at the table, so the vertical axis is foreshortened)
- The table-top vanishing points give the table normal in camera coordinates as (0.114, -0.887, -0.448). The ray to
  the cup is 26–30° above the table plane (cos ≈ 0.89). As a check, sin 26.4° = 0.444 at the rim, against the
  measured rim ellipse ratio of 0.44–0.47.
- Route 1 (height.py): a 3D vertical segment along the table normal, with its midpoint 1.727 m from the camera, made
  to project onto base (476, 398) and top row 344.5. Result h = 13.45 cm (13.2–13.7 over base 397–399 and top
  344–345).
- Route 2 (rim-ellipse foreshortening): h = d·L/(f·cosθ) = 1.727 x 53.5 / 763 / 0.90 = 13.45 cm.
- Plain method card without the foreshortening correction: d·L/f = 12.1 cm. That is a lower bound, since a
  ruler-measured true height is wanted.
- Rim diameter check: 1.727 x 38.5/763 = 8.7 cm, which is plausible for a tumbler.

Answer: 13.5 cm. Confidence moderate: about ±5%, set mainly by the occluded base position (±1 px = ±0.25 cm).
The prior (ball acceleration) is not needed.
