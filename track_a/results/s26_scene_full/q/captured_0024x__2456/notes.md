# q 2456 — length of the book (cm)

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959*1280 = 762.8 px, principal point (640,360).
Book = light-blue small book sliding down the white ramp (frames 19-31) and coming to rest on the table (36-48).
Its top face is a rectangle with a long edge running ACROSS the ramp and a short edge running DOWN the slope.

## Route 1 (main): book top face at t = 1.0 s (frame 24, depth 1.0685 m)
- Top-face corners measured in code (`measure2.py`, blue-tint mask b-r>6, polygon fit, overlay frames/poly2_24.png):
  (731,374), (809,382), (774,418), (689,407).
- Plane orientation: world "up" from the table's two vanishing points (`geom4.py`; the two table edge directions come out
  91.9 deg apart, which checks f); ramp across direction = horizontal and along the ramp's bottom edge line;
  incline 25.1 deg, from both the book's own depths (t=1.0 -> 1.2 s, 1.0685 / 0.977 m) and its image trajectory
  (the two agree).
- Corners back-projected onto the plane through the book centre (depth 1.0685 m), offset 0-1 cm for half the thickness (`geom6.py`):
  long (across) edge 15.9-17.0 cm, mask 1 px larger: 16.3-17.2 cm; short (slope) edge 9.9-11.4 cm.
## Route 2 (check): book lying on the table, frames 40-48
- Table plane = horizontal (same "up"), height from the slope_near depth (camera 0.169 m above the table). The book's bottom
  corners (500,481), (596,499), (646,489) (read on the median image) project to edges of 17.2 cm (long) and 8.1 cm (short) (`geom5.py`).
  This route is rough: the table_left check gives 1.115 vs 1.035 m.
- Crude method-card value: mask main axis 125 px at frame 24 * 1.0685 / 762.8 = 17.5 cm.

## Answer
The length (long edge) is about 17.0 cm. Confidence: moderate, about ±5%. The main uncertainties are the plane orientation (the camera is
almost level, so the lines near the horizon are poorly conditioned) and the cover rim and thickness offset.
