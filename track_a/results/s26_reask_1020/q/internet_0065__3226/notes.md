# q3226 – displacement of the ball, 0.30 s to 0.40 s

- Time base: question_fps = 30, which is also the file's rate. 0.30 s is frame 9 and 0.40 s is frame 12.
- Scale: the prior (gravity 9.8 m/s^2) gives no usable scale. The camera looks straight down and the basketball rolls
  horizontally across the floor at a constant pixel speed, so there is no vertical acceleration to use. I took the
  scale from the ball's own size instead: a regulation basketball (size 7) is 0.24 m across.
  - Ball diameter in these frames is about 255 px. That is the vertical extent across the motion, so it has no blur: 255
    in the record's bbox_h for frames 9–12, and 252–253 in my own mask (check.py).
  - Scale = 0.24 / 255 = 9.41e-4 m/px.
- Positions are mask centroids, from a Lab mask with a > 136 combined with the difference from ball-free frames 0 and 30.
  I checked the overlay in frames/check12.jpg.
  - Frame 9: (555.3, 399.5). Frame 12: (847.9, 411.5). The record gives (555.3, 399.6) and (846.7, 411.8).
  - Displacement = 292.9 px raw. Against the background (stabilised track) it is 292.9 px, because the camera drift
    over these 3 frames is only about 1 px in x and 6 px in y.
- Result: 292.9 px x 9.41e-4 = 0.276 m. I answer **0.275 m**.
- Second-route check: the per-frame step over frames 5–21 averages about 98 px. Three steps make 294 px, which agrees.
- Sensitivity: if the ball is size 6 (0.232 m), the result is 0.266 m. If the diameter is taken as the blurred length
  (about 262 px), it is 0.268 m.
- Confidence: moderate-high. The main uncertainty is the assumed real size of the ball.
