# q2086 – keyboard width (cm), prior: credit card width = 5.4 cm

Internet video, static overhead camera (scene/ record: shift < 1 px). Following the annotator convention: one scale =
5.4 cm / card short-side pixel length, applied to the keyboard's width. "Width" here means the keyboard's front-to-back
depth (the shorter horizontal extent), as the task's naming rules say.

## Card width (prior object) – card2.py
Black Visa card held in the left hand. I fitted straight lines (Huber fitLine) to the card's top long edge (right of
the thumb), its bottom long edge and its right short edge, using the largest dark-pixel component. The two long edges
are parallel to within 1°.
- Distance between the long edges, per frame: 190.5 (frame 0) … 193–194 (frames 4–8) … 200–202 (frames 11–20) … 196–197 (frames 25–27).
  The card tilts a little as it is held. Mean 197.2 px, median 197.8 px.
- Right short edge, corner to corner (a second route): mean 200.1 px, which agrees within 2 %.
- Card width used: about 196 px (between the frame-0 value and the mean over all frames).

## Keyboard width – kb.py
I took perpendicular intensity profiles across the keyboard at 26 points along its long axis (axis from the corners
(2882,505)→(3805,1190)) and found the back edge (battery bar) and the front edge as gradient maxima. Wherever both
edges are clearly visible (not covered by the hand), the width is 515–519 px in frames 0, 13 and 27. Median about
516 px. This matches the record's 512 px from manually read corners and the corner-pair distances of 518 / 507 px.

## Result
516 / 197 × 5.4 = 14.1 cm. Using the frame-0 card width (190.5 px) gives 14.6 cm; the full range is 13.8–14.6.
Answer: 14.2 cm.

Sanity check: the card's long side (354 px = 8.56 cm) would give 41.4 px/cm, i.e. a keyboard 12.4 cm deep. The card's
visible aspect ratio is 1.8, while a real card's is 1.586, so its short side is foreshortened by the tilt. The real
Apple Wireless Keyboard is about 13 cm deep. The answer follows the annotators' single-scale-from-prior convention, so
it inherits that foreshortening. Confidence: moderate (±5 % on the convention; the reference could differ if the
annotator measured the card on a different frame).

Frame rate: this is a size question, so the 22 vs 22.37 fps difference does not matter.
