# q_692 speed of the moving chess piece at t=1 s
- 2D sim, 24 fps (file = question fps). The moving object (called a soap block in scene/ notes) is the Chinese chess piece: a disc seen nearly edge-on sliding down the inclined board.
- Scale: its diameter = extent along the slope = 81.5 px (median over frames 0-38, range 80-83; checked on a zoomed frame 24) -> 0.097/81.5 = 1.190e-3 m/px.
- Track: scene/tracks/block.csv centroids (checked against frame 24 zoom). The video has duplicate frames paired with skipped frames.
  A quadratic fit of x,y against the re-indexed source frame (rms 0.8 px) gives a backward-difference speed of 23.3 px/frame at source frame 24 (0.666 m/s)
  and 24.3 px/frame at source frame 25 (0.695 m/s). Video frame 24 shows source frame 25; its raw backward diff is 24.5 px (0.700 m/s).
  Fit vs raw frame index at 24: 0.681 m/s. Acceleration ~0.69 m/s^2 (uniform).
- Answer 0.68 m/s: middle of 0.666-0.700, the uncertainty from which frame index the reference uses. Within about 3% of either.
- measure.py reproduces these numbers.
