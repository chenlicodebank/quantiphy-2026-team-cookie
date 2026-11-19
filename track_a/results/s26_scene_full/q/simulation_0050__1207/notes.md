# Q1207: average speed of the bicycle from 1.0 s to 2.0 s (m/s)

File fps = question_fps = 33, so t=1 s is frame 33 and t=2 s is frame 66. The camera is static. This is a 3D scene.
The bicycle moves right to left and away from the camera, along a nearly straight line in 33-66.

## Method (prior route, used for the answer)
- Pinhole model with principal point (960,383). Position = d * unit ray(u,v,f), using the given depths:
  bike 11.8960 / 14.6419 m and human 15.8652 / 16.6708 m at frames 33 / 66.
- Pixels: pedestrian torso_x (or bbox_cx) with pelvis_y_est, averaged over ±0-4 frames. Bicycle hub_mid_x/hub_y
  or the box centre. These come from the scene record, and I checked them on frames 33 and 66.
- The focal length comes from the prior: the pedestrian moves 1.236 m between frames 33 and 66, which gives
  f ≈ 3005 px (HFOV ≈ 35°).
- The bike moves 3.75 m in 1 s. For a straight, constant-speed path the mean of per-frame speeds equals the
  chord / 1 s.
- Sensitivity (final.py): ped point choice, smoothing, bike point choice and a principal point at cx = 960-1300
  give 3.68-3.80. Median 3.74.

## Cross-checks and the conflict (read this)
Measurements of the bicycle alone disagree with the prior:
- The vertical wheel diameter from the tyre centre-line dips (wheeldiam.py) is 97.0 / 100.4 px at frame 33 and
  81.7 / 84.6 px at frame 66. That ratio is 1.1865 for both wheels. With cx = 960 it needs f ≈ 1850, while
  f = 3000 predicts 1.213.
- The wheel ellipse aspect is about 0.90 at frame 33 and 0.80 at frame 66. At frame 33 this means the bike's
  heading is about 64° from the line of sight. With f = 3000 the chord direction is only 48°, so the bike would
  be moving about 15° off its own heading. With f ≈ 1850 heading and motion agree.
- The manhole ellipse (aspect 0.095) suggests f ≈ 1600. This reading is unreliable: at that grazing angle it is
  very sensitive to road tilt.
- The change in wheel aspect along the path (constant-heading assumption) gives f ≈ 2300-3000.
- The pedestrian's size trend does not fit the given human depths with cx = 960 for any f. A principal point at
  cx ≈ 1300 (an off-centre crop) would reconcile the prior with the wheel-size ratio (f ≈ 3040, bike 3.69 m/s).
- If f ≈ 1850 (bicycle geometry only), the bike would do 4.9 m/s and the pedestrian 1.70 m/s, which contradicts
  the exact prior of 1.236.
I follow the instruction that the prior is exact. Every prior-consistent setting gives 3.68-3.80 m/s.

Answer: 3.74 m/s. Confidence: moderate. The main risk is the f conflict above; the alternative answer is ~4.9.
Scripts: solve.py, final.py (answer), joint.py, wheeldiam.py, wheelasp.py, heading.py, manhole*.py, level.py, pedsize.py.
