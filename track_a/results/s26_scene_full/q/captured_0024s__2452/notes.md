# q_2452 — width of the table (cm)

Lab video, 1280x720, 24 fps (same as question_fps). Intrinsics from the card: f = 0.5959*1280 = 762.8 px, principal point (640,360).
Camera is static; I measured the table at frame 48 (plus frame 0 for the part of the back-left edge that the book hides later).

## Measurements (scripts in this folder)
- `table.py`, `fit_table.py`: table mask (non-blue pixels) → top boundary (back edges, top surface) and bottom boundary
  (lower apron edges). `front_edge.py`: top-surface front edges (light top → dark apron step); the front top corner is at about (643,576).
  `top0.py`: back-left edge from frame 0.
- `fit_table2.py`: 3D table model (rectangle or square of sides a,b, top thickness T, camera pitch and roll) fitted to all four
  edge sets with soft-L1. Scale is fixed by the left-corner depth of 1.035 m.
  * Square: side 58.6 cm, image rms 0.95 px. Predicted distances: left 1.035, front 0.496, right 0.933 m.
  * Rectangle: 55.1 (left-front edge) x 67.7 (front-right edge) cm, image rms 0.78 px. Predicted distances: left 1.035, front 0.539, right 1.06 m.
- The given "distance_table_right = 0.573 m" can't be the right corner: every model puts that corner at 0.93-1.06 m.
  On the table only the area near the front corner is about 0.57 m away, so I read "left/right" as the two ends of
  the left-front edge (left corner and front corner).
- `check_depths.py`, `combined_fit.py`: the other given depths, used as checks:
  * The slope's near-edge midpoint (658,479) lies on the table. The models predict 0.875 m (square) or 0.923 m (rectangle); the given value is 0.99 m.
  * The front corner: predicted 0.496 m (square) or 0.539 m (rectangle); given 0.573 m.
  * The ratios between depths don't depend on scale, and they fit the rectangle much better than the square.
  * The book at t=1.2 s (depth 0.977 m) comes out only 1.6-2.3 cm above the table top at L-scale (L-scale = scale set by the
    left-corner depth). It should be about 3.5-4.5 cm, so the true scale is about 5-12% larger than L-scale. The table_left
    click was probably slightly inside the corner, which would give a shorter distance.
  * Joint fits of edges plus depths (rectangle): with L+F, width 55.2 cm; with L+F+slope, 57.9 x 72.0 cm; with F+slope, 60.6 x 74.3 cm.
- `ramp_accel.py`: ramp plane from the given slope depths 0.99 and 1.243 m. It reproduces the book depths within 2%
  (1.093 and 0.997 m against the given 1.0685 and 0.977 m). The book's acceleration along it is 2.2-2.4 m/s², against the
  prior of 2.8, so if anything the acceleration also points to a larger scale.
- Direct two-point route (left and front corners back-projected with the given 1.035 and 0.573 m): 52.3 cm. This is
  lower because those two depths don't sit on one consistent plane with the rest.

## Answer
Width = the shorter horizontal side (the left-front edge). Estimates range from 55 to 61 cm: 55.1 at L-scale, 57.9-60.6
when the slope and front depths are included, and 58.6 if the table is square at L-scale. Answer: **59 cm**.
Other readings: if "width" meant the longer side, it would be about 72 cm; the straight left-to-right chord using the
given 0.573 m depth is 77.5 cm.
Confidence: moderate (±7%). The main uncertainties are the depth scale (the given depths disagree by 5-15%) and whether the top is square or rectangular.
