# q_501 — bottle body diameter

2D scene, one m/px scale from the prior: the horizontal width of the "skynova" text = 0.00188 m.
The text runs vertically down the left side of the bottle. Only "NOVA" is visible because the rest is cut off by the
bottom of the frame. So the text's horizontal (world-X) extent is the height of its letters as they appear across the
image.

Measurements (`measure.py`, mean of frames 0/25/49; everything is static):
- Text: mask of white, low-saturation pixels in x 1050–1250, y 2030–2560. Its columns run x 1106–1185, so the
  **width is 80 px**, which matches the zoomed grid crop (`frames/text.png`).
- Bottle body: the strongest horizontal gradient at each edge, on rows 1900–2550. The width grows slightly
  downward (1137 → 1183 px) because the bottle is seen a little from below. Over the rows the text covers
  (y 2036–2559) the width is about 1150–1180 px. At mid-text (y ≈ 2200–2300) it is **≈ 1160 px**, matching the
  scene record's 1160 px.
- Scale = 0.00188 / 80 = 2.35e-5 m/px. Diameter = 1160 × 2.35e-5 = **0.0273 m**.

Check: the scene record gives the label "NOVA" at x 1080–1190 and the body at x 1000–2160, consistent with these
measurements. The text-to-body ratio of 14.5 gives a bottle about 27 mm wide with letters about 1.9 mm tall, which is
plausible for a serum bottle.

Uncertainty: about ±3% from blur at the text edges (±2 px) and from the perspective change in width. There is also
some ambiguity about what "horizontal width" of the text means. If it meant the length of the whole word, the answer
would be far smaller and physically implausible, so that reading was rejected.
