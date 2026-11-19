# Q363: speed of the turtle at t = 1.5 s (m/s)

The prior is that the turtle's acceleration is 2.639 m/s^2. The scene is 2D, fps = question_fps = 24, so t = 1.5 s is frame 36.

## Method (fit.py)
- I used the carapace track `shell_x/shell_y` from scene/tracks/turtle.csv. It is rigid and not disturbed by the flippers. The motion is purely horizontal and the camera is static, as the record checks.
- A quadratic fit of x(frame) has residual rms 0.38 px. The fitted acceleration is 0.927 px/frame^2 and the vertex is at frame 0.09, so the turtle starts at rest at frame 0 and accelerates uniformly.
- The per-frame steps are linear in frame number and extrapolate to zero at frame 0.51. That is what a start from rest at frame 0 gives, since the step from i-1 to i is a*(i-0.5).
- Scale: 2.639 / (0.927 * 24^2) = 0.00494 m/px.

## Speed at frame 36 (backward difference p(36)-p(35))
- Quadratic fit, derivative at frame 35.5: 3.893 m/s
- Linear fit of the per-frame steps: 3.902 m/s
- Raw step at frame 36: 3.899 m/s. Mean of the steps at frames 34-38: 3.909 m/s
- Fit over frames 11-47 only: 3.881 m/s
- Pure kinematics with the exact prior (start from rest at frame 0): a*35.5/24 = 3.904 m/s. The continuous value a*t = 3.96 would be 1.5% higher.

## Answer
**3.90 m/s.** Confidence is high: all routes agree within about 0.5%.
