# q_1981: length of the deer (m)

The "deer" is the large horned quadruped (called "ibex" in scene/). It is a 2D scene: the animal walks left to right in a
plane facing a static camera.

## Method (measure.py, output in my_track.csv)
- Mask: min(RGB) < 247, 3x3 opening, largest component plus non-rabbit fragments. I re-measured every frame (0-74).
- Speed in pixels: linear fits of x(t) give the same slope for the centroid (6.520 px/frame), the trunk centre
  (6.531) and the snout edge x1 (6.523). Net centroid shift / 74 frames = 6.535. The motion is uniform, so the
  constant prior speed applies. I took 6.52 px/frame x 30 fps = 195.6 px/s.
- Scale: 1.277 / 195.6 = 0.006529 m/px.
- Length: horizontal bbox extent, from the tail tip to the snout (the horns curve back and stay inside that range).
  Median 489 px, mean 489.8, range 471-510 (changes with tail and leg pose).
- Length = 489 x 0.006529 = 3.19 m.

## Checks
- Second route for the speed: using the snout edge (x1) slope instead of the centroid changes the answer by under 0.1%.
- Spread from pose: the bbox range 471-510 px gives 3.08-3.33 m.
- Other reading: torso-only length (~273 px) would give 1.78 m. That is not what the AABB convention measures, so I
  did not use it.
- fps 30 = question_fps, so no re-timing.

Confidence: moderate-high. The main uncertainty is which frame/pose the reference AABB used (about ±4%).
