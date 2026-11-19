# q1422 – trolley speed at t = 1 s

Prior: the trolley (shopping cart) accelerates at 1.507 m/s² (exact). question_fps = 24 = file fps, so t = 1 s is frame 24.

Start of motion: I fitted x(n) = x0 + b·(n−n0)² (+ a small cubic term for perspective) to scene/tracks/cart.csv
bbox_cx (fit.py). This gives n0 ≈ 0.15–0.17 frame over frames 0–24, 0–30 and 0–36, with residuals of about 0.6 px.
So the cart starts from rest at frame 0. A check on the pixel ratio agrees: x(24)−x(0) = 155.5 px and
x(12)−x(0) = 38.5 px, a ratio of 4.04 (≈ 4 for t²). The track shows no stop or impact before frame 24.

Speed under the benchmark convention (one-frame backward difference at frame 24, uniform acceleration from rest
at frame 0):
v = a·(24² − 23²)/(2·24) = 1.507 × 47/48 = 1.476 m/s.
Continuous value a·t = 1.507 m/s, which is 2 % higher.

Depth check: the depth goes from 12.589 m to 12.513 m over 0.5 s. That is consistent with the cart moving about
0.19 m (= ½·1.507·0.5²) along a path slightly toward the camera.

Answer: 1.476 m/s. Confidence: high (both readings are within about 2 %).
