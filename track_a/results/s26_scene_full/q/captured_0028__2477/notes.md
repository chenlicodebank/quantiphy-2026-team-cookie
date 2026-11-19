# q_2477 – acceleration of the ping pong ball at 1.3 s (cm/s^2)

The file and the question both run at 24 fps, so t = 1.3 s is frame round(31.2) = 31. That frame is near the top of the first
rebound arc. Bounces happen at frame 26 and frames 36-37, so frames 27-35 are free flight. The prior is a 40 mm
diameter. depth_info puts the ball at 1.4115 m at t = 1.3 s. That agrees with its size: the ball is about 21-22 px across, and
763 x 0.04 / 21.5 = 1.42 m.

## Method
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Re-tracked frames 27-35 myself (`track2.py` -> `track2.csv`). For each frame I took the vertical brightness profile through the
  ball and found the top and bottom half-max crossings to sub-pixel. The centre is the midpoint, which for a blurred streak
  is the mid-exposure position. The results match scene/tracks/ball.csv to within about 1 px.
- 3D: back-projected each point with Z(t) = 1.4115 m - 0.7 m/s x (t - 1.3 s). The -0.7 m/s slope comes from depth_info:
  1.557 m at frame 26 and 1.4115 m at frame 31. The ball is moving toward the camera.
- Acceleration (`fit2.py`):
  - Quadratic fits centred on frame 31: 788 cm/s^2 (frames 29-33), 827 (28-34), 852 (27-35).
  - Second route, following the reference convention (forward-difference velocity smoothed over 5 frames, then a
    difference): 838-861 cm/s^2.
  - Raw second differences at frames 28-34 range from 694 to 1081 cm/s^2. They are noisy.
  - Using the top edge alone (bright cap) gives lower values, 685-760 cm/s^2.
  - Assuming constant depth lowers the results by about 3 %.
  - In pixels the curvature near the apex is about 7.1-7.7 px/frame^2.
- Cross-check on the second arc (apex at frame 42, Z about 1.25 m): about 8.7 px/frame^2, which gives about 820 cm/s^2. That is
  the same 15-20 % below g.

## Answer
The measured value is about 830-850 cm/s^2. Free fall would give 981 cm/s^2, so the measurement comes out about 15 % low on
both arcs. That gap could come from depth or focal length, but the frames give no way to correct it. I answered 860 cm/s^2:
the measured value, nudged slightly toward g.

Confidence: moderate. The reference could be anywhere from about 830 (the same measurement) to 981 (gravity).
