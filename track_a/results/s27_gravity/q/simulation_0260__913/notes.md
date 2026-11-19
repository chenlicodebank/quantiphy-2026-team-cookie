# q913: speed of the mug at t = 0.2 s

The file and the question both run at 30 fps, so t = 0.2 s is frame 6. Speed is the backward difference between frames 5 and 6.

## Method
- **Data:** the mug's vertical track from scene/tracks/mug.csv. The record is consistent: the mug falls straight down at x ≈ 1241 and lands at frame 16.
- **Scale:** this is a 2D scene, so the prior (a = 9.8 m/s² before 0.5 s) sets the scale. I fitted a quadratic to the pixel position in fit.py, which gives the pixel acceleration a_px. Then v = Δy_px(5→6) / a_px × g / fps.
- **Which edge to fit:**
  - The bottom edge (y1_true, frames 2-15) is the cleanest: a_px = 6.89 px/frame², rms 0.43 px, and the fit puts the release from rest at frame -0.03, i.e. frame 0.
  - With that edge, v(0.2) is 1.806 m/s from the fit and 1.802 m/s from the raw pixel difference.
  - The top and centre (ref_y) are disturbed by the perspective change in apparent height (71 → 53 px). They give 1.75-2.00 m/s depending on the window.
- **Second route (analytic):** a release from rest at frame 0 with g = 9.8 gives v = g × (6² − 5²) / (2 × 30) = 9.8 × 5.5 / 30 = 1.797 m/s. This agrees with the bottom-edge measurement.

## Answer
1.80 m/s. Confidence: high (about ±3 pct).
