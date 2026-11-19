# q_2391: acceleration of the ping pong ball at 1.2 s (cm/s^2)

The file and question_fps are both 24 fps. t=0.6 s is frame 14 (from 14.4), t=0.8 s is frame 19, and t=1.2 s is frame 29.
I used the lab camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).
Ball pixel centres come from scene/tracks/ball.csv. I checked them: rolling starts at frame 12 and stays on the board through frame 45. There is an irregular 11.5 px step between frames 35 and 36, probably a dropped frame, so I keep the fits to frame 35 or earlier.

## Route A (main): ball on a 3D line in the board plane (plane.py)
- I took the board-plane normal from two vanishing points: the board's side edges and its front/back edges. The two directions come out 88.6 deg apart, which is consistent with a rectangular board.
- The ball's 3D line is where the board plane meets the plane through the camera that contains the image track.
- I anchored the line on the given depths, either least squares through all three or each depth alone. Each frame's ray is then intersected with the line, and I fit a quadratic of path length against time.
- a = 12-15 cm/s^2 for windows around frame 29: 20-35 gives 12.0, 22-34 gives 13.0, 24-34 gives 15.3, and 13-45 gives 12.4. Anchoring on t = 1.2 s (1.526 m) gives 11.8-15.0.
- The line model reproduces the given depths to within about 1-3 cm. Anchored at frame 14 it gives 1.751, 1.690 and 1.568 m against the given 1.751, 1.687 and 1.526 m.
- Speed is about 0.37 m/s at 1.2 s. Just after release (frames 12-18) the ball slows down, which fits sliding turning into rolling. After that it speeds up slowly, so the incline is very shallow.

## Route B: back-projection with depth interpolated from depth_info (depthroute.py)
- A linear fit of depth through the three given values (residuals up to 7 mm) gives a = 3-11 cm/s^2.
- An exact quadratic in depth through the three values gives a = 25-31 cm/s^2. That curvature rests on the ±7 mm residuals alone.
- For any straight line, depth change per pixel goes as Z^2. That predicts a depth-change ratio of about 2.0 between the 19-29 and 14-19 frame spans, and route A matches it. The given depths imply 2.5. So their curvature is most likely depth-sensor noise and not real acceleration.

## Answer
13.5 cm/s^2. That is route A's central value, and it lies between the two depth-interpolation variants of route B.
Confidence is moderate. The acceleration is small, and the reference value depends on how its depth series was smoothed.
