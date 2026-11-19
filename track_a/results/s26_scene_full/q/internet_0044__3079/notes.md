# q3079 – height of the plate (cm), prior g = 9.8 m/s^2

- "Plate" = the white wavy bowl/dish at the left (the only plate-like object). Its height is the vertical image extent.
- Time base: file fps = question_fps = 30, so I used 30 fps.
- Scale from gravity (measure.py): I fitted y-parabolas to the ball's stabilised centre (scene/tracks/ball.csv, cy_f0) on each
  arc between bounces, leaving out the arc-fit fill rows and the first and last frame of each arc. The clean arcs gave
  19.0-20.4 px/frame^2 (64-69: 19.36, 73-79: 19.32, 83-89: 19.12, 93-98: 19.01, 132-137: 19.94, 139-144: 19.70,
  42-47: 20.39, 51-58: 19.70). I left out the noisy arc 126-130 against the white bowl (25.0).
  Adopted value: 19.6 px/frame^2 = 17640 px/s^2, so the scale is 9.8 / 17640 = 5.56e-4 m/px.
- Bowl pixel height: from the white-mask bounding box at frame 0, top of the rim at y=649 and the base at y=810, giving 161 px.
  The scene record gives 648-812 (164 px), so I adopted 162 px.
- Height = 162 x 0.0556 cm = 9.0 cm.
- Check by a second route: at the same scale, the ball's 76 px diameter comes to 4.2 cm, close to a real 40 mm table-tennis ball.
  The ball is slightly nearer the camera, so this is consistent. A real bowl of about 20 x 9 cm is plausible.
- Confidence: moderate-high. The acceleration spread (about ±3%) and the edge reading (±2 px) give about ±4% in total.
