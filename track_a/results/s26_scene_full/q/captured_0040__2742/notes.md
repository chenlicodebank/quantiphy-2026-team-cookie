# Q2742 – velocity of the white ball at t = 1.5 s (cm/s)

Time base: question_fps = file fps = 24, so t = 1.5 s is frame 36. Frame 48 is t = 2.0 s.

## Data
- Ball centres come from scene/tracks/ball.csv. I checked frames 32-40 on a gridded crop
  (view.py -> frames/f32_40.png), and the centroids match the visible ball within about 2 px
  (f35 ≈ 691, f36 ≈ 756, f37 ≈ 786, f38 ≈ 820 px in x).
- Bounces happen at f33 (table) and f41 (table). Frames 34-40 are a single free-flight arc, and f36 is near its apex.
  At f36 the ball passes in front of the cup rim: its depth is 0.70 m, while the cup is at 0.842 m
  (the "8420m" in the question is a typo).
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Depth: 0.7045 m at f36 and 0.627 m at f48. For the frames in between I interpolated the depth linearly in time.
  The ball's apparent diameter roughly agrees (about 3.6 cm at f36 and 3.7 cm at f45).
  The result hardly depends on this: assuming a constant depth changes the speed by only 1 cm/s.
- Centres were back-projected as the unit ray x the Euclidean distance (measure.py, smooth.py).

## Results (3D speed at f36, cm/s)
- 5-frame smoothed forward difference, i.e. the mean of the forward-difference vectors for frames 34..38
  (= moving average of 5 positions, then forward difference): **86.0**
- Linear fit to frames 34-39: 87.8. Linear fit to 35-39: 85.3. Linear fit to 34-40: 83.6.
- Centred estimates (34-38 linear or quadratic, 34-40 quadratic): 99.3. Ballistic fit to 34-40: 91.4.
- Raw one-frame differences are erratic: 35→36 = 162, 36→37 = 71. The image steps around f33-36 are irregular:
  x moves 60 px, then 32 px. This looks like uneven frame timing in the capture, possibly a dropped frame.
  For that reason I used smoothed values only. Averaging the per-frame scalar speeds would give about 110,
  which is inflated by the jitter and was not used.

## Answer
89 cm/s. This is mostly the reference convention (5-frame smoothed forward difference = 86),
nudged toward the centred and ballistic estimates (91-99).
The lateral component is about 80-88 cm/s and the depth component about -25 to -30 cm/s.
Confidence: moderate, about ±8% because of the frame-timing irregularity.
