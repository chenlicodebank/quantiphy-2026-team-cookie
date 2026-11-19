# q1032 — butterfly displacement 0.5 s → 1.0 s

- 2D scene, static camera, 24 fps (file = question_fps). Frames 12 → 24.
- Track (scene/tracks/butterfly.csv, ref point = thorax) checked via measure.py: straight leftward flight,
  linear fit frames 2–71 gives 15.67 px/frame (vx −15.67, vy +0.18), residual std 3.8 px (wing-flap mask noise);
  quadratic term negligible → constant speed, straight line.
- Scale from prior: 0.32 m/s ↔ 15.67 px/frame × 24 = 376 px/s → 8.51e-4 m/px.
- Route 1 (fit / constant speed): 12 frames × 15.67 px = 188 px → 0.160 m (= 0.32 m/s × 0.5 s).
- Route 2 (raw positions frames 12 and 24): 194.0 px → 0.165 m (frame 12 is near a wing fold, where ref_x is biased by a few px).
- Answer 0.16 m. Confidence high (path is straight, speed constant).
