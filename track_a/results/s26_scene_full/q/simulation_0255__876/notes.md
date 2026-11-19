# Q876: acceleration of the tennis ball at t = 1.5 s (frame 36)

- fps = question_fps = 24, so there is no retiming. This is a 2D-style clip: the ball rolls right along a constant image row
  (y ≈ 562.6), so its depth is constant and one m/px scale applies.
- Track: scene/tracks/ball.csv (chroma centroid, jitter about 0.2 px). I checked it against the frames. The per-frame dx falls
  smoothly from 43.8 to 33.6 px, with no bounce.
- Pixel acceleration (measure.py): quadratic fits of x(frame) over frames 0–40, 10–40, 20–40 and 26–40 give
  −0.2661, −0.2653, −0.2638 and −0.2664 px/frame². A cubic fit evaluated at frame 36 gives −0.2627. The deceleration
  is uniform. I used a = 0.265 px/frame² = 152.6 px/s².
- Diameter (measure.py, background-difference profiles at the half-maximum crossing, frames 10–40): horizontal
  23.1–23.6 px, vertical 23.5–24.2 px (the vertical value includes a little contact shadow). The equivalent diameter of a
  thresholded mask is 24.4–24.8 px, which is looser and includes the shadow and rim blur. Best estimate: 23.6 px.
- Scale = 0.17 / 23.6 = 0.00720 m/px. Acceleration = 152.6 × 0.00720 ≈ 1.10 m/s² (magnitude; the ball is decelerating).
- Second route: a cubic fit (local value at frame 36) gives 1.09 m/s². Using the record's 24.5 px diameter gives
  1.06 m/s². The uncertainty is about ±4%, and it comes mainly from the pixel diameter.
