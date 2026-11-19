# q_681 – horizontal length of the xiangqi board

Question: board length (horizontal) in metres. Prior: piece diameter = 0.097 m. 2D scene: the board is seen almost
straight from above, so one metres-per-pixel scale from a piece. fps 24 = question_fps; time is not involved.

## Measurements (frame 44, static scene; `measure.py`, `profile.py`)
- Piece diameter: 12 static pieces in the middle rows (y 322–753), measured with sub-pixel half-level edge
  crossings through the centre: horizontal 85.2 px, vertical 85.1 px (range 84.2–86.3). The scene record's
  86.5 px for the general was taken at y≈156, where everything looks slightly larger (see below).
- Board outer extent (orange rim, colour mask R−B > 70) per row: 1042 px at y≈120–160, 1036 px at y≈460–640,
  1032 px at y≈700–980. The board narrows slightly towards the bottom of the image (mild perspective tilt), so I use
  the mid-height width, 1036 px, which matches the rows where the pieces were measured. Left edge ≈ 450, right ≈ 1485.
- Scale: 0.097 / 85.15 = 1.139e-3 m/px.

## Answer
1036 × 0.097 / 85.15 = **1.18 m** (horizontal outer extent, i.e. the bounding box of the board).

## Second-route check
- Top rows: general diameter 86.5 px and board width there 1042 px → 1042/86.5 × 0.097 = 1.168 m.
- Rows with the per-row width ranging 1032–1042 px against a piece diameter of 84.2–86.3 px give 1.16–1.20 m.
- If the inner playing-surface edge (≈1030 px) were meant instead, the answer would be 1.17 m (within 1%).

Confidence: good, about ±2%.
