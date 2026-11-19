# q_3229 – diameter of the ball (cm)

Prior: gravity = 9.8 m/s^2. The clip is a top-down hand-held view of a gym floor. A basketball rolls across it from right to left (frames 49–72) with no fall or bounce, so the gravity prior gives no usable scale (there is no vertical acceleration in the image plane). The scale was taken from known real sizes instead. File fps = question fps = 30.

- Ball pixel diameter: 256 px, the median blur-free vertical extent over full frames 53–69 (scene/tracks/ball.csv; range 250–261). Checked on frame 60.
- Route 1 (standard object): the ball is a regulation men's basketball, size 7, circumference 74.9–78 cm, so diameter about 23.9–24.8 cm, nominally 24 cm.
- Route 2 (court lines): painted court lines are 2 in = 5.08 cm wide and measure 50 px (maroon lines; the blue line is 47 px). That gives 0.1016 cm/px on the floor plane, so the ball is 26.0 cm at floor-plane scale. The ball's centre is about 12 cm above the floor, which is closer to the camera, so it looks larger. Correcting for a camera height of 1.2–1.6 m gives 23.5–24.1 cm (check.py).
- The two routes agree. Answer: 24 cm.

Confidence: good (about ±5%). The ball could be a size 6 (about 23 cm), but it looks like a standard size 7.
