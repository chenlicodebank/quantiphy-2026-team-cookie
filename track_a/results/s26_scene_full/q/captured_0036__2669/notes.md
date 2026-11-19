# q_2669 - width of the table (m)

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959*1280 = 762.8 px, principal point (640,360).
Table: rectangular wooden top, long axis pointing away from the camera. Width = shorter horizontal extent =
the left-right extent (front edge); the front-to-back extent is ~0.73-0.83 m (longer, poorly measured because the
back edge is blurred/grazing), so the answer is the left-right dimension.

## Scale
depth_info: t=0.9 s -> frame 22, ball centre (569,457), D=1.010 m; t=1.4 s -> frame 34, (838,513), D=0.716 m.
Prior check: diam_v 31 px * 1.01/f = 4.10 cm, 45 px * 0.716/f = 4.22 cm (prior 4 cm; consistent, ~+3% blur).
Ball 3D centres: X22 = (-0.093, 0.127, 0.998), X34 = (0.177, 0.137, 0.680) m.

## Route 1 - table-row width at the ball's contact row (rowwidth.py, sides.py)
Side edges of the top fitted per row on frame 48 (no ball) from the V-channel 50% crossing:
left x = -1.5863 y + 1112.6 (resid 0.67 px), right x = 1.6443 y + 27.2 (resid 0.46 px); vanishing point (579.6,336.0).
A horizontal image row on the table plane is a 3D line parallel to the front edge at the depth of the ball contact
point, so width = row pixel width * Z_ball / f:
- frame 22: contact row 472.3, 440.3 px * 0.998 / f = 0.576 m (S-channel edges: 0.579)
- frame 34: contact row 535.4, 644.2 px * 0.680 / f = 0.575 m (S-channel: 0.577)

## Route 2 - front edge back-projected onto the table plane (width.py)
Front face x extent measured by gradient at rows 594-621: x 186 -> 1001 = 815 px (frames 0, 24, 48 identical).
Table plane: contains the front-edge direction and the side vanishing direction (or the ball path direction),
passing 2 cm below the ball centres. Front-edge depth Z ~0.528-0.535 -> width 0.564-0.572 m depending on the
plane estimate (tilt 1.4-1.8 deg; the best-measured vanishing point (577-580,336) gives 0.572).

## Answer
Routes agree within ~1-2%: 0.575 m (route 1 x2: 0.576/0.575, route 2: 0.572). Back edge 3D length 0.59-0.60 is less
reliable (blurred by chair behind it, grazing view). Confidence: +-3%.
Record correction: scene.json right side edge (x = 1.782 y - 40.5) and FR corner were imprecise; refined lines above.
