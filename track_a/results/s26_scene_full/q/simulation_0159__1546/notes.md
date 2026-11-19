# q1546: How long is the turtle (m)?

Prior: turtle acceleration = 2.639 m/s². Depth to turtle origin: 15.232 m at t=0 and 14.968 m at t=0.5 s (frame 12). The file fps and question_fps are both 24.

## Tracking (shell.py → shell.json)
- Background: frame 0, with frame 40 used for x ≥ 1450. Mask: max-channel diff > 14. Largest component.
- Tracked point: the rear (right) edge of the shell, measured on rows top+20/30/40 of the mask. The shell is rigid, so this avoids the flipper noise that affects the scene/ core centroid. The top row is used for v.
- The per-frame pixel speed rises from about 0 at f0 to about 22 px/frame at f40, roughly linearly. This fits uniform acceleration from rest.

## 3D fit (fit3d.py, length.py)
- Model: P(t) = P0 + d·½·a·t², with a = 2.639 and d a fixed unit direction.
- P0 is back-projected from the f0 pixel with D0 = 15.232. The tracked point is the origin plus a fixed offset.
- Unknowns: f, d. Fitted to u(t) and v(t) over 41 frames plus D(0.5) = 14.968.
- Result: f ≈ 2436 px. d = (-0.82, -0.01, -0.57) in camera coordinates, so the turtle swims left and toward the camera. Z goes from 14.54 to 12.43. Fit residual rms is 2 px.
- Variants give f = 2370–2620: different edge rows, origin offsets, f0–30 only, and a free initial speed (fitted v0 ≈ 0).
- Check: the predicted growth in apparent size (Z0/Z40 = 1.17) matches the measured growth of the shell's pixel length (≈1.2).

## Length
- I assume the body axis lies along the motion direction d through the origin. Each endpoint pixel is mapped to a point on that 3D line.
- Endpoints were read on 4x zooms. Head = the leftmost point of the grey head disc. Shell tip = the pointed rear of the carapace. Rear-flipper tip = the mask's right end.

| frame | head → shell tip | head → rear-flipper tip |
|---|---|---|
| f20 | 1.733 m | 2.063 m |
| f30 | 1.718 m | 2.027 m |
| f40 | 1.691 m | 2.074 m |

- The results agree across frames, which serves as the second-route check. Varying f across the variants changes them by ±3%.
- Readings:
  - Head to carapace tip: ≈ 1.71 m.
  - Full mesh extent along the body, including the trailing rear flippers (bounding-box length): ≈ 2.05 m.
- Answer: **2.03 m**, the bounding-box reading, nudged slightly down.
- Uncertainty:
  - Whether the reference counts the rear flippers.
  - The front-flipper span, which is not measurable from this view.
  - The world bounding box is assumed to be aligned with the body.
