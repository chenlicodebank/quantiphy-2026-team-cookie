# Q3112 — height of the gray chairs (m)

Prior: average speed of the scooter rider = 3.8 m/s. Internet video, 2D convention, one scale. fps = question_fps = 30.

## Object
The "gray chairs" are the gray metal benches of the gray picnic table at the front left (frame 0, x ≈ 185–830).
The height is measured from the ground (bottom of the leg foot) to the top of the seat's front edge, at both bench ends (bench.py, zoomL/zoomR.png):
- left bench end (x≈200–250): seat top y≈1352, foot bottom y≈1492 → 140 px
- right bench end (x≈555–620): seat top y≈1356, foot bottom y≈1496 → 140 px

## Scale (speed.py)
I used the rider torso track from scene/ (unflagged frames 143–259) to get the mean horizontal speed:
- raw pixels: net 30.9 px/frame, linear fit 31.3
- background-relative: net 31.4, smoothed mean of per-frame speeds 31.3
- manual front-wheel readings f147→f233 (raw): 30.6
I took 31.1 px/frame, which is 933 px/s. The scale is 3.8 / 933 = 0.00407 m/px.

## Answer
140 px × 0.00407 = **0.57 m**

## Checks
- Rider cap-to-sole 420 px → 1.71 m, and scooter length 263 px → 1.07 m. Both are plausible, so the scale is sound.
- The benches are closer to the camera than the rider's path. Their true height is therefore probably lower (about 0.45 m). Following the single-scale planar convention, I report 0.57.
- Uncertainty: about ±3% from the pixel speed and ±2 px on the bench height.
