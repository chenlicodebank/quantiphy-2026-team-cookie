# q_193: boat length (m). Prior: shark acceleration = 1 m/s^2

2D side view, static camera, 24 fps (file fps = question_fps, no re-timing).

Scale: a quadratic fit of the shark's x(t) over frames 1-72 (fit.py, scene/tracks/shark.csv) gives an acceleration of
-85.9 px/s^2 for the centroid, -86.6 for the bbox centre, -86.8 for the nose and -86.4 for the tail. Fits over the
first half (frames 1-36) and the second half (36-72) agree to within ±1.5 px/s^2, so the acceleration is constant.
I take 86.3 px/s^2, which gives 1/86.3 = 0.01159 m/px.

Boat length: 858 px from bow tip to stern (856-860 px over frames 26-72, the frames where the whole boat is visible).
I confirmed this on frame 72 with a grid: the bow is at x≈227 and the stern at x≈1085.
Length = 858 / 86.3 = 9.94 m.

Second check: the shark comes out at about 275 px, which is 3.2 m, and the boat at about 10 m. Both are
realistic, and the acceleration estimates from the different shark reference points agree to within about 1%.
Confidence: high (about ±2%).
