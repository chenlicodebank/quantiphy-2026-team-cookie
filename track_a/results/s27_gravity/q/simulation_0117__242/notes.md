# q_242 – height of the door (m)

2D frontal render. The prior is g = 9.8 m/s², which gives the scale from the falling ball.
Time base: question_fps = 24.0 (the file's rate is 24.020228; I used frame indices / 24).

## Scale (measure.py)
- I fitted a quadratic to the ball centre y(frame/24) from scene/tracks/ball.csv over frames 2-18 (unclipped). This
  gives a = 6289 px/s² with an rms residual of 0.19 px. Starting at frame 3 or 4, or using the bbox centre or
  min-circle centre instead, gives 6290-6292. Taking 6290 px/s² → scale = 9.8/6290 = 1.558 mm/px.
- Check: the ball's 45 px diameter is 7.0 cm, which is about a tennis ball (6.7 cm). The scale is consistent.

## Door (edges.py, frame 18; the camera is static)
- Door leaf: the bright top edge line is at y≈374. The leaf bottom is at y≈1837, where a light strip/threshold runs
  down to the floor. That makes 1463 px → 2.28 m.
- Outer casing: the top is at y≈355 and the wall/floor line at y≈1849, so 1494 px → 2.33 m.
- The scene record's bbox (372-1846) is 1474 px → 2.297 m.
- The readings span 2.28-2.33 m. I answer with the middle value of 2.30 m, which is within about 1.5% of either
  reading.

Confidence: the scale is good (<0.5%). The main uncertainty is whether the frame/casing counts as part of the door
(±1.5%).
