# Q2132 – toy truck length (cm), prior: sofa total height = 90 cm

Internet video, so I used the annotators' convention: one scale = prior cm / prior pixels, with no perspective correction.
Timing doesn't matter here because this is a size question.

## Sofa pixel height (sofa_measure.py, frames 5/10/20)
- Red-pixel column scans: the highest point of the sofa is the top of the arm nearest the camera, at y ≈ 128 (x ≈ 640-660).
  The top of the back further left is at y ≈ 156.
- Bottom: the red body ends at y ≈ 538-540 near x ≈ 500-530, with a dark base/shadow down to y ≈ 548. I took the floor
  contact as y ≈ 545.
- Total height ≈ 545 − 128 = **417 px** (±6 px). The value is the same in all three frames (the sofa is static and the
  camera drift is mostly horizontal).

## Truck pixel length (truck_len.py)
- From the record's track: bbox width bumper to bumper = 312 px (median of frames 3-28, range 310-318; frames 0-2 are
  occluded by the man's knee).
- Independent colour-extent check at frames 6, 18 and 24: 318, 311 and 312 px. At frame 12 the colour extent picks up
  the man's jeans, but the bbox there is 311 px. The overlay (frames/check12.png) confirms the box.

## Answer
scale = 90 / 417 = 0.2158 cm/px → length = 312 × 0.2158 = **67.3 cm**.

Alternative reading: if the sofa height is taken from the top of the back (y 156) instead of the arm, it is about
389 px, giving 72 cm. I answered with the "total height" (highest point) reading.
The truck is closer to the camera than the sofa, so the single planar scale overstates the truck's real size.
I followed the convention anyway.
Confidence: moderate. The main uncertainty is which sofa endpoints the annotators chose (about ±5%).
