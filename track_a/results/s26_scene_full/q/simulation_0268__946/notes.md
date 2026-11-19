# Q946 — width of the spacecraft (m)

2D top-down render, 24 fps (file fps = question_fps, so no re-timing). The spacecraft starts at rest and accelerates
uniformly to the left along y ≈ 720 px. The camera does not move.

## Scale from the prior (acceleration = 4 m/s² at 1.0 s)
- `fit.py`: quadratic fits to the silhouette-centre track (`x_ref` in scene/tracks/vehicle.csv) give a pixel
  acceleration of 696.5 px/s² (frames 2-58). The fits agree within 0.3% across windows (2-30: 695.4, 30-58: 697.6,
  12-36: 695.2). The per-frame second differences near frame 24 scatter around about 700.
- Scale = 4 / 696.5 = 0.005743 m/px.

## Width
- Seen from above, width is the vertical image extent (the shorter horizontal extent, across the nose-to-tail
  axis). `width.py` builds a background-difference mask (background = mean of the empty frames 67-71). It gives
  y 463-976, so 514 px, at frames 24, 30 and 36. This matches the scene record, and the extent is constant over time.
- Width = 514 × 0.005743 = **2.95 m**.

## Checks and confidence
- The texture track's acceleration (721 px/s², top surface nearer the camera) would give 2.85 m. The rear-fin track
  (680 px/s²) would give 3.02 m. I used the silhouette-centre track because it matches the silhouette-based width
  measurement. Length for comparison: about 1020 px, or 5.9 m.
- Confidence: good. The result is within about ±3%, the uncertainty coming from which point on the 3D craft the
  origin corresponds to.
