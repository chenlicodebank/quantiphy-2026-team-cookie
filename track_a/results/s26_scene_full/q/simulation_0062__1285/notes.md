# q1285 – height of the turning yellow car (taxi)

The question and the file both use 24 fps. The camera is static and level, and the horizon is at y = 540 (cy = 540, cx = 1080).

## Focal length (focal.py, cyc.py)
- The white van moves at constant depth, parallel to the image plane. Its two given distances (30.065 m at f14, u = 516; 29.307 m at f38, u = 860) give f = 2256 px and Z_van = 29.17 m.
- The prior (4 m/s²) with the van's pixel acceleration (307.2 px/s², quadratic fit, rms 0.5 px) gives f = 2240 px. I used f = 2248 px.
- Checks: the cyclist's distances are reproduced (27.15 m predicted vs 27.07 m given at f38). The pedestrian comes out at 252 px → 1.82 m tall, which is plausible.

## Taxi height = AABB from the tyre contact to the top of the roof sign
- H = hc + (540 − v_top)·Z_sign/f, where hc is the camera height above the ground. With a level camera, the ground-to-horizon part equals hc.
- Top of the sign, from luminance and chroma profiles (signtop.py) and zoomed crops: 486 at f14 and 477.5 at f38 (±1 px).
- Taxi origin depth: Z = D/sqrt(1 + (du² + dv²)/f²). At f14 that is 24.855 → 24.49 (u ≈ 690). At f38 it is 21.723 → 21.67 (u ≈ 920).
- Camera height from ground contacts at known depths:
  - cyclist rims at 620.5, Z = 27.0 → 0.967
  - pedestrian's lowest foot → 0.975–1.0
  - van near wheels → about 0.94 (assumes a van width)
  - taxi f14 wheels → about 0.97
  - taxi f38 front wheels → about 1.0 (assumes an axle offset)
  
  I took hc ≈ 0.97.
- Results: f14 gives 0.97 + 54·24.49/2248 = 1.558 m. f38 gives 0.97 + 62.5·21.67/2248 = 1.572 m. The two frames are independent and agree, so I answer **1.56 m**.
- The scene/ record's taxi bbox_y0 and ground_y at f14 and f38 (467/638 and 466/661) are wrong: the box top includes something above the sign. I did not use them.

Confidence: moderate-to-good, about ±3%. The main uncertainty is the camera height (0.94–1.0), which moves the answer by about ±0.03 m.
