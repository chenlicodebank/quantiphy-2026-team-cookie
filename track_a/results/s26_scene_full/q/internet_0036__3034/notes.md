# q_3034: average speed of the bottom (receiving) hand, 1.72 s to 2.6 s

- Time base: I used question_fps = 25. At that rate 1.72 s and 2.6 s land exactly on frames 43 and 65, and frame 65 is
  the last frame where the receiving hand is visible. At the file's 24.0625 fps they would fall on 41.4 and 62.6.
- Scale: prior = $1 bill width 66.3 mm, which is the bill's short edge. It measures 611 px at frame 0 and 607 px at
  frame 44, giving 0.1085 mm/px.
- Reference point: the receiving hand grips the bill and carries it out of frame, so I used the bill-rectangle centre
  from scene/tracks/bill.csv (SIFT-chained, about ±3-15 px). It is tracked up to frame 64; I extrapolated frame 65
  with the last step, because per-frame steps level off at about 200 px/frame (frames 62-64).
- Path length over frames 43-65 = 2448 px in 0.88 s, so speed = 0.302 m/s (net displacement gives 0.301).
- Second route: the receiving hand's fingertip track (topmost skin pixel) gives 0.301-0.304 m/s (0.306 with the 607 px
  scale).
- Answer: 0.302 m/s. Confidence: moderate-high. The main uncertainties are the time base and how the annotator
  chose the reference point.
