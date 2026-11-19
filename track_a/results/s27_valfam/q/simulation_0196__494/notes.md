# Q494: horizontal length of the droplet (m)

- 2D scene with a static camera. File fps = question fps = 30.
- Prior: the bubble (the sphere sinking inside the hanging drop) moves at 0.00144 m/s. The scene record gives its
  pixel speed as 109.0 px/s (constant-velocity fit, RMS 0.77 px).
  - My check (`measure.py`): the sphere's top edge, taken from frame differences, is at y 901 in frame 10 and y 952
    in frame 24. That is 3.64 px/frame = 109 px/s, so the record is confirmed.
  - Scale = 0.00144 / 109.0 = 1.321e-5 m/px.
- Droplet width (`width.py`, frame 24): I measured the outer silhouette against the local background on each row.
  - The widest part is at y ≈ 1090–1100, from x 580.5 to 727.5, which is about 147 px.
  - The scene record has 151 px (x 579–730).
  - Adopted: 149 ± 3 px.
- Answer: 149 × 1.321e-5 = **0.00197 m** (about 2.0 mm).
- Confidence: about ±3%, covering the edge definition of the transparent drop and the speed uncertainty.
