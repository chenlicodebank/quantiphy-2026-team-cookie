# Q1283: length of the white car (white cargo van)

The "white car" is the white van on the cross street (scene/tracks/van.csv). It translates horizontally at constant image size, so it stays at a constant depth and moves parallel to the image plane. Image x is therefore linear in world X, and one m/px scale applies. The file fps and question_fps are both 24.

- Pixel length: 453 px, rear bumper to front bumper. I checked it on frame 54 (rear ≈1034, front ≈1487) and frame 57 (rear ≈1121–1124).
- **Route 1 (prior)**: a quadratic fit of ref_x against t = frame/24 over f1–71 gives an acceleration of 307.2 px/s² (rms 0.53 px). Sub-windows give 22–71: 307.4, 36–71: 307.5 and 2–35: 311.2; only 54–71 gives 322. So the scale is 4 / 307.3 = 0.01302 m/px, and L = 453 × 0.01302 = **5.89 m**.
- **Route 2 (depth_info)**: the white-car distances are 30.065 m at f14 and 29.307 m at f38. With constant Z, D1² − D2² = (Z/f)²(X1² − X2²), using box-centre x offsets from cx = 1080 (−564 and −220 px). This gives Z/f = 0.012929 m/px, so L = **5.86 m**.
- The two routes agree within 0.5%. Answer: 5.88 m (a plausible full-size van). Confidence: high, ±3%.

Scripts: fit.py (both routes), edges.py (attempted edge profile, contaminated by taxi and cyclist; the visual check was used instead).
