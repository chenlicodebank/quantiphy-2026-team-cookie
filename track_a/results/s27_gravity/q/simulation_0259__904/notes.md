# Q904: speed of the red cup at t = 0.4 s

- The video is 2D, 30 fps, and question_fps is 30, so t = 0.4 s is frame 12. The cup falls freely from rest at frame 0 and first hits the table at frame 15.
- Scale comes from the prior (a = 9.8 m/s² before 0.5 s). I fitted a quadratic to the vertical track over frames 0–14 (fit2.py, using scene/tracks/cup.csv).
  The pixel acceleration is 6.96 px/frame² (top_y 7.03, centroid 6.96, bbox centre 6.96, bottom 6.90). That gives 9.8 / (6.96 × 900) = 1.565e-3 m/px.
- Speed is the backward difference from frame 11 to frame 12. The centre moves 80.5 px (top_y 81, centroid 80.4), so the speed is 80.5 × 30 × 1.565e-3 = 3.78 m/s.
  The result does not depend on the scale: v = Δy / a_px × 9.8 / 30.
- Second check:
  - All tracking points and fit windows give 3.76–3.81 m/s.
  - Ideal fall from rest at frame 0: backward difference = g × 11.5 / 30 = 3.757 m/s.
  - The fitted rest time is frame −0.05, which agrees with release at frame 0.
- I re-tracked the cup myself (measure.py) and got matching top edges for frames 4–14. In early frames my mask threshold picked up background noise, so I used the scene record's track instead.
- Answer: 3.77 m/s. Confidence is high (about 1%).
