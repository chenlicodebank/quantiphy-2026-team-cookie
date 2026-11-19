# Q951 — speed of the phoenix at 0.5 s (m/s)

Prior: acceleration at 2.0 s = 2 m/s^2. 2D video, 24 fps (file fps = question_fps), static camera.

## Method (fit.py)
- Track: beak_x from scene/tracks/bird.csv. I checked it against the record notes and the contact sheet: it is the only bird, the motion is horizontal and leftward, and y stays constant to within 4 px.
- Model: x(n) = quadratic in the frame number + Fourier terms with a fitted period of 25.0 frames (the wing-flap cycle moves the head fore and aft).
  - Beak, H = 1–3 harmonics: a = 0.4134–0.4140 px/frame^2, v(0) ≈ 0.00–0.03 px/frame, so the bird starts from rest at frame 0. The rms residual is 0.95 px, which is about the 2 px quantisation.
  - Mask centroid, as an independent reference point: a = 0.415–0.417 px/frame^2, and v(0) is again ≈ 0.
  - Same-flap-phase triplets (frames p, p+25, p+50), a model-free second difference: a = 0.410–0.422, mean ≈ 0.414.
- So the origin moves with uniform acceleration from rest: a = 0.4135 px/frame^2 = 238.2 px/s^2.
- Scale: 2 m/s^2 / 238.2 px/s^2 = 0.008397 m/px.

## Answer
- Speed at t = 0.5 s is taken at frame 12, using the backward difference |p(12) − p(11)| × fps.
  - Under uniform acceleration from rest this is a·(11.5/24) = 2 × 0.4792 = **0.958 m/s**.
  - In pixels: 0.4135 × 11.5 = 4.755 px/frame = 114.1 px/s, and 114.1 × 0.008397 = 0.958.
- Instantaneous a·t would give 1.00 m/s, which is 4 % away. I followed the stated backward-difference convention.
- Confidence: high. The ratio of speed to acceleration does not depend on the scale, and a and the rest start are consistent across the beak fit, the centroid fit and the triplet second differences.
