# q_2967 — keyboard length (cm); prior: credit card width = 5.4 cm

## Problem
The credit card named by the prior is not visible in any frame. The segmentation removed it: the left hand at
(~700-825, 330-470) is pinching empty white space, and the rest of the scene is white background, keyboard, pen, tin and hands.
So I could not measure the card's pixel width, and could not reproduce the annotators' scale (5.4 cm / card px) directly.

## Measurements (kb_measure.py, frame 0 / 18)
- Keyboard footprint (non-white, non-skin, largest component, minAreaRect): 362.5 x 167.7 px; the long axis is
  ~36 deg below horizontal. The long extent is stable at 362.4-362.6 px over angles 35-38 deg, and it matches the
  scene/ record (363 px).
- Key pitch along the long axis (autocorrelation of rows in the de-rotated image, frame 18): 24.1 px (consistent across
  7 rows; 5th harmonic also gives 24.2 px). Keyboard length = 15.04 key pitches.

## Scale (fallback, real-world)
The keyboard is a white Apple Wireless Keyboard (compact, no numpad), which is 27.9 cm long. 27.9 cm / 15.04 pitches gives
an 18.6 mm key pitch, which is normal for Apple keyboards (a 19.05 mm ISO pitch would give 28.6 cm). The left hand/wrist is
~107 px wide. Taking a hand breadth of ~8.5 cm gives ~0.079 cm/px, so the keyboard would be ~28.7 cm. That is consistent.
If the annotators measured the card correctly, their single-scale answer should be close to the real length.

## Answer
27.9 cm. Confidence: moderate. The scale could not come from the prior because the card is not in this segmented clip;
the error depends on how accurately the annotators measured the card's pixel width.
