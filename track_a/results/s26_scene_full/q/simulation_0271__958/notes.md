# q_958 — wingspan (width) of the phoenix

2D simulation, 24 fps (same as question_fps), top-down view, head pointing left, bird flies left.
Prior: the phoenix's acceleration at 2.0 s is 2 m/s². That sets the metres-per-pixel scale.

## Scale from the acceleration (fit2.py)
- Beak-tip x track (scene/tracks/phoenix.csv, frames 0-69; the beak moves rigidly with the body) shows uniform
  acceleration from rest plus a ripple from the flapping, which repeats every 25 frames (the flap period).
- Fit: x = x0 + v0·f − ½·a·f² + Fourier terms with a 25-frame period (2-6 harmonics). Result: a = 0.6571 px/frame²
  = **378.5 px/s²**, v0 ≈ 0, residual 1.1 px. Using sub-windows 0-49 and 20-69 gives 378.5 and 378.4.
  Scanning the period shows 25 frames fits best (the residual rises quickly away from it).
- The round prior (2 m/s²) fits a constant acceleration of the origin. The local beak ripple is flapping motion of the
  model relative to its origin.
- Scale = 2 / 378.5 = 0.005284 m/px.

## Wingspan in pixels (span.py)
- Width = wingspan = the vertical (y) image extent in this top-down view. Frames 21, 46 and 71 have the wings at
  their widest: 1008 px, holding within 1004-1009 px for mask thresholds 8-30. Other peaks are 930-940 px; the
  narrowest is 374 px with wings folded. Checked visually at frame 21: the extent runs wing tip to wing tip.
- Maximum span: 1008 × 0.005284 = **5.33 m**. Other readings: the 938 px peak gives 4.96 m; minimum width
  374 px gives 1.98 m. I answer with the maximum wingspan, the full spread.

## Second route
- Body-template cumulative shift (phoenix_body_shift.csv) gives the same fit at a = 368.8-380.5 px/s², so a span of
  5.30-5.47 m.
- Mean per-cycle beak speed rises by 16.4 px/frame per 25 frames, which gives a = 378 px/s². This agrees.

Confidence: the scale is good (±1-2 %). The main uncertainty is whether the reference uses the maximum spread (5.33 m).
