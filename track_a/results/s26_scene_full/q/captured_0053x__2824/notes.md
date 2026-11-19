# q_2824: length of the book (cm)

The book is the static white package with green print at the bottom centre ("notebook" in scene/). It lies flat on the
floor at about 30 deg in the image. The file runs at 24 fps, the same as question_fps, and t=0.4 s is frame 10.
f = 0.5959*1280 = 763 px, principal point (640, 360).

## Checks on scale
- Prior check: the trashbin (the blue box) moves about 11.5 px/frame at frame 10 at 2.73 m, giving 11.5*2.73/763*24 ≈ 0.99 m/s,
  against the prior of 0.996 m/s. So f and the depths agree.
- Basketball: 63 px at 2.925 m gives 24.2 cm, which is a real basketball's size.

## Floor plane (plane.py)
I back-projected the book, cup and basketball centres with their depth_info. I put the centres at assumed heights above the
floor: book 1.5 cm, cup 7.2 cm, ball 12 cm. I also made the floor parallel to the box's 3D path; the box depth per frame is
scaled by sqrt(area). The fit residuals are about 1 mm. The camera is about 1.87 m above the floor and looks down about 46 deg.

## Book size
- Route 1 (box_fit.py, main): I fitted a 3D cuboid lying on the floor plane (centre, yaw, L, W, T) to the book's soft mask.
  The keyed-out green print was hole-filled. The fit renders the convex hull of the projected corners. On frames 0, 10, 24
  and 40 it gives L = 0.1832, 0.1836, 0.1840 and 0.1800 m. Frame 40 converged to a thicker T (3.0 cm); with T = 2 cm it gives
  0.184 m. Fitted values: W ≈ 0.115 m, T ≈ 0.022 m.
  The fitted centre depth is 2.051 m, against the given 2.082 m. Scaling by 2.082/2.051 = 1.015 gives **L ≈ 0.1865 m**.
  With T fixed between 1 and 3 cm, L ranges from 18.2 to 19.1 cm after scaling.
- Route 2 (book_edges.py, method card): I fitted lines to the silhouette edges. The long edge is 71.5 px including the grey
  side face, or about 68 px for the top face alone. 2.082*68/763 = 18.6 cm. Including the side face gives 19.5 cm, which is
  too high. Back-projecting the line-intersection corners onto the floor plane gives 18.8-19.1 cm, but those corners include
  the side face.

Answer: 18.6 cm. Confidence: moderate-good, about ±4%. Width ≈ 11.7 cm, thickness ≈ 2.2 cm.
