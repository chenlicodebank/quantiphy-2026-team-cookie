# Q903: speed of the red cup at t = 0.2 s

- This is a 2D scene. The file and question_fps are both 30 fps, so t = 0.2 s is frame 6.
- The cup falls freely from rest over frames 0–14 (scene/tracks/cup.csv) and first hits the table at frame 15.
- Scale comes from the prior, g = 9.8 m/s². I fitted a quadratic to the vertical pixel positions over frames 0–14 (`fit.py`). The fitted acceleration is 6.95–7.03 px/frame² (residuals ≤0.5 px), depending on which point is used: top_y, bbox centre, mask centroid or bottom.
  That gives a scale of 9.8 / (a·900) m/px.
- Speed at frame 6 is the backward difference (y6 − y5)·30·scale:
  - top_y: 1.814 m/s
  - bbox centre: 1.806 m/s
  - centroid: 1.807 m/s
  - fitted parabola: 1.805–1.818 m/s
- Check: free fall released at t ≈ −0.04 s (from the fit) gives 9.8·(5.5 + 0.04)/30 ≈ 1.81 m/s.
- Answer: **1.81 m/s**. Confidence is high (±1%).
