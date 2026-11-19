# q_2735: white ball velocity at t = 1.0 s (frame 24, question_fps 24 = file fps)

Method (measure.py): lab camera with f = 0.5959*1280 = 762.8 px and principal point (640,360). Ball centres come from
scene/tracks/ball.csv, edge circle fit for frames 19-40. I checked frame 24 on a gridded crop: the ball spans about
x 527-559, y 443-475, which matches the record (542.95, 458.47, D 32.1).
Depth per frame: Z = k / D_smooth, where D_smooth is a linear fit of 1/D over frames 19-40. k is set by the given
distance 1.014 m at t = 1 s, and the distance at 1.5 s checks it: the model gives 0.751 m against the given 0.737 m,
1.9 % off. The 3D centre is the unit ray times the distance. Velocity is a linear fit of the 3D positions over
frames 21-27 (7 frames).
- Main result: 54.1 cm/s, components (-3.0, 1.3, -54.0) cm/s. Motion is almost entirely toward the camera; the
  pixel speed is only about 4.1 px/frame.
- Variants: k as the average of both depths gives 53.5; a quadratic 1/D fit gives 52.3 / 51.8; a 5-frame window gives
  the same values.
- Second route, ignoring the diameter: depth interpolated linearly between the two given values (1.014 m to 0.737 m
  over 0.5 s) gives 56.8 cm/s, the average over 1.0-1.5 s.
Answer 54 cm/s. Confidence: moderate (±5 %). It depends on the depth rate, which comes from the apparent diameter.
