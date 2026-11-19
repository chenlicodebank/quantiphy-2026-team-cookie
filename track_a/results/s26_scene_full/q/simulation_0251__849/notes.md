# q_849 — speed of the soccer ball at t = 1 s

- fps = question_fps = 24, so t = 1 s is frame 24. Speed = |p(24) - p(23)| x 24.
- 2D scene, static camera, ball rolls horizontally with constant apparent size.
- Scale: ball diameter 50 px. I checked this on contrast-enhanced 8x crops of frames 24 and 40 (`viewcrop.py`,
  frames/crops.png): the outline spans about 50 px across and about 49.5 px top to bottom. That gives 0.344/50 = 0.00688 m/px.
  (My simple threshold mask in `measure.py` under-segments the white parts of the ball because they are close to the
  grey background, so I did not use it for size.)
- Pixel speed: the record's track gives cx(23) = 710.25 and cx(24) = 740.00, a step of 29.75 px/frame. The record's
  quadratic fit over frames 2-50 (rms 0.47 px) gives 29.74 px/frame. My own mask-centre track (`measure.py`, noisier)
  gives a quadratic-fit speed of 726.8 px/s against the record's 714 px/s, which agrees within 2 %.
- Speed = 29.75 x 24 x 0.00688 = 4.91 m/s.
- Confidence: good. The main uncertainty is the ±1 px diameter, which is about ±2 %.
