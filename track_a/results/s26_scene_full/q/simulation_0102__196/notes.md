# q196 — shark speed at t = 0.0 s (prior: shark acceleration = 1 m/s^2)

2D video, 24 fps (file fps = question_fps). The shark swims left in the lower panel and speeds up uniformly. Frames 0
and 1 are identical (a hold before the motion starts); from frame 1 on, x(f) is an exact quadratic.

Method (fit.py): a quadratic fit x(f) = c0 + c1 f + c2 f^2 to the shark track (scene/tracks/shark.csv, mask
centroid), frames 1–60, where the shark is fully visible. Residual 0.54 px. The fitted value at f1 (794.48) matches
the measured 794.77, so the track is consistent.
- Pixel acceleration = 2|c2| x 24^2 = 86.54 px/s^2. Since this equals 1 m/s^2, the scale is 0.011555 m/px.
- Pixel speed at the start: 172.4 px/s (fit extrapolated to f0) to 176.0 px/s (fit at f1), which gives
  1.99–2.03 m/s.
- The sub-fits (frames 1–30 and 30–60) agree to within about 3 % on the acceleration.

Second route: the nose-edge track gives 87.36 px/s^2 and 1.97–2.02 m/s. The tail edge is noisier because the tail
beats.

Answer: 2.0 m/s, the shark's initial speed under constant acceleration. The strict backward difference at frame 0 is
undefined, and frames 0–1 are a render hold. Confidence: high (about ±2 %).
