# q_2408: book velocity at t = 1.4 s (cm/s)

The file rate and question_fps are both 24, so t = 1.4 s is frame 34 (round(33.6)). Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## What happens around frame 34 (frames/seq.png, frames/z*.png)
- The book slides down the ramp from f21 and reaches the ramp foot at f30.
- f31-33: it tips off the foot and lands on the table.
- f33-36: it keeps sliding toward the camera on the table, then stops at f37.
- While it slides on the table, its right end stays at x ≈ 654 (close to cx), and its left end and bottom contact line move out from the principal point:

  | frame | left end x | bottom y |
  |---|---|---|
  | 33 | 492 | 496 |
  | 34 | 490 | 502 |
  | 35 | 484 | 507.5 |
  | 36 | 480 | 512 |
  | 37 and later (rest) | 476.5 | 512 |

  This is a clean scale-up, which means the book is approaching the camera.
- So at 1.4 s the book is decelerating on the table, and the prior (|a| = 2.8 m/s²) fits friction-type deceleration.

## Depth series
- On the ramp: Z = K / (long-axis pixel length), with K set so that Z = 1.02 m at f29, which is the given value.
- On the table: Z = 0.851 x (rest pixel scale / frame pixel scale), using the left-end and bottom-line scales averaged. This gives Z34 ≈ 0.916, Z35 0.883, Z36 0.859, Z37 0.852.
- Conflict: the given depth at 1.4 s is 0.857, but the image scale puts the book about 6% farther away at f34. The given value matches about f35.7 in my series. The reference's own depth series evidently has the book close to its rest depth already by f34.

## Velocity (reference convention: 3D centres back-projected, positions smoothed, forward difference) — vel.py, vel2.py
| depth series | 5-frame smoothing | 7-frame smoothing |
|---|---|---|
| my image-scale depths | v34 = 0.52 m/s, \|a\| = 2.82 (matches the prior) | 0.44 m/s |
| linear through the given depths (1.02 at f29, 0.857 at f34, 0.851 at f38) | 0.355 | 0.37, \|a\| = 2.6-2.75 (close to the prior) |
| constant speed until f34, then rest | 0.33 | 0.356, \|a\| = 2.9 |

The prior's acceleration can be reproduced both with v ≈ 0.36-0.37 (series honouring the given depths) and with v ≈ 0.52 (my depths). I answer 0.40 m/s, weighted toward the series that honours the reference's own depth at 1.4 s.

## Answer
**40 cm/s**

Confidence is low to moderate. The answer depends on smoothing across the landing and on depth values that conflict with each other; the plausible range is 33-52 cm/s.
