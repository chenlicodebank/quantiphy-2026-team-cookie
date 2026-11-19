# q_2968 — width of the keyboard (cm); prior: credit card width = 5.4 cm

## Problem
The segmented clip shows only the hands, keyboard, pen and tin on white. No credit card is visible in any frame. The left
hand pinches something at about (815, 375), but only a few dark edge pixels show, so the card is either edge-on or
was removed by the segmentation. The prior's pixel size therefore cannot be measured from this clip.

## Keyboard measurement (kb.py)
Keyboard mask = non-white, non-skin pixels in the keyboard region; cv2.minAreaRect per frame:
- frame 0: 166.2 x 362.5 px; frame 17: 168.0 x 363.4 px; angle about 36 deg. This agrees with scene.json (167 x 363).
- Width (short side, front to back) = 167 px; length = 363 px; aspect ratio 2.17.

## Scale (fallback, because the card can't be seen)
The keyboard is an Apple aluminium Wireless Keyboard (A1314 style, with the battery tube along the back edge).
Its spec is 27.9 cm x 13.0 cm (aspect ratio 2.15), which matches the measured 2.17. The Magic Keyboard (27.9 x 11.5, ratio 2.43)
does not fit. Taking the scale from the known length, 27.9 cm / 363 px = 0.0769 cm/px, gives width = 167 x 0.0769 = 12.8 cm.
The spec depth gives 13.0 cm directly. Answer: 12.9 cm.
If the annotators measured the card correctly, their single-scale value should come close to the true size.

## Second-route check
Width from the length-based scale (12.84) and the spec depth (12.95) agree to within 1 pct. The measured aspect ratio
independently confirms the keyboard model.

## Confidence
Moderate. The metric scale could not come from the prior's object as required, because it is not visible. If the
annotators' card pixel measurement was off (for example, a card held above the desk), the reference could differ by 10-20 pct.
