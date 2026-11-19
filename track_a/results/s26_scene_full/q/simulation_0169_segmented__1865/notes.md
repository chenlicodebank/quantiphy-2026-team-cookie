# q_1865: acceleration of the astronaut at t = 3 s

- 2D segmented render. fps = question_fps = 24, so t = 3 s is frame 72. The astronaut is the only object; it rises up the image with a slow clockwise tilt and comes to rest at f78.
- Scale: the prior is height = 2.2 m. At f0-f3 the figure stands upright (tilt about 4°). Its pixel height is 90-91 px at mask thresholds 200-240 (`height.py`), so I use 90.5 px, which gives 0.02431 m/px.
- Motion (`fit.py`, on the scene/ centroid track): cy(f) fits a Blender ease-in/ease-out curve (smoothstep 3u²-2u³) closely, with rms 0.20 px. The fit runs from f = -0.4 to f = 78.3, with D = 274.7 px. The path-distance fit gives the same result (-0.3 to 78.2, 274.4 px).
- Acceleration as the benchmark defines it, speed(72) - speed(71) = y''(71) for a cubic:
  - y-curve fit: -0.217 px/frame²
  - path-distance fit: -0.218 px/frame²
- Second route: local quadratic fits to the raw track around f72, with half-windows of 4-7 frames, give 0.211-0.226 px/frame². If the keyframes sit exactly at f0 and f78, the result is 0.222.
- Result: 0.218 px/frame² × 576 × 0.02431 m/px = 3.05 m/s². This is a deceleration; the answer is given as its magnitude.
- Confidence: good. The scale uncertainty is about 1-2 % and the acceleration uncertainty about 3 %.
