# Q3215 – ball velocity at 3.6 s (internet_0064)

Time base: file fps = question_fps = 30, so t = 3.6 s is frame 108. The ball is in its first free flight (frames 81–113, released at about 80/81, bounces at 114).

Scale comes from the prior, g = 9.8 m/s². The pixel acceleration of the ball's centre comes from quadratic fits to cy(t) in scene/tracks/ball.csv (the circle-fit centre, checked by overlays in the record):
- flight 1, frames 81–113: 3539 px/s² (raw) / 3546 (camera-drift-corrected); frames 84–110: 3539
- flight 2, frames 116–143: 3531 / 3558
- I used g_px = 3540 px/s², so the scale is 9.8/3540 = 0.002768 m/px.
- Sanity check: the ball's 85 px diameter comes out at 0.235 m, about the size of a basketball.

Velocity at frame 108 (px/s), from fit.py and fit2.py:
- forward difference p(109) − p(108): (810, 1734), so |v| = 1914 (bg coords: 1932)
- central difference: 1870 (bg: 1876)
- local quadratic fits over frames 98–113 give an instantaneous value at t = 3.6 of 1878–1882 px/s, and 1928–1932 at t = 3.6167 (the forward-difference midpoint)
- global flight-1 fit: 1921

Answer: about 1905 px/s (between the forward-difference and instantaneous values), times 0.002768, which is **5.28 m/s**. The range across routes is 5.18–5.35 m/s.
Confidence: good (±3%). Late in flight 1 the y residuals show a small systematic wave of ±3 px, probably from motion blur or a slight change in depth.
