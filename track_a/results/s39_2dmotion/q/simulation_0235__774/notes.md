# Q774 — speed of the basketball at t = 1.5 s (m/s)

Prior: ball diameter = 0.282 m. 2D video, static camera, question_fps = file fps = 24, so t = 1.5 s -> frame 36.
Speed = |p(36) - p(35)| x 24. Frame 36 is in the rising phase after the bounce (contact at frames 23-24), so the fit window 25–49 does not cross the bounce.

## Scale (prior object = the ball)
- `analyze.py`: half-level edge crossings of an (R-G) profile through the centre, 5 rows/cols averaged, frames 28–45.
  Horizontal diameter is 106.4–107.9 px, median about 107.4 px. The vertical diameter is about 108–110 px, which is likely slightly inflated by vertical motion blur, so I used the horizontal one.
- SAM 3 (`segment "basketball"`, frames 35 and 36) gives horiz_px 107 at both frames and vert 109–110. My bbox is 108 x 108–110. All agree to within 1 %.
  The scene record's circle fit (106.1) is 1.2 % smaller, which is within 3 %.
- Scale: 0.282 / 107.4 = 0.002626 m/px.

## Displacement 35 -> 36
- My hull circle-fit centre (`measure.py`): y 609.73 -> 593.37, which is 16.36 px. x is constant at about 907.3.
- Scene record circle fit: 609.58 -> 592.82, which is 16.76 px. SAM centroid: 609.8 -> 593.5, which is 16.3 px.
- Raw per-frame differences are noisy at about ±0.5 px. A parabola fitted to y over frames 25–49 (rms 0.11 px, a = 1.238 px/frame²) gives 16.71 px for the 35->36 interval. I used that: 16.7 px/frame.

## Answer
v = 16.7 x 0.002626 x 24 = **1.05 m/s**.

Second route: raw differences give 1.03 m/s (mine and SAM) and 1.06 m/s (record). With the record's 106.1 px diameter the answer is 1.07. All of these are within ±2 %.

Confidence: high (about ±3 %).
