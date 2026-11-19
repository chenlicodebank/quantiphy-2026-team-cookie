# q_2262 – velocity of the rolling ball at t = 0.6 s (cm/s)

File fps = question fps = 24. t = 0.6 s -> frame round(14.4) = 14.

## Method (m1.py, m2.py)
- Ball centres from scene/tracks/ball.csv (ref_x, ref_y). I checked them on 3x crops of frames 0, 8 and 10-16
  (frames/crops*.png); the circles sit on the ball.
- Lab intrinsics: f = 0.5959*1280 = 762.8 px, principal point (640, 360).
- 3D points: P0 = 1.8180 m * unit ray(frame 0) and P14 = 1.7288 m * unit ray(frame 14), both distances from depth_info.
  The ball rolls straight down the board, so its centre moves along the 3D line P0->P14. For every other frame
  the position is the point on that line closest to the frame's ray. S = arc length along the line.
- Forward-difference speeds (m/s), shown as i->i+1: 12->13 0.762, 13->14 0.871, 14->15 1.025, 15->16 1.189,
  16->17 1.203. The 11->12 step (1.36) is a real jump in the image: the ball comes over the board's top edge.
  It is left out of the window.
- Smoothed over 5 frames around frame 14: mean of the forward differences from 12 to 16 = 1.01 m/s.
  A linear fit of S over frames 12-16 gives 0.96 m/s (centred at frame 14). A quadratic fit over frames 9-16
  gives 1.03 m/s at frame 14.
- Check against the prior: the per-frame speed rises by about 0.15-0.16 m/s per frame, which is about 3.7-4 m/s^2.
  The prior says 4.6 m/s^2, so this roughly agrees.

## Answer
v(0.6 s) ≈ 1.00 m/s = **100 cm/s**. The routes give 96 to 103 cm/s. Confidence: moderate, about ±7%.
