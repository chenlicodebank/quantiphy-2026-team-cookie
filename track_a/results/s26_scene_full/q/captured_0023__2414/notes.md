# Q2414 – width of the table (cm)

File fps = question fps = 24. Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Measurement (edges.py, edges2.py)
- I segmented the wood-coloured table by R−B and found its left and right edges per row (frames 0 and 48 agree).
  - Top-surface front edge (y 528-534): x 282-917/921, 635-639 px wide.
  - Front face band (y 536-560): x 278-925, 641-647 px wide.
  - Outer extent used: about 640 px, from x ≈ 280 to x ≈ 922.
- depth_info: table_left = 0.704 m, table_right = 0.725 m. Method card: size = depth x px / f.
  - Back-projecting the two ends: X_left = (280−640)/763 x 0.704 = −0.332, X_right = (922−640)/763 x 0.725 = 0.268,
    dZ = 0.021. This gives a left-right extent of **0.600 m**.
  - Simple form: 0.7145 x 640 / 763 = 0.599 m.

## Check by a second route (ramp, independent of the table depths)
- Ramp width: 145 px at the top edge x 1.201 / 763 = 0.228 m, and 183 px at the bottom edge x 0.9555 / 763 = 0.229 m.
  These agree, so the depth values behave as Z-depths and f = 763 is consistent.
- Table plane: the horizon is at y ≈ 338 (vanishing point of the side edges). The ramp foot is on the table at
  y ≈ 481 with Z = 0.9555, which gives camera height h ≈ 0.179 m. The front edge at y 531 then sits at Z ≈ 0.708.
  That matches the given table distances (0.704 / 0.725). Front edge = 640 x 0.708 / 763 = 0.594 m.
- The resting book also fits this geometry.
- If the table distances were Euclidean distances to the corners instead, the length would be about 0.55 m. That
  reading does not agree with the ramp geometry, so I rejected it.

## Ambiguity
- The given table points (left / right) define the left-right extent, which I measured as ≈ 60 cm.
- The front-to-back depth cannot be measured: the person's forearms hide the back edge.
  - The table is visible to at least Z ≈ 1.09 m, i.e. at least 0.38 m deep.
  - The ramp top at Z = 1.2 m, if it is supported on the table, implies a depth of at least about 0.49 m.
  - The table (wood top on a central pedestal) is plausibly square, about 60 x 60 cm.
- Answer: 60 cm. Confidence: moderate for the left-right extent (±3 %); lower if the reference means the
  front-to-back depth.
