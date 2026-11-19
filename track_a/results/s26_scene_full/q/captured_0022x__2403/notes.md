# Q2403 – acceleration of the ping pong ball at t = 1.2 s (cm/s^2)

The file is 24 fps and question_fps is also 24, so t = 1.2 s is frame 29. The depths are given at frames 14, 19 and 29. The focal length is f = 0.5959 x 1280 = 763 px, with the principal point at (640, 360). The ball track is scene/tracks/ball.csv. I checked it: it follows the white ball for the whole clip. The ball rolls toward the camera from frame 12, so the motion is mostly in depth.

## Route A – depth_info trajectory (route_depth.py, measure.py)
- I back-projected the ball centre at the three times with the given depths.
- 3D path lengths between those points:
  - 0.6 → 0.8 s: 7.52 cm, an average of 36.1 cm/s.
  - 0.8 → 1.2 s: 18.24 cm, an average of 43.8 cm/s.
- Fitting constant acceleration through these three positions gives a = 26.7 cm/s^2.
- Per-frame version: depth(t) is a quadratic through the three given depths, and the pixel centres are smoothed with a quadratic fit. The acceleration is d|v|/dt at frame 29.
  - Result: 26–29 cm/s^2, depending on the fit window. The speed at 1.2 s is about 50 cm/s.

## Route B – table-plane model (plane.py)
- I took the table-plane normal from the vanishing points of the table corners. The two edge directions come out orthogonal (cos = 0.03), which supports f.
- I set the plane offset from the given depths. The three depths imply offsets that differ by 1.4%; the one at 1.2 s is about 1.5 cm closer than the plane predicts. So the given depths carry about 1–2 cm of sensor noise.
- I intersected each frame's ray with the plane.
  - Speed is about 38 cm/s for frames 15–28 and about 44 cm/s for frames 37–45.
  - Quadratic fits that avoid the frame-36 jump give a ≈ 5–11 cm/s^2.
  - Fits whose window includes frames 35→36 (where a capture frame was probably dropped, with a step of about 2x) give 19–28 cm/s^2.
  - If I shift the frames after 36 by one frame, the fits drop to about 4–5 cm/s^2.

## Choice and confidence
The reference positions use the measured depth (the given depth_info values) and the reference does not know about the dropped frame. Both of those effects point to about 25 cm/s^2: route A gives 26–28, and the route-B fits that include the jump give 19–28.

The image-only plane model, corrected for the dropped frame, says the physical acceleration is smaller (about 5 cm/s^2). So the true value is uncertain.

**Answer: 25 cm/s^2. Confidence: low to moderate.**
