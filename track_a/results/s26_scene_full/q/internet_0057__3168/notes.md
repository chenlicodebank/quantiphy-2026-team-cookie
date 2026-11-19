# q3168 – ball-to-floor distance at t = 4.00 s (frame 120, 30 fps)

Prior: g = 9.8 m/s². file fps = question_fps = 30, so frame 120 (no re-timing; scale from g gives a
ball diameter of 47 px × 0.0052 = 0.244 m, a real basketball, so 30 fps is plausible).

## Scale (fit.py)
Fitted quadratics to the ball's bg-fixed centre y (scene/tracks/ball.csv, checked against frames) on clean
free-flight segments: 55–72: 1897 px/s²; 78–96: 1810; 100–133 (the arc that contains t=4.0): 1889 (rms 1.3 px);
138–162: 1857; 166–186: 1870. Scale used: 9.8 / ~1885 ≈ 0.0052 m/px.

## Floor (contact.py)
Floor contact = where neighbouring parabolas intersect: centre y 886.6 at frame 97.1 (x 1302) and 880.4 at frame
134.9 (x 1515). Interpolated to the ball's x at frame 120 (1430): ball centre at contact ≈ 882.9 px.
Ball centre at frame 120: 527.6 px measured (526.3 from the fit). Checked on a zoomed frame (frames/f120.png).

## Result
- Gap from the ball's bottom to the floor = centre rise above its contact position = 355 px → 1.85 m.
- Centre height above the floor = 355 + radius 23.5 = 379 px → 1.97 m.
The question doesn't say which reference point it means, so I answer 1.90 m, about halfway between the two
(about 3 % from either).
Second route: the ball's bottom edge on frame 120 is at about 550 bg-fixed px, and its bottom at the bounces is
at about 902–906 px, which gives a gap of about 354 px. That agrees with the parabola route.
Confidence: moderate-high (scale ±3 %; the main uncertainty is which reference point is meant).
