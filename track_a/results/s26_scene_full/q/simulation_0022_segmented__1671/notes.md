# q_1671: height of the rock (m). Prior: boat length = 10 m; boat distance 148.75 m (t=1 s), 146.97 m (t=2 s)

The file runs at 25 fps and the question at 24 fps, so t=1 s is frame 24 and t=2 s is frame 48.
"Rock" = the static pale island/rock mound in the left half of the image (the only other object).

## Measurements (measure.py, bottom.py, geom.py)
- Boat full bbox width (fully visible) is 290 px at f48 (288–294 px over f36–74). Focal length from
  f = 290 px x 146.6 m (Z of the origin at f48) / 10 m ≈ 4250 px.
- From geom.py: back-projecting with the given distances shows the boat translating ≈4.0 m/s left and ≈1.47 m/s
  toward the camera. Its image scale grows ≈1 %/s, which matches. The boat still looks broadside, so I treated the
  10 m length as the horizontal pixel extent.
- Rock (frame 0, threshold 255-min(RGB)>25): bbox x 31–557, y 534–655 (122 px). The flat base is tilted
  (y 626 at the left end to 654 at the right tip) because of depth, not height. The tallest column is 108 px
  (x≈302: crest 536 to base 642). I take the rock's height as about 107 px.
- The boat's keel and rudder are fully visible (no water cut). Its waterline (end of the red/boot stripe) is near
  y≈655, the same as the rock's right-tip base. The boat's bow covers that tip from frame 63 on, so the rock is
  at about the boat's depth or a bit behind it. The base under the crest (y≈640) is higher in the image, so the
  middle of the rock is farther away. With a roughly level camera (horizon near y=480), camera height ≈ 6 m and
  the rock middle is at Z ≈ 155–160 m.

## Result
- Route 1 (rock at the boat's depth, same scale): 107 px x 10/290 = 3.7 m.
- Route 2 (rock middle at Z≈155–160 m): 107 x Z / 4250 = 3.9–4.05 m.
- Answer: 3.9 m. The bbox-height reading (122 px) would give 4.2–4.6 m, but it includes the base's depth tilt.
- Confidence: moderate. The rock's depth is not given and is inferred, which leaves about ±10 % uncertainty.
