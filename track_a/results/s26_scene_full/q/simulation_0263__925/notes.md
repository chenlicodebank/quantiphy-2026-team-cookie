# Q925 — length of the spacecraft (m)

Prior: acceleration at 1.0 s = 4 m/s^2. 2D top-down scene, static camera, fps = question_fps = 24.
The "spacecraft" is the single dark vehicle (scene/ calls it a car) that starts at rest and accelerates
straight left along y ≈ 718.

## Scale (from the prior)
- Track: scene/tracks/car.csv ref_x (template-matched rear end, sub-pixel). Steps grow by 0.90 px/frame
  every frame (from 1.3 px to 63.4 px), so acceleration is constant.
- Quadratic fits of x(t): frames 2-71: 517.6 px/s^2; 5-40: 517.5; 30-71: 517.5; 10-60: 517.7.
  Second route: mean second difference of the per-frame step = 0.90 px/frame^2 × 576 = 518 px/s^2. They agree.
- Scale = 4 / 517.6 = 0.007728 m/px.

## Pixel length (measure_len.py)
- Frame 40, when the vehicle is centred in the image (ref_x 1281.8 ≈ cx 1280), against a car-free background
  built from frames 0 and 71:
  dark body mask x 902–1670 → 769 px; mask of all differences x 882–1671 → 790 px. The extra ~20 px at the nose
  is a mid-grey (≈105) band that appears only on the upper side of the nose (y ≈ 700–718, not at y = 740). That
  matches the cast shadow, which is offset up and ahead, so I left it out.
- Across the clip the body-mask length goes from 788 px (right of the image) to 742 px (left), which looks like
  mild perspective on parts at different heights. The centred frame gives about 768 px and the clip median is
  776 px.
- Length = 768 px × 0.007728 = 5.94 m (776 px → 6.00 m). Answer 5.95 m.

## Width check (not asked)
Width = 366 px × 0.007728 = 2.83 m, so length/width ≈ 2.1.

Confidence: the scale is good to about 0.5 %; the pixel length is uncertain by about ±2–3 % because of
perspective and the shadow fringe.
