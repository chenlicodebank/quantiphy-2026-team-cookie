# q_2440 — width of the slope (cm)

The slope is the white board that leans from the table (lower left, near) up onto the book stack (upper right, far).
"Width" is the board's extent across the slope direction, i.e. along its top (far) and bottom (near) edges.
File fps = question fps = 24. The board is static, so frame 48 (2.0 s, notebook off the board) is used.

## Measurement (board.py, geom.py, geom2.py)
- Board mask: grey > 200, saturation < 40, in an ROI, largest component (overlay: frames/board_ov.png).
  I fitted lines to the four straight sides with the rounded corners excluded and intersected them to get the
  rectangle corners: TL (750.9, 359.8), TR (863.3, 361.6), BL (604.5, 469.5), BR (707.3, 491.4).
  Pixel lengths: top edge 112.4 px, bottom edge 105 px.
- Camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- Far-edge midpoint back-projected at 1.243 m, near-edge midpoint at 0.990 m. Slope vector length 0.374 m.
- The width direction d1 comes from the vanishing point of the top and bottom edges, (36, 348). It is strongly
  oblique in depth: the edge recedes to the left at about 45°. This is why the naive formula
  (depth × pixel length / f) underestimates: it gives 18.3 cm on the top edge and 13.6 cm on the bottom edge.
- I placed each edge on the 3D line through its depth-anchored midpoint along d1 and intersected it with the corner
  rays:
  - top edge (anchored at 1.243 m): **22.7 cm**
  - bottom edge (anchored at 0.990 m): **20.8 cm**
- Second route: I reconstructed the full plane, with d2 forced orthogonal to d1 along the left and right edge lines
  (the rectangle constraint; the raw side vanishing point is badly conditioned). With the plane anchored at either
  given depth, the widths are 20.8–22.7 cm and the board length is 33–35 cm. The plane model reproduces only about
  0.20 m of the given 0.253 m depth difference, so the depth points or edges carry a few % of inconsistency.
- Answer: the mean of the two anchored estimates, about 21.7 cm. Sanity check: the board looks like an A4-size
  board (21 × 29.7 cm), which is consistent.

Confidence: moderate. The likely range is 20.8–22.7 cm.
