# q 3071 — height of the plate (cm)

- "Plate" = the white wavy bowl/plate at the left of the desk (the only plate-like object). Height = vertical extent.
- fps = question_fps = 30. t = 1.0 s -> frame 30.
- Prior: egg ("white ball") speed at 1.0 s = 33.38 cm/s. Egg pixel speed at frame 30, from scene/tracks/egg.csv
  (drift-corrected centre): forward diff 1344 px/s, backward 1374, central 1359, quadratic fit f26-34 1365 px/s.
  I used about 1355 px/s (between the forward difference and the smoothed values) -> scale 0.02463 cm/px.
- Bowl pixel height (measure.py, whiteness mask, top of highest rim lobe to bottom of base): 170, 169, 171, 170 px on
  frames 0/10/30/50. I checked it on a zoomed grid crop: top about y 602, bottom about y 772.
- Height = 170 x 0.02463 = 4.19 cm. The range across speed estimates is 4.13-4.22 cm.
- Check: the real-world sanity check fails. At this scale the egg (79 px) would be about 1.9 cm, and a real bowl like
  this would be about 10 cm tall. That means the prior implies a small scale. I follow the benchmark convention of
  one scale taken from the prior anyway.
- Confidence: moderate. The result depends on the annotators' pixel speed for the egg.
