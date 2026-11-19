# q_1580 — typewriter speed at t = 0.25 s

Prior: acceleration 9.8 m/s^2 before 0.45 s (free fall). question_fps = file fps = 24, so t = 0.25 s is frame 6.

Method (fit.py): quadratic fits to the pixel track in scene/tracks/typewriter.csv (bottom edge and bbox centre, frames 0-9,
all in free fall; impact is between frames 10 and 11). Pixel accel is about 11.3 px/frame^2 (bottom edge). The velocity reaches
zero at frame 0.00 to -0.25, so the typewriter is released from rest at frame 0 (t = 0).
Bottom-edge steps 6, 18 px for frames 0->1->2 match 0.5a and 1.5a exactly.

Convention: speed = one-frame backward difference of the origin, x fps.
p(i) = 0.5 g (i/24)^2  ->  v(6) = g (36 - 25) / (2*24^2) * 24 = 9.8 * 11 / 48 = 2.246 m/s
(the instantaneous value g*t would be 2.45).

Second route: use the prior's pixel acceleration as the scale (planar approximation). The bottom edge moves 62 px from f5 to f6:
62 / 11.3 * 9.8/24 = 2.24 m/s. Using the bbox centre (55.5 px, 10.4 px/f^2) gives 2.18 m/s. If release happened 0.2 frame
before frame 0, the answer would be 2.33. Answer: 2.246 m/s. Confidence: high (within about 4 pct).
