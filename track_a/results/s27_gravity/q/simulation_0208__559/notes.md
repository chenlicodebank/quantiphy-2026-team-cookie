# q_559: speed of the typewriter at t = 0.25 s

The video is a 2D simulation at 24 fps, and question_fps is also 24. t = 0.25 s is frame 6, so the speed is the backward difference (p6 - p5) x 24.
The prior says the typewriter falls with a = 9.8 m/s^2 before 0.45 s (frames 0-10 are airborne; it hits the mat between frames 10 and 11).
The scale comes from the pixel acceleration: m/px = 9.8 / (a_px/frame^2 x 576). So speed = v_px/frame x 9.8 / (24 x a_px/frame^2).

## Measurements (fit.py, on scene/tracks/typewriter.csv)
- I fitted a quadratic to the bbox centre over frames 0-8, 0-9 and 0-10. a = 12.48-12.78 px/frame^2, and the
  fitted v at frame 5.5 (equal to the backward difference at frame 6) = 69.7-70.0 px/frame. Speed = 2.23-2.28 m/s.
- Raw difference: centre y 415.5 -> 484.5 = 69 px. With a = 12.5 px/f^2 this gives 2.25 m/s.
- Mask centroid: 2.22-2.27 m/s. Top edge: 2.31-2.33 m/s. Bottom edge: 2.17-2.24 m/s (motion blur moves the edges in opposite ways). The mean of the two edges is about 2.27.
- Physics check: the fitted release time is about frame 0 (between -0.08 and +0.05 frames). For a fall from rest at frame 0, the speed at frame 6 is
  g x 5.5/24 = 2.246 m/s. That matches.

Answer: 2.26 m/s. Confidence is high (about ±2 pct).
