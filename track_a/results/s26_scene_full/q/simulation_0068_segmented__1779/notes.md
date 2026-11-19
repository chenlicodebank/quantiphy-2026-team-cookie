# Q1779 – average speed of the yellow car (m/s)

- 2D top-down simulation at 24 fps (the file's fps and question_fps are the same), 72 frames. "Yellow car" = the beige/tan car (scene's beige_car). "White car" = the white van that drives straight up from rest.
- Script: `measure.py`. It re-segments every frame (non-white mask, morphology, filled contours larger than 3000 px), then takes the centroid of each car.
- Scale from the prior (white car a = 4 m/s²):
  - A quadratic fit of the van's y(t) gives |a| = 160.8 px/s² (160.9 px/s² when fitted from frame 10 on).
  - Route 2: the slope of the per-frame speed against time gives 160.4 px/s².
  - Scale = 4 / 160.8 = 0.02487 m/px. Sanity check: the van is 240 px ≈ 6.0 m and the car is 223 px ≈ 5.5 m, plausible sizes.
- Yellow car: the mean of the per-frame speeds |p(i) - p(i-1)| x 24 over frames 1–71 is 161.36 px/s. After Savitzky-Golay smoothing (window 9, order 2) it is 161.40 px/s.
  - This gives 4.013 m/s raw and 4.015 m/s smoothed. Excluding the first step (the car is still starting) gives 4.05 m/s.
- The scene record agrees: path 477.4 px over 71 steps = 161.4 px/s.
- Answer: **4.01 m/s**. Confidence high (about ±2%).
