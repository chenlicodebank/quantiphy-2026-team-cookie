# Q1386 – speed of the bowling ball at t = 0.5 s (frame 12 at 24 fps; file fps = question fps = 24)

Prior: ball diameter 0.21 m; depth_info: camera→ball-centre distance 9.391 m at t = 0.5 s.

Ball track: scene/tracks/ball.csv (circle-fit centres and diameters). I checked it on a zoomed crop of frame 12:
the ball spans x 400-481, y 601-686, which matches cx 440.4, cy 642.6, diam 82.1.

## Route 1 – 3D trajectory fit (fit3d.py)
Pinhole camera with the principal point at the image centre. Unknowns: f and the 3D position and velocity
(plus acceleration for the order-2 fit). The fit uses the u and v centres and the projected sphere diameter
(off-axis ellipse), with |P(12)| fixed to 9.391 m.
- f ≈ 3600-3660 px (HFOV ≈ 29.5°). Frame 12's smoothed diameter alone gives f = 3663.
- Constant velocity: 3.97-4.07 m/s, but the diameter residuals are high (1.57 px over frames 6-37).
- Constant acceleration: 3.81-3.86 m/s at frame 12 (diameter rms 0.6-0.7 px). The ball slows down toward impact.

## Route 2 – vanishing-point line (vp_route.py)
The motion direction is the lane vanishing point (5680, 205) back-projected with f. Each position is the
3D line through P12 intersected with that frame's ray. Depth therefore does not depend on the noisy diameters.
- Smoothed speed at t ≈ 0.5 s: 3.77-3.85 m/s across f 3600-3663 and the VP uncertainty.
- The raw single-frame difference (frames 11→12) is 3.90-3.97, which is noisy.
- Speed falls to about 3.35-3.4 m/s just before impact (frame 37).

## Answer
3.82 m/s: the smoothed backward-difference speed at frame 12, where both routes agree.
Confidence: about ±4%.
