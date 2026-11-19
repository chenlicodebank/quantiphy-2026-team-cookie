# q_2544 — width of the table (cm)

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959*1280 = 762.8 px, (cx, cy) = (640, 360).
Prior: tennis ball diameter 6.7 cm. depth_info at t = 1.5 s (frame 36): tennis 1.183 m, ping-pong 1.353 m.

## Table top corners (edges.py, frame 0, static camera)
Table mask = (R-B > 5) | gray < 120, restricted to y 395-540. Robust line fits: back edge (top boundary), side edges
(left/right-most pixel per row), front top edge (strongest bright-to-dark vertical step = top surface/front slab).
Corners: BL (573.8, 425.2), BR (850.6, 427.6), FL (462.8, 482.5), FR (959.7, 495.0) (overlay frames/edges_f0.png).
Front edge 497 px, back edge 277 px. Side-edge vanishing point (722.6, 348.4) -> horizon ~349 px. The pixel ratio
front/back = 1.79 gives the same horizon (348.9), so the plane geometry is consistent.

## Balls at frame 36 (balls.py, profile.py)
Tennis: centre (583.0, 433.5), circle-fit diameter 43.1 px (expected from the given depth: 43.5). Ping-pong: centre ≈ (722, 433)
from the SAM halo bounds (x 710-733, y 424-443); ~23 px, which matches 4 cm at 1.35 m. (The record's white-ball diam 29 px at f36
includes the halo and blur: too large.)
3D centres = depth x unit ray: tennis (-0.088, 0.113, 1.174), ping-pong (0.144, 0.127, 1.339).

## Geometry (geom.py)
Table plane normal from the vanishing line (both vanishing points); camera height above the top h = n.P_ball + r_ball.
Corners back-projected onto the plane.
- Route A, h from tennis (0.162 m): left-right 0.577 m, front-to-back 0.705 m.
- Route A, h from ping-pong (0.168 m): left-right 0.598 m, front-to-back 0.730 m.
- Route B (normal ⟂ side-edge direction, tilted so both balls fit): back 0.599, front 0.591; sides 0.70-0.77.
Second route (ball apparent size as a depth gauge at the back edge, where both balls sit at rest in frames 0-21):
tennis 32.5 px -> Z ≈ 1.56-1.57 m -> back edge 277 px -> 0.567 m; ping-pong 18 px -> Z ≈ 1.70 m -> 0.617 m. Mean 0.592 m.
The depth/length ratio, ~1.23, does not depend on h, so the front-to-back extent is the longer side (~0.70-0.73 m).

## Answer
Width = shorter horizontal extent = left-right extent ≈ 0.59 m -> **59 cm** (spread of routes 57-62 cm).
Other reading: the front-to-back depth ≈ 71-73 cm. Under the stated convention (a table's width is its shorter side),
the left-right value is used.
Confidence: moderate (±3-4 %). The main uncertainty is the tennis vs ping-pong height inconsistency (~4 %).
