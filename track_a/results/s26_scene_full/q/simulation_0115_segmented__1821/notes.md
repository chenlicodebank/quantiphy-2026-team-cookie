# Q1821: velocity of the boat at 1 s (prior: acceleration of the boat = 3 m/s^2)

2D top-down video at 24 fps, which matches question_fps, so no re-timing. The boat moves left (-x) with no y-motion or rotation, and the camera is static.
Scale comes from the prior's own quantity, the pixel acceleration: m/px = 3 / a_px. That makes v(1 s) = 3 x v_px(1 s) / a_px, which depends
only on the ratio v/a in pixels.

## Route 1: scene record mask centroids (fit.py)
Quadratic fit of x(t) over frames 0-36: a = 138.5 px/s^2 and v(1 s) = 236.7 px/s, giving v = 5.13 m/s. The backward-difference
convention (frames 23 to 24, i.e. t = 23.5/24 s) gives 5.06 m/s. Sub-windows give 5.05-5.45 m/s.

## Route 2: my own template matching with sub-pixel peaks (track.py)
Using the full frame-0 boat template:
- frames 0-36: a = 136.8 px/s^2, v(1 s) = 235.3 px/s, giving 5.16 m/s (backward difference 5.10 m/s)
- frames 0-18: 5.20 m/s

The second half alone gives a slightly lower a (130 px/s^2). That is consistent with noise or edge blur at higher speed.
The fitted v0 is about 2.16 m/s.

## Answer
5.1 m/s, a compromise between the backward-difference values (5.06-5.10) and the instantaneous fits (5.13-5.16).
If the true v0 is exactly 2 m/s, the reference would be 4.94-5.0. Confidence: within about 5%.
