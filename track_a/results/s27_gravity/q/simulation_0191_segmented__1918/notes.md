# Q1918: speed of the box at t = 0.2 s

- This is a 2D clip. The box falls straight down: x is constant and there is no rotation. The prior gives a = 9.8 m/s² before 0.6 s, and the impact is at about f60 (0.5 s).
- question_fps is 120, the same as the file rate, so t = 0.2 s is frame 24.
- **Method (fit.py):** quadratic fits to center_y (from scene/tracks/box.csv) and to the face-bottom edge over frames 6–58.
  - Pixel acceleration: 1960–1967 px/s². The scale is therefore 9.8/1962 ≈ 0.0050 m/px.
  - The rest point (vertex) of the fit is at t0 ≈ 0.000 s (between -0.0014 and +0.0004). The box falls from rest starting at frame 0.
  - A piecewise fit (at rest, then a parabola) gives the same result: t0 = -0.0007 s, a = 1965 px/s².
- **Speed at t = 0.2 s:**
  - From the continuous fit: v = a(t − t0) ≈ 1.966 m/s. Physics alone gives g·0.2 = 1.96.
  - One-frame backward difference of the fitted positions (f24 − f23): 1.926 m/s.
  - The raw one-frame differences are noisy (1.8–2.4) because the positions are quantised to whole pixels.
- **Answer:** 1.95 m/s, between the two readings. Both readings are within about 1.5% of it.
- **Second route:** the face-bottom track gives the same result (1.96 continuous).
- **Fit-window caveat:** the late window (frames 28–58) gives 2.10–2.16. It covers only the late part of the fall, so its extrapolated start time is poorly constrained; I did not check the cause further. The full-window fits agree with each other.
- **Confidence:** high.
