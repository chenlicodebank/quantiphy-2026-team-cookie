# Q948 — speed of the spacecraft at 1.0 s (prior: acceleration at 1.0 s = 4 m/s^2)

2D simulation, 24 fps (file fps = question_fps, so no re-timing). t = 1.0 s -> frame 24.
The spacecraft (the only moving object, "vehicle" in scene/) moves left along y = 719.5 with constant acceleration.

## Method (fit.py)
Scale cancels: speed = 4 m/s^2 x (pixel speed / pixel acceleration).
Fitted a quadratic x(frame) to the scene/ tracks over frames 2-58:
- x_ref (silhouette centre): a = 1.2093 px/frame^2, rms 0.16 px, start of motion t0 = frame 0.04;
  backward-difference speed at frame 24 = 28.374 px/frame -> v = 4 x 28.374 / 1.2093 / 24 = 3.911 m/s.
  The raw step 23->24 (28.41 px) gives 3.916.
- x_body_texture (top-surface texture, a separate measurement): 3.911 (raw step 3.915).
- Second route, rear fin edge (silhouette edge, frames 8-64): 3.925 (raw step 3.96).
These match the analytic value for uniform acceleration from rest at t = 0: 4 x 23.5/24 = 3.917 m/s (the
backward difference is the speed at the middle of frames 23-24).

## Answer
3.91 m/s. Confidence high (all routes agree within 0.5%). If the reference took v = a·t instead, it would be 4.0 (2% off).
