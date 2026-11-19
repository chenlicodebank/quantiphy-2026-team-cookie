# Q937 — length of the spacecraft (m); prior: acceleration at 1.0 s = 4 m/s^2

The "spacecraft" is the single black vehicle (the record calls it a snowmobile). It is seen from above and moves
left along row y≈720, starting from rest at about frame 1. The camera is static, and fps = question_fps = 24.

## Scale from the prior (fit.py)
Quadratic fits of x(t) from scene/tracks/snowmobile.csv over frames 2-60 (and the sub-windows 5-40, 10-35, 20-60):
- bbox centre: 508-513 px/s^2 (rms 0.5 px). A cubic fit gives 514 at t=1 s, so the acceleration is uniform.
- rear edge x1: 519-523. Front edge x0: 495-506 (noisier). The centre is the mean of the two, ≈513.
- I used a = 513 px/s^2, so the scale is 4/513 = 0.00780 m/px.

## Pixel length (lencentre.py)
The bbox length changes linearly with horizontal position: 786 px at x≈1995 and 741 px at x≈400 (rms 1.1 px
from the line). This is perspective parallax from a camera looking straight down, where parts at different
heights shift differently away from the image centre. The width (rows 536-902) stays constant because the
vehicle runs along the centre row. I took the length at the image centre (x=1280): the fit gives 767.3 px, and
frame 40 (cx=1287) measures 768 px directly.

## Answer
767.3 px × 4/513 = **5.98 m**.

Check: frame 40 measured directly gives 5.99 m. The off-centre extremes would give 5.78 m and 6.13 m (±3 %).
Using the rear-edge acceleration instead of the centre's gives 5.89 m.
Confidence: about ±3 %.
