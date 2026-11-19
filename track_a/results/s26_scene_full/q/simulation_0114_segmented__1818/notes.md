# q_1818: speed of the plane at 1.5 s (prior: acceleration = 18 m/s^2)

- 2D top-down clip, 24 fps (the file and question_fps agree, so no re-timing). The plane moves straight down from rest at frame 0.
  t = 1.5 s means frame 36.
- Track: scene/tracks/airplane.csv `ref_y` (template-matched bbox centre, about ±1 px). Notes and frame checks: ref_x is constant, so the motion is vertical only.
- `fit.py`: a quadratic fit of ref_y over frames 0-75 gives acceleration 342.6 px/s^2 and v0 of about 1.6 px/s (≈0). The vertex is at
  t ≈ -0.005 s, so it starts from rest at t=0. Fits starting at frame 10 or 20 give 343.1 and 345.4 px/s^2, which agree with each other.
- Scale: 18 / 342.6 = 0.05254 m/px.
- Speed at frame 36, one-frame backward difference of the fitted track: 26.71 m/s. Instantaneous a·t value: 27.08 m/s. Theory with
  v0=0: 18·35.5/24 = 26.63 m/s.
- Second route: the mean raw per-frame step over frames 30-42, centred on frame 36, is 26.75 m/s. The raw single-frame steps are
  noisy (24-33 m/s) because of the ±1 px tracking error.
- Answer: 26.7 m/s. Confidence high: every reading falls between 26.6 and 27.1.
