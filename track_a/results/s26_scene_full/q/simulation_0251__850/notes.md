# Q850: speed of the soccer ball at t = 1.5 s (m/s)

- fps 24 (file and question agree) -> frame 36. 2D scene, static camera, ball rolls horizontally and slows down evenly.
- Scale: prior diameter 0.344 m. Ball pixel diameter checked again in diam.py: the horizontal threshold extent is 50 px
  at frames 30, 36, 40 and 50, the vertical extent is 46-51 px, and the record's free-radius circle fit gives 50 px.
  Used 50 px -> 0.00688 m/px.
- Speed (measure.py): the scene track cx gives a raw backward step of 27.75 px between frames 35 and 36. A quadratic
  fit over frames 2-50 gives a step of 27.68 px/frame (0.47 px rms), and a local quadratic over frames 26-46 gives 27.67.
  -> 27.68 x 24 x 0.00688 = 4.57 m/s.
- Second route: a local quadratic fit to the midpoints of my own threshold mask gives 27.41 px/frame -> 4.53 m/s (agrees within 1%).
- Main uncertainty is the pixel diameter (±1 px, about ±2%). Confidence: high.
