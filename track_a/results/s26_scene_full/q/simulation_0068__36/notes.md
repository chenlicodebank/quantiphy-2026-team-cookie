# q36 – width of the white car (simulation_0068)

- 2D top-down scene, 24 fps (file fps = question_fps; no retiming). The white car is the white van driving straight north at x≈831.
- Prior: van acceleration = 4 m/s² → scale from van pixel acceleration.
- Pixel acceleration (measure.py): quadratic fits of the vertical position vs time
  - record colour-mask centre ccy: 161.1 / 161.1 / 160.8 / 159.8 px/s² (fits starting at frame 3/5/10/20), rms 0.3-0.4 px
  - own white-mask front edge: 162.4 / 162.4 / 162.1; own mask centre: 160.1 / 159.5 / 157.8 (rear edge is softer, so it is less reliable)
  - per-frame steps grow linearly from ~1 px to ~20 px over frames 2-71 → (20-1)/69 × 24² ≈ 159 px/s²; agrees.
  - adopted 160.5 px/s² → scale = 4 / 160.5 = 0.02492 m/px.
- Width (shorter horizontal extent across the body): white body mask 84 px (record cwidth median 84; my own mask median 84).
  Background-difference mask 87-88 px (includes soft shadow / small mirrors).
- Width = 84 × 0.02492 = 2.09 m (if mirrors/shadow are included: 88 px → 2.19 m).
- Second-route check: van length 234 px → 5.83 m, length/width ≈ 2.8, which fits a minibus/van, and a width of about 2.1 m is realistic.
- Confidence: moderate-high; main uncertainty is ±2-3 px on the edges (±3%) and whether the bounding box includes the mirrors.
