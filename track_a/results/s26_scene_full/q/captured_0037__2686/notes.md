# q_2686: speed of the ping pong ball at t = 1.4 s (cm/s)

File fps = question_fps = 24, so t = 1.4 s is frame round(33.6) = 34. Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Track
The scene/tracks/ball.csv centroids were checked against my own re-measurement (measure.py: background-difference mask
at 0.3 x peak contrast). The two agree to about 1 px in frames 29-35. Frames 29-35 are a single free-flight arc,
between bounce 2 (tape roll, frame 28) and bounce 3 (jar, frame 35-36). At frame 34 the ball is falling: pixel
velocity is about (-14.2, +16.8) px/frame at frame 34 and (-15.2, +22.5) for the raw forward difference 34->35.

## Depth
depth_info gives a range of 1.055 m at t = 1.0 (frame 24). Evidence that the ball's depth stays near 1.05 m up to
frame 36:
- At frame 28 it bounces on top of the tape roll (tape centre at 1.038 m, roll about 10 cm across: 72 px x 1.038 / 763).
- At frames 35-36 the jar lid hides the top of the ball, and the ball then bounces on the table behind the jar
  (jar at 1.008 m, about 7.5 cm wide). So the ball is at about 1.04 m or more there.
- The apparent diameter rises from about 26 px to about 29-31 px (vertical profiles at the apex frames,
  profile.py), which would mean about 10 % closer. This conflicts with the occlusion evidence, and the measurement
  is unreliable (dark tripod pole behind the ball at frame 24, shading, blur). I used Z ≈ 1.045 m at frame 34 and
  treated motion along the depth axis as negligible. Between 1.03 and 1.06 m the result changes by only ±1.5 %.

## Speed (velocity.py)
- Route 1: fit a line to x and a parabola to y over frames 29-35 (also 30-35 and 29-34), take the instantaneous
  velocity at frame 34, and scale by Z / f: 70.5-74.6 cm/s. The fitted g ≈ 8.0-8.7 m/s² is a plausible sanity check.
- Route 2: the reference convention, a forward difference smoothed over 5 frames. A centred 5-frame moving average
  gives (P37 - P32) / 5 = (-19.1, +9.4) px/frame, which is 70.1 cm/s.
- For comparison only: the raw unsmoothed forward difference 34->35 gives 83-89 cm/s. The instantaneous value at the
  exact time t = 1.4 s (frame 33.6) is about 63 cm/s.

Answer: **72 cm/s**. Confidence is moderate. The main uncertainty is the smoothing convention, because the speed
changes quickly near the bounce. Depth adds about ±3 %.
