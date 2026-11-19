# Q173 — height of the plane (m)

2D video at 24 fps (question_fps = file fps = 24, so no re-timing). The prior is the car's acceleration, 10 m/s², and it sets one metres-per-pixel scale for the whole frame (the record shows both objects at the same depth).

## Car acceleration in pixels
- Route 1 (fit.py): a quadratic fit to the record's car x tracks (frames ≥1) gives 0.347–0.353 px/frame²
  (bbox centre 0.3494, mask centroid 0.3506).
- Route 2 (measure2.py): I tracked the car's grey-level template with subpixel brute-force matching and fitted a
  quadratic over frames 1–40. This gives a = 0.3527 px/frame² (fit residual rms 0.025 px), and the result holds
  for every start frame. The per-frame steps grow linearly (0.92 … 14.31 px/frame), so the acceleration is uniform.
- I used a = 0.3527 px/frame² × 24² = 203.2 px/s², so the scale is 10 / 203.2 = 0.04922 m/px.

## Plane height
- The plane is fully visible in frames 0–10. Its vertical extent from fin top to engine bottom is y 284–510, which
  is 227 px (225–228 depending on the threshold, at frames 3, 5 and 8). This matches the record's 226.8 px.
- Height = 227 × 0.04922 = **11.17 m** (11.1–11.2 m across the range of a and pixel height).

## Sanity check
- At this scale the car is 113.5 px × 0.0492 = 5.59 m long, close to a Cybertruck's 5.68 m.
- The plane's 750 px length gives 36.9 m, close to an A320-family airliner (37.6 m long, 11.8 m tall).
- Confidence: high (about ±2%).
