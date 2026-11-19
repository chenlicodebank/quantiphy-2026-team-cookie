# q936 speed of the spacecraft at 1.0 s (simulation_0265, 2D)
Object: the only moving object (dark top-down futuristic vehicle = spacecraft), moving straight -x. fps 24 = question_fps; frame 24 = t 1.0 s.
Prior: acceleration 4 m/s^2 (constant). Scale: m/px = 4 / (a_px * fps^2).
Method (fit.py): quadratic fits of x(frame) on the scene track (checked: rms 0.1-0.5 px).
- ref_x (bbox centre) frames 7-50: a = 1.2048 px/frame^2, vertex at frame 0.01 (starts from rest at t=0), m/px = 0.00576.
- Backward-difference speed at frame 24 (x24 - x23): fit 28.30 px/frame -> 3.914 m/s; raw 28.5 -> 3.94.
Second routes: nose edge 3.917, tail edge 3.924, mask centroid 3.915, ref_x 10-40 3.907, ref_x 2-58 3.921 m/s.
Analytic: uniform accel from rest at t=0 -> backward diff speed = 4*(23.5/24) = 3.917 m/s (instantaneous would be 4.0).
Answer 3.92 m/s. Confidence high (the scale cancels out, so only the ratio v/a matters).
