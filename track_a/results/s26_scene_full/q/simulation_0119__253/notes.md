# q_253: chessboard side length (m)

2D top-down video. The prior says the moving dark chess piece has a speed of 0.04 m/s.

- Speed in pixels: I fitted a line to the piece track (scene/tracks/dark_piece.csv, circle-fit centre circ_cy) over frames 0–35,
  where the motion is uniform. Slope = 1.3984 px/frame (frames 3–33 give 1.4002). At 24.012 fps that is 33.58 px/s.
  At 24 fps (question_fps) it is 33.56 px/s; the 0.05% difference does not matter.
- Scale: 0.04 / 33.58 = 1.191e-3 m/px.
- Board size: board.py finds the square edges on frame 47. Along a row they run from x=247/248 to 583/584, and along a
  column from y=504 to about 840. That is 10 squares at a 33.6 px pitch, so the side is 336 px.
- Side = 336 × 1.191e-3 = 0.400 m.
- Second check: the piece moves almost exactly one square (33.6 px) per second. So one square is 0.04 m, and 10 squares
  make 0.40 m. This agrees.
- Confidence: high, within about 1–2%. The board is the playing grid only; no extra frame border is visible.
