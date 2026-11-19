# Q362 – turtle speed at t = 1 s (frame 24, 24 fps; file fps = question fps)

Prior: acceleration = 2.639 m/s^2 (2D scene, single scale from the prior).

Method (fit.py): carapace track shell_x from scene/tracks/turtle.csv (template-matched rigid shell, motion purely
horizontal, shell_y constant). Quadratic fits of x(frame):
- frames 0-47: a = 0.927 px/frame^2, rest at frame 0.09, residual 0.38 px
- 12-36: 0.920, rest -0.05; 0-30: 0.921, rest 0.00; 20-47: 0.936, rest 0.43
So the turtle starts from rest at frame 0 with uniform acceleration.

Scale-free conversion: m/px s = a_m / (a_px * 24^2); speed(frame 24) = |x24 - x23| * s * 24
= a_m * dx24 / (a_px * 24). Fits give 2.537-2.589 m/s; the ideal uniform-from-rest case gives
a * (23.5/24) = 2.584 m/s (backward-difference convention). Raw dx24 = 21.31 px (noisy) -> 2.53-2.55.

Second route: the fitted rest frame ~0 independently confirms v(t) = a*t form; a*t = 2.639 (central),
backward difference 2.584. Answer 2.584 m/s. Confidence high (alternatives within ~2%).
