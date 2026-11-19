# q_2852: velocity of the white ball at 1.5 s (m/s)

The file and the question both run at 24 fps. t = 1.5 s is frame 36.

## Which ball is "white"
- The depth_info gives orange (basketball), white and green balls at t = 1.0 s (frame 24): white 3.0735 m, green 3.039 m.
  At frame 24 the yellow-green tennis ball (`tennis_ball_yellow`) and the small whitish ball (`grey_ball` in scene/)
  sit 30 px apart in the standing person's hands, so their depths should be almost equal, and they are.
- The black-and-white soccer ball is beside the crouching person, much nearer the camera. From its size (65-70 px
  for a ~0.22 m ball) it is at ~2.5 m. At 3.07 m it would have to be 0.27 m across, which is too big.
  On a zoomed frame the small ball looks whitish grey.
- So the "white ball" is the small thrown ball (`grey_ball`). It is released at frame 23, is in flight at frame 36
  just before bouncing (lowest image point at frame 38), and is caught at about frame 42.
- If the soccer ball were meant instead, the answer would be about 1.4 m/s. I think that reading is unlikely.

## Timing anomaly (dropped capture frame)
- Between frames 35 and 36 both small balls jump about 120 px, against about 45 px per frame before that.
  A ballistic fit only works if one capture frame is missing between 35 and 36:
  - grey-ball rms 1.24 px with the dropped frame, against 3.98 px without it;
  - tennis-ball rms 0.42 px against 4.55 px.
- The basketball also skips a frame between 11 and 12 (fit rms 0.6 px with the gap, 3.6 px without).

## Method (ballistic.py, joint.py)
- Lab camera: f = 0.5959 × 1280 = 763 px, principal point (640, 360).
- Centroids come from scene/tracks. I re-segmented frames 31-40 in seg.py, and the soccer-ball masks came out
  identical to the record.
- Model: 3D projectile P(t) = P0 + V0 t + ½ g ĝ t², with |g| = 9.81 m/s², and the camera pitch and roll fitted.
  - |P0| at frame 24 is fixed to the given depth.
  - The grey and tennis balls are fitted together, sharing the gravity direction.
  - Frames used: grey 24-36, tennis 25-36.
  - The time of frame 36 includes the dropped frame.
- Joint fit: rms 0.97 px, pitch 15°, roll 1°. Grey-ball speed is 4.02 m/s at frame 35, **4.79 m/s at frame 36**
  and 5.19 m/s at frame 37. Depth falls from 3.07 m (frame 24) to 2.34 m (frame 36).

## Checks
- **Reference-style velocity (refstyle.py).** 3D centres from the tracked centroids, back-projected with the
  model depth, then forward differences × 24.
  - The single forward difference 36→37 gives 4.95 m/s.
  - 5-frame windows give 4.78 (34-38), 4.81 (32-36) and 4.89 (33-37). The doubled 35→36 step and the
    slowdown at the bounce roughly cancel.
- **Focal-length sensitivity (ftest.py).** For f from 763 down to 560 px, the speed at frame 36 is 4.79-4.93 m/s.
  Gravity fixes the vertical speed, so the answer barely depends on f.
- **Fits on one ball only, with and without frame 36:** 4.83-5.07 m/s.
- **Prior check (basket_fit.py).** With the given depths (2.3557 m at frame 12, 1.81 m at frame 24), the basketball
  speed at 0.5 s comes out at 1.66-1.71 m/s, against the prior's 2.21 m/s. No f in 560-763 px reproduces 2.21.
  - A gap this size fits noise in the reference's per-frame depth readings: ±0.1 m depth noise gives about
    ±0.7 m/s after 5-frame smoothing.
  - I did not rescale by the 1.31 ratio. The rescaled answer would be about 6.3 m/s.
- **Gravity-implied depth.** If the depth at frame 24 is left free, gravity implies about 4.0 m instead of 3.07 m,
  which would give 5.2 m/s. That depth conflicts with the floor and person geometry, so I kept the given depth.

## Answer
4.85 m/s: the centre of 4.79 (model), 4.95 (forward difference) and 4.8-4.9 (smoothed windows).
Confidence is moderate. Identifying the ball is fairly secure. The main risk is how the reference handled the
dropped frame and the bounce, and noise in its depth readings (the prior could not be reproduced).
