# q_2011: width of the blue car (the light-blue cart)

**Answer: 0.87 m.** This is the cart's horizontal extent across its direction of travel (the depth axis).

**Inputs**
- Prior: car tyre diameter 0.764 m; blue cart tyre diameter 0.369 m.
- depth_info: at t = 0.5 s (frame 12), the yellow car's left front tyre is 11.38 m from the camera.
- 24 fps (the file and question_fps agree), 1920x1080. It is a 3D Blender render, segmented.

## Why the width can be measured
- The width runs along the depth axis, so it cannot be read from the side view.
- At frames 0–1, though, the cart sits far right of the image (u ≈ 1600–1700). There it is seen about 14° obliquely from the front, so its front face shows.
- For two mirror points at the same world x and height, on the near side (depth Z1) and the far side (Z1 + W):
  `(u_near − cx)/(u_far − cx) = (Z1 + W)/Z1`, so `W = Z1 · (u_near − u_far)/(u_far − cx)`.
- cx = 960 is assumed (Blender default, no lens shift). It could not be checked independently: the car's nose is rounded in plan view, so it is not usable for this.
- Camera yaw relative to the travel direction is about 0:
  - The cart's tyre-bottom row (818) and apparent size stay constant while it crosses about 1200 px.
  - So the depth direction vanishes at u = cx.
- Pitch is about 1.4°, with the horizon near v ≈ 477. Its effect, cos θ, is negligible.

## Scale: the cart's near-side depth Z1
**Tyre pixel diameters** (`lowsector.py`, `hubrim.py`, `rays.py`)
- I used outer-edge radii from the rim centre on the lower sector of the tyre. The upper part is spoiled by arch shadow and fender.
  - Car: 181–184 px (frames 18–32, front and rear wheels).
  - Cart: 73.3–74.6 px (frames 32–41).
  - Ratio: 2.47 (both methods agree within 0.3 %).
- The scene record's values (car 175–186, cart 80) were too rough. Its 80 px for the cart included the fender shadow.

**Car depth and focal length**
- The car's front hub at frame 12 is at (1649.5, 791.8), from rim template matching.
- 11.38 m is a 3D distance. Converted to camera-axis depth: Zc = 10.95 m, with f ≈ 2594 px (horizontal FOV ≈ 40°).
- The silhouette comes from the tyre's outer sidewall, which sits about 0.12 m nearer than the tyre's origin. That gives 10.83 m.

**Cart depth**
- Z1 = 10.83 × (0.369/0.764) × 2.47 = **12.92 m**.
- Equivalently, f · 0.369 / 74 px.

**Sanity checks**
- Cart: length 374 px → 1.86 m; height 328 px → 1.63 m.
- Car: length 1153 px → 4.8 m.
- Camera height from the two ground-contact rows (car 883, cart 818): about 1.70 m, horizon at v ≈ 477. Consistent.

## Front-face measurements (`front0.py`, `match_hub.py`)
**Near-side reference**
- The cart's near front hub, by rim template matching from frames 36/38/41: (1672.3, 781.0) in frame 0 and (1671.1, 780.9) in frame 1. Hub y equals frame 41's, which confirms the same depth.
- Near-side features relative to the hub come from frames 36, 38 and 41. There the cart is left of centre, so its leftmost silhouette is the near corner, and the offsets are constant across those frames:
  - body front −12.5 px;
  - bumper −21 px;
  - tyre −36.3 px;
  - roof front +30.5 px.

**Far-side features in frames 0 and 1** (leftmost silhouette = far corner)

| feature | u_near (f0) | u_far (f0) | (u_n−u_f)/(u_f−cx), f0 / f1 | W = Z1 × ratio |
|---|---|---|---|---|
| body front (headlight rows 690–720) | 1659.8 | 1615.6 | 0.0674 / 0.0672 | **0.87 m** |
| bumper | 1651.3 | 1607.5 | 0.0676 | 0.87 m |
| wheels, outer to outer | 1636.0 | 1595.0 | 0.0643 / 0.0657 | 0.84 m |
| roof front (amber light bar on its front face) | 1702.8 | 1660.0 | 0.0611 / 0.0611 | 0.79 m |

- The bounding-box width is the widest part, which is the body/bumper: **0.87 m**. The wheels (0.84) and roof (0.79) sit inside it.
- The body's rear part, the cargo box, cannot be seen obliquely: it is clipped by the window and hidden by the car. If it were wider than the front cowl, the true width would be larger.

## Second-route checks
- **Frame 1 vs frame 0:** independent silhouettes and hub match give the same ratios to within 0.3 %.
- **Vertical perspective:**
  - Near/far headlights give a horizontal depth ratio of about 1.045, consistent with a vertical shift of the far headlight of about 9–10 px for a horizon near 477–500.
  - The far wheel's hub row (~765) agrees with the predicted 762 for a depth ratio of 1.065.
- **Roof-to-post spread in frames 15–41** (the scene record's 25 → 4 px spread): qualitatively consistent, giving kr = 0.048–0.077 depending on the unknown post-tip slope. Too ill-conditioned to use numerically.

## Confidence
About ±6 %. The main error sources:
- the tyre pixel ratio (±2 %);
- the face-projection pixel extents (±1 px of 44, ±2.5 %);
- the car tyre's half-width offset (±0.5 %);
- the cx = 960 assumption.

Another reading of "width" (wheel track, outer faces) would give 0.84 m.
