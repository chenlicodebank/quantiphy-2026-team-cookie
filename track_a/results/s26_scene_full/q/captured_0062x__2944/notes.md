# q_2944 – width of the white box (cm)

Object: the small printed white carton ("small_white_box" in scene/, static, centroid ~(517,495)), lying on the floor
with its long axis pointing away and to the right. Visible faces: top face, near end face (orange), right side face.
Width = shorter horizontal extent = edge between the top face and the near end face (across the top face).
File fps = question fps = 24; the box is static, so frames 30, 34, 40, 44 and 47 were averaged (boxseg.py).

Method (lab card: f = 0.5959 x 1280 = 763 px, principal point (640,360), depth to box centre 2.082 m at t=1.4 s):
- Floor normal from the vanishing points of the moving white board's quad in frames 20-35 (floor.py):
  n ≈ (0.08, -0.845, -0.53), so the camera looks down about 32 degrees. The corners in frames 36+ of the scene record are inconsistent, so I didn't use them.
- Box centre = mask-centroid ray x 2.082 m. Box height h comes from the near-right vertical edge (B(512.5,514.5) to
  C(512.5,527.5)), with the top plane at centre + h/2 and the floor at centre - h/2: h = 4.5 cm (solve.py).
- The corners were read from 10-16x zoomed grids (z1/z2.png) and back-projected onto the top plane:
  near top edge A(491.3,507.8)-B(512.5,514.5) gives 5.99 cm; far top edge (522.5,463.5)-(542.5,471) gives 6.34 cm;
  the bottom edge of the end face gives 6.6 cm (its corner is less clear). The naive estimate, pixel length x depth / f, gives 6.07 cm.
- Sensitivity: moving a corner by 1 px changes the width by about 0.23 cm (about 4%).
- Consistency check (check.py): the top-face length is 18.3-18.9 cm, the top-face corner angle is 92 degrees, and the reconstructed centre has
  depth 2.083 m and reprojects to (517.8,494.8), matching the given depth and the mask centre.

Answer: about 6.2 cm (mean of the near and far top-edge widths, 6.0 to 6.3). The box is about 18.5 x 6.2 x 4.5 cm.
Confidence: moderate (±5-8%), limited by the 20-px edge length and soft corners.
