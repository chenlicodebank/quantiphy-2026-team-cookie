# q1315 — average speed of the walking pedestrian, 1.0 s to end (frames 24–71, question_fps 24 = file fps)

## Geometry
- The pedestrian (white T-shirt) walks right to left along the far sidewalk of the cross street, at a constant image row
  (feet y ≈ 299, pelvis row v ≈ 243). The street vanishing point is ≈(1060,−121) and the horizon is level, so the
  cross-street direction is ≈ the camera x-axis. Model: pelvis at constant camera Y and Z, with X linear in time.
- He is hidden behind the near-left signal head until f33, so frames 14 and 24–32 come from extrapolating at
  constant walking speed.
- Focal length from the human's own depth_info: d = Z·n/f with n = sqrt((u−cx)²+(v−cy)²+f²) and principal point
  (1080,540). The ratio d38/d14 = 38.7220/38.3473 together with u14 and u38 (from the linear fit) gives f ≈ 2190 px and Z ≈ 36.35 m.
  This reproduces both given human distances by construction.
- Speed = pixel speed × Z/f.

## Pixel speed (solve.py, fit2.py, shirt.py)
- Record track ref_x (mask centroid), fit over f36–71 excluding f46–52 (a thin pole crosses in front of him there):
  3.077 px/frame → f 2190, speed 1.226 m/s.
- Late segment f53–71: ref_x 3.02 px/f → 1.213 m/s; white-shirt centroid 3.12 px/f → 1.236 m/s.
- Early segment f36–45 is slower (2.7 px/f): there the trailing side of his body is still partly hidden by the signal
  head and its shadow, which biases the centroid, so I gave it less weight.
- One-frame speeds of a walking pelvis include vertical bob and sway, which adds roughly 1% to the mean.

## Check
- Second check: 103 px standing height × Z/f = 1.71 m, a plausible human height, which supports f ≈ 2150–2200.
- Routes give 1.19–1.24 m/s. Answer: 1.23 m/s. Confidence: moderate (±5%). The main uncertainties are the
  extrapolated, unseen positions at f14 and f24–32 and the centroid biases.
- The white-car acceleration prior was not needed. Its sensitivity to f is weak.
