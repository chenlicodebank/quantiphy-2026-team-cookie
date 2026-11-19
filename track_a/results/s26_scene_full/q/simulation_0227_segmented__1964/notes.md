# q_1964: speed of the "red general chess" at t = 1.5 s (prior: cat speed = 1.041 m/s)

- fps = question_fps = 24, so t = 1.5 s is frame 36.
- I found no chess piece in the clip. scan.py checks every 6th frame (and frame 36) for non-white and red
  pixels. The only non-white parts are the static chairs, the cat and the pink/red flamingo float, and the only
  red-ish moving object is the float. I therefore take the float to be the asked object. **This identification is
  the main uncertainty.**
- I treat the clip as 2D and use one scale from the cat. The cat's centroid moves a net 5.48 px/frame, and a linear
  fit gives 5.46 px/frame; the bbox right edge gives 5.47 px/frame. Using 5.47 px/frame (131.3 px/s), the scale is
  1.041 / 131.3 = 0.00793 m/px.
- Float speed at frame 36 (speeds.py, from the scene tracks):
  - The raw backward difference of the centroid is 10.4 px/frame.
  - Neighbouring frames give 11.0, 10.4 and 9.7.
  - A quadratic fit to frames 26–49 gives 9.99 for the centroid and 9.89 / 9.92 for the bbox x0 / x1 edges.
  - I use about 10.2 px/frame.
- Speed = 10.2 × 24 × 0.00793 = 1.94 m/s. The routes give a range of 1.90–1.98 m/s.
- Confidence: the measurement is good to about ±3% if the float is the asked object. The identification of the
  object is uncertain.
