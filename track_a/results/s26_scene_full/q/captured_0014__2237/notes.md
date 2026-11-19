# q_2237 — length of the book (cm)

The file rate and question_fps are both 24. The book is the light-blue notebook lying flat on the table, to the right of the white board.
Its centre is at about (653, 410) px. Given depth: 1.6650 m at t=0. Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

## Why the naive card formula is not enough
The book lies flat, and its long side points away from the camera, toward the back of the table. The camera looks down at only
about 28° to the table plane, so the long side is foreshortened about 2x in the image: its cover spans only 44.8 px along the long axis.
The naive depth*px/f estimate gives about 10–11 cm, which is too small. I back-projected the cover edges onto the table plane instead.

## Table-plane orientation (two independent routes)
1. Vanishing points of the table-top edges (corners: back-right (658,310), front-right (730,456), front-left (426,500), back-left ~(442,332)).
   The right and back edges were also fitted from a colour mask (`table_edges.py`). This gives normal n = (-0.002, -0.879, -0.477), i.e. the camera
   sits 28.5° above the plane. The two edge directions come out 87° apart (they should be 90°), a good self-check (`plane.py`).
2. Free fall of the ball (frames 23–28) after it rolls off the table (`fall.py`). For each tilt I put the ball on the table plane,
   launched it with its measured rolling velocity and gravity of 9.81, and projected its path. The measured pixel path (472, 494, 525, 566, 615, 672)
   is matched best at a tilt of 27–28°. Pixel acceleration: measured 8.7–9.2 px/frame², predicted 8.3 at 28° and 9.4 at 25°.
   Check: the ramp direction from the ball's two given depths makes a 30–31° slope with this plane, consistent with the 4.6 m/s² prior
   (g·sin 30° = 4.9 for sliding, and less for rolling).
   The 3-point plane through the pen, book and slope_near depths is unreliable: it gives 20°, and the table sides do not come out as a sensible rectangle.

## Book edges (`book.py`, `profile.py`, `length3d.py`)
I took the median of 7 frames (the book never moves). I measured the B−R colour profiles along the book's long axis at 25 lateral offsets, with subpixel
half-level crossings:
- far edge: cover-to-table edge
- near edge: cover-to-white page strip. The white strip (~5 px) is the book's thickness face (about 1.2 cm thick), not the cover, so it is excluded.
Cover image length: 44.8 ± 0.8 px. I back-projected both edges onto the plane through the book centre, at depth 1.665 m along the centre ray.

| plane normal | length | width |
|---|---|---|
| table VP (28.5°) | 17.5 cm | 9.5 cm |
| 28° | 17.7 | 9.6 |
| 27° (fall fit) | 18.2 | 9.6 |
| 25° | 19.4 | 9.6 |

Lifting the plane 0.6 cm to the cover height changes the length by only −0.1 cm.
Sensitivity: 1 px of edge position ≈ 0.4 cm, and 1° of tilt ≈ 0.5 cm.

## Answer
Length ≈ 17.8 cm. This is the cover length along its longer horizontal side, averaging the vanishing-point and free-fall tilts. The width is about 9.5 cm.
Confidence: moderate, about ±7%. The main error sources are the camera tilt and the soft cover edge.
Under the naive card reading (largest image extent × depth / f), the value would be about 10.9 cm. I did not use it because of the strong foreshortening.
