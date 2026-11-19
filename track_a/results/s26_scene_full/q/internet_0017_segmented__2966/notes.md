# q_2966 — diameter of the round container (cm)

Prior: credit card width = 5.4 cm. **No credit card is visible in this segmented clip.** I checked frame 0, a
contact sheet of 8 frames, and a 4x zoom of the left hand's pinch. The segmentation kept only the hands, the keyboard,
the pen and the tin, so the card's pixel size cannot be measured. Because of that, I took the scale from a known-size
object in the same plane, which reproduces the scale the card would have given if the card were also on the desk.

Scale object: an Apple Wireless Keyboard (aluminium, A1314 type, Russian layout), which measures 27.9 x 12.8 cm.
Its pixel aspect ratio is 363/167 = 2.17, which matches 27.9/12.8 = 2.18. A Magic Keyboard would give 2.43, so that
model is ruled out.
- Keyboard long side: 362.5-363.8 px (minAreaRect and axis projection, frames 0/10/20/30) -> 27.9/363 = 0.0769 cm/px.
- Keyboard short side: 167 px on frames that are not occluded -> 12.8/167 = 0.0766 cm/px, which agrees.

Tin (measure_tin.py; static, frames 0/10/20/30):
- bbox 131-133 x 125 px; ellipse fit 131.3 x 123.8; equivalent-area diameter 128.4 px.
- The view is slightly oblique: the vertical extent is foreshortened and includes the side wall, so the true rim
  diameter is the major axis, about 132 px.

Result: 132 px x 0.0768 cm/px = **10.1 cm**.

Check: the equivalent-area diameter gives 128.4 x 0.0768 = 9.9 cm, and the short side of the keyboard gives
10.1 cm. The pen (181 px) would come out at 13.9 cm, which is plausible for a pen. A desk tin of about 10 cm is
plausible.

Confidence: moderate. The main risk is that the reference answer used the card's pixel width in the original footage,
which I cannot see here. If the card lay on the desk plane, it should give the same scale as the keyboard to within a
few percent.
