# Q2238: width of the book (cm)

The book is the light-blue notebook lying flat on the table, right of the board, at about x 620–687 px and y 383–440 px.
It is static. The file rate and question_fps are both 24. The ball-acceleration prior isn't needed: the scale comes from
depth_info (book at 1.665 m at t=0) and the lab camera, f = 0.5959*1280 = 762.8 px, principal point (640, 360).

## Measurement
- Book outline: saturation threshold (S<65; the book is low-saturation, the wood is S~90–105). I checked this on
  printed S/V profiles (`prof.py`). The grey cover rim belongs to the book; shadows on the wood keep a high S, so they
  are excluded. Frames 0, 3, 6, 40, 44 and 48 were averaged.
- The left and right side edges were found as sub-pixel crossings on rows y 392–429 (`width3d.py`). Horizontal row widths
  are 44–50 px.
- Table plane normal: from the right table edge (fitted, `tedges.py`), the left edge and the front edge (record
  corners), with the vanishing point of the table sides and the front-edge interpretation plane: n = (-0.04, -0.85, -0.53).
  The plane passes through the book centre at 1.665 m, moved up by half the book's thickness.
- Both side edges were back-projected onto that plane and fitted as 3D lines. They come out parallel to within 0.6–1.0°,
  which supports both the plane and f. Width is their perpendicular separation in the plane:
  **10.0–10.1 cm** across three choices of left-edge normal and a book thickness of 0 or 1.5 cm.

## Checks
- Method-card route (horizontal pixel width × D/f, with no slant or foreshortening correction): 10.45 cm. It reads
  slightly high because a horizontal row cuts the slanted sides at an angle.
- On the same plane, the table comes out 0.59 x 0.64 m with an 88° corner, so it is nearly square. The ~5–8% mismatch
  between the lateral and depth sides gives a few percent of plane uncertainty. The pen comes out 14.6 cm and the book's
  long side about 16.7 cm, so width (~10 cm) is clearly the shorter side.

## Answer
10.2 cm: the 3D value of 10.05 cm, nudged toward the method-card value because the table check hints that the
lateral direction is slightly underestimated. Confidence: about ±5%.
