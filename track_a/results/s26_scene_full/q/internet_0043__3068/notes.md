# q_3068: height of the white cylinder (cm)

Prior: the white ball's velocity at 1.0 s is 33.38 cm/s. The "white ball" is the rolling egg (the only moving object). The file and the question both use 30 fps, so 1.0 s = frame 30.

## Scale (annotator convention: one planar scale)
- Egg ref_x comes from scene/tracks/egg.csv (edge midpoints; I checked the per-frame values for consistency).
  - Forward difference x30→x31: 45.2 px/frame (raw); 44.8 px/frame (drift-corrected).
  - Backward difference: 45.9 px/frame. Central difference: 45.55 px/frame. Mean over frames 28-33: 45.2 px/frame.
  - Value used: 45.3 px/frame = 1359 px/s.
- Scale = 33.38 / 1359 = 0.02456 cm/px.

## Cylinder pixel height (cup_edges.py, measure_cup.py, frame 0)
- Measured from column brightness profiles at x = 1020-1080.
  - Top of the silhouette (back of the rim against the dark monitor): y ≈ 554.5.
  - Bottom (contact with the desk, start of the shadow): y ≈ 753-754.
- Height ≈ 199 px. This matches the record's bbox height (199) and is the same in frames 0, 10 and 60.
- Other reading: from the front of the rim (y ≈ 570) to the base gives ≈ 183 px, i.e. 4.5 cm. Not used, because the annotators measure the full extent.

## Answer
199 px × 0.02456 = **4.89 cm**.

## Check
The second route uses the backward or central speed (45.9 or 45.55 px/frame), giving 4.82-4.86 cm, within 1.5 %.

## Caveat
The prior implies the egg is about 1.9 cm across (79 px), which is small for a real egg. A real cup of about 10 cm would mean a scale about 2.8× larger. The task says the prior is exact, so I followed it. Confidence: moderate.
