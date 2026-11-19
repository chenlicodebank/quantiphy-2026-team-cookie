# q_1589 – speed of the typewriter at t = 0.25 s

The question rate (question_fps) is 24, the same as the file rate. t = 0.25 s is frame 6, and the typewriter is in free fall from frame 0 until it hits the desk between frames 9 and 10. The prior gives the acceleration before 0.45 s as 9.8 m/s² (gravity).

## Method
- I checked the scene/ track (tracks/typewriter.csv) for frames 0–9. It covers the right object. The pixel motion has a nearly constant pixel acceleration of about 9–10.5 px/frame², which fits a uniform fall.
- `fit.py`: fits a quadratic in pixels to y1, bbox_cy and y0. The frame where the speed is zero comes out between −0.3 and −1.0. This route is biased by perspective and by the bbox growing as the typewriter falls.
- `fit3d.py`: a 3D pinhole model. The camera is tilted down by θ and the focal length f is unknown. The origin starts at depth 4.32 m (from depth_info at t = 0) and falls vertically with g = 9.8 m/s² from time t0. The free parameters are f, θ, t0 and the starting pixel height, fitted to frames 2–9.
  - Fit to bbox_cy: f = 2585 px, θ = 15°, t0 = −0.34 frames. Speed at frame 6 = 2.39 m/s.
  - Fit to y1: f = 2748 px, θ = 12.5°, t0 = −0.22 frames. Speed at frame 6 = 2.34 m/s.
  - With t0 fixed at 0, the fits are almost as good (rms 0.4–0.6 px).
  - Check against depth_info: the model's depth at impact (frame 10) is 4.46–4.48 m, which agrees with the given 4.501 m at t = 0.5 s, when the typewriter is on the desk.
- Release from rest at frame 0 is what a Blender rigid-body simulation does: the first frame is the initial state. Under that, p(i) = ½ g (i/24)², and the backward-difference speed at frame 6 is 9.8 × 5.5 / 24 = 2.246 m/s.

## Answer
The speed lies between 2.246 m/s (release exactly at frame 0, the analytic value) and 2.34–2.39 m/s (the fitted t0 a fraction of a frame earlier). The fitted t0 is weakly constrained, so I lean towards the analytic value: **2.27 m/s**. That is within 1% of 2.246 and within 4–5% of the fitted values.

Confidence: good; the answer is within about ±5%.
