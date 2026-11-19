# q_1891 — displacement of the elephant (m)

Prior: speed of the elephant = 1.424 m/s. 2D clip, 24 fps (file and question rates agree), 60 frames (t = 0 to 59/24 = 2.458 s).

## Method
- The elephant walks right in a straight line at a steady speed. There are no starts, stops or turns, and vertical drift is only 3 px (check.py on scene/tracks/elephant.csv).
- Pixel speed is steady. Linear-fit slopes over 15-frame windows are 3.2–3.9 px/frame for the mask/body centroids and 3.28–3.46 px/frame for the head-end torso edge, which is the most stable. A quadratic fit shows no meaningful acceleration.
- Since the speed is constant, displacement = v × T = 1.424 × 59/24 = **3.50 m**.

## Second route (pixel scale)
- Scale = 1.424 m/s ÷ (3.40 px/frame × 24) = 0.01745 m/px, using the mean centroid speed (net 200.7 px / 59 frames). Net displacement 200.7 px → 3.50 m. The torso front edge gives 200 px → 3.49 m.
- Using the fitted slope of 3.36 px/frame for the scale would give 3.54 m. The two routes agree within about 1%.

## Confidence
High, if the prior is the constant walking speed.
