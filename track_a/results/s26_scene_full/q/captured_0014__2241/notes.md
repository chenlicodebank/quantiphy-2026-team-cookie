# q_2241: length of the slope (cm)

The slope is the white board lying tilted on the table. The ball rolls down it, from the top (back) edge to the bottom (front) edge.
The file runs at 24 fps, the same as question_fps.

## Method (lab card)
- f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Board mask at frame 46 (no ball or hand on it), threshold min(RGB) > 215, in `board.py`. Hull corners: TL(500,314),
  TR(592,303), BR(609,407), BL(510,422). Top edge at the ball's path is y≈307 (x 546); bottom edge is y≈417–418 (x 551–558).
- Each point was back-projected with depth_info: slope_far = 1.854 m (top edge midpoint) and slope_near = 1.701 m (bottom
  edge midpoint). The script is `length.py`.
  - Using the midpoints of the true edges (top 547,306.8 to bottom 558,417): 29.8 cm. Along the ball path: 29.8 cm.
  - Using midpoints between hull corners (the rounded corners pull these inward): 29.0 cm. Left side 29.1 cm, right side 28.8 cm.
- Answer: 29.7 cm.

## Checks
- Board width at the top edge (depth 1.854) is 22.1 cm, and at the bottom edge (depth 1.701) it is 22.0 cm. The two agree, so the
  depths fit the two edge midpoints. A board of 22 x 29.7 cm is close to A4 size, which is plausible.
- Ball kinematics check (rough): released at frame 8±1, leaves the board at frame 17.5. With s = ½·4.6·t² this gives 0.29–0.36 m,
  which agrees within the ±1 frame release uncertainty.

Confidence: good, about ±3%.
