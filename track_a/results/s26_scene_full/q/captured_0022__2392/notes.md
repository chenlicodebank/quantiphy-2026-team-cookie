# q_2392: displacement of the ping pong ball between 0.6 s and 1.6 s (cm)

The video file and question_fps are both 24, so t=0.6 s is frame 14 and t=1.6 s is frame 38.
Camera: f = 0.5959*1280 = 763 px, principal point (640,360).

## Track
I used the ball centroids from scene/tracks/ball.csv. Overlays in the record were checked, and the centroid bias of about 1-2 px is constant, so it cancels in a displacement.
- f14: (435.71, 393.20)
- f38: (407.57, 508.96)

## Depth at f38 (not given)
The given depths are 1.751 m (f14), 1.687 m (f19) and 1.526 m (f29).
- **Main route (measure.py, check_s.py):** I back-projected the three given points along their rays at the given distances. They lie on a straight 3D line (residuals ≤4 mm), as expected for a ball rolling on a flat board with a straight image path. I then intersected the f38 ray with that line, which gives Z38 = 1.374 m (ray-line gap 3 mm).
- **Physics check:** the 3D path length along this line, s(t), over frames 12-45 is close to constant speed (~0.45 m/s, fitted acceleration ≈0.08 m/s², rms residual 0.57 cm), so the result is smooth and physical.
- **Depth-trend check:** extrapolating depth over time gives 1.392 m with a linear fit and 1.343 m with a quadratic fit. These bracket 1.374 m.
- **Ball-size route (size2.py, compare.py):** depth = k / half-max width, with k calibrated on the given depths. It gives Z38 ≈ 1.44 m, but it is noisy (±1 px, and the board glare behind the ball shrinks the half-max widths). It would also mean the depth change slows down while the image speed rises, which is inconsistent. I treated it as an upper bound and did not use it.
- **Sensitivity:** a ±1 cm error in any one given depth moves the answer by about ±1.3 cm.

## Result
- P14 = ray14*1.751 = (-0.452, 0.074, 1.690) m
- P38 = ray38*1.374 = (−0.394, 0.252, 1.292) m
- Displacement |P38 − P14| = **44.0 cm**. The plausible range is 42.6-46.5 cm across the depth routes; the size route alone would give 38.6 cm.

Confidence: moderate-good, with an expected error of about 5%.
