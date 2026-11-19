# q_454 – truck speed at t = 1 s (frame 30)

2D sim, 30 fps (file fps = question_fps, no re-timing). Prior: truck acceleration 10.757 m/s^2 (constant).
Scale comes from the prior: m/px = 10.757 / (pixel acceleration).

Speed is wanted at frame 30 as a one-frame backward difference, so the answer is
v = 10.757 * (dx(30) * 30) / (slope * 900), where dx is the pixel shift per frame and slope is dx's change per frame.
That ratio is in seconds; it equals 29.5/30 if the truck starts from rest at frame 0.

## Route 1 (scene track, fit.py)
I fitted a straight line to dx_from_prev_px from scene/tracks/truck.csv over several frame windows:
- 15-54: slope 2.043 px/frame^2, v = 10.56
- 20-45: v = 10.51
- 25-40: v = 10.66
- 36-50: v = 10.53

A quadratic fit to the positions over frames 14-55 puts the vertex (start from rest) at about frame 0.07 and gives v = 10.55 m/s.

## Route 2 (independent, check.py)
I matched column profiles of the gradient inside the foreground mask (band y 400-850) between consecutive frames, at
whole-pixel steps. Over frames 21-49, dx rises from 42 to 99 px (slope about 2.0-2.04), with the start of motion at about
frame 0-1, which agrees with route 1. Frames 50-51 are outliers because the truck is leaving the frame.

## Answer
If acceleration is constant from rest at frame 0, the analytic value is 10.757 * 29.5/30 = 10.58. The measured values are
10.51-10.66. Answer: 10.56 m/s. Confidence: high (within about 1-2 %).
