# Q2505 – tennis ball velocity at t = 1.0 s (cm/s)

File fps = question fps = 24, so t = 1.0 s is frame 24. At that point the ball is in flight away from the camera, just
before it lands on the far part of the table. depth_info gives 0.901 m at frame 24, 1.144 m at frame 30 (hits
the whiteboard) and 1.027 m at frame 38. I read "0.901s" as 0.901 m.

## Method (measure.py, velocity.py, smooth.py)
- Ball mask: HSV yellow (H 21-45, S, V >= 50), largest component, re-measured for frames 19-32. Centroids agree
  with scene/tracks/ball.csv to within 1 px, and the f24 crop overlay (frames/f24.png) sits on the ball.
- Pinhole: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Depth per frame: Z(i) = 0.901 m x D(24) / D(i), where D is the ball's apparent diameter. I used the minor PCA
  extent because motion blur stretches the mask along the direction of motion.
  Check against the given anchors: predicted Z(30) = 1.150 (given 1.144) and Z(38) = 1.046 (given 1.027), so the
  depth profile from size agrees with the given depths to within 0.5-2 %. Using the equivalent diameter instead
  predicts Z(30) = 1.171, which fits worse.
  The plain size route (6.7 cm / D x f) gives Z(24) = 0.946, about 5 % above the given depth.
- 3D centre = ((u-cx)/f, (v-cy)/f, 1) x Z. Velocity = local polynomial fit of X, Y, Z over 5-7 frames around
  frame 24, as a stand-in for the smoothed forward difference.

## Results (cm/s)
- Minor-axis depth: linear fit over frames 22-26 gives 138.1; quadratic over 22-26 gives 138.1-138.7; quadratic
  over 22-27 gives 134-136; cubic fits give 120-130. The mean of the 5 forward differences (22-26) is 131.7.
- Equivalent-diameter depth: 150-163 (depth fits the anchors worse).
- Depth interpolated linearly from 0.901 to 1.144 m over frames 24-30: 110. This underestimates, because the ball
  clearly slows down: its image speed drops from 29 px/frame at f24 to 10 px/frame at f30. So this is the
  average over the interval, not the speed at f24.
- Speed is mostly in depth (about 1.25 m/s) plus about 0.75 m/s sideways.

Answer: 138 cm/s. Confidence: moderate, about ±12 %. The depth rate depends on the apparent-size change of a
blurred ball over a few frames.
