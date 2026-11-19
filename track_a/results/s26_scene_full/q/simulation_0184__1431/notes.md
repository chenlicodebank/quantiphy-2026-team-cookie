# q1431 – speed of the box at t = 1.5 s (simulation_0184, 3D Blender)

question_fps = file fps = 24, so t = 1.5 s is frame 36. Speed(36) = |p36 - p35| x 24.
Prior: box acceleration after 1.25 s = 1.58 m/s^2. Depth: 9.194 m at f0, 9.096 m at f12.

## Measurements (scripts in this folder)
- `tm.py`: template-matched the box in the free fall (f0–7: pure translation, cx constant to ±0.3 px, so the camera is
  level). Fall is from rest: 4.17 px/frame^2. With g = 9.81, Z0 = 9.194/n0 = 9.03 m, this gives **f ≈ 2210 px**.
  Same script: multi-scale template track on the ramp, f20–44.
- `ecc.py`: affine ECC tracking of a box-face patch from f30 over f20–44. Gives a rigid point (u,v) and the image
  stretch along the box long axis (0.949 → 1.127) and across it.
- `fit3d.py`: the ramp descends toward the camera (its edges diverge, and the box's image grows), so I fit a straight
  3D trajectory line. The direction d is fitted to the track and to the along-axis stretch; the fit reproduces the
  stretch to <0.2 %. Result: d ≈ (0.82, 0.48, -0.30), slope about 28–29°, distance falls about 2 % per 6 frames.
  Absolute scale comes from the given depth 9.096 m at f12. Per-frame path speeds come from that.

## Results (f = 2210)
- Route 1, gravity focal length: the fitted ramp acceleration is 1.59–1.61 m/s^2 (window f20+ or f26+). This
  reproduces the prior 1.58 within 2 %, which checks the scale independently. Speed at f36 is 2.736 m/s from the
  quadratic fit, and 2.757 m/s as the raw one-frame difference.
- Route 2, prior scale: the ratio v(f35→36)/a does not depend on f (1.697 for f = 2050 and for f = 2350; 1.70–1.725
  for different windows). So v = 1.58 x 1.70 ≈ 2.68–2.72 m/s.
- An alternative anchor, the box length from frame 0, gives 2.63 with a = 1.53–1.55. That matches the prior less
  well and is less reliable.
- If depth change is ignored (2D-only analysis), the acceleration comes out 1.75–2.0, which is inconsistent with the
  prior. The toward-camera motion matters.

Answer: **2.71 m/s** (between the two routes). Confidence: about ±4 %.
