# q_2461 — length of the table (cm)

Lab video, 24 fps (file and question fps are the same), 1280x720, f = 0.5959*1280 = 763 px, principal point (640,360).

## Method
- Frame 48 (static). Table mask = largest non-black component (`corners.py`, `vp.py`).
- Table edges fitted in code (rms 0.3–0.8 px): front-left face bottom, front-right face bottom, back-left top
  edge, back-right top edge (`vp.py`). Vanishing points VP1 (171,353) and VP2 (1974,340). With f = 763 the two
  edge directions are 88.2° apart (90° would need f = 791), so the table is a horizontal rectangle and the
  benchmark focal length fits.
- Table-top plane normal = d1 x d2. Scale: plane through the left corner (413.5,468.5) at the given
  distance_table_left = 1.035 m -> camera 0.151 m above the table top (`plane.py`, `plane2.py`).
- Corners: L (413.5,468.5), F top (642,578) (bottom of face 612 minus slab thickness 2.3 cm), R top (1138,489.5)
  (from lines; the real right corner is faded by segmentation), B (773,438, hidden behind the ramp/books).
  The overlay `frames/overlay.png` matches the table outline.
- 3D edge lengths: FR 0.604, LB 0.6035 (parallel pair), FL 0.560, BR 0.574 (other pair); diagonal L–R 0.837 m.
  -> table ~60 x 57 cm; length (longer horizontal extent) = **60.4 cm**.

## Checks
- Other given depths on the same plane: ramp bottom-left corner on the table (610,468) -> 0.987–0.991 m
  (given slope_near 0.990). Book centre at t = 1.2 s (frame 29, about 1.5 cm above the top) -> 0.988 m
  (given 0.977). The scale agrees with three of the given values.
- The given distance_table_right = 0.573 m does not fit: the geometry puts the right corner at 0.97 m. On this
  plane, 0.573 m matches a point on the front-right edge near x ≈ 760, not the right end. Back-projecting
  the left and right ends with 1.035 / 0.573 m anyway gives 0.77–0.79 m, but that value conflicts with the
  rectangle geometry, the ramp depth and the book depth, so I did not use it. If the reference answer was
  instead computed from those two depths, it would be about 78 cm.
- Second route: the parallel edges give the same length (FR 0.604 vs LB 0.6035 m, two independent
  line fits).

Confidence: moderate–high for ~60 cm (true size); the main risk is how the reference treated the inconsistent right-end depth.
