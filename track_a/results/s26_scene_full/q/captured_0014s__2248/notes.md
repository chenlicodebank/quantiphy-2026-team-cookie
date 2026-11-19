# q_2248 — length of the book (cm)

The file and the question both run at 24 fps. The book is the light-blue notebook to the right of the board. It does not move,
so frames 0 and 48 give the same mask. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
Scale: book centre depth 1.665 m at t = 0.

## Method
1. `seg_book.py`, `book_final.py`: colour mask of the book (V > 190, S < 65). Line fits to the four edges of the top
   cover give these corners (frame 48): BL (625.1, 389.1), BR (662.1, 383.1), FR (681.8, 424.4), FL (639.8, 432.0).
   The white page block below the front edge (about 4-5 px, roughly 1.1 cm thick) is the front side face, so it is excluded. An
   earlier mask that included it made the long side about 2-3 cm too long. Overlay: `frames/book_corners.png`.
2. `plane.py`: table-top orientation, taken from the vanishing point of the table's left and right edges (VP at
   (497, -22)) and its front edge, assuming the table corners are right angles. Camera looks down about 27.3 deg
   relative to the table, roll about -3.9 deg.
   Independent check: the cup's top ellipse (about 15 x 40 px) implies a view angle of about 22-27 deg.
   A plane fitted to the cookie, pen and book depths alone gave about 52 deg. That fit is wrong because the cookie stands
   upright against the cup: its centre is about 4 cm above the table. With the vanishing-point plane, the cookie depth
   implies a height of about 4.4 cm, which matches a standing cookie of radius about 3.75 cm.
3. `final.py`: the corner rays are intersected with the plane through the book centre (back-projected at 1.665 m),
   raised 0.55 cm for the top face. Edges (cm): back 8.64, right 18.47, front 8.95, left 18.62. Corner angles are
   87.5-91.5 deg, so the back-projected shape is nearly a rectangle, which supports this plane.
   Long side = 18.5 cm; short side = 8.8 cm.

## Checks
- `scan.py`: searching the plane tilt and roll for the most rectangular book gives tilt 26, roll -5.25, long side
  about 19.4 cm. Rectangularity changes little near the optimum, so this is a weak constraint. At that tilt the pen depth
  is reproduced (1.674 vs 1.6725 given).
- `tilt_fit.py`: with the vanishing-point plane, the predicted depths of the pen (1.659 vs 1.6725) and of the
  slope's near edge (1.682 vs 1.701) are both 1.3-2 cm short. That points to a small depth offset (or a slightly flatter
  plane), which would make the length about 1-4 % larger.
- Sensitivity: about -0.55 cm per +1 deg of tilt.

## Answer
Length (longer horizontal extent) = **18.7 cm**: the vanishing-point value of 18.5 cm, nudged up because the depth and
rectangularity checks point higher. Width (short side) = 8.8 cm. Likely range 18.2-19.4 cm. Confidence moderate (about ±4 %).
