# q_352 — acceleration of the blue car at t = 1.5 s

fps = question_fps = 24, so t = 1.5 s is frame 36. accel(36) = (speed36 − speed35)·fps = (x36 − 2·x35 + x34)·fps².
The scene is 2D: a light-blue cart moves side-on, left to right, at constant depth. I used one m/px scale from the tyre.

## Scale (prior: tyre diameter = 0.369 m)
- radial.py / radial_plot.py: I sampled the outer tyre edge along radial profiles of the front wheel (sides only, because the
  fender is above it and the shadow below) and fitted a circle (Kasa fit with outlier rejection).
  Results: D = 112.6 px (f32), 114.6 (f34) and 113.3 (f36). The overlays (frames/fit_*.png) fit well. At f38/f40 the
  right-side edge detection failed (105.9 and 100.3 px), so I rejected those fits. By eye the tyre at f36 spans
  y 836→948 (≈112 px) and about 113 px horizontally.
  **D = 113 ± 1 px → 0.003265 m/px.** The record's "≈105 px" wheel diameter is too small.

## Motion
- I took the panel template track from scene/tracks/cart.csv (panel_x, smooth, NCC ≈ 0.9) and checked it with my own masked
  whole-body template registration from 4 reference frames (track2.py). Both show the same profile: peak ≈ 50 px/frame at
  frames 29–31, then a deceleration that grows steadily (the second differences go from 0 to −1.3 px/frame² over frames 31–41,
  so the jerk is roughly constant).
- accel.py: a cubic fit to the positions over frames 29/30–41 gives x36 − 2x35 + x34 = −0.63 px/frame². The fit rms is
  0.04 px on the panel track. The body track gives −0.628/−0.658. A linear fit to the panel's raw second differences
  over 31–41 gives −0.628. The raw single value is −0.53, which is noisy.
  Quadratic fits centred on frame 36 give −0.74. That is the value at frame 36, not at the frame-35 centre of the backward
  difference, and it agrees with jerk ≈ −0.12 px/frame³.
- −0.63 px/frame² × 576 = −363 px/s² → × 0.003265 = −1.18 m/s². The cart is decelerating; the magnitude is reported.

## Second route
The masked whole-body registration (independent of the panel template) gives the same −0.63 to −0.66 px/frame² from the cubic fit.
The tyre diameter from 3 frames agrees within ±1 %.

Answer: 1.18 m/s² (uncertainty about ±5 %, mostly from the tyre pixel diameter and how the reference evaluates a changing deceleration).
