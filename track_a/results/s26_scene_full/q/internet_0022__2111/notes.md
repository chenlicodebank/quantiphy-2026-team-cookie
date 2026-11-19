# q2111 — length of the table (desk), m

Prior: mouse width = 57 mm. Static top-down camera; one planar scale (internet convention).

- Mouse (frame 35, white mask, `measure.py`): minAreaRect 198.1 x 102.5 px → width 102.5 px.
  Scale = 0.057 / 102.5 = 5.56e-4 m/px.
- Desk length = its long horizontal extent (left–right in image). Measured along the far edge (the near edge is
  out of frame): left corner x ≈ 125 px (y≈775), right corner x ≈ 3485 px (y≈805), read on zoomed crops
  (frames/left.png, frames/right.png); the edge tilt (≈30 px in y) is negligible. Gradient search (`edges.py`) is
  noisy from background clutter but consistent (≈3375–3450). Length ≈ 3360 px.
- Answer: 3360 x 5.56e-4 = 1.87 m.

Check: the "Business Goals" sheet on the desk is 534 x 382 px (ratio 1.40 ≈ A4). If it is A4 (297 mm), its scale
is 0.297/534 = 5.56e-4 m/px, the same as the mouse scale → desk ≈ 1.87 m. A 1.8–1.9 m office desk is plausible.
The time base doesn't matter here, since this is a static size.
Confidence: good (about ±3%, mostly from where the desk corners are read).
