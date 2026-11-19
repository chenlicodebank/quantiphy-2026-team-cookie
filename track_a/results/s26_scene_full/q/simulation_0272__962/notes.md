# Q962 – phoenix wingspan (m)

2D top-down render, 24 fps (file fps = question fps). Prior: acceleration at 2.0 s = 2 m/s^2.

## Scale from the prior (pixel acceleration)
- Track: scene/tracks/bird.csv (beak_x and body_cx). Checked the record: it follows the phoenix over frames 0-71, and the camera is static.
- The speed pulses with each wingbeat (period ~12.5 frames), so a one-frame difference at frame 48 is noise-dominated.
  Instead I used mean speeds over whole two-flap windows (25 frames each) (fit.py):
  - beak: 10→35: 224.6 px/s (t=0.94), 35→60: 470.4 px/s (t=1.98) → a = 236.0 px/s²
  - beak: 21→46: 333.1 px/s (t=1.40), 46→71: 580.8 px/s (t=2.44) → a = 237.8 px/s²
  - body_cx gives the same values (±1 px/s²). A global quadratic fit over frames 2-71 gives 240-242 px/s² (rms 12 px, from the wingbeat ripple).
  - Fitting harmonics plus a quadratic (fit2.py) was unstable (the period ran to the edge of the search range), so I did not use it.
- The acceleration looks uniform (the windows agree), so a ≈ 238 px/s² → scale = 2/238 ≈ 0.00840 m/px.

## Wingspan in pixels
- wing_span_px maxima (wings flat/horizontal, which gives the largest projected extent): 616 (f21), 613 (f46), 618 (f71).
  I also checked frame 71 on a crop with a grid: the wing tips run from y≈405 to y≈1030 (~620 px), which matches.
- Span ≈ 617 px × 0.00840 = 5.18 m. Using 240 px/s² instead gives 5.14 m; using 236 gives 5.23 m.

## Answer
5.2 m. Confidence: moderate-high on the scale. The main uncertainty is whether the reference uses the maximum spread
in flight or the model's rest-pose bbox (likely similar if the rest pose has the wings spread).
For reference, the body length of 436 px would be ≈ 3.7 m.
