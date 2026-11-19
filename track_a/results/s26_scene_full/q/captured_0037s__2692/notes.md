# q_2692 – ping pong ball velocity at t = 1.4 s (cm/s)

t = 1.4 s -> frame round(1.4*24) = 34 (file fps = question fps = 24). Frame 34 lies on the descending part of the
arc between bounce 28 (tape roll) and bounce 36 (in front of the jar), with the apex at about frame 32.

## Method
- Lab camera: f = 0.5959*1280 = 763 px, principal point (640,360).
- Ball centre: centroid of a background-difference mask (median background, half-contrast threshold), in
  `measure2.py`. It agrees with scene/tracks/ball.csv to within about 1 px on clean frames.
- Depth: the only given depth is at t = 1.0 s (frame 24): 1.055 m. Depth at other frames comes from the apparent
  diameter (the mask's width across the blur direction). I fitted 1/d linearly in frame over clean frames 21-27,
  29-34 and 37-40: d(24) = 27.5 px, d(34) = 32.8 px. Then Z(k) = 1.055 * d(24)/d(k), so Z(34) is about 0.885 m.
  Absolute check: a 4 cm ball at 1.055 m should look 28.9 px wide; I measure 27.5 px (5% low, threshold bias).
  Using absolute depths Z = f*0.04/d instead makes the speeds about 5% higher.
- 3D points: unit ray times the distance. Velocity: quadratic (ballistic) fit to the 3D points of frames 29-35
  (between the bounces), derivative at frame 34 times 24.

## Results (ratio depth)
- Quadratic fit 29-35: 72.1 cm/s at frame 34 and 81.5 cm/s at 34.5 (where the forward difference is centred).
- Other fit windows (30-34, 30-35, 29-34, 31-35): 70.7-78.3 cm/s at frame 34.
- Raw forward differences: 33->34 67.6 cm/s, 34->35 74.1 cm/s.
- Components at frame 34: about (-32, +43, -49) cm/s in camera (x right, y down, z forward).
- Fitted acceleration is 6.4-7.9 m/s² (expected about 8-9.8 after projection), so the measured scale is about right
  or slightly low.

Answer: 75 cm/s, the middle of the fit range at frame 34, which also matches the forward difference from 34 to 35.
With absolute depths it would be about 79 cm/s.
Confidence: moderate (about ±10%). The main uncertainties are the depth trend from apparent size and the
reference's smoothing convention so close to the bounce at frame 36.
