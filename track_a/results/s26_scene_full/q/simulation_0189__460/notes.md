# Q460 – truck tyre diameter (m)

2D side view, 120 fps (file fps = question_fps, so no re-timing). Prior: box speed = 0.094 m/s.

Scale (speed.py): box centre track in scene/tracks/cardboard_box.csv rises at a constant rate. A linear fit over
frames 0–400 gives 0.15995 px/frame (residual std 0.05 px). The rate per 100-frame block is 0.1593 / 0.1595 /
0.1606 / 0.1601, and the quadratic term is negligible. That makes 19.19 px/s → 0.094/19.19 = 0.004897 m/px.
Independent check (check_box.py): the sub-pixel top edge of the box moves 0.1594 px/frame between frames 0 and 400,
which agrees.

Tyre (prof2.py, enh.py, frame 0; the wheels are static): intensity profiles across the dark gaps around each tyre.
- Front: left 1500, right 1662.5 → 162.5 px; top 862.5, ground contact 1025 → 162.5 px.
- Rear: left 623, right 786 → 163 px; top 863, bottom 1025 → 162 px.
Diameter = 162.5 ± 1 px → 162.5 × 0.004897 = 0.796 m (range 0.793–0.798).

This assumes the box and the wheels sit at roughly the same depth (side plane of the truck), as the 2D
convention says. Confidence: good (≈1–2 % measurement uncertainty).
