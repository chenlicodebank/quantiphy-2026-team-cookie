# Q1544 – speed of the blue car (light-blue cart) at t = 1 s

question_fps = file fps = 24 → t = 1 s is frame 24; speed = |p(24) − p(23)| × 24.
The blue car moves left → right parallel to the image plane at constant depth (constant hub row and apparent
size), so its speed is (pixel step) × (metres per pixel at its depth). The origin moves like any other rigid point
on the cart, so the near-side pixel step × the near-side scale gives the origin's speed.

## Pixel step at frame 24 (shift.py, template matching with sub-pixel peak)
| step | scene track | chassis+wheels | front wheel | rear wheel |
|---|---|---|---|---|
| 22→23 | 46.44 | 46.93 | 46.40 | 47.18 |
| **23→24** | **47.85** | **47.80** | **47.60** | **47.81** |
| 24→25 | 47.76 | 48.35 | 48.02 | 48.54 |
→ 47.75 px/frame (±0.2) = 1146 px/s.

## Scale (metres per pixel at the cart's near side)
- Rear near-side tyre, frames 37/38 near the image centre (extent.py, half-level edges, overlay checked):
  width 107.7 px → 0.369/107.7 = 3.426e-3 m/px.
- Front near-side tyre measures 112.2 px (W = H, frames 34-39). That is 4 % larger than the rear tyre and
  inconsistent with the two checks below, so I did not use it. With it the scale would be 3.29e-3 and the speed 3.77 m/s.
- Check 1 (depth_info): right (near-side) front tyre at frame 24, hub (623.5, 892.5), r = 487 px from the principal
  point (960, 540). s = 9.312 / sqrt(f² + r²). With f = 2667 px (50 mm lens on a 36 mm sensor) s = 3.435e-3,
  which matches the rear-tyre value, i.e. 0.369 m ↔ 107.4 px.
- Check 2 (floor geometry plus the yellow-car tyre, independent of the cart tyres): yellow front tyre hub
  (904.4, 797.6), bottom 893.8 → D = 192.4 px for 0.764 m, so camera height = 354.8·0.764/192.4 = 1.409 m. The cart's
  ground contact is 409.4 px below the horizon (y = 539), so s = 1.409/409.4 = 3.441e-3. The f that this implies
  from depth_info is 2662 px (≈ 50 mm).
- Adopted s = 3.43e-3 m/px. The hub faces are ~5 cm nearer than the tyre centre, so this is about 0.5 % smaller
  than the depth-route value at the tyre centre.

## Answer
v = 47.75 × 24 × 3.43e-3 = **3.93 m/s**. The routes give 3.92–3.94; using the front tyre would give 3.77.
Confidence: good (±2 %), with the main residual risk being the front/rear tyre-size discrepancy.
