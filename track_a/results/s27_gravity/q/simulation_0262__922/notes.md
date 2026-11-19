# Q922: speed of the red cup at t = 0.25 s (frame 6 at 24 fps)

The video is 2D, 24 fps (the file rate and question_fps are the same). The prior is a = 9.8 m/s^2 before 0.75 s (free fall, frames 2–18).

Method (`measure.py`): background = frame 0. The red body is found with HSV saturation > 90, which gives its bottom edge. The diff mask gives the top edge.
Quadratic fits of y(t) over the airborne frames give the pixel acceleration. Speed is the backward difference at f6, converted with
scale = 9.8 / a_px.
- Bottom edge, f6–18: a = 6540 px/s^2, v(f6) = 2.14 m/s
- Top edge, f6–18: a = 6102 px/s^2, v = 2.53 m/s (the top and bottom routes differ because the apparent height shrinks with perspective)
- Midpoint (origin proxy), f6–18: a = 6321 px/s^2, v = 2.33 m/s, residual 0.6 px
- Bottom edge, f2–18: a = 6443 px/s^2, v = 2.21 m/s. The raw backward difference (62 px) gives 2.23 m/s.

Second route: the bottom-edge fit puts v = 0 at t = 0.003 s, and the midpoint fit at about -0.008 s. So the cup is released from rest at t = 0.
With a = 9.8 exactly, the backward difference at f6 is g·(6² − 5²)/(2·24) = 9.8·11/48 = 2.246 m/s.
This matches the measured routes (2.21–2.33).

Answer: 2.25 m/s. Confidence: high (within about 4 pct).
