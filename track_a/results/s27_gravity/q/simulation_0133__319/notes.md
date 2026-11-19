# q_319: speed of the apple at t = 1.2 s (frame 36 at question_fps 30, which matches the file's fps)

Method (2D video, one m/px scale taken from the gravity prior), in fit.py:
- I used the apple track from scene/tracks/apple.csv (cx_ref, cy_ref). The apple is in free fall from frame 35 to frame 47. It leaves the counter edge at frame 34 and lands at frame 48.
- I fitted a quadratic to y over frames 36-47: a = 7.077 px/frame² = 6369 px/s². Residual rms is 0.16 px. The vertex is at frame 34.44, which is consistent with leaving the edge at frame 34.
- Scale = 9.8 / 6369 = 0.001539 m/px. Check: the apple's 62 px diameter comes to 9.5 cm, which is a realistic apple size.
- x is linear, with vx = -14.32 px/frame.
- The speed at frame 36 is the backward difference between frames 35 and 36: 0.745 m/s from the fitted curves, and 0.754 m/s from the raw track.

Robustness: changing the fit window (35-47, 37-47, 38-46) gives a = 7.05-7.08 and a speed of 0.745-0.750 m/s from the fit, or 0.754-0.756 m/s from the raw track.

Answer: 0.75 m/s. Confidence is high (about ±2%).
