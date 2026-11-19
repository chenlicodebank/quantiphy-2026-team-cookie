# q_689 — length of the Chinese chess board (simulation_0224)

The clip is a 2D Blender scene: a tilted Chinese chess board, about 26° below horizontal in the image, with a chess
piece sliding down it. The scene record calls the piece a "soap block", but it is the chess piece seen edge-on: a
disc lying on the board. fps = question_fps = 24, but no timing is needed for this question.

## Scale (from the prior: piece diameter = 0.097 m)
- `measure_piece2.py` subtracts a background frame (frame 30 or 36, when the piece is far away) and measures the
  piece mask's extent along the slope direction at frames 0, 4, 8, 12 and 16: 81.9, 81.5, 81.9, 81.5 and 81.5 px.
  The scene record gives 81.5 px. I used a diameter of 81.7 px, so the scale is 0.097 / 81.7 = 1.187e-3 m/px.
- Frame 43 (free fall) gives 84.6 px, but that frame is motion-blurred, so I did not use it.

## Board
- `measure_board.py` builds a colour mask of the red-brown board on frame 0. The overlay is in
  `frames/board_mask.png`.
- The board's ends are perpendicular to the slope. Its extent along the slope is 1063 px, from (424,955) to
  (1381,492). This matches the scene record (1065 px). That gives 1063 × 1.187e-3 = **1.262 m** for the board's own
  length.
- The world axis-aligned horizontal extent of the tilted board is 422 to 1427 px = 1005 px, which gives **1.19 m**.
- The convention is ambiguous: the reference could use the object's own dimension or the horizontal extent of the
  world axis-aligned box. The two values differ by about 6%. I answer 1.235 m, which is within about 4% of both and
  leans toward the board's own length.

## Check
- The lower body of the board measures about 1027 px along the slope. It is shifted perpendicular to the slope by
  the slab's thickness, which confirms that the slope direction is the board's long axis.
- Measuring with slope angles of 25.9° or 26.4° gives the same extent.

Confidence: moderate. The pixel measurements are good to about 1%; the main uncertainty is which size convention
the reference uses.
