# q_2496 — tennis ball velocity at t = 1.6 s (cm/s)

t = 1.6 s → frame round(1.6 × 24) = 38 (question_fps = file fps = 24). The ball is in its rebound phase (it hit the board at frame 30, t = 1.24 s), moving left and back toward the camera.

## Method (lab method card)
- f = 0.5959 × 1280 = 762.75 px, cx, cy = 640, 360.
- Ball centres come from scene/tracks/ball.csv. These are circle fits to the HSV mask, ±1 px in frames 24-48. The track agrees with the frames.
- Depth comes from depth_info: 1.144 m at frame 30 and 1.027 m at frame 38, interpolated linearly per frame (−14.6 mm/frame).
- Each 3D centre is the back-projection ((u−cx)/f, (v−cy)/f, 1)·Z. Speed is the forward difference × 24, smoothed over 5 frame steps (36→41).
- Image motion near frame 38 is about −10.3 px/frame in x and +0.5 px/frame in y.

## Results (measure.py)
- Route A (given depths): per-frame speeds 36..40 are 49.6, 46.7, 49.6, 45.6, 47.0 cm/s, mean 47.7. A linear fit of position over frames 36-41 gives |v| = 47.6 cm/s (vx −32.1, vy −2.2, vz −35.1).
- Route B (a second check, with depth taken from the trend in apparent size): Z ∝ 1/diam, using a linear fit of the circle-fit diameter over frames 31-48, scaled so that Z(38) = 1.027 m. This gives 44.0 cm/s. It is lower because the apparent size suggests a slightly slower approach (−1.2 %/frame against −1.4 %/frame).
- The scene record notes a possible dropped capture frame between frames 35 and 36. If it is counted, the depth rate becomes 9 intervals instead of 8 and the speed is about 44.8 cm/s. The smoothing window 36-41 avoids the 35→36 jump itself.

## Answer
47 cm/s (route A, which follows the reference convention of using the given depths). Confidence: moderate, ±7 %.
