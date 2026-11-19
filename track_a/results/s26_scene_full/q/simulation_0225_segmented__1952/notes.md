# q_1952 — width of the beach chair (m)

Prior: black cat speed = 1.041 m/s. No depth_info. fps = question_fps = 24.

## Method
- Static camera, loungers viewed from the foot end, so their horizontal image extent is the chair width (the short side).
  The cat walks parallel to the image plane, just in front of the front row (its feet are at y ≈ 915; the front-row legs
  end at y ≈ 900). The chair sizes barely change from the front row to the back row, so the camera is far away and
  perspective can be ignored. I used one planar scale.
- Cat pixel speed (scene/tracks/cat.csv centroid, re-analysed in measure.py): a linear fit gives 5.403 px/frame in x and
  -0.05 px/frame in y, so 129.7 px/s. The bbox edges give the same slope (5.42 px/frame). The mean of the per-frame
  centroid steps is 133.5 px/s, but gait jitter inflates it; a 5-frame smoothed average gives 131.0 px/s.
- Scale = 1.041 / 129.7 = 0.00803 m/px.
- Chair width, from non-white column spans measured in code on frame 0:
  - front-left: 182 px at the legs, 184 px at the seat base
  - front-middle: 185 px at the legs, 187–188 px at the seat base
  - front-right: 184 px at the legs (the wider spans at y 844–872 include the back-right chair's leg)
  - adopted width: 185 px

## Result
Width = 185 × 0.00803 = 1.485 m.

## Checks
- Range from the pixel width alone (182–188 px): 1.46–1.51 m.
- Using the jitter-inflated per-frame speed (133.5 px/s) instead gives 1.44 m.
- Sanity check: the cat is 107 px long including the tail, which is 0.86 m at this scale, about 1.2× a real cat. That fits
  a render scaled up a little, so the chair also comes out larger than a real one.

Confidence: moderate-high (about ±4%).
