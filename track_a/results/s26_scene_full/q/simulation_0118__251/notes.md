# q_251 — width of the table (m)

2D scene: static top-down, nearly orthographic camera; the toy car moves in a straight line across the table top.

Scale from the prior (car speed 0.05 m/s):
- Car centroid x against frame (scene/tracks/toy_car.csv, cx_mask) fits a line with slope 2.609 px/frame and 0.51 px residual. The rear edge gives 2.615 px/frame. My own rougher saturation mask (measure.py) gives 2.67 px/frame, but its residual is 5.8 px, so it is noisier and I used the record's value.
- fps: the file's 24.003 and question_fps 24.0 differ by only 0.01%, so the choice doesn't matter. Speed = 2.61 × 24.0 = 62.65 px/s.
- Scale: 0.05 / 62.65 = 7.98e-4 m/px.

Table (measure.py: saturation mask → contour → approxPolyDP on frame 60):
- Corners: (158,144), (94,807), (953,907), (1019,246).
- Sides: 864.8 and 867.0 px for the long pair, 666.1 and 664.3 px for the short pair. This agrees with the scene record (867 × 665). Opposite sides agree to within 0.3%, so perspective is negligible.
- Width is the shorter horizontal extent: 665 px × 7.98e-4 = **0.531 m**. The other reading, length, is 866 px, which gives 0.691 m.

Second-route check: minAreaRect of the same contour gives 668.9 × 879.1 px. These are slightly larger because of the rounded or shadowed edges, and give a width of 0.534 m. That agrees with the corner-based value to within 1%.

Confidence: high. The main uncertainty is the pixel speed (about 1%) plus the height difference between the car origin and the table plane, which is negligible for an overhead view.
