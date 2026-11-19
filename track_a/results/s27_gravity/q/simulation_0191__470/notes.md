# q470 — truck tire diameter (simulation_0191, 2D, 120 fps = question_fps)

Scale (fit.py): I fitted a quadratic to the box centre cy (scene/tracks/box.csv, template-matched, ±0.3 px) over free fall
frames 0–60 (impact at frame 61). The pixel acceleration came out at 1963–1985 px/s² depending on the window (rms residual
0.05 px). With the prior g = 9.8 m/s², that gives 0.00494–0.00499 m/px; I used 0.00497 m/px.

Tire (wheel.py, wheel2.py, frame 180): I read the tire edges from full-resolution intensity profiles. The edge is where the
dark wheel-well gap (~0) meets the tire tread (~10–30), and the bottom is the ground transition.
- Front tire: x 1499.5–1662.5 (163 px), y 900.5–1063.5 (163 px).
- Rear tire: x 621.5–787.5 (166 px), y 898.5–1063.5 (165 px).
- Mean about 164.5 px, so 164.5 × 0.00497 = 0.818 m.

Checks: the scene record's eyeballed value is 165 px, which agrees. With this scale the truck is 1690 px = 8.4 m long and
the wheelbase is 875 px = 4.35 m, both plausible for a catering truck. A tire diameter of about 0.82 m is realistic.
The truck side is slightly nearer the camera than the box, so the true size could be a few % smaller. I used the single 2D
scale, which is the convention here.

Confidence: good, about ±3%.
