# Q377: speed of the ball at t = 1 s (m/s)

Prior: ball diameter = 0.21 m. 2D video with a static camera; file fps = question_fps = 24, so t = 1 s is frame 24.
Speed = |x(24) - x(23)| x 24 x (m per px).

## Measurement (measure.py -> my_track.json, speed.py)
- Mask = |frame - frame 0| > 40, then open/close. A circle is fitted to the left/right mask edges in the top 66 rows
  plus the top row, so the shadow is left out. The overlay frames/my24.png shows the circle sitting on the rim.
- Centre x: frame 23 = 133.74, frame 24 = 150.30, so the raw step is 16.56 px. A quadratic fit over windows of
  6–12 frames gives 16.36–16.54 px. I used 16.54 px/frame. The scene record agrees (133.74 -> 150.29).
- Diameter: the fitted diameter changes with x. It is ~84–85 px near the left and right edges and 80.2–80.5 px near the image
  centre. This is perspective elongation of an off-axis sphere along the horizontal axis: a fit of D0*sqrt(1+((x-x0)/f)^2) gives
  D0 = 80.24, x0 = 949 and f ≈ 2680 px. It is not motion blur, because the width gets smaller while the speed rises. The vertical size stays
  ~80 px everywhere (top at 607–609, centre at ~647.5). The true metres-per-pixel of the motion plane (which is parallel to the image plane, with no
  perspective in the lane bands) is therefore set by the on-axis/minor-axis diameter, 80.3 px. The scene record's 81.5 px median
  mixes in the elongated frames.
- Scale = 0.21 / 80.3 = 2.615e-3 m/px.
- Speed = 16.54 x 24 x 2.615e-3 = **1.038 m/s**. The raw step gives 1.039.

## SAM 3 check
- Frame 24: box 108.1–192.8 x 608.2–687.6 (horizontal 84.7, vertical 79.4). Frame 23: box 92.1–175.7.
  The box-midpoint step is 16.55 px, which matches mine (16.56). The SAM centroid step is 17.0 px, but the centroid is biased by the shadow edge and mask texture.
  The difference is under 3 pct, and the box midpoints agree with my values.
- Frame 59 (near the centre): box 79.9 x 79.3 px, against my 80.3 px. They agree within 1 pct.
- The vertical extent at frame 24 is 79.4 (SAM) against ~80 (mine), within 1 pct. On the zoomed overlay my fitted circle lies on the rim.

## Second route
Using the SAM numbers alone (step 16.55 px, diameter 79.6 px): 1.048 m/s, within 1 pct. Using the scene record's 81.5 px diameter
would give 1.023 m/s. Confidence is high, at about ±2 pct.
