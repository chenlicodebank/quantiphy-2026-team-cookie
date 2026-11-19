# q_2849: velocity of the green ball at 1.0 s (m/s)

The question fps and the file fps are both 24. t = 1.0 s is frame 24.

**Identification.** The green ball is the yellow-green tennis ball (`tennis_ball_yellow` in scene/). At frame 24 it is at the
standing person's right fingertips, at (599.3, 290.2) px, just being released. Its depth is 3.039 m. The "white ball"
(3.0735 m) is the light-grey ball that was thrown with it (`grey_ball`). It is not the soccer ball: that ball is near the
crouching person at about 2.3–2.6 m.

**Track.** I re-measured the ball with a yellow-green colour mask (measure.py) for frames 18–34. It agrees with the
scene record to within about 1 px. In frames 22–29 there is no frame-gap anomaly; the dropped-frame jump in the
record is at 35→36. Pixel step around frame 24 is 15.4, 13.9, 13.3 and 14.6 px per frame.

**Geometry.** I used f = 763 px and cx, cy = 640, 360.
- Lateral speed only, at constant depth 3.039 m: 1.33 m/s. The ball is also moving quickly toward the camera, so
  depth motion matters.
- The floor was estimated from the basketball centres at the prior's depths: frame 12 at 2.3557 m and frame 24 at
  1.81 m, ball diameter 0.239 m from the prior depth. Camera tilt is 3.2° down. Check: the standing person's feet
  land on this floor at 3.20 m, which is consistent with the ball in their hand at 3.04 m.

**Route 1: projectile fit (check3.py).** The 3D origin was fixed at 3.039 m along the frame-24 ray. Velocity and an
effective gravity (along the floor normal) were free, fitted to frames 24–35.
- Result: v = (-0.044, -0.023, -0.080) m per frame. Speed is 2.26 m/s at frame 24. RMS error is 0.49 px.
- Forward differences 24→25 to 28→29 are 2.21, 2.16, 2.17, 2.23 and 2.35 m/s.
- Independent check: extending this trajectory, it reaches the floor at about frame 37.75 at pixel (347, 664). The
  observed bounce is the lowest image point at frame 37, (340, 657). That frame index is about 1 lower because of the
  dropped frame at 35→36. So the depth rate (about 1.9 m/s toward the camera) is confirmed by the floor plane.
- Effective gravity comes out at 8.5 m/s². A fit with g forced to 9.81 m/s² gives 1.9–2.0 m/s, but it fits worse
  (1.5–2 px RMS) and is inconsistent with where the ball bounces.

**Route 2: the white (grey) ball (check3.py).** It was tossed together with the green ball, and I used its own depth
of 3.0735 m. Speed is 2.37 m/s, with forward differences of 2.25–2.33 m/s. Similar magnitude.

**Prior.** The prior gives the orange ball 2.21 m/s at 0.5 s. My own geometric estimate is about 1.6–1.7 m/s. The
reference likely includes the dropped-frame jump at 11→12 (32.8 px against about 18 px) and depth-camera noise.
There is no such anomaly near frame 24 for the green ball, so I did not rescale.

**Answer.** About 2.2 m/s (smoothed forward difference at frame 24). Confidence is moderate: the depth-rate component
is the main uncertainty, and the range is roughly 1.9–2.3 m/s.
