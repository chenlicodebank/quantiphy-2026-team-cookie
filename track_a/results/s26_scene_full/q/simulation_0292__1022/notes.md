# q1022 – displacement of the column below the drone, 0.5 s → 1.0 s

- Here "the column" means the drone's cylindrical body under its top plate. It is fixed rigidly to the drone, rises straight up with it, and moves at constant speed from frame 2 to frame 71 (24 fps, question_fps = 24 too, so frames 12 → 24).
- Record check (check.py): the top-plate track gives 7.143 px/frame (linear fit, rms 0.27 px, no quadratic term). The column's measured bottom edge gives 7.07 px/frame, which is the same. Steps over frames 13–24 average 7.12 px/frame.
- Scale from the prior: 0.96 m/s / (7.143 px/frame × 24) = 0.00560 m/px.
- Route 1: the speed is constant, so displacement = 0.96 × 0.5 = 0.480 m.
- Route 2: the measured pixel displacement from frame 12 to 24 is 85.40 px × 0.00560 = 0.478 m.
- Answer 0.48 m. Confidence is high.
