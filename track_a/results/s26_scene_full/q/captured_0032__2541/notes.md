# q_2541: white (ping-pong) ball velocity at t = 1.5 s (frame 36 at 24 fps)

The file and the question both run at 24 fps. Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Data
- I used the white-ball track from scene/tracks/white_ball.csv (mask centroids). I checked it visually on frames
  29-38 (view.py -> frames/seq.png), and it sits on the ball. Frame 31 is hidden behind the yellow ball and frame 32 is
  partly hidden.
- Depth at frame 36 is 1.353 m (given), which gives Z = 1.340 m along the optical axis.
- Depth per frame: the ball rolls on the tabletop, so I used a ground-plane model. Camera pitch comes from the table's
  horizon (vanishing point y ≈ 341), and Z_i = H / ((v_i - cy)/f cosθ + sinθ), with H fixed by the given depth at
  frame 36.
  - Check 1: a 4.0 cm ball at these depths should measure 21.0 / 22.5 / 23.3 / 24.1 / 26.0 / 28.0 px across at
    frames 34 / 36 / 38 / 40 / 44 / 48. The measured bb_w is 22 / 22 / 24 / 25 / 27 / 29, about 1 px wider from blur.
    So the depth model agrees with the apparent size.
  - Check 2: solving the pitch from the two given depths (tennis ball and ping-pong ball) puts the horizon at about
    336 instead of 341. That changes the answer by about 5 %.
- The ball moves mostly toward the camera, about 2.2 cm per frame in depth, against about 1 cm per frame sideways.
  Ignoring the depth change would give only about 23-35 cm/s, which is wrong.

## Velocities (cm/s, 3D frame-to-frame steps x 24)
- Steps from frame 33 to frame 40: 103, 108, 154 (35->36), 56, 58, 55, 63.
- The scene record notes a dropped frame between frames 35 and 36: the yellow ball's step there is exactly twice its
  normal step. The white ball also slows down sharply around frame 35-36.
- What each convention gives at frame 36:
  - Raw forward difference 36->37: 55.6 (52.8 with horizon 336).
  - Reference-style smoothing over 5 frames centred on frame 36 (mean of steps 34..38, or positions smoothed with a
    5-frame window then forward-differenced): 86.0 (81.6 with horizon 336). A 7-frame window gives 85.
  - Physical speed just after the dropped frame (mean of steps 36..40): 58.
- The reference convention (centres back-projected, forward difference smoothed over at least 5 frames, timed by
  frame index) would not know about the dropped frame. It most likely lands near 80-86. The true physical speed at
  that instant is about 55-58.

## Answer
82 cm/s. This is the smoothed value (81-86 across the two horizon estimates), pulled slightly toward the unsmoothed
value as a hedge.

Confidence: moderate. The main uncertainty is whether the reference smoothing spans the dropped frame or the sudden
slow-down (about 85) or not (about 56).
