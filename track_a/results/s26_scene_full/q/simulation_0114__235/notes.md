# Q235: speed of the plane at 1.5 s (prior: acceleration = 18 m/s^2)

- 2D scene, static camera (scene record). The plane moves straight down the image from rest at frame 0.
- fps: file 24.0024, question 24.0. The difference is negligible. Frame i = round(1.5 x 24.0024) = 36.
- fit.py fits a quadratic to ref_y(frame) from scene/tracks/plane.csv:
  - frames 0–75: a = 0.5969 px/frame^2, zero-velocity point at frame −0.025, rms 0.45 px.
  - Sub-windows 2–40, 20–60 and 40–75 give a = 0.5962–0.5965 with v0 near frame 0. So the acceleration is uniform and the plane starts from rest at t = 0.
- Scale: 18 m/s^2 / (0.5969 x fps^2 px/s^2) = 0.05235 m/px.
- Speed by the benchmark convention (one-frame backward difference at frame 36), from the fitted positions: 26.64 m/s.
- Second route, analytic with a start from rest at frame 0: a(i − 0.5)/fps = 18 x 35.5 / 24.0024 = 26.62 m/s. This agrees.
  - The instantaneous value a·t = 27.0 m/s would be the answer under the other reading. It is 1.4% higher.
  - The raw single-frame difference is 27.6 m/s, but it is noisy because the positions are quantised to 0.5 px.
- Answer: 26.63 m/s. Confidence high.
