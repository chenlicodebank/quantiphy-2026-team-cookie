# q_2683: height of the glass jar (cm)

File fps = question_fps = 24, so t = 1.0 s is frame 24. The camera is static, and so is the jar (box ~[443,406,500,485] in scene.json).
Lab card: f = 0.5959 x 1280 = 763 px. The given jar depth is 1.008 m at t = 1.0.

## Measurement (prof.py, crops frames/jar24.png, jartop.png, jarbot.png)
- I took the per-pixel median of frames 0, 24 and 48 (this removes the ball) and read column and row profiles across the jar.
- Top of the lid (far rim): y ≈ 408.7, the half-rise of 113 -> 207. Bottom front edge of the jar on the table: y ≈ 484.4.
  The full vertical pixel extent is 75.7 px.
- Lid: its top-surface ellipse spans y 409-415.6 (~6.6 px minor axis) and its skirt spans 416-420. Lid width x 444.7-498.7 = 54 px,
  which gives 7.1 cm at 1.008 m.
- Because the camera looks down about 7° (sin e ≈ 6.6/54), the top and bottom ellipses add about 6.5 px of minor axis to the
  extent. The silhouette height, measured between the ellipse centres, is ≈ 69.2 px, or 69.7 px after correcting for cos e.

## Results
- Raw bbox extent: 75.7 x 1.008 / 763 = 10.0 cm.
- Perspective-corrected cylinder height: 69.7 x 1.008 / 763 = 9.2 cm.
- Second-route check with the ball prior (ball.py): at frame 24 the ball measures ~25-27 px, but 4 cm at 1.055 m should give 28.9 px.
  This suggests the pixel extents run ~8% low, so the corrected height scales to ~9.9 cm. The ball's edges are blurred and its
  lower half is shaded, so this check is weak.
- Answer: 9.5 cm, a compromise between 9.2 (geometric), 10.0 (raw bbox) and ~9.9 (ball-calibrated). Every route lies within ±5%.
  Confidence: moderate.
