# q1128 — length of the eagle (m)

File 25 fps, question_fps 24: t=1 s -> frame 24, t=2 s -> frame 48 (frame column of scene/ tracks used, not their seconds).
Answer: **0.72 m** (low confidence, see below).

## Camera calibration (calib.py, calib2.py, calib3.py)
Pinhole model, principal point (480,480), camera pitched down by theta, unknowns f and theta.
- Prior: person walks 1.3 m/s. The person's given distance hardly changes (139.95 -> 139.98 m) although the body
  moves down-left in the image, so that distance belongs to a near-static origin. I used it only to fix the height of the
  person's horizontal plane (camera height ~38 m). I intersected the pelvis track (linear fit, 72 frames) with that plane
  and solved theta so that the ground speed is 1.3 m/s at 24 fps.
- Person height: 76 px from head top to lowest foot (median), at 140 m. Each f gives a theta from the speed constraint,
  and with it a height: f=6000 -> 1.85 m, f=6500 -> 1.70 m. I took **f ~ 6250 px** (HFOV ~8.8 deg, which makes the
  person ~1.76 m tall) and theta ~ 14.8 deg.
- Independent check: the boat's two given distances (130.35 / 133.74 m at frames 24/48) put the boat's tracked centre
  at the same height at both times to within 0.15 m. The boat floats, so this is consistent.
- Eagle: distance 139.76 -> 130.25 m. Its 3D velocity is ~11.5 m/s, nearly level, about 34 deg from the line of sight.
  It flies ~4.5-5 m above the person's pelvis. All of this is plausible.

## Eagle size (span.py, crops*.py)
- The eagle is seen nearly head-on. In every frame the body is hidden inside the wing silhouette. Its length cannot be
  measured directly: the projected body is about 8-10 px, mixed in with body thickness and the wing roots.
- Wingspan: in flat-wing frames 5-6 and 31-33, the largest convex-hull extent of the difference mask, times the
  distance at that frame (interpolated linearly), is ~10100 px*m. That gives a projected span of 10100/6250 = 1.62 m.
- The span line is tilted ~3-5 deg with its right end higher, so the wings are turned ~10-18 deg from the image plane.
  The true span is then ~1.62/cos15 = **~1.67 m**, a plausible eagle.
- Length from eagle proportions, beak to tail ~0.43 x wingspan (bald eagle / golden eagle): 0.43 x 1.67 = **0.72 m**.
  Real eagles are 0.7-1.0 m long, so the value is plausible.
- Sensitivity: f 6000-6500 gives L 0.69-0.75. If the body were aligned with the flight direction (34 deg), the span
  would be 1.95 m and L ~0.84. The ratio itself is uncertain by ±10 pct.

Confidence: low to moderate. The scale is well tied to the prior and to the person's height, but the length is
inferred from the wingspan, because the body is foreshortened along the line of sight.
