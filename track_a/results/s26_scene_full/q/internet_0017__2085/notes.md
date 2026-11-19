# Q2085 – keyboard length (cm), prior: credit card width = 5.4 cm

Convention (internet video): one scale = 5.4 cm / card pixel width; keyboard length in pixels x scale.
Static overhead camera, so timing and fps don't matter here.

## Measurements
- Keyboard length (bumper to bumper along the long axis, back-left corner to right end), frame 0: corners about
  (2883,503) and (3810,1180), read from 3x zooms (frames/kb_tl.png, kb_r.png). That gives 1148 px; scene record 1145 ±8. Used 1145 px.
- Held Visa card (card.py, dark mask, min-area rect, contour in frames/card_mask.png): long side 354–355 px at all
  frames. Width between the long edges is 193 / 196 / 204 / 203 / 200 px at frames 0/7/14/20/27, mean about 199 px. The width changes
  because the card is held tilted (a flat card would be 354/1.586 = 223 px wide).
- Second route: the card lying flat on the desk under the right wrist. Its fully visible short edge is about 197 px
  (corners about (3368,1752) and (3268,1922)); scene record gives 201.

## Result
- Scale from card width ≈ 197–199 px → 5.4/198 = 0.0273 cm/px → keyboard = 1145 x 5.4 / 197 ≈ 31.4 cm.
  Range 31.0–32.0 cm for widths from 193 to 200 px.
- Sanity check: using the held card's long side (354 px = 8.56 cm) gives 27.7 cm, which is close to the real Apple keyboard
  (about 28 cm). But the held card is raised toward the camera, and the prior is the card *width*, so the answer
  follows the width convention: **31.4 cm**.
- Confidence: moderate. The two card-width routes agree within 2%. The main risk is that the reference used a different card
  dimension.
