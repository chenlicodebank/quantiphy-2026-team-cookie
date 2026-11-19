# q_3132 — width of the no-parking sign (m)

Prior: average speed of the scooter rider = 2.91 m/s. Internet video, planar single-scale convention. 30 fps (file = question fps).

## Rider pixel speed (from scene/tracks/rider_scooter.csv, checked consistent)
- Raw-frame (annotator-style, un-stabilised) mean |dx|/frame x 30: front wheel edge 555.1 px/s, bbox centre 555.4, person centre 550.0.
- Stabilised (camera drift removed): 560 px/s. The camera drift is about 1%.
- Used 555 px/s, so scale = 2.91 / 555 = 0.005243 m/px.

## Sign width in pixels (sign.py)
- Horizontal brightness-gradient edges on clean rows (y 585-600, below the text) in frames 0, 15, 40, 55: 44-47 px.
  A zoomed crop at t = 0.5 s shows the plate spanning x ≈ 951 to 997, about 46.5 px. The record lists 48 px. Used 46.5 px.

## Answer
46.5 px x 0.005243 = **0.243 m**. Using the stabilised speed gives 0.242 m, and the range over 45-48 px is 0.236-0.252 m.
Sanity check: a standard sign is 0.30 m wide. The sign stands behind the rider's plane, farther from the camera, so the single planar scale reads it smaller. This is the annotators' convention.
Confidence: moderate. The plate's edge is uncertain by about ±1.5 px (±3%).
