# Q3227 – ball displacement 0.40–0.50 s

- question_fps = file fps = 30, so the interval runs from frame 12 to frame 15.
- The prior (g = 9.8 m/s²) gives no usable scale. The camera looks straight down and the ball rolls horizontally across the
  floor, so gravity acts along the line of sight. I took the scale from a regulation size-7 basketball instead, diameter
  0.2386 m (29.5 in circumference).
- Ball pixel diameter: 255.6 px. This is the mean vertical extent, across the motion so it is not blurred, over frames
  10–17. I checked it by eye on frame 15 (y ≈ 293 to 550). Scale = 9.334e-4 m/px.
- Displacement: the camera-stabilised centroid moves 292.4 px from frame 12 to frame 15 (raw image: 291.1 px).
  292.4 px × 9.334e-4 m/px = **0.273 m**.
- Second route: the mean step over frames 9–18 is 97.6 px/frame, which gives 292.9 px over 3 frames, or 0.273 m.
- Confidence: the pixel measurement is good (±1%). The main uncertainty is the ball's real size: a size-6 ball (0.232 m)
  would give 0.265 m.
- Script: measure.py, using the centroids from scene/tracks/basketball.csv. I checked frames 12 and 15 visually.
