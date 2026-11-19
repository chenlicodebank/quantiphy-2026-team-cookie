# q_2698 – ball velocity at t = 1.4 s (cm/s)

- t = 1.4 s, question_fps 24 (the file is also 24 fps) -> frame round(33.6) = 34. Between bounces at ~28 (tape roll) and ~36 (glass jar); the apex is at ~frame 32.
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- `measure.py`: my own ball mask (median-background difference) with the centre at the midpoint of the extents. Diameter = mask extent perpendicular to the motion (not affected by blur).
  At frame 24 d_perp = 30.4 px. With R = 1.055 m that gives 4.2 cm, against the 4 cm prior (within 5 %), so the depth and focal length agree.
- Depth over time: R(k) = 1.055 x d(24)/d(k), with 1/d fitted linear in frame over the clean frames 21–40 (excluding the occluded frames 28, 35, 36).
  R falls from 1.055 m (frame 24) to 0.900 m (frame 34), so the ball moves toward the camera at about 0.37 m/s.
- 3D points = R x unit ray through (u, v). Velocity at frame 34 (`velocity.py`, `variants.py`):
  - raw forward difference p35 - p34: 74.6 cm/s
  - central difference (p35 - p33)/2: 70.2
  - ballistic quadratic fit over flight frames 29–35, instantaneous at frame 34: 71.5 / 75.1 / 77.6 (three exclusion choices)
  - 5-frame moving-average smoothing: 68.4
  - Smoothing windows that cross the bounce at frame 36 vary more (SG5 gives 111, mean of the speeds 89). I rejected these because they mix in the bounce.
- Answer: **73 cm/s** (centre of the bounce-free estimates, 68–78).
  Components at frame 34 are about (-34, +47, -45) cm/s in camera x, y-down and z.
- Caveat: the fitted vertical acceleration is about 7–8 m/s² rather than 9.8 (camera tilt, blur-centroid bias). Confidence: moderate, about ±10 %.
