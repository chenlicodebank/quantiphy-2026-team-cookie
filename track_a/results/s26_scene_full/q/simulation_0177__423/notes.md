# q423 — elephant height (simulation_0177, 2D side view, 24 fps; file and question fps agree)

Scale from prior (speed 1.424 m/s):
- Pixel speed: record's torso template track has a mean step of 3.53 px/frame (84.8 px/s). I re-checked it with my own
  dark-pixel mask (measure.py): the rump edge slope is 3.72 px/frame, and the record's rump edge gives 3.42. All agree at ≈3.55 px/frame
  ≈ 85 px/s. Camera is static.
- m/px = 1.424 / 85.0 = 0.01675.

Height (pixels):
- My own mask: top ≈ 656–660 (the mask misses the light head-top patch), bottom ≈ 831–847. Median extent 180 px.
- On a 2x zoom at f30 the head top is at y≈654 and the feet at y≈835–840, so ≈183 px. The record says 184 ±6.
- Using 183 px: height = 183 × 0.01675 ≈ 3.07 m. Grass hides the soles by a few px, so the true value may be slightly
  higher, up to about 3.1 m.

Second route: the record's own numbers (184 px, 84.7 px/s) give 3.09 m.
Answer: 3.08 m. Confidence: moderate-high (±5 %). Most of the uncertainty is the pixel speed.
