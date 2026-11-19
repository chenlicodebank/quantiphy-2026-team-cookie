# q_3061 – width of the black car (prior: white car length = 4.572 m)

Top-down drone shot; internet convention = one planar scale from the prior. No time conversion is needed
(the size is static), so the fps / question_fps difference doesn't matter here.

## Scale (white car length)
check.py: bright-pixel extent along columns x=1030/1046/1060 at frames 12, 14, 16 gives 454-456 px
(rear to front bumper), which matches the record's 457 px. Used 456 px, so the scale is 4.572/456 = 0.01003 m/px.

## Black car width (wheel-to-wheel body width, no mirrors)
- I did not use the record's `width_px` = 203 for the dark car. It counts the dark car's soft shadow on its
  left (sun side) and lands near the mirror span. Contrast-stretched crops (frames/dark_st*.png) show the body
  edges at x≈930 (left) and x≈1103 (right). The roof rails sit symmetrically around x≈1018, so the edges are
  consistent with each other.
- edges.py / check.py: per-row edges at mid-body rows. Left edge = first pixel <11 after the shadow
  penumbra (~17-24); right edge = start of the road (>=33).
  Frames 2, 5, 8: 169-175 px, median ≈174 px. Later frames (lower in the image, larger ground scale) give 175-180 px.
  The front (bonnet) is narrower, at 158-160 px.
- Width = 174 × 4.572 / 456 = **1.745 m**.

## Other readings
- Including mirrors (≈913→1118, about 205 px), the width would be about 2.06 m. That isn't the asked reading.
- Using the record's 203 px would give 2.03 m. I rejected it because that measurement includes the shadow.

## Second check
The two cars' widths can be compared directly: the white body is 172 px against the dark car's 174 px, and in
the frames the two bodies look about the same width. Using the later-frame dark width of 178 px instead gives
1.78 m (+2 %).
Confidence: moderate-high on the convention; about ±3 % from edge picking.
