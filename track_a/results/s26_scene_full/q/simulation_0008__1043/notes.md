# q1043 – average speed of the boat, 1.0 s to 2.0 s (m/s)

The timing uses question_fps = 24, so the interval runs from frame 24 to frame 48. The file's own rate is 22.80 fps, and I used the
frame column from scene/, not its seconds. The depths given are at t=0 (frame 0), 7.452 m, and at t=1 (frame 24), 6.655 m.
The scene is 3D with a static camera, and the boat translates right to left.

## Measurements
- Bow track (scene/tracks/boat.csv, bow_x, sub-pixel): the bow moves 735.7 to 489.7 px over frames 24 to 48, an average of
  10.25 px/frame. The pixel speed drops slowly over the clip, from 10.7 px/frame early to 9.9 px/frame late.
- `fit.py`: a projective constant-velocity model u-cx = (a+bn)/(1+cn) fits the bow with 0.37 px rms (a straight line gives 2.2 px).
  The fitted c = 6.6e-4/frame means the boat recedes by about 1.6 % in Z every 24 frames.
- `scale.py`: scale-searching template matching of the bow, with frame 24 as the reference, gives about 1.01 for frames 0-23 and
  about 0.98-0.99 for frames 44-65. That independently confirms the slow recession, at a rate matching the fit. The waterline
  rises 760 to 755 over frames 24-65, close to the predicted 5.8 px.
- I took the origin as the centre of the full boat box: bow + L/2, with L = 648 px at frames 55-57 and scaled by 1/Z. I put
  origin v at 689.

## Scale (`solve3d.py`)
- Pinhole model with cx = cy = 540. Two unknowns, the focal length f and Z0, come from the two given distances plus the image
  positions of the origin at frames 0 and 24 (r0 ≈ 790 px, r24 ≈ 535 px off-axis), with Z(n) = Z0(1+cn).
- Result: f = 929 px, Z0 = 5.645 m, Z24 = 5.735 m. This reproduces d0 = 7.452 and d1 = 6.655.
- 3D origin positions per frame give per-frame speeds |P(i)-P(i-1)|·24. Their mean over frames 25..48 is **1.529 m/s**.
  It is the same over frames 24..48 because speed is constant in the model.
- Hand check: Z/f at frame 36 is 0.00622 m/px; 10.25 px/frame × 24 × 0.00622 = 1.531 m/s; adding Vz ≈ 0.09 m/s gives 1.534 m/s.

## Second route (height prior 0.75 m) and sensitivity
- Taken naively, 0.75 m comes to only about 120 px at the boat, while the visible span from post top (y 620) to waterline
  (y 760) is about 141 px. That span is inflated by perspective, though. The camera looks down about 13° (the interior is
  visible), the post top is at the centreline and the waterline is on the near side. Using y - 540 = f(H - h)/Z
  (level camera, camera height H, half-beam about 0.6 m), the post top comes out about 0.72 m above the water. That is consistent with a
  0.75 m box once a small draft is included, so the depth route and the prior roughly agree.
- Sensitivity:
  - A constant-Z model (c = 0) gives 1.44 to 1.47 m/s, but both the scale measurement and the fit reject it.
  - Shifting the origin by ±10 % of the boat length gives ±5 %.

Answer: 1.53 m/s. Confidence: moderate (about ±6 %).
