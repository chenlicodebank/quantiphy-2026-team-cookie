# q_2170: basketball's distance from the camera at t = 1.2 s

**Answer: 1.564 m.** The depth_info gives this directly ("t=1.2s, distance_ball_camera = 1.5640m"). The measured camera distance is the reference quantity. Time 1.2 s is frame round(1.2 × 24) = 29; the file fps and question_fps are both 24.

## Check (apparent size; f = 0.5959 × 1280 = 763 px)
- Frame 24 (t = 1.0 s): diameter 124.1 px at the given 1.401 m. That implies a real diameter of 0.228 m, which is plausible for a basketball.
- Frame 36 (t = 1.5 s): diameter 113.3 px, so the predicted depth is 1.401 × 124.1 / 113.3 = 1.534 m. The given value is 1.5225 m (0.8 % off), so the size model agrees.
- Frame 29 (t = 1.2 s): diameter about 106–107 px, which predicts about 1.63 m (4 % above the given 1.564 m).
  - This frame is heavily motion-blurred (circle inlier fraction 0.34), and the ball is about to hit the board, so its diameter is unreliable.
  - The 4 % gap is within that uncertainty. I keep the given measured value.

Confidence: high, since the value is given exactly in depth_info.
