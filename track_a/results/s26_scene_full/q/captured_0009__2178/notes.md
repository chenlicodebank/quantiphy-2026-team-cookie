# q 2178 — maximum rebounce height of the basketball (cm)

Lab video, 1280x720, file fps 24 = question_fps 24. f = 0.5959*1280 = 763 px, principal point (640, 360).
depth_info: ball 1.3210 m at t=0 (frame 0), floor 2.0285 m at t=0, ball 1.5835 m at t=1.8 (frame 43), ball 1.5795 m at
t=1.92 (frame 46, apex). Prior a = 9.8 m/s^2.

## Measurements (measure.py)
HSV/RGB ball mask restricted to an ROI around the scene track, circle fit to the contour (frames 33-48).
Bounce (lowest) frame 37: centre (547.3, 655.5), D 96.6 px, ball bottom y = 705. Apex frame 46: centre (528.0, 480.3), D 106.6 px.
Matches scene/tracks/ball.csv within ~1-2 px (the record is fine for this question).

## Geometry (check_floor2.py, traj3d.py, tilt.py)
- Apex centre = ray(528, 480.3) * 1.5795 m.
- Floor: the floor distance 2.0285 m is taken as the floor spot where the ball lands (bounce contact under the frame-37 ball).
  That fixes the bounce ball-centre distance at ~1.96-1.98 m, i.e. dist*D = 190 px*m, which independently agrees with the held
  ball at t=0 (1.321 m * 145.5 px = 192). The alternative reading "floor directly under the ball at t=0" is inconsistent
  (it needs > 30 deg camera tilt and a 1.2-1.8 m hold height).
- Camera tilt (gravity direction in camera frame) from the 3D trajectory: ~0-20 deg, best ~5-12 deg (noisy, size-based depths).
- Results vs tilt 0 / 5 / 12 / 20 deg:
  apex ball-centre height above floor = 0.584 / 0.604 / 0.624 / 0.635 m;
  rise of the centre from bounce to apex (= ball-bottom height at apex) = 0.469 / 0.489 / 0.509 / 0.520 m.
  Level-camera reading (camera-Y as vertical, floor point at the landing spot): 0.577 m.
- If instead the bounce depth comes from apparent size scaled to the given apex depth (k=166), the rise is only 0.38 m
  (centre height 0.49 m); the given apex/t=1.8 depths are ~14% smaller than the size-implied ones (inconsistent with t=0).

## Second route / physics
At 24 fps, bounce f37 -> apex f46 = 0.375 s -> g t^2/2 = 0.69 m. But the fitted 3D acceleration of the rise is only ~6-7 m/s^2
with these depths, suggesting the true capture interval is shorter than 1/24 s (~30 fps camera); timing-based heights are not
trusted. The given depths set the scale.

## Answer
Reading: height of the ball (centre, as reference positions are centres) above the floor at the apex: ~0.58-0.62 m;
ball-bottom reading ~0.49-0.51 m. Answer 58 cm (between the level-camera and tilted values, leaning slightly toward the
alternative reading). Confidence: moderate-low (interpretation of floor point and centre vs bottom, ±15%).
