# q3073: distance between cylinder (white ridged cup) and plastic bottle (iced-tea bottle), cm

Time base: file fps = question_fps = 30, so t = 1.0 s is frame 30.

Scale from the prior (white ball = the rolling egg, 33.38 cm/s at 1.0 s):
- Egg x (drift-corrected, scene/tracks/egg.csv): forward difference f30->f31 = 44.8 px/frame; central difference over f28-32 = 45.35;
  linear fit over f26-35 = 45.23 px/frame (the speed is nearly constant here). I used 45.2 px/frame = 1356 px/s.
- Scale = 33.38 / 1356 = 0.02462 cm/px. (A real egg would make this scale too small, but the prior is taken as exact.)

Object positions (frame 30; the scene/ bbox values checked against column-gradient edges in measure.py):
- Cup edges x 988-1110, centre x ≈ 1049, centre y ≈ 654.
- Bottle bbox x 582-702, centre x ≈ 642, centre y ≈ 574.
- Horizontal centre-to-centre distance ≈ 407 px -> 10.0 cm. The 2D Euclidean distance between the bbox centres is ≈ 415 px -> 10.2 cm;
  that includes the bottle's extra height, which is not a separation between the objects.
- Answer: 10.1 cm, between the two readings (they differ by about 2%).

Second-route check: using the plain forward difference (44.8 px/frame) instead of the fit gives a scale of 0.02484 -> 10.1-10.3 cm, which agrees.
Confidence: moderate. The scale depends on the speed convention, but that adds only about 1% uncertainty.
