# q_662: acceleration of the vacuum cleaner at t = 1 s

- The file runs at 24 fps and question_fps is also 24, so t = 1 s is frame 24.
- Acceleration = (speed(24) - speed(23)) x fps, where speed(i) = |p(i) - p(i-1)| x fps.
- The scene is a 2D top-down view with a static camera. The only mover is the round robot vacuum.

## Scale
- The prior is diameter = 0.438 m.
- The rim circle fit (scene track) gives an apparent diameter of 121.5 px at frame 24. The diameter ranges from 120.7 to 122.9 px along the path, a 1.7% variation.
- Scale = 0.438 / 121.5 = 0.003605 m/px.

## Motion
- The raw one-frame steps are too noisy to difference directly: about 0.3 px of noise against a step change of only about 0.2 px.
- So I fitted smooth polynomials to x(f) and y(f) and differenced the fitted positions with the benchmark convention. Degrees were 3 to 6, over windows from 18-30 up to 8-38 (`fit.py`).
- Route 1, the scene/ rim circle-fit track: Δspeed(24-23) = 0.19-0.22 px/frame², most fits 0.20-0.21. Fit residuals are about 0.03 px.
- Route 2, an independent soft-mask intensity centroid of the bright disc (`cent.py`, frames 6-34): windows that stay out of the sunlit patch give 0.20-0.21 px/frame². Frames 32 and later are biased by the sunlight.
- I also tried masked template matching (`tm.py`). I rejected it because it drifts by 2 px with the shading on the vacuum's top.
- Adopted value: 0.207 px/frame² (speeds about 20.07 to 20.28 px/frame).

## Answer
a = 0.207 x 24² x 0.003605 = 0.43 m/s²

Confidence: moderate. The acceleration is small because the speed is near its peak (frame 26). The fit spread is about ±7%, and the choice of scale adds about ±1%.
