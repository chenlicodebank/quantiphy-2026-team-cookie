# q_359 – turtle speed at t = 1 s (frame 24)

2D scene, 24 fps (file fps = question_fps, so no re-timing). Both animals swim leftward in planes facing the camera,
the camera is static, and nothing is in front of them. One metres-per-pixel scale comes from the prior (shark speed 7 m/s).

## Measurements (track.py, track2.py)
- Shark: I template-matched the front body region (dorsal fin and gills), frame to frame, over frames 14–30. The speed is
  58.3–59.7 px/frame, mean 59.2 px/frame. A fixed frame-24 template gives 59.3 px/frame over frames 17–30. The record's mask
  centroid gives 58.0 and the tail tip about 57; both are biased by the tail wagging.
  Scale = 7 / (59.2 x 24) = 0.00493 m/px.
- Turtle: I template-matched the shell frame to frame. Frame 24 (backward difference) = 22.3 px/frame. The mean over
  frames 22–26 is 21.8 px/frame, and a fit over frames 19–34 gives 21.7 px/frame. I used 21.8 px/frame.
- Speed = 21.8 / 59.2 x 7 = 2.58 m/s.

## Second route
Using the mask centroids from the scene record instead: turtle 20.9–21.2 px/frame and shark 58.0 px/frame give 2.53–2.56 m/s.
With the raw single-frame turtle value (22.3 px/frame) the answer is 2.64 m/s. The routes agree to within about 3%.

Confidence: good. The answer should be within about 4%.
