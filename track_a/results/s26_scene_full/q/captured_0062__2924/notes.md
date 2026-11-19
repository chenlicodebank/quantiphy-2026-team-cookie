# q_2924: width of the whiteboard (cm)

The file rate and question_fps are both 24 fps. t = 1.4 s is frame 34. depth_info gives the board centre at 2.815 m.

## Method (measure.py)
- The board is a flat rectangle lying on the floor, so its short side recedes in depth and the image foreshortens it. A plain pixel extent would therefore be wrong. I used a full pinhole rectangle reconstruction instead, with f = 0.5959 x 1280 = 762.8 px and the principal point at (640, 360).
- **Corners:** at each frame 22-48, I thresholded the grey level at the midpoint between board and floor. That edge is unbiased under motion blur. I then fitted robust lines to the middle 60 % of each of the 4 contour edges and intersected them. The clips and rounded corners are excluded.
- **Plane:** the vanishing points of the two pairs of opposite edges give the two edge directions. At f = 763 they come out 89.8 deg apart (frame 34), so the given focal length is consistent with a rectangle. Their cross product gives the plane normal. The centre is the intersection of the diagonals, put at 2.815 m along its ray. The corners are then intersected with that plane.
- **Frame 34:** sides 0.8107 m (far/near edges) x 0.6063 m (left/right edges).
- The fitted plane is about 1.80 m from the camera centre, which is plausible for a camera elevated above the floor.

## Second route and checks
- **Fixed plane, other frames:** I kept the absolute plane from frame 34 and reconstructed frames 22-48. The median sides are 0.812 / 0.607 / 0.811 / 0.609 m. They are constant across frames even though the board's depth changes a lot.
- **Each frame on its own:** I reconstructed each frame from its own vanishing points, scaled so that its centre lies on the frame-34 plane. The median is 0.811 x 0.601 m.
- **Prior check:** the per-frame speed on this plane is about 1.5-1.7 m/s. The capture has a doubled step at frame 35 to 36 (3.2 m/s). A 5-frame smoothing window around frame 34 gives (1.36 + 1.53 + 1.57 + 3.23 + 1.59)/5 = 1.85 m/s, which is close to the prior of 1.934. So the scale agrees with the prior to within about 5 %.
- **Other objects:** their depth_info values do not fit the floor plane well (bag 3.44 vs 3.31 given; the carton/box, bear and bin are off by more). Either the labels map to different objects or those objects are not on the floor. I did not use them for the scale. The board's own depth sets the scale, and the size is linear in it.

## Answer
- Width (shorter horizontal side) is about 0.607 m = **60.7 cm**.
- The length (the long side) is about 81 cm.
- Confidence: good, with an estimated error of about ±3 %. That is dominated by the given depth and the corner blur.
