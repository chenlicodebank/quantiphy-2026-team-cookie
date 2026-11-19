# q_2401: ping pong ball velocity at 0.8 s (cm/s)

The file runs at 24 fps and question_fps is also 24, so t = 0.8 s is frame 19. Depths are given at frames 14, 19 and 29 (1.751, 1.687 and 1.526 m).

## Method (vel.py)
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Ball centre: taken from scene/tracks/ball.csv (mask centroid `cx,cy`; the bbox-based `cx_box,cy_box` was also tried). The track is smooth and moves about 4 px per frame on frames 13–30.
- I back-projected the centre at frames 14, 19 and 29 using the given depths. The three 3D points are almost collinear (residual singular value 4 mm), which fits a ball rolling in a straight line. I fitted a 3D line to them.
- For every frame, the position is the point on that line closest to the camera ray through the tracked centre. This reproduces the given depths as 1.756, 1.680 and 1.528 m, against the given 1.751, 1.687 and 1.526.
- Speed at frame 19: from a linear fit of position over ±2, ±3 and ±4 frames I get 41.6, 42.1 and 41.7 cm/s with the centroid track, and 43.4, 44.3 and 42.5 with the bbox track. The mean forward difference over frames 19–23 is 41.7 cm/s (both tracks), and 41.2 over frames 17–21.

## Second route (depth values alone)
- The chord from frame 14 to 19 gives 7.5 cm in 5 frames, i.e. 36.1 cm/s. The chord from frame 19 to 29 gives 18.25 cm in 10 frames, i.e. 43.6 cm/s.
- Interpolating to frame 19 gives about 38.6 cm/s. The gap from the image route comes from the 14→19 depth step (64 mm), which is about 12 mm shorter than the image track implies. That is within plausible depth noise.

## Answer
41.5 cm/s. Confidence: moderate, roughly ±8%.
