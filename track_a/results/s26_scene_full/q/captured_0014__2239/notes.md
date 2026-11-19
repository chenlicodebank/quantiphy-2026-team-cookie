# Q2239: height of the book (cm)

The file is 24 fps, the same as question_fps. The book is the light-blue notebook lying flat on the table, right of the board
(it does not move). It lies flat, so its **height = vertical extent = thickness** (the named-size rule).

## Method (lab camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360))
- I averaged frames 0, 30 and 40 (the book is static) and cropped the book (`profile.py`, `book_crop.npy`).
- The front face of the book (cover edge, white page block, bottom edge/contact) is visible at x 646-675. `lines.py` finds,
  in luminance, the dark teal top-cover edge line and the dark bottom/contact line in each column (sub-pixel minima). On the
  clean columns the centre-to-centre gap is 6.1-6.5 px (median 6.2). Adding about half a line width for the top cover edge
  gives a face extent of about 6.5-6.7 px. The visible white page block alone is about 5 px, and top-of-cover to the end
  of the dark shadow is about 8 px, so it lies between 5 and 8 px.
- Geometry (`geom.py`, `topface.py`): I took the table-plane normal from the vanishing points of the table-top edges
  (the edge directions meet at 87.2 deg, so the square-table assumption checks out). Normal in camera coordinates =
  (-0.002, -0.879, -0.477). Viewing rays meet the table at about 34 deg below the horizontal (that is, 124 deg from the up
  normal). The table plane runs through the book centre at depth_info 1.665 m, which puts the front-face bottom point at
  1.587 m depth. A vertical segment there projects to: 6.0 px = 1.48 cm, 6.5 px = 1.61 cm, 7.0 px = 1.73 cm, 8 px = 1.98 cm.
- Answer: **1.65 cm** (about 6.6 px).

## Checks
- The simple scale route without the plane (depth 1.62-1.665 m, table normal, `geom.py`) gives 1.52-1.56 cm for 6 px and
  1.77-1.82 cm for 7 px. This matches the route above.
- The book's top face reconstructed on the plane measures about 10 x 19 cm, a plausible small notebook, so the scale is sane.
- The ball-acceleration prior is not needed for this size.

## Ambiguity
If "height" meant the book's long cover dimension (the spine length), the answer would be about 19 cm (from the top-face
reconstruction: sides 18.6 and 19.8 cm, short sides 8.6 and 11.1 cm, so ±1-2 cm). I answer with the vertical-extent
reading, as the named-size rules say.

## Confidence
Moderate. The thickness is only about 6.5 px, so ±1 px means ±15 %. The camera-pitch error is about ±5 %.
