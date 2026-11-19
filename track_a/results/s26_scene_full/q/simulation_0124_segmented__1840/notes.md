# q_1840 — width of the grey (silver) and red car

2D top-down simulation, 24 fps (file fps = question_fps = 24, no re-timing). Camera static, one m/px scale.

## Scale (prior: black car speed 26.085 m/s)
- measure.py: threshold the white-background frames (RGB min <= 235), connected components, dark car = mean brightness < 75.
- Dark-car centroid step on clean frames (4–45, excluding tree-occluded frames 30–36 and edge frames): mean 27.12 px/frame,
  median 27.16, sd 0.51 (33 steps). The scene record's template-fit steps give the same value (~27.2). Speed is constant.
- Scale = 26.085 / (27.14 x 24) = 0.04005 m/px.

## Silver car width
- Minimum-area rotated rectangle over clean frames 5–54: median width 51.6 px (scene record: 51.6). Maximum per-slice width
  across the car axis: 51.6 px. The body without mirrors is about 48 px (median slice width).
- The world AABB width includes the side mirrors, so I use 51.6 px -> 51.6 x 0.04005 = **2.07 m**.
  (Body only: 48 px -> 1.92 m.) Sanity check: length 126 px -> 5.05 m, which is plausible for a car.

## Check
- Second route for the scale: the template-fit ref-point steps in scene/tracks give about 27.2 px/frame, within 0.3 %.
- Confidence: about ±4 %. The main uncertainty is anti-aliased edge pixels (±1 px, which is 2 %).
