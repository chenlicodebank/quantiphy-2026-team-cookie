# q_2390 — speed of the ping pong ball at t = 1.2 s (cm/s)

File fps = question fps = 24, so t = 1.2 s is frame 29. The depth samples fall at frames 14, 19 and 29.
Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360). depth_info is the Euclidean distance to the ball centre.

## Method (line3d.py)
- Pixel centres come from scene/tracks/ball.csv. I checked them with retrack.py, my own background-difference centroid
  over frames 18-40. My centroid sits a constant +0.6 px in x and +3.2 px in y from the record (my mask takes in the
  contact shadow), but the frame-to-frame steps agree. Example: the v step from frame 25 to 33 is 37.76 px in the
  record and 37.57 px in mine.
- I back-projected the three depth samples to 3D points. They are collinear to within 1-4 mm, as expected for a ball
  rolling straight down the board.
- I fitted a 3D line through them. For every frame, the ball position is the point on that line closest to the
  camera ray through the tracked pixel centre (ray misses are under 1 mm in frames 14-32). This reproduces the given
  depths: 1.757 / 1.679 / 1.528 m against 1.751 / 1.687 / 1.526 m.
- Speed at frame 29:
  - central differences over 5, 7 and 9 frames: 42.7, 43.7, 42.2 cm/s
  - quadratic fit of the 3D positions over frames 25-33, 23-35, 20-35 and 14-35: 42.74, 42.62, 42.71, 42.48 cm/s
  - the raw per-frame speeds jitter between 36 and 46 cm/s
- **Answer: 42.7 cm/s.**

## Second route (compute.py)
Interpolating depth linearly in time through the three samples gives 42.6 cm/s, which agrees.

A quadratic-in-time depth through the three samples gives about 49 cm/s. I rejected it because it is not consistent
with the image motion. The ball's image speed is almost constant, about 4-5 px per frame, so the ball moves at nearly
constant speed around frame 29. The quadratic curve makes the depth rate speed up in a way that the straight-line
geometry does not support.

## Confidence
Moderate to good, about ±5%. The main uncertainty is how the reference interpolated depth between its samples.
The frame 35→36 jump of 11.5 px (a capture irregularity) lies outside the windows used here.
