# q_3265: length of the toilet paper holder (cm)

Prior: the toilet paper's width is 10 cm. "Width" here is the roll's sheet width, i.e. its length along its axis. In this front view that axis is horizontal.
I used the internet-video convention: one scale factor, planar, no perspective correction. The camera is static (scene record). Time base does not matter, because this is a size question.

## Measurements (measure.py: gradient edges on Gaussian-smoothed gray frames)
- **Roll at rest (frames 57–59):**
  - Left edge x = 1614–1620; right edge x = 2200–2203, measured above the hand.
  - Length = 586 px (the scene record gives 583.5–585.2).
  - Scale: 10 cm / 586 px = 0.01706 cm/px.
- **Holder (frame 0, nothing in front of it):**
  - Suction cup's left edge x ≈ 1443 (rows 1000–1100, steepest edge 1435–1451).
  - End tab's right edge x = 2338–2340.
  - Arm's left end at the bracket x ≈ 1517.
  - Full horizontal extent (suction cup to tip): 896 px → **15.3 cm**.
  - Arm only (bracket to tip tab): 822 px → 14.0 cm. This is the other possible reading.

## Answer and checks
- Answer: 15.3 cm, the whole holder's longer horizontal extent.
- Check against the scene record: the cup is at 1445 and the tab at 2344, giving 899 px → 15.3 cm. The arm is 817 px → 13.9 cm. This agrees with my measurement.
- The scale is consistent with the vertical size: the roll's diameter is 698 px → 11.9 cm, which is realistic for a toilet roll.

Confidence: moderate. The main uncertainty is which reading is meant (whole holder or arm only), a difference of about 9%.
