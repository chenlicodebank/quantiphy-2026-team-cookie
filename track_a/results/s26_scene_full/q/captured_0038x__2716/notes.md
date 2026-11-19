# q_2716 – diameter of the white ball (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). t = 1.4 s -> frame 34. f = 0.5959*1280 = 763 px.
depth_info at t=1.4 s: white ball 0.7160 m, credit card 0.6867 m.

## Ball pixel diameter (vert.py)
The ball rolls horizontally (~16 px/frame), so horizontal extents are smeared by motion blur and frame 34's
left edge sits over the white cards. The vertical extent is unaffected by blur: on the mean of the 5 central
columns, top = steepest-ascent edge (table -> white), bottom = steepest-descent edge (shaded underside ->
contact shadow), sub-pixel by parabola fit.
- frame 34: top 486.9, bottom 528.1 -> 41.2 px; frames 32-36 median 41.5 px. The trend is smooth over the
  whole run (40.3 px for frames 17-29, 41.9 px for frames 36-46, as the ball comes closer). I used 41.4 px.
- The scene record's heights (35 px) were too small: they cut off the shaded underside.

## Size
D = 0.716 m * 41.4 px / 763 = 3.885 cm -> **3.89 cm**.

## Check of the scale (card.py)
The credit card lying flat, frame 34: mask long axis 93-94 px, and by eye 90 px on the back edge and 100 px
on the front edge (about 95 px mean). 0.6867 * 95 / 763 = 85.5 mm, which matches the 85.6 mm prior.
So f = 763 px together with the given depths reproduces the prior.

## Notes and confidence
- A projection of an off-axis sphere (about 12 deg off axis) that includes the obliquity factors would give
  about 3.73 cm. The method-card convention (size = depth * pixel extent / f) gives 3.89 cm. That convention
  reproduces the card prior, and 3.89 cm is close to the size of a real table-tennis ball (4.0 cm), so I
  answered 3.89 cm.
- Edge uncertainty is ±1 px (about ±2.5 %). Confidence is good.
