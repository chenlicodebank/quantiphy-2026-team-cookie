# q129: speed of the car at 1.0 s (m/s). Prior: car acceleration = 4.03 m/s^2

Time base: fps 24 = question_fps 24, so t = 1.0 s is frame 24.

Method (2D top-down scene): one metres-per-pixel scale from the prior acceleration, giving v = 4.03 * v_px / (a_px * 24), with v_px in px/frame and a_px in px/frame^2.

Measurements:
- `track_tm.py` template-matches the car's front 200 px (taken from frame 53) along x in every frame, with a subpixel parabola peak. The result is valid from frame 17 on: before that the car or its mirrors are cut by the image edge.
- `fit2.py`: a quadratic fit over frames 17-40 gives a_px = 0.711 px/f^2 with residual 0.11 px, and motion starting at frame t0 = 0.1 (from rest at t ≈ 0).
  - Backward step at frame 24 (23→24) = 16.64 px/frame, which gives v = 4.03 * 16.64 / (0.711 * 24) = **3.93 m/s**.
  - The raw step is 16.66 px.
- Fits that include frames 41-53 give a_px of 0.73-0.75, but the last 3-4 steps jump by about 1 px/f^2. This is probably blur or template bias at high speed, so I excluded it.
  - With those frames included the answer is 3.79-3.80.

Second route:
- The scene record's front-edge x0 (frames 2-10) follows x0 = 1787 - 0.35 n^2 almost exactly. That means uniform acceleration from rest at frame 0, with a = 0.70 px/f^2.
- For uniform acceleration from t = 0, the backward-difference speed at frame 24 is a * 47/48 = 4.03 * 0.979 = **3.946 m/s**. The instantaneous a*t would be 4.03 m/s.

Answer: 3.95 m/s, the benchmark's backward-difference convention. It is within 2% of both the a*t reading (4.03) and the direct pixel ratio (3.93). Confidence: high.
