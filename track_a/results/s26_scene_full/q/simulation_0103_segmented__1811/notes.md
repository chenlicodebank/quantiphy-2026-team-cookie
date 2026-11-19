# q_1811 – height of the shark (m)

2D side-view render, 24 fps (file fps = question_fps, no re-timing). Prior: shark acceleration = 1 m/s^2.

## Scale from prior
Shark moves left with constant acceleration from f2 on (f0-f1 at rest).
- scene track (fit.py), quadratic fits of x(t) for f1-53: bbox centre 85.6, mask centroid 85.8, nose 86.4, tail 84.8 px/s^2;
  half-windows f2-27 / f27-53 of the mask centroid: 85.3 / 84.9.
- independent re-measurement from the video (check.py, intensity-weighted centroid): 86.0 (f1-53), 85.0 / 85.3 (halves).
- adopted a = 85.7 px/s^2 -> 1/85.7 m/px = 0.01167 m/px.

## Shark height
Vertical extent of the mask (incl. dorsal/pectoral fins): 103-104 px (record bbox_h mean 103.2; video re-measure 103-105 px
at thresholds 30-60, all frames). Adopted 103.6 px.

Height = 103.6 / 85.7 = 1.21 m.  (Length for sanity: ~276 px -> 3.2 m, plausible shark.)

Confidence: good; uncertainty ~2% (acceleration fit ±1%, edge ±1 px).
