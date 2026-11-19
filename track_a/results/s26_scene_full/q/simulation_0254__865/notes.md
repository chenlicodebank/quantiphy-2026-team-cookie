# Q865: speed of the tennis ball at t = 1.5 s

- fps = question_fps = 24, so t = 1.5 s is frame 36. Speed is the backward step from frame 35 to 36. The prior is a ball diameter of 0.17 m. This is a 2D scene, so one metres-per-pixel scale is used.
- **Track:** scene/tracks/ball.csv (mask centroid). I checked it with my own HSV masks at several thresholds in measure.py, and the centroids agree within about 0.5 px. The ball rolls down the 44° ramp from frame 19 to 47.
- **Pixel step at frame 36:**
  - The raw step is 55.2 px. Neighbouring steps are 53.6 (frame 35), 55.8 (37) and 57.1 (38).
  - Local linear fits of step against frame (windows 29-43, 31-41, 32-40, 33-39) give 54.6-54.8 at frame 36.
  - Local quadratic fits of path position give 54.7-54.8.
  - A global quadratic over frames 19-47 gives 54.4, but it has a 1.7 px residual: the acceleration is not quite uniform.
  - Value used: **54.7 px/frame**.
- **Pixel diameter (diam.py):**
  - Method: subtract frame 0 as background (the ball is out of view then) and threshold the difference at half of the ball-interior level.
  - Equivalent-circle diameter is 24.2-24.6 px over frames 32-40, 24.2 at frame 36. A soft-alpha area gives 24.4 px.
  - The 30% threshold gives 26.5 px, which includes the blur halo and shadow. The 70% threshold gives 21.7 px, which is too tight.
  - On an 8x zoomed crop of frame 36 the ball reads about 23.8 px wide and 24.4 px tall.
  - Value used: **24.3 px**, so the scale is 0.17/24.3 = 0.00700 m/px.
- **Speed:** 54.7 × 0.00700 × 24 = **9.18 m/s**.
- **Second route:** the raw step of 55.2 px gives 9.27 m/s. The scene record's diameter of 23.5 px would give 9.5 m/s.
- **Confidence:** the main uncertainty is the pixel diameter, about ±4%.
