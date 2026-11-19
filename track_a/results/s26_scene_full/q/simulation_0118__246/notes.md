# Q246 — total displacement of the toy car (m)

Prior: speed of toy car = 0.05 m/s (exact). 2D top-down scene, static camera.

Track (scene/tracks/toy_car.csv, mask centroid, frames 0–120): straight line to +x, y constant (730).
fit.py: linear slope 2.609 px/frame, quadratic term −6e-5 px/frame² (negligible) → uniform motion over
the whole clip; car moving at frame 0 and frame 120 (no start/stop).

Scale from the prior: 0.05 m/s / (2.609 px/frame × 24.003 fps) = 7.98e-4 m/px.
- Route 1: net centroid displacement 312.2 px × 7.98e-4 = 0.2493 m.
- Route 2: constant speed × clip duration = 0.05 × 120/24.003 = 0.2500 m (same with question_fps 24).

fps 24.003 vs question_fps 24 differ by 0.01% — irrelevant.
Answer: 0.25 m. Confidence high (routes agree within 0.3%).
