# q_3066 - diameter of the white ball (cm)

Prior: the white ball's velocity at t = 1.0 s is 33.38 cm/s. fps = question_fps = 30, so t = 1.0 s is frame 30.
The white "egg" in scene/ is a white ball that rolls right to left. Up close it looks spherical.

## Scale (from the prior)
- Pixel velocity at frame 30, from the forward difference of the centre:
  - scene track, raw: 1166.3 - 1211.5 = 45.2 px/frame
  - scene track, drift-corrected: 44.8 px/frame
  - my own half-max edge midpoints (measure.py): 45.8 px/frame
  - average over frames 29-32: about 45.3-45.6 px/frame
- Value used: 45.3 px/frame = 1359 px/s.
- Scale = 33.38 / 1359 = 0.02456 cm/px.
- The camera drifts by less than 0.3 px/frame, which is negligible.

## Diameter in pixels
- Vertical extent (not blurred by the horizontal motion), half-max of the whiteness profile through the centre:
  77.6-78.5 px in frames 26-32 (median 77.8 over frames 29-53).
- scene record, gradient edges: 77-80 px (median 79).
- Visual check on the zoomed frame 30: about 79 px tall and 80 px wide. The horizontal width is inflated by motion blur.
- Value used: 78.5 px.

## Answer
78.5 x 0.02456 = **1.93 cm**.

The answer stays within ±3% using the extreme inputs:
- 77.8 px diameter with 45.8 px/frame speed gives 1.89 cm.
- 79 px diameter with 44.8 px/frame speed gives 1.96 cm.

As a real object, a ping-pong ball is about 4 cm across. The prior is treated as exact, so the answer follows its
scale. Confidence: moderate-high under the single-scale convention.
