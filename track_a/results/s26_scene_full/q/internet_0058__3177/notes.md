# q3177: ball–floor distance at t = 2.00 s (frame 60, 30 fps; file fps = question fps)

## Scale from the prior (g = 9.8 m/s²)
fit.py fits parabolas to the ball centre `cy_stab_px` (scene/tracks/ball.csv, checked against the video) over the free flight (release at frame 22, catch at frame 64):
- frames 24-62: a = 2.2265 px/frame² = 2004 px/s², so 0.004891 m/px
- other windows (23-63, 26-60, 30-55, 24-42, raw or stabilised): 0.00483-0.00490 m/px; the falling half alone gives 0.00509
- Sanity check: ball diameter of about 50 px × 0.00489 = 0.245 m, which matches a real basketball (0.24 m).
- Value used: 0.00489 m/px.

## Floor level under the ball
- First bounce (frame 77, at x ≈ 1116, the same column as the ball at frame 60 at x ≈ 1118). Intersecting the pre- and post-bounce parabolas puts the contact centre at stabilised y = 894.9. Adding the radius (≈ 25 px) puts the floor at stabilised y ≈ 920. On a 3× zoom, the ball's bottom edge at frame 77 is at raw y ≈ 886-889, which agrees.
- Second route: the player's shoe bottoms at frame 60 are at stabilised y ≈ 913 (raw 889). She is standing just behind the ball's path.
- Value used: stabilised floor y ≈ 917 ± 4.

## Ball at frame 60
Stabilised y = 393.6 (raw 369.6), radius ≈ 24.5 px.

## Result
- Centre to floor: 523 px, which is 2.56 m (range 2.54-2.57 depending on the floor reference).
- Bottom of ball to floor (the gap): 499 px, which is 2.44 m (range 2.42-2.45).
- Answer: 2.5 m, between the two readings, so it is within about 2.5 % of either.

Confidence: moderate-high. The scale is good to about 1-3 %. The main uncertainty is whether the question means the ball's centre or its bottom edge (a 5 % difference).
