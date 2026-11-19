# q_1291 – height of the walking pedestrian (m)

File fps = question_fps = 24, so frame = round(t*24): t=0.58 -> f14, t=1.58 -> f38. Static, level camera; principal point taken as (1080, 540).

## Focal length (two independent routes)
- Route A (van/"white car" depths): van origin u = 516.4 (f14) and 860.0 (f38), v ≈ 534 (scene track, constant image size → constant optical-axis depth).
  d² = Zc²(1 + ((u-cx)²+(v-cy)²)/f²) solved for both given distances (30.065, 29.3069) → f = 2256 px, Zc = 29.17 m.
- Route B (prior, a = 4 m/s²): quadratic fit to the van's track gives 307.2 px/s² (same from f1+ or f22+).
  f = a_px·Zc/4 → f = 2239 px. Route A predicts a = 3.97 m/s² (0.8 % from the prior). Use f ≈ 2250.

## Pedestrian
- Pelvis x (track ref_x): 269.8 (f14), 204.7 (f38). Optical-axis depth from given distances:
  Z14 = 17.2804/sqrt(1+(810²+5²)/f²) = 16.26 m; Z38 = 16.1558/... = 15.06 m.
- Pixel height (head top → lowest sole), re-measured in code (ped2.py, background residual): f14 249 px (record 252), f38 270 px (record 272).
  Visual check of crops (frames/ped14_raw.png, ped38_raw.png) agrees within ~3 px (bottom may include a contact shadow of 1-3 px).
- H = h·Z/f: f14 → 1.80–1.82 m; f38 → 1.80–1.82 m. The two times (different depth and size) agree, confirming f and the depths.

Answer: **1.81 m**. Confidence: high (±2 %); main uncertainty is walking vs rest height (gait dip of the head) and a few px at the feet.
