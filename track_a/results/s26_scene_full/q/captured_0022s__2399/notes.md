# q_2399 – width of the table (cm)

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959*1280 = 762.8 px, principal point (640,360).
Table = tilted rectangular wooden top on one post; ball rolls down it from the far edge to the near edge.

## Method
1. `board.py`: median of frames 2/30/45 (removes ball), board mask (R-B>15), outer contour, line fits to the far,
   left and right edges (rms 0.4–1.0 px). `frontedge.py`: the near edge of the *top face* (bright top -> dark front
   face transition, column by column, leg excluded): y = -0.22498 x + 664.46 (rms 0.3 px).
   Top-face corners: FL (282.4,418.4), FR (599.7,362.7), NR (670.3,513.6), NL (225.4,613.7).
2. `recon.py` / `sens.py`: vanishing points of far/near edges (D1) and left/right edges (D2) -> board plane normal.
   Check: D1 vs D2 = 88.9 deg (rectangle reproduced with the paper focal length).
3. Metric scale from depth_info: ball centres (track x_ref,y_ref at frames 14, 19, 29) back-projected as
   depth * unit ray (depth = Euclidean distance) define the ball-centre plane offset; top face = 2 cm (ball radius)
   below it. Plane reproduces the given distances: 1.741/1.674/1.546 m vs given 1.751/1.687/1.526 m (<=2 cm).
4. Corners intersected with the top-face plane: left-right edges 71.1 cm, front-back edges 58.4 cm.
   Width = shorter horizontal extent = front-back = **58.4 cm** (length would be 71.1 cm).

## Checks
- Monte-Carlo with 1.5 px corner noise: front-back 58.4 ± 0.9 cm, left-right 71.2 ± 0.4 cm.
- Second route: plane from the ball's 3D path + D1 (no left/right edges) gives 63.8 x 70.4 cm, but that quad is not a
  rectangle (diagonals 94.3 vs 95.7 cm) and the three ball depths themselves are not collinear (6.9 deg kink, i.e. ~1–2 cm
  depth noise), so the vanishing-point plane, which reproduces a right angle and the given depths, is preferred.
- Focal sensitivity: f factor 0.55/0.65 -> width 59.2/57.6 cm.
Confidence: moderate-good (~±3 cm).
