# q_718: length of the teacher's table (prior: chalkboard length = 5 m)

Static scene, camera static and frontal (board edges horizontal/vertical -> no tilt; principal point / vanishing
point taken as image centre (960,540), confirmed below). fps 24 = question_fps (time irrelevant here).

## Measurements (frame 0 / static background frames; scripts board.py, prof.py, colcrop.py, enh*.py)
- Chalkboard incl. wooden frame: outer x 321 -> 1693 = **1372 px** (green surface 341.5 -> 1670.5 = 1329 px).
  Board lies on the back wall, depth Zw.  Scale at wall: 5 / 1372 = 3.644 mm/px.
- Teacher's table (long pale counter, left): top slab front edge x **80 -> 771 = 691 px** (front face panel below it
  96 -> 751 = 655 px; the slab overhangs both ends). Top-front-right corner (771,766), receding top edge to the
  back-right corner (791,~743) - this line passes through the vanishing point (960,540).
- Table is NOT at board depth (clear perspective, right side face visible):
  - route A (x of the side edge): Zback/Zfront = (960-771)/(960-791) = 189/169 = 1.118
  - route B (floor): table front bottom y = 999.5, wall-floor junction y = 951 (horizon 540):
    Zwall/Zfront = 459.5/411 = 1.118
  -> the table's back touches the wall; its front face is at Zf = Zw / 1.118.

## Answer
Length (bbox x-extent, slab) = 691 px x (5/1372) m/px x (Zf/Zw) = 2.518 / 1.118 = **2.25 m**.
Check: back edge at wall depth spans 791 - (960-(960-80)/1.118 = 173) = 618 px -> 618 x 3.644 mm = 2.25 m (same).
Sensitivity: using the green surface as "chalkboard" would give 2.33 m; ignoring perspective (pure 2D) 2.52 m;
using the front panel (655 px) instead of the slab 2.13 m. Chosen: full object incl. frame and slab.
Confidence: moderate (~±5-8 %), main uncertainty is what the board/table bounding boxes include.
