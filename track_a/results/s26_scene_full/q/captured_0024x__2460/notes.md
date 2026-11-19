# q 2460 — width of the slope (cm)

File fps 24 = question_fps 24. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
"Width" = the white ramp board's short edge across its face (perpendicular to the slope), i.e. the top/bottom edges.

## Measurement (ramp_fit.py, check.py)
- White-board mask (V>200, S<40) on frames 40/44/48 (static). Fitted straight lines to the 4 edges using only the
  straight middle parts (rounded corners and the white pages of the resting book at the lower left left out);
  line residuals <= 1.5 px. Corners (frame 48): TL (751.0,359.5), TR (864.2,361.0), BR (707.1,492.4), BL (604.9,468.9).
- The top and bottom edges are far from parallel in the image (vanishing point at x ~ 70): the width direction
  goes about 37 deg into depth, so the simple "depth x pixel length / f" gives wrong values (13.4 cm at the
  near end, 17.5 cm at the far end) and was not used.
- Rectangle pose from the homography with known K: the edges meet at 87 deg (a rectangle should give 90; good
  check), the width direction is 87 deg from the table normal (the bottom edge lies on the table, so this is
  consistent), and the board is tilted 34 deg. Aspect width/length = 0.71.
- Scale: near-end centre distance 0.990 m -> width 21.8-22.0 cm, length 30.7 cm.
  Far-end distance 1.243 m -> width 23.6-23.8 cm, length 33.3 cm. These two depths do not agree with the rectangle
  geometry (with the near scale, the model puts the far end at 1.149 m, not 1.243 m).
## Second route (check2.py)
- With the near-end scale, the book's centre ray at t=1.0 (frame 24) meets the board plane at 1.102 m. Putting the
  centre half a book's thickness (~1.3 cm) above the board gives the given 1.0685 m. So the near-end scale agrees
  with the independent book depth, and the far-end depth looks too large by about 8%.
## Answer
Width = 22.0 cm (near-end scale, backed by the book depth). Using the far-end scale would give 23.7 cm, and the
mean of the two 22.7 cm. Board ~31 x 22 cm, which looks like a clipboard, so the value is plausible.
Confidence: moderate-high, about ±5%.
