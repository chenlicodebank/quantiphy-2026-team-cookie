# q 3238 – displacement of the ball, 2.00 s -> 2.10 s (frames 60 -> 63 at question_fps 30 = file fps)

Scene: top-down hand-held view of a gym floor; a basketball rolls right-to-left across the floor (frames 49-72).
Prior "gravity = 9.8 m/s^2" describes no visible motion (no fall/bounce; the ball rolls horizontally in the image
plane), so it gives no usable scale. Scale taken from the standard object: a regulation (size 7) basketball,
diameter ~0.24 m.

Measurements (measure.py, scene/tracks/ball.csv):
- Ball diameter across motion (blur-free vertical extent): 256 px (record, frames 53-69); my own mask 255-263, mean ~259.
  Used 257 px -> 0.24/257 = 9.34e-4 m/px (the ball's centre moves in one plane, at the same depth as its diameter).
- Centre displacement 60 -> 63: record direct 274.5 px; linear fit over frames 53-69: 271.1 px; local fit 57-66: 272.0 px.
  My cruder mask (contaminated by shadow on the leading/trailing side) gave 254-259 px; not used.
  Adopted 273 px.
- Displacement = 273 x 0.24/257 = 0.255 m. (Speed check: ~90.4 px/frame -> 2.5 m/s, plausible for a rolled ball.)

Confidence: moderate; main uncertainty is the scale (ball size 0.23-0.245 m) -> about ±4%.
