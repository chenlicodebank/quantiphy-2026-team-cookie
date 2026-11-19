# q_773 — acceleration of the basketball at t = 0.5 s (frame 12)

fps = question_fps = 24, so no re-timing; t = 0.5 s -> frame 12, which is in the free fall (frames 0-23, bounce in 23->24).
2D scene with a static camera (scene record: shift < 0.04 px), so one m/px scale comes from the prior (diameter 0.282 m).

## Scale
- `diam2.py`: subpixel horizontal edge-to-edge width through the ball centre (half-level colour-distance crossing).
  Horizontal is not affected by the vertical motion blur. Width = 107.36, 107.61, 107.47, 107.46, 107.56 px
  (frames 0, 1, 12, 48, 49) -> **107.5 px**. The record's circle fit gives 106.1 px (it is biased slightly inward); bbox 108.
- Scale = 0.282 / 107.5 = 2.623e-3 m/px.

## Acceleration
Free fall at constant acceleration, so a quadratic fit over the fall is the right estimate. Single-frame second
differences are too noisy (about ±0.5 px/f²).
- Route 1 (`fit.py`, the record's circle-fit centre): 2 x quadratic coefficient = 1.337 px/f² (frames 0-23), 1.340 (2-22),
  1.331 (6-18), 1.323 (8-16). Fit residual rms is 0.22 px.
- Route 2 (`topedge.py`, my own subpixel top edge from the R-G crossing, median of 5 columns): 1.350 (0-23), 1.354 (2-22),
  1.361 (6-18), 1.325 (8-16).
- Adopted: 1.343 px/f² x 576 = 773.6 px/s² -> 773.6 x 2.623e-3 = **2.03 m/s²**.
  With the circle-fit diameter (106.1 px) it would be 2.06, so the answer depends on the diameter by about 1.5 %.
- Side note: the rise after the bounce fits about 1.24 px/f², roughly 8 % lower than the fall. This does not affect t = 0.5 s,
  which is in the fall.
- The scene is not at real-world scale: 2 m/s² instead of 9.8. As the benchmark states, the prior sets the scale.

Confidence: good, about ±3 %.
