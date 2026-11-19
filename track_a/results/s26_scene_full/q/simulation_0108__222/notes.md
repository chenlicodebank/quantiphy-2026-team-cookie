# q_222 – distance between the two viruses at t = 1.0 s (frame 24)

The prior is the left virus (A) speed, 1.7393 m/s. There is no depth_info. fps = question_fps = 24, so t = 1.0 s is frame 24.

## Observations
- Centres come from the scene/ tracks (template matching, ±0.05 px per frame). At frame 24, A is at (713.24, 295.00) and B at (1622.76, 598.90).
  The pixel distance between them is 958.9 px. f24.png shows that both viruses are fully visible.
- A is not moving in the image plane. Its size grows by about 4–5% over frames 2–27, its pixel speed grows (11.48 → 12.4 px/frame), and it drifts
  away from the image centre. All three point to a 3D motion toward the camera.
  A projective model of uniform 3D motion, p(n) = (P0 + Q n)/(1 + w n), fits A's track over frames 1–45 with an rms error of 0.06 px.
  It gives w = -0.00142 per frame, i.e. A moves toward the camera. The body-size growth gives a similar value, -0.0018.
  The 3D speed is therefore constant, which matches a single "speed" prior.
- B moves at a constant pixel velocity and its size stays constant, so its depth is constant.

## Method (fit.py)
- I assume that A and B start at the same depth Z0. I back-project A as ((u-cx)/f, (v-cy)/f, 1) x Z0(1+w n) and B at depth Z0.
- Z0 is set so that A's 3D per-frame speed equals 1.7393/24 m.
- The focal length cannot be found from this video. The result depends on f as follows:
  f = 800 px → 5.93 m, 1200 → 5.90, 1600 → 5.85, 2000 → 5.80, 2667 (Blender default 50 mm) → 5.68, 3500 → 5.51.
- Check by a second route, the planar 2D convention with one scale from A's pixel speed: using the speed at frame 24 gives 5.66 m,
  and using the mean speed over frames 1–24 gives 5.84 m.

## Answer
5.75 m. This is the middle of the 3D estimates for plausible focal lengths and of the planar estimates.
Confidence is moderate, about ±4%. The main uncertainties are the unknown focal length and the assumption that A and B start at the same depth.
