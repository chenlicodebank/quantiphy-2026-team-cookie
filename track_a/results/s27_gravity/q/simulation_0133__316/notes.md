# q316: height of the table (simulation_0133)

Prior: g = 9.8 m/s^2. No depth_info. File fps = question_fps = 30.

## Method (fit.py)
- The apple rolls off the counter ("table") and falls freely in frames 35-47 (it hits the floor at frame 48).
  A quadratic fit to the apple's centroid y over several windows (35-47, 36-47, 37-47, 38-47, 40-47, 36-44) gives
  a pixel acceleration of 6361-6398 px/s^2 (rms 0.12-0.19 px). I used **6363 px/s^2**, so the scale is 9.8/6363 = 1.540e-3 m/px
  in the apple's plane of motion.
- Table height = the vertical drop of the apple's centre from rolling on the table top to rolling on the floor, measured
  in the same plane. I used the mask's top edge (y0) to avoid the occlusion behind the counter's front edge and the shadow
  at the floor: median y0 is 852-854 on the counter (frames 27-33) and 1492 on the floor (frames 52-80), so the drop is 640 px.
- H = 640 x 1.540e-3 = **0.986 m**.

## Check
- Perspective consistency: the counter's front face spans y 907-1663 (756 px). The apple's plane spans 915-1555 (640 px),
  so it lies 1.18x deeper. Solving for the horizon from both edges gives y ≈ 960, which is exactly the image centre.
  That fits a level camera, so the measurement in the apple's plane is consistent.
- Plausibility: the apple diameter is 62 px, or 9.5 cm, which is a realistic apple. A table/counter height of about 0.99 m is realistic.
- Uncertainty: about ±2 px in the drop and ±0.5% in the acceleration, so about ±1%.
