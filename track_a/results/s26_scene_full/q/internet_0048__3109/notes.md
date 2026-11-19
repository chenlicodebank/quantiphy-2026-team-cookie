# Q3109: walker's average speed, 2.50–3.50 s (frames 75–105 at 30 fps)

The file's fps and question_fps are both 30, so no re-timing.

Scale from the prior (g = 9.8 m/s²): I fitted a quadratic to the ball's free flight in scene/tracks/ball.csv, using
camera-compensated y over frames 36–60 (after release, before the bounce at frame 61). The fit gives
a = 3713 px/s² (rms 0.6 px). Other windows and columns give 3694–3787 px/s².
Scale = 9.8/3713 = 0.002639 m/px. Sanity check: a 94 px ball diameter gives 0.248 m, which matches a real
basketball (0.24 m). The scale is consistent.

Walker: head track head_x_bg0 (camera-compensated) goes from 128.19 px (frame 75) to 686.00 px (frame 105).
That is 557.8 px in 1.0 s, or **1.472 m/s**. The mean of the forward-difference speeds equals this net value.
- Including the head's vertical bob (2D path length) gives 1.483 m/s.
- Second route: the hand-read hip x from frame 78 to 105 (128 → 631 px) gives 1.475 m/s.

Answer: 1.473 m/s. Confidence: good. The main uncertainty is the ±1.5 % spread in the scale fit, and whether the
ball's plane matches the walker's (the ball's size suggests it does).
Scripts: fit.py, speed.py.
