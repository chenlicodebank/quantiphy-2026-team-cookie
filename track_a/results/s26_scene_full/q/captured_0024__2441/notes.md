# q_2441 – "What is the length of the table in cm?"  (captured_0024, lab, 24 fps = question_fps)

Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Table is static, so I used frame 48 (and checked frame 0).
depth_info: table_left = 1.035 m, table_right = 0.573 m.

## Which table points the depths belong to
The table is a rectangular top on a single central pedestal, seen almost edge-on: the camera is about 16 cm above the
top and nearly level. Top-surface corners, from sub-pixel edge fits (edges.py, backedge.py):
- left corner L ≈ (414, 468)
- front corner F = intersection of the left-front edge (y = 0.4722x + 271.7) and the front-right edge
  (y = −0.1703x + 684.4), at (642.3, 575.0)
- right corner R ≈ (1130–1145, 492), partly blurred or occluded by the person's arm

Thickness check (thick.py, thickfit.py): the top's side face is about 20.0 px thick at L and 37.4 px at F. For a
level camera, pixel thickness is proportional to 1/z. The z ratio from thickness is 1.87; from the given depths
(L = 1.035, F = 0.573) it is 1.78. That gives a consistent top thickness of 2.6 cm. R's thickness (about 20–22 px) puts
it about 1.15 m away, so 0.573 cannot be the far right corner.
=> "table_left" = left corner L and "table_right" = front corner F. Both lie on the table's left edge.

## Measurements
- P_L = 1.035 · ray(414, 468.5) = (−0.291, 0.140, 0.983) m
- P_F = 0.573 · ray(642.3, 575.0) = (−0.002, 0.154, 0.552) m
- **|L − F| = 0.522 m.** Sensitivity: ±1 cm in either depth gives ±1 cm; ±3 px at the corners gives <0.2 cm.

Long front edge F→R (the other horizontal side). Back-projecting it is poorly conditioned because the camera is at
nearly table height:
- Route 1, right angle at F (perp.py): R lies in the plane through F perpendicular to L−F. Gives 0.74–0.80 m for
  uR 1125–1145; 0.78 m at uR = 1138.
- Route 2, pedestal under the table centre (pedestal.py): the pedestal column is at x ≈ 771 (745–797). Requiring the
  midpoint of L and R to project there gives 0.73–0.79 m. The implied corner angle at F is 89–92°, which
  independently confirms the rectangle. The predicted face thickness at R, about 20.5 px, matches the measured ~20–22 px.
- Route 3, face-thickness extrapolation: 0.8–1.0 m. The face's lower edge is noisy because the edge banding is layered.
- Route 4, vanishing points: 0.6 m. It is very sensitive to the short back-edge segment, and it contradicts the given
  F depth (it gives 0.51 instead of 0.573), so I rejected it.
=> long side ≈ 0.76 ± 0.03 m; short side (L–F) = 0.52 m.

## Answer and reading
- Reading A, the edge between the question's own two depth points (table_left → table_right): **52.2 cm**.
- Reading B, the longer horizontal side (front edge F–R): ≈ 76 cm (uncertain ±3 cm).

The depth_info written for this question gives exactly the two ends of the L–F edge, named left and right. That is
what the question's scale and endpoints define, and no depth is given on the long edge. So I answer 52.2 cm, from
the given depths and back-projection of the corner pixels. If the reference instead uses the long side, the value is
about 76 cm.

Confidence: the L–F measurement is solid (±2 cm). Which edge the reference calls "length" is the main uncertainty.

Scripts: edges.py, backedge.py, overlay.py, geom.py, vp.py, perp.py, plane3.py, thick.py, thick2.py, thickfit.py,
pedestal.py, zoom.py, rightzoom*.py. The scene/ record's table corners (left 413,467; front 640,610 – that is the
bottom of the face, the top-surface corner is at 642,575; right ~1140,505) are roughly right.
