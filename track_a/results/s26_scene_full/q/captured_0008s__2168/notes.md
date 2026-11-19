# q_2168: maximum rebounce height of the basketball above the desk (cm)

The file fps (24) is the same as question_fps (24). Camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360).

## Data
- I used the ball track from scene/tracks/ball.csv (RANSAC circle centre and diameter) and checked it on frame 30 (contact) and frame 36 (apex).
- **Contact:** frame 30.
- **Apex:** frame 36 (t = 1.5 s, matching the depth_info "max rebounce" entry). The centre is at (547.7, 303.7) and the diameter is 114.3 px.
- **Desk centre:** the intersection of the board diagonals in the image is (586.8, 465.2). Its depth is 1.725 m (given).
- **Ball diameter:** D = diam·depth/f gives 0.228 m at t = 1.0 and at t = 1.5, which is a size-6 basketball and is consistent.

## Scripts
- **fit3d.py:** back-projects the ball centres, using depth from the diameter (calibrated with D = 0.228).
  - A 3D parabola fit over arc 1 (frames 31–40) gives |a| = 9.86 m/s², matching the prior of 9.8.
  - It also gives the gravity direction in camera coordinates: (0.12, 0.85, 0.52).
- **desk.py:** builds the desk plane through the desk centre (1.725 m), normal to gravity. A second normal, fitted on the assumption that the board is square, lies within 6.5° of it and gives the same numbers.

## Results (all at apex frame 36)
- **Ball centre above the desk plane: 0.403 m.** The plain 3D distance from the ball centre to the desk centre is also 0.403 m, because the apex is almost directly over the desk centre.
- **Ball bottom above the desk:** 0.289 m.
- **Rise of the centre from contact (frame 30) to apex:** 0.270 m.
- **Route from flight timing:** the impacts are at frames 30.15 and 41.0, so T = 0.452 s and g·T²/8 = 0.25 m, which is the rise of the centre.
- **Plane check:** at contact the ball centre is 0.133 m above the plane, against a radius of 0.114 m, so the plane is good to about 2 cm.

## Answer
The question names the desk, and depth_info gives the desk-centre distance, so I followed the paper's centre-based convention: ball centre at maximum rebounce relative to the desk (centre/plane). That gives **40.3 cm**.

Other readings: the ball's bottom above the desk is about 29 cm, and the rise of the centre is 25–27 cm.

Confidence is moderate. The measurement itself is solid (to about 2 cm); the uncertainty is which definition the reference used.
