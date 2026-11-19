# Q2783 — initial distance yoga ball ↔ shoe (m)

File fps = question_fps = 24; frame 0 = initial. Lab camera: f = 0.5959*1280 = 762.8 px, principal point (640,360).

Method (measure.py):
- Ball: circle track from scene/tracks/exercise_ball.csv (checked against frames). Frame 0 centre (617.3, 509.5), diameter 130.1 px;
  frame 24 (t=1.0) centre (571.7, 541.9), diameter 147.0 px.
- The ball moves before t=1.0 (rolls from frame 19), so its frame-0 depth is not the given 2.612 m. Ball radius from
  frame 24: angular diameter (tangential, off-axis corrected) with D=2.612 m -> R = 0.243 m (diam 0.486 m).
  Frame-0 distance D0 = R/sin(alpha0/2) = 2.913 m.
- Shoe static, centre (284, 654) px (mask centroid in static_measure.json, confirmed on a zoomed crop), D = 2.231 m.
- Back-projection: P = D * unit ray. Ball f0 (-0.085, 0.560, 2.858); shoe (-0.891, 0.735, 1.909).
- Distance = 1.257 m (frame 0); 1.248 using mean of rest frames 0-4; shoe centre ±3 px -> 1.249-1.257.

Check: same depth model reproduces the prior speed at t=1.0: 2.11 m/s (5-frame window) vs given 2.19 m/s (~4%),
so the depth scaling of the ball is consistent.
Alternatives: plain 1/diameter scaling 1.284 m; if the ball depth 2.612 were (wrongly) used at frame 0: 1.07 m.

Answer: 1.255 m. Confidence: moderate-good (~±5%), main uncertainty the ball's frame-0 depth (diameter ±2 px ≈ ±1.5%).
