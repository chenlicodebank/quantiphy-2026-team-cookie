# q2454 — book velocity at t = 1.0 s (frame 24), cm/s

The file and the question both run at 24 fps, so t = 1.0 s is frame 24 and t = 1.2 s is frame 29.

## Method (measure.py)
- I took the book centre track from scene/tracks/book.csv, using both the full-mask centroid and the cover centroid.
  The crops at frames 24 and 26 match the track: the frame-24 centre is about (751, 397).
- Camera model: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- 3D: I back-projected frame 24 with depth 1.0685 m and frame 29 with depth 0.9770 m. Those two points fix the
  book's straight 3D line down the ramp. For every other frame, the 3D point is the point on that line closest to the
  frame's pixel ray. The depths run from about 1.116 m at rest to 0.977 m.
- Speeds come from frame-to-frame 3D displacements. The book starts moving at frame 19.

## Key numbers (cm/s)
- Forward differences at frames 22–26, mask centre: 32, 64, 64, 71, 79. Mean 62.0.
- Same for the cover centre: 44, 53, 67, 68, 85. Mean 63.4.
- Forward difference at frame 24 alone: 63.5 (mask) and 67.2 (cover).
- Quadratic fit of path length over frames 19–28:
  - v at t = 1.0 is 58–59 and v at frame 24.5 is 62–64.
  - The fitted acceleration is 2.1–2.3 m/s², against the prior's 2.8.
- Physics check: with a = 2.8 from the start at frame 19 (0.79 s), v(1.0) is about 58 and v(1.02) about 65.

## Answer
The reference convention is the forward difference smoothed over 5 frames, so I answer 62.5 cm/s.
A centred or instantaneous reading would give about 58. Confidence: moderate, about ±8%.
