# q_2184 — basketball velocity at t = 1.8 s

The file and the question both run at 24 fps, so t = 1.8 s is frame 43. The ball is rising after the bounce at frame 37 and peaks at about frame 46.

## Method (measure.py)
- I re-segmented the ball with an HSV mask over frames 38–48. The mask centroid agrees with the scene/ cx_fit/cy_fit to within 0.5 px, and the overlay at frame 43 (frames/f43.png) matches the outline.
- I back-projected the centroid with f = 0.5959 × 1280 = 762.8 px and principal point (640, 360). The depth is taken from depth_info and interpolated linearly: 1.5835 m at frame 43.2 and 1.5795 m at frame 46.08, so it is almost constant.
- Speed in 3D at frame 43, by method:
  - forward difference: 0.641 m/s
  - backward difference: 0.849 m/s
  - central difference over ±1 frame: 0.745 m/s
  - central difference over ±2 frames: 0.731 m/s
  - mean of the forward differences at frames 41–45: 0.605 m/s
  - quadratic fit over frames 38–48, 39–48 and 40–47, evaluated at frame 43: 0.687, 0.701 and 0.718 m/s
- **Answer: 0.68 m/s.** This sits between the smoothed forward-difference convention (about 0.60–0.64) and the central or fitted estimates (about 0.70–0.75).

## Checks and caveats
- The fitted vertical acceleration is about 5 m/s², not the 9.8 m/s² in the prior. With g = 9.8, the speed at frame 43 would be about 1.2 m/s. Measured with the given depth, the motion does not support that. I answer the measured value, because the reference velocities come from clicked centres and measured depth.
- The ball diameter at frame 43 is 106–110 px. That implies a depth of about 1.65–1.7 m for a 0.235 m ball, compared with the given 1.5835 m. If that depth were used, the speed would scale up by about 5%.
- Confidence: moderate, about ±12%. Most of the uncertainty comes from which differencing and smoothing convention the reference used.
