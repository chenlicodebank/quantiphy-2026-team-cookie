# q_2969 — pen length (cm), prior: credit card width = 5.4 cm

## Problem
The prior's object (the credit card) cannot be seen in this segmented clip. I checked all frames, including a zoom on the
left hand's pinch at (760-830, 360-410): it holds nothing visible, and there is no card anywhere else on the white
background. So the card's pixel width can't be measured directly.

## Measurements (measure_pen.py)
- Pen: PCA extent of the non-white mask, frames 0/10/20/33, thresholds 220-245: length 181.8-183.2 px (mean ~182.5),
  width ~19 px. The ends are at (162.5,426.6) and (280.3,563.8). The pen is static and the camera is static, top-down.
- Keyboard (minAreaRect, frame 0): 362.5 x 166.2 px. The ratio 2.18 matches an Apple Aluminium Wireless Keyboard
  (A1314, ~28.4 x 13.0 cm, ratio 2.18). It does not match the Magic Keyboard (ratio 2.43).

## Scale (fallback)
The card isn't visible, so the scale comes from the keyboard as a stand-in on the same desk plane: 28.4/362.5 =
0.0783 cm/px. The depth gives 13.0/166.2 = 0.0782 cm/px, which agrees.
At this scale a 5.4 cm card would be ~69 px wide, a reasonable size next to the hands.
Pen = 182.5 x 0.0783 = 14.3 cm. That fits a typical ballpoint or gel pen (14-14.5 cm).

## Confidence
Moderate. The answer rests on identifying the keyboard model, not on the prior's own object. If the original footage
had the card held above the desk, the reference value could be somewhat different.
