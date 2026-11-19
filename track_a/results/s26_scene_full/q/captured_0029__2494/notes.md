# q_2494 — tennis ball velocity at t = 1.0 s (frame 24), cm/s

The file and the question both run at 24 fps, so t = 1.0 s is frame 24. Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

I took the ball centres from scene/tracks/ball.csv (circle fit to the mask). I checked frame 24 by eye: the ball is at about (819, 465) on the back half of the table, with no blur.

depth_info gives Euclidean distances (the "0.901s" is read as 0.901 m). Converted to Z along each pixel's ray:
- frame 24: Z = 0.869
- frame 30: Z = 1.134 (the board hit; t = 1.24 s rounds to frame 30)
- frame 38: Z = 1.020

The three back-projected centres all have Y ≈ 0.115–0.120 m. That is what you expect for a ball rolling on a horizontal table, so the depths agree with each other.

Scripts: vel.py (first look) and vel2.py (final).

Route 1 (Z linear in time between the given depths): the per-frame forward speeds for frames 21–29 run from 122 down to 109 cm/s, close to a constant velocity. The smoothed 5-frame chords centred on frame 24 give 116 cm/s (22–26: 116.1; 23–25: 116.2; 21–27: 116.8).

Route 2 (independent check: each centre lies on the plane through the three given 3D centres, i.e. the table top plus the ball radius): intersecting each ray with that plane gives a Z per frame. The 5-frame chords give 116–123 cm/s (22–26: 115.9; 22–27: 118.4), and the mean of the forward vectors over frames 22–26 is 118.4 cm/s.

Not used: depth from apparent size (Z = f·6.7 cm / diam_px). It is noisy (±2 px on a 40–48 px diameter) and comes out about 15 % deeper than the given depths. Its smoothed values range from 98 to 137 cm/s.

Breakdown at frame 24: about 105 cm/s away from the camera and about 48 cm/s sideways (leftwards).

**Answer: 117 cm/s.** Confidence: good, about ±5 %.
