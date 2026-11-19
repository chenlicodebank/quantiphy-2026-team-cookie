# q_2561 – ping pong ball velocity at t = 0.5 s (cm/s)

File fps = question_fps = 24; t = 0.5 s -> frame 12 (ball falling after the first apex, just before the
first bounce at frame 14). Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Measurements (scene/tracks/ball.csv checked on zoomed frames 11-13; fit.py)
- Vertical centroid cy, frames 9-14: 181.4, 192.6, 213.9, 288.6, 342.6, 405.4 -> steps 11, 21, **75**, 54, 63.
- The 75 px step is two frames of free fall: a parabola with one dropped frame between index 11 and 12 fits
  frames 8-14 with residuals < 0.6 px (without the drop: residuals ~14 px). Pixel acceleration 10.53 px/frame^2.
- Depth near frame 12, two independent routes:
  * gravity: Z = g f / a_px = 9.81/576 x 763 / 10.53 = 1.23 m
  * ball size: minor extent ~25.3 px (f8-13) -> Z = 763 x 0.04 / 25.3 = 1.21 m
- The given depth 1.457 m at t = 0.9 s (frame 22) contradicts the ball's 32 px size there (-> 0.94 m); the
  0.738 m at t = 1.4 s agrees within 5 pct with size (0.78 m). The 0.9 s value looks like a sensor error on a blurred
  moving ball (it mixes with the background).
- The ball also comes toward the camera during the flight (size 25.9 -> 31.6 px, f8 -> f20): ~0.4 m/s along depth.

## Velocity at frame 12
- Physical (real time, dropped frame accounted for): vertical 47.9 px/frame -> 1.84 m/s; with depth component ~1.88 m/s.
- Per frame index the way the reference does it (forward difference y13 - y12 = 54 px/frame, Z 1.21 m): 2.04 m/s
  vertical, ~2.08 m/s with the depth component.
- Same thing with the given 1.457 m depth: ~2.5 m/s.
Answer: 220 cm/s. This is a hedge in favour of the index-based reference convention (2.1-2.5 m/s), with the
physical 1.9 m/s as the lower bound.

Confidence: moderate (the answer depends on which depth and time base the reference used; spread ~ +/-15 pct).
