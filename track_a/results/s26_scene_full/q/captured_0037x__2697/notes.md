# q_2697: speed of the ping pong ball at t = 1.0 s (cm/s)

The file and question_fps are both 24, so t = 1.0 s is frame 24, the top of the second arc (between the bounces at frames 19 and 28).
Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360). Depth_info: the ball is 1.055 m from the camera at t = 1.0.

## Measurements (measure.py, velocity.py)
- Ball mask in frames 12–40 (difference from the median background). The diameter is measured perpendicular to the motion
  direction, so motion blur does not inflate it. At frame 24 it is 29.4 px, which gives 763 x 0.04 / 29.4 = 1.038 m.
  The given range is 1.055 m, so the prior and depth_info agree to within 1.7%.
- Depth trend: Z = k x f x 0.04 / diameter, anchored to 1.055 m at frame 24. A linear fit over the clear frames 21–35 (or 13–35)
  gives dZ/dt = −0.345 m/s, so the ball moves toward the camera. Fitting only frames 21–27 gives −0.21 m/s, which is noisier.
  Occlusion check: at frame 28 the ball is partly hidden behind the tape roll (1.038 m away), so its depth there is about 1.0 m or more.
  That matches the trend (1.055 − 4 x 0.014 ≈ 1.0).
- Image motion in the arc: x moves about −12.4 px/frame, which is −0.415 m/s at 1.383 mm/px. Vertically the ball is at the top
  of its arc. A parabola fitted to the arc gives g ≈ 8.5 m/s², a plausible check on the scale.
- A table-plane route (plane fitted through the bases of the cup, jar, tape and card tent; ball centre 2 cm above it at the bounces)
  gave inconsistent bounce depths (about 1.1 m at every bounce). That route is too crude and was not used.

## Speed at t = 1.0 (3D, in m/s)
- Instantaneous (fit over the arc): (−0.415, 0.065, −0.345), |v| = 0.544
- Forward difference 24→25: 0.587. Forward differences 22..26 averaged as vectors: 0.598. Central difference 23→25: 0.53.
- Answer: 56 cm/s, between the instantaneous value and the forward-difference value (the reference convention).

Confidence: moderate. The main uncertainty is the depth rate (±0.1 m/s), which changes the answer by about ±10%.
If depth were held constant, the speed would be only about 42–50 cm/s.
