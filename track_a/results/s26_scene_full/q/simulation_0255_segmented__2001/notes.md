# q_2001 — speed of the tennis ball at t = 1 s

- 2D segmentation video, 24 fps (file fps = question_fps = 24, so no re-timing). t = 1 s → frame 24.
- Only one object (the ball). It moves horizontally to the right and slows steadily. The camera is static.
- Scale from the prior: the ball diameter is 0.17 m. Measured diameter: vertical half-max extent 25 px (median), sub-pixel vertical
  half-level crossing 24.96 px (median over 41 frames), soft-area equivalent diameter 24.6 px, and 25.0 px in the scene record.
  I used 25.0 px, so the scale is 0.0068 m/px.
- Speed (measure.py, my own weighted-centroid track): the raw backward step from frame 23 to frame 24 is 37.83 px. A quadratic fit
  over ±3, ±5, ±7 and ±10 frames, and over the whole clip, gives a derivative at frame 23.5 of 37.88–37.91 px/frame
  (residual std 0.19 px). I used 37.88 px/frame.
- Speed = 37.88 × 24 × 0.0068 = 6.18 m/s.
- Second route: the record's step from frame 23 to frame 24 is 37.76 px, which gives 6.16 m/s. The global quadratic gives 6.19 m/s.
  The main uncertainty is the diameter (±0.4 px, about 2%).
- Confidence: high (about 3%).
