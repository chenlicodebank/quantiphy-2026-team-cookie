# Q848: speed of the soccer ball at t = 2 s (m/s)

- 2D simulation, static camera, ball rolls horizontally and slows down steadily. fps = question_fps = 24, so t = 2 s is frame 48.
- Scale: prior diameter 0.344 m. Pixel diameter checked on frame 48 by overlaying an R = 25 px circle at
  (1401.6, 557.4) on an 8x zoomed crop (`crop.py`, frames/c48o.png). It matches the top, left, right and bottom
  silhouette, so D = 50 px (±1) and the scale is 0.00688 m/px. Mask- and ray-based circle fits (`fitcirc.py`, `rays.py`)
  are noisy because the ball has low contrast and a shadow (R 24-26.7). They are consistent with 25 px.
- Motion: scene track cx (`scene/tracks/ball.csv`). Raw backward difference 47→48 = 25.74 px. Quadratic fits of cx(frame)
  (near-uniform deceleration) give a 47→48 step of 25.62-25.67 px over the windows 2-50, 20-50 and 34-50 (`speed.py`).
  Used 25.64 px/frame.
- Speed = 25.64 px × 0.00688 m/px × 24 /s = **4.23 m/s**.
- Second route: an independent ray-edge track gives a step of 25.95 px (4.29 m/s), and the raw difference gives 4.25 m/s.
  Both are within 1.5%.
- Confidence: about ±3%, dominated by the pixel diameter (±1 px of 50).
