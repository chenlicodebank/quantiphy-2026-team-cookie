# q_1453 — speed of the car at t = 1.0 s (prior: a = 5 m/s^2)

File fps = question_fps = 24, so t = 1.0 s is frame 24.

## Method (fit_track.py)
- Image track (scene/tracks/car.csv: est_cx/cy centroid and bbox top-left corner x0,y0) lies on a straight image line
  (2nd singular value 0.6 px vs 3846 px), as expected for straight-line 3D motion.
- For uniform acceleration from rest along a 3D line, the position along the line is lambda = 0.5 a ((i - s)/24)^2
  and its image coordinate along the line is projective: w = (A + B q)/(1 + E q), q = (i - s)^2.
  Fitted to the track:
  - centroid frames 21-71: rms 0.13 px, s = -0.46
  - x0 corner frames 0-71: rms 0.46 px, s = 0.01; frames 0-40: s = 0.08; frames 21-71: s = 0.41
  The excellent fit confirms constant acceleration from rest; the start frame is s ≈ 0 (car at rest at t = 0).
- Speed by the benchmark convention (one-frame backward difference at frame 24):
  v = 0.5·a·((24-s)^2 - (23-s)^2)/24^2 · 24 = 5·47/48 = 4.896 m/s for s = 0
  (range 4.81–4.99 over the fitted s values; the instantaneous a·t would be 5.0).

## Check against depth_info
Fitted perspective term gives z ∝ 1 + 0.0477·lambda (lambda in m with a = 5): z(48)/z(24) = 1.32, vs given
distance ratio 23.199/17.828 = 1.30, and implies a plausible depth-axis direction component ≈ 0.76. Consistent with a = 5.

Answer: 4.896 m/s. Confidence: high (±2%).
