# Q1303: average speed of the walking pedestrian over the whole clip (m/s)

The video file and the question both run at 24 fps, 72 frames (0-71). Frames 0 and 1 are identical.

## Focal length (vanfit.py)
- The prior is the white car (the van) accelerating at 4 m/s^2. I modelled the van as moving in a straight line
  on the ground with constant acceleration. Data used: the measured rear edge rear_x (f28-71), the front edge
  (f69-71), the change in its pixel height (f28-57, measured bottoms only), and the two given van depths
  (f14, f38) to its centre. Unknowns: f, heading, position, v0, length.
- With a = 4 fixed: **f = 2039 px**. The rear edge rms is 3.9 px and both depths are reproduced to 0.2 mm.
  With the acceleration left free, the fit gives f = 2086 and a = 3.86 m/s^2. So the data agree with the prior
  on their own.
- The fit has a sharp minimum: cost 120 at f=2000, versus 830 at f=1600 and 530 at f=2500.

## Pedestrian (manspeed2.py)
- Pelvis pixel = (hip_x, ref_y) from scene/tracks/man.csv. I used robust polynomial fits in time because the
  raw values jump with the gait and with occlusion (e.g. hip_x at f30 is interpolated).
- Depth shape over time comes from the image scale: 1/(feet_y - horizon 532) and 1/(height_px), both fitted.
  An offset and a gain are then solved so the two given human distances (16.6692 m at f14, 15.5003 m at f38)
  are reproduced exactly.
- Back-projection: X = (u-cx)Z/f, Y = (v-cy)Z/f, with the principal point at (1080, 540).
- Speed at frame i = |P(i)-P(i-1)|·24. The average is over frames 1..71, which equals path length / 2.958 s.
  Speed at frame 1 is 0 because frames 0 and 1 are identical.
- Results:
  - Linear-in-time fits: 1.170 m/s (1.187 if frame 1 is excluded).
  - Quadratic fits: 1.187 m/s.
- The result hardly depends on f: f=1800 gives 1.178, f=2086 gives 1.169, f=2300 gives 1.164. This is because
  most of the motion is toward the camera, and the given depths fix that part.
- Second route: the start and end positions (-5.42, 1.16, 16.35) -> (-3.63, 1.19, 13.39) m give a net
  displacement of 1.17 m/s. That matches, since he walks in a near-straight line.
- The pelvis bob and sway of the gait are smoothed out; they would add about 1-2%.

## Answer
**1.18 m/s**, the middle of 1.17-1.19. Confidence is good, about ±4%.
