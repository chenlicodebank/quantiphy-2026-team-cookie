# q_3113 — height of the brown table (m)

Prior: the rider's average speed is 3.8 m/s. This is an internet video, so I used a single planar scale from the prior. fps = question_fps = 30, so no re-timing was needed.

## Scale (speed.py)
- Track: scene/tracks/rider_scooter.csv, torso centroid, background-relative x_bg_px. The camera drift is only about 0.2 px/frame (about 0.7 %).
- Average pixel speed of the unflagged rows:
  - linear fit 143–260: 31.7 px/frame
  - endpoint 143–260: 31.4 px/frame
  - 150–250: 31.5–31.9 px/frame
  - raw (not background-corrected): 31.3 px/frame
  - all valid rows 138–264 (including flagged edges): 30.5 px/frame
- Adopted 31.2 px/frame = 936 px/s, giving a scale of 3.8 / 936 = 0.00406 m/px.

## Table (table.py, frame 0)
- The brown table is the front-centre wooden picnic table (x 1709–2406), the most prominent brown table.
- Top edge of the tabletop: median over 32 columns found by a wood-colour mask, y ≈ 1253 (the edge seen by eye is about 1250).
- Bottom of the front legs: y ≈ 1495–1496 in 4 leg columns.
- Height ≈ 242 px (±4), so 242 × 0.00406 = 0.98 m.

## Checks
- The same scale gives sensible sizes for the rider:
  - cap to sole: 420 px → 1.71 m
  - scooter length: 263 px → 1.07 m (a typical e-scooter is about 1.1 m)
- So the scale is plausible.
- The table is nearer the camera than the rider, so in reality it is about 0.75 m. Following the annotators' convention (one scale, no perspective correction), the answer is about 0.98 m.
- Other reading: the front-right brown table is about 250–265 px tall, which would give about 1.03 m.

Confidence: moderate. The scale is uncertain by about ±4 % depending on which speed window the annotators averaged.
