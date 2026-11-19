# Q976: raccoon displacement from 0.5 s to 1.0 s

- The video is a 2D top-down render at 24 fps; question_fps is also 24. The camera is static, according to the scene record. The question times map to frames 12 and 24.
- **Scale:** the prior gives the raccoon length, tail included, as 1.51 m. The nose-to-tail-tip bbox width has a median of 295 px over frames 2–71. I checked it by eye at frame 24: the tail tip is at about x 1077 and the snout tip at about x 1365, so about 290 px. That gives 0.005119 m/px.
- **Displacement, route 1:** the mask centroid moves 248.3 px from frame 12 to frame 24. The tail tip moves 248 px and the snout tip moves 248 px, so the route is consistent.
- **Displacement, route 2:** a linear fit of the centroid x over frames 6–30 gives 20.43 px/frame. Over 12 frames that is 245.2 px, or 1.255 m.
- **Answer:** 248.3 px × 0.005119 = **1.271 m**.
- **Confidence:** about ±3%. The main uncertainty is the pixel length (±5 px).
- **Script:** `measure.py`.
