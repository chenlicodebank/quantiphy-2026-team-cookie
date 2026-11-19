# q_766: speed of the basketball at t = 1.5 s (m/s)

The prior is the basketball's diameter, 0.282 m. This is a 2D video, so I used one scale from the ball's pixel diameter. question_fps and the file's fps are both 24, so t = 1.5 s is frame 36, and the speed is the backward difference |p36 - p35| x 24. The ball is still rising after the bounce at frame 24, so frames 26-49 are free of impacts.

## Measurements (scripts in this folder)
- `measure.py` uses the HSV colour mask from the scene record and fits a least-squares circle to the contour in frames 26-49. It gives the centre at frame 35 as (986.90, 823.95) and at frame 36 as (986.67, 812.23), which matches scene/tracks/ball.csv. The raw displacement is 11.72 px, or 281.2 px/s.
  A parabola fitted to the ascent (frames 26-49) gives a backward difference of 11.75 px, or 282.0 px/s.
- Ball diameter (`edges.py`): 12 radial profiles per frame, with sub-pixel 50 % crossings of the colour distance from the local background, give 75.4-75.7 px (frames 0, 35, 36, 49). The binary mask's area-equivalent diameter is 75.6 px.
  - The circle fit to the binary contour gives 74.6 px. That method is biased low by about 1 px, because the contour runs along the centres of the edge pixels.
  - The saturation-based edge gives 73.7 px. It is biased low because the shaded limb of the ball has lower saturation.
  - I used **D = 75.5 px**, so the scale is 0.282 / 75.5 = 3.735e-3 m/px.
- SAM 3 (`basketball` on frames 35 and 36, instance k0):
  - **Centre:** the SAM centroid (986.7, 812.3) agrees with mine to 0.1 px. The displacement from the SAM box centres is 12.0 px against my 11.72 px, a 2.4 % difference. That is under 3 %, and the SAM boxes are coarser.
  - **Diameter:** SAM gives 4733 px area, an area-equivalent diameter of 77.6 px, and a box of 75.3 x 76.9 px. That is 2.7 % above my 75.5 px.
  - **Which diameter is right:** in the zoomed overlay `frames/check36.png`, the SAM outline bulges 2-3 px outside the ball on the left and right sides. A circle of 75.5 px follows the visible edge, so I kept 75.5 px.

## Result
speed = 11.73 px x 24 x 3.735e-3 = **1.051 m/s** (raw difference 1.051, parabola route 1.053).

## Second route
The parabola fit to the whole ascent reproduces the raw one-frame difference to 0.3 %. The SAM centres give 1.075 m/s with my scale, which is 2.3 % higher.

## Confidence
High, roughly ±2 %. The main uncertainty is the edge definition of the diameter (74.6-75.7 px).
