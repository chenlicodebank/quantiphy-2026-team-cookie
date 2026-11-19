# q_2799: initial distance from the yoga ball to the shoe (m)

The file and the question both use 24 fps. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640,360). Script: `measure.py`; overlays are in `frames/ov_*.png`.

- **Ball size:** at frame 24 (t = 1.0 s) the circle fit is cx = 573.3, cy = 544.1, diam = 152.5 px. The ball's depth there is 2.612 m, which gives Z = 2.530 m and a ball diameter of 0.506 m.
- **Initial ball position:** the ball is at rest in frames 0-9, with a mean diameter of 131.9 px. That gives Z0 = 2.925 m and a range of 2.98 m, about the same as the bin's (2.977 m); the ball sits beside the bin, so this is plausible. The ball centre is at (617, 507) px.
- **Shoe:** the foreground-component centroid is (285.6, 658.1) px, back-projected with the given 2.231 m.
- **Result:** the 3D distance is **1.306 m**. Using frame 0 alone (diam 130.2) gives 1.335 m, and the shoe's bbox centre instead of its centroid changes the result by less than 0.002 m.
- **Second check:** I rebuilt the 3D track with a constant ball radius. The smoothed speed over frames 24-29 is 2.12 m/s, against the prior's 2.19 m/s (3% apart), so the ball size and scale are consistent.
- **Answer:** 1.31 m. Confidence is moderate to good, at about ±4%.
