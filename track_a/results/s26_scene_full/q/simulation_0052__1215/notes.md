# q1215 – height of the orange car (m)

File fps 30.003297; question_fps 30 is used (frame indices from the scene record).

## Method
- Pixel height (side profile, frames 50-90, car fully in view): roof crest at row 643 to near-side tyre contact
  at row 794 = 151 px (from scene/tracks, confirmed on a zoomed grid crop of f60 (c60.png)).
- Scale from the prior (route 1): the orange car moves parallel to the image plane (hub separation stays 323.2 px).
  A quadratic fit to the measured hub reference x over f6-80 (excluding the interpolated/extrapolated frames;
  residual ≤0.65 px) gives 0.3346 px/frame² (sub-windows: 0.331 for f6-34, 0.338 for f46-80) = 301.1 px/s².
  The fit's stop frame is 87.1, which matches the observed stop. m/px = 2.86/301.1 = 0.009497 (at the depth of
  the near-side hubs) → H = 151 × 0.009497 = **1.434 m**.
- Route 2 (depth_info): if the perpendicular depth Z is the same at t=0 (d=17.260, u≈1345, extrapolated) and at
  t=1 (d=15.436, u=621.3), then f ≈ 1588 px, Z ≈ 15.3 m and Z/f = 0.009637 → H = 1.455 m. That is the
  origin-depth scale, and it relies on the extrapolated t=0 position. Agreement with route 1 is 1.5%.
- Perspective check: the near side measured gives 151 px, while the roof crest lies slightly deeper. Lamp-pole
  verticals spread apart toward the bottom of the frame (verticals.py), so the camera is tilted slightly up and
  the horizon is near row ~620-650, close to the roof row. The roof is seen almost edge-on, so the depth
  correction is below 1% (1.39 even in the worst case, horizon at 540).

## Answer
1.43 m (sanity check: a typical sports sedan is ~1.40 m tall). Confidence: good, about ±3%.
