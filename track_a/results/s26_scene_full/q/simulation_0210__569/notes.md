# q569 – height of the floor mirror (prior: cat speed 0.94 m/s)

fps 24 (file and question agree). Static camera; the cat walks left to right on the floor in front of the wall, and the mirror leans on the wall behind the table.

## Cat speed in pixels (speed.py, scene/tracks/cat.csv)
- The mask-centroid x is linear over the clip: a linear fit gives 427.7 px/s, the net displacement gives 429.7 px/s, and windows of 18–36 frames (gait-period multiples) give 427.8 ± 1.5 px/s. Bbox, torso and nose tracks give 426–433 px/s. There is no vertical drift.
- Taken as 428 px/s, so the scale at the cat's depth is s_cat = 0.94/428 = 0.002196 m/px.

## Mirror in pixels (edges.py, gradient edges on frame 0)
- The top of the outer frame is at y = 398 (x 1650–1870). The bottom of the frame on the floor is at y ≈ 977–978.
  The wall/floor seam is at y = 953.
- Pixel height is 580 px.

## Perspective (the furniture is not in the cat's plane)
The floor is visible from y = 953 to the bottom of the image, so the camera is above the floor and the wall/mirror is
farther away than the cat.
- The cat's ground line is about y = 1024: near paws at ~1030 and far paws at ~1018.
- Horizon y_h ≈ 590 ± 30. The bottom rim of the lamp shade is almost a straight line (a ~2 px downward bulge at
  y ≈ 618), so the eye is just above it. The vase mouths are seen nearly edge-on, and the table top is seen from above.
- Pinhole camera with a horizontal view: a floor point at depth Z appears at y = y_h + f·h/Z.
- The mirror top touches the wall (depth Z_wall), so its height H = 555 px (953 − 398) × h/(953 − y_h).
  The cat's scale is h/(1024 − y_h).
- H = 555 × s_cat × (1024 − y_h)/(953 − y_h) = 555 × 0.002196 × 1.196 = **1.46 m**.
- Sensitivity: y_h 560 → 1.44 m, y_h 620 → 1.48 m. A cat ground line of 1018–1030 changes it by ±1.5 %.

## Check / alternative
- A single planar scale with no depth correction gives 580 × 0.002196 = 1.27 m. I rejected this because the floor
  perspective clearly puts the mirror about 20 % farther from the camera than the cat.
- Sanity check with the same model: the table is ≈0.42 m tall and a floor mirror is typically ~1.5 m tall, so both
  are plausible.

Confidence: moderate. The main uncertainty is the horizon estimate and whether the reference expects the depth
correction (about ±3 % within the model).
