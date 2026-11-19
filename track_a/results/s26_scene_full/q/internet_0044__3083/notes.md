# q_3083 – velocity of the white (ping-pong) ball at t = 2.50 s

- Time base: file fps = question_fps = 30, so t = 2.50 s is frame 75. At that frame the ball is in free flight on arc 3
  (bounce at 71.15, apex near 76, next bounce at 81.2). The camera only drifts slowly (<0.2 px/frame), so it does not matter here.
- Scale from the prior (g = 9.8 m/s²): I fitted parabolas to the vertical image position of each clean arc (fit.py) and got
  20.05, 19.83, 18.84, 19.50, 19.67, 19.60 and 19.94 px/frame². I used 19.6 px/frame² = 17640 px/s², which gives
  5.556e-4 m/px. The local arc 72-80 from my own segmentation gives 19.37 px/frame².
- Ball centre: I re-segmented frames 72-80 myself (seg.py: difference from a background median plus a white mask, blob centroid).
  Frame 75 is at (840.8, 556.8) and frame 76 at (825.7, 544.7), which agrees with scene/tracks/ball.csv to within about 3 px.
- Internet convention (forward difference): |p76 - p75| = 19.35 px/frame, which is 0.322 m/s.
  - Check with a parabola fit of the arc, forward difference: 0.320 m/s. The record's own track gives 0.315 m/s.
  - Other conventions: central difference 0.427, the fit's instantaneous value at frame 75 0.445, backward difference 0.559.
    The answer follows the forward difference that the annotators used.
- Answer: 0.32 m/s. Confidence: moderate. The measurement itself is good (±3%), but the answer depends on the
  difference convention, because the vertical speed changes quickly near the apex.
