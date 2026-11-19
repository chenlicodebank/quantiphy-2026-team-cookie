# q_2397: ping pong ball acceleration at t = 1.2 s (cm/s^2)

Lab video, 24 fps (file rate = question_fps), 1280x720, f = 0.5959*1280 = 763 px, principal point (640,360).
t = 1.2 s -> frame 29; depth_info frames: 0.6 s -> 14 (1.751 m), 0.8 s -> 19 (1.687 m), 1.2 s -> 29 (1.526 m).

## Track
I used scene/tracks/ball.csv x_ref/y_ref (centre = core top + half width) and checked it on frame 29 (zoomed crop:
ball spans about x 412-432, y 445-465, centre about (422,455), which matches). The ball rolls down the tilted board
toward the camera. Two irregular steps (13->14 and 35->36, about 2x a normal step) look like dropped capture frames.
I kept them out of the fit windows.

## Routes (scripts accel.py, stimeline.py, routeB2.py)
- Route B (follows the reference pipeline: back-project ray(u,v) x depth(t)): depth(t) is the exact quadratic
  through the three given depths (z-only acceleration is 25.3 cm/s^2). Pixel track smoothed by a quadratic in time.
  The 3D speed then gives these acceleration estimates at frame 29:
  - window 15-35: 25.5 (arc fit 26.2)
  - window 14-29: 22.9
  - window 15-32: 24.0
  - window 19-35: 27.6
  Unsmoothed pixels with wider windows give 28-34. Speed at 1.2 s is about 48 cm/s.
- Three-point chord check (only the given depths and the back-projected centres at 14, 19 and 29): mean speeds are
  36.4 cm/s (t = 0.70 s) and 43.7 cm/s (t = 1.00 s), so a = 23.3 cm/s^2.
- Route A (disagrees): I forced the path onto a 3D line fitted through the three given points and placed each frame
  on it by its pixel ray. That gives near-constant speed, a = 6-36 depending on the window. The line misses the given
  depths by 6-9 mm, and the acceleration is very sensitive to mm-level depth changes, so I do not rely on this route.
  The reference uses the measured depth at every frame, which is what Route B approximates.

## Answer
About 26 cm/s^2 (Route B centre; the chord route gives 23). This fits physically: a hollow ball rolling down a board
tilted about 2.5 degrees. Confidence: low to moderate. The result is dominated by how depth changes over time and is
sensitive to mm depth errors; the plausible range is about 20-34.
