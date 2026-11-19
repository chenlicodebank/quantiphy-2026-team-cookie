# q_1980: height of the deer (m)

The "deer" is the large horned quadruped (the "ibex" in scene/). It is the only large animal; the other is a small rabbit.
This is a 2D clip with a static camera, the animal fully in view, and 30 fps (the file rate and question_fps are the same).

## Scale (from the prior: speed of the deer = 1.277 m/s)
- I re-measured the mask centroid x on every frame in measure.py (min(RGB)<247, 3x3 opening, largest component).
- Linear fit: 6.520 px/frame. The net shift over 74 frames is 6.535 px/frame, and the mean per-frame step of the
  5-frame-smoothed centroid is 6.532 px/frame. trunk_cx, bbox centre, x0 and x1 in scene/ all fit 6.51-6.52.
- Speed = 6.52 x 30 = 195.6 px/s, so the scale is 1.277 / 195.6 = 0.006529 m/px.

## Height
- Mask vertical extent (horn tip to hooves): median 421 px over all frames (range 415-426). Top is at y≈1131,
  ground at y≈1551.
- Height = 421 x 0.006529 = **2.75 m**.

## Checks
- If I use the mean per-frame step (6.535) instead of the fit, the height is 2.74 m.
- Plausibility with the same scale: shoulder height ≈ 261 px = 1.70 m and length ≈ 489 px = 3.2 m. That is a large,
  elk or moose-sized fantasy animal; its tall swept-back horns make up the extra height. The rabbit comes out about
  0.47 m long and 0.41 m tall with ears, which is plausible for a hare, so the scale holds up.
- Without the horns, the head/body top is at y≈1210 (≈340 px → 2.2 m). The answer uses the full bounding-box height,
  following the world-space AABB convention.

Confidence: moderate-high for the scale. The main uncertainty is whether the reference counts the horns (it should,
under the AABB convention).
