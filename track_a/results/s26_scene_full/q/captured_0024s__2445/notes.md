# q_2445 — velocity of the book at t = 1.2 s (frame 29), cm/s

File fps = question_fps = 24, so t = 1.2 s is frame 29 (the book reaches the bottom of the ramp and touches the table).

## Method (m1.py, m3.py)
- Book centres come from scene/tracks/teal_book.csv. I checked frames 29, 30 and 32 on zoomed crops: the mask is the teal book.
- f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- 3D anchors: frame 24 back-projected at 1.0685 m, giving (0.154, 0.052, 1.056); frame 29 at 0.977 m, giving (0.039, 0.119, 0.969).
  They are 0.1585 m apart.
- The book slides along a straight line on the ramp. For frames 15-29 I placed each centre on the 3D line through these
  two anchors (closest point to each pixel ray). The line's direction is within about 8 deg of the slope direction found
  from the slope_far/slope_near depths, which is consistent.
- Per-frame speeds on the ramp, backward difference, m/s:
  20: 0.13, 21: 0.25, 22: 0.36, 23: 0.46, 24: 0.52, 25: 0.66, 26: 0.73, 27: 0.76, 28: 0.84, 29: 0.815.
- Check against the prior: the raw second difference at frame 24 is about 3.4 m/s^2; with 5-frame smoothing it is
  1.9-2.4 m/s^2. The prior of 2.8 m/s^2 falls inside this range, so the metric scale is consistent.

## Value at frame 29
- End-of-ramp speed: 0.815-0.84 m/s from the measured steps; a linear fit over frames 22-29 gives 0.89.
- After frame 29 the book hits the table and slows down. A 5-frame smoothed forward difference centred on frame 29
  uses table frames (30-32), assuming depth stays near 0.97 m. That gives about 0.65-0.70 m/s.
- I could not build a reliable table-plane model. The camera is almost level with the table top, so a ray-plane
  intersection is ill-conditioned. The left/right table depths with the corner pixels also did not give a consistent
  square table.
- Answer: 78 cm/s, a compromise between the instantaneous end-of-ramp speed (~83) and the smoothed value that includes
  the impact (~67).

Confidence: moderate. The impact at frame 29 makes the smoothing convention the main uncertainty (about ±15%).
