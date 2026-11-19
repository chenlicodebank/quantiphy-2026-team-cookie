# q_668 — width of the TV stand (m)

Width = the front-to-back depth of the dark media console along the top wall (per the naming rule: TV stand width = depth).
Prior: robot vacuum diameter = 0.438 m. depth_info: none. fps 24 = question_fps (time is irrelevant here; static object).

## Measurements (frame 77, code: measure.py, edge2-4.py, final.py)
- Robot vacuum: circle-fit diameter 117.8 px (median over the non-occluded frames in scene/tracks; checked).
- Console back edge (image top): y = 168.3 (luma gradient at x 713-722, the only stretch not hidden by the shadow).
- Console front edge: the top surface ends at y ≈ 282.5 (luma step at all columns from 790 to 1130); then there is a ~10 px
  darker, warmer band (the console's **front face**, visible because of perspective) down to a sharp floor edge at y = 292.7.
- Naive single scale (back edge to floor edge, 124.4 px): 0.4625 m. This counts the front face and the magnified top, so it is too big.

## Perspective correction
Overhead camera with the principal point taken at the image centre (960, 540). The top-surface magnification relative to
the floor is k = (540-282.5)/(540-292.7) = 1.041. Check: the radial model predicts that the front face's floor-level left corner
is at x = 960-(960-711)/k = 720.9; the measured value is x = 721 (row 291). So the model holds: the front face reaches the
floor, and the principal point is near the centre. The TV panel's top and bottom edges also form a radial trapezoid (~8 % scale change), which matches.
Top depth = 114.2 px at top-surface scale, which is 109.7 px at floor scale. The vacuum's top rim sits slightly above the floor
(I assumed h_v/Z ≈ 0.012, i.e. about 0.1 m at a camera height of about 8 m; the range 0 to 0.02 changes the answer by
-1.2 % to +0.8 %).
Width = 0.438 x 114.2/117.8 / 1.041 / (1-0.012) = **0.413 m** (range 0.408-0.416).

## Confidence
Moderate to good. The main uncertainty is whether the band at y 282-292 is the front face (the corner geometry strongly
supports this). If it is not, the answer would be about 0.46 m.
