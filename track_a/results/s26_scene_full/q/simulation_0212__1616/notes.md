# Q1616: distance between the black cat and the camera at t = 1.5 s (frame 36 at 24 fps; the file is also 24 fps)

The cat is mostly hidden behind the dog in frames 28–40, so frame 36 cannot be measured directly. I worked from the
given depths and the speed prior instead.

## Main route (closed form, solve.py)
The cat walks on a straight line at a constant speed, so P(t) = P0 + v t with |v| = 0.94 m/s (the prior).
- |P0| = 4.199 and |P0 + v| = 4.481, so 2 P0·v = 4.481² − 4.199² − 0.94² = 1.5642.
- D(1.5)² = 4.199² + 1.5·1.5642 + 2.25·0.94² = 21.966, so **D(1.5) = 4.687 m**.
This result needs no focal length.
- To check it, I solved for the focal length from the rays through the core centroid at frames 0 and 24
  (f ≈ 2100–2156 px, horizontal FOV about 48°). Its predicted pixel positions match frame 12 to within about 5 px,
  and frames 45–49 to within about 15 px.

## Second route (fit.py)
I fitted a 3D line to the cat's core centroids in frames 0–23 and 45–49, with the focal length, P0 and v all free
and only the two given depths imposed. The speed was not imposed.
- Straight-line fit: RMS error 3.3 px. The residuals look like gait wobble, not a trend. It gives D(1.5) = 4.700 m,
  with a fitted speed of 1.03 m/s.
- Fit that also allows a depth acceleration: D(1.5) = 4.678 m.
So the track fits a straight path, and the three estimates fall within 4.68–4.70 m.

## Answer
4.687 m (the closed form, which uses the exact prior speed). Confidence: high; the routes disagree by less than 0.5 %.
