# q167 – length of the plane (m)

2D simulation, 24 fps (file fps = question_fps = 24). Prior: car acceleration = 10 m/s^2.

## Scale (fit.py)
- Quadratic fit to car mask centroid x (scene/tracks/car.csv) over frames 2–71: a = 0.5072 px/frame^2 = 292.1 px/s^2
  (frames 2–40: 292.0; 40–71: 290.3; bbox centre: 290.8). Residual 0.17 px.
- Scale = 10 / 292.1 = 0.03423 m/px.

## Plane length (plane.py)
- Mask |rgb-bg| > 6 + 3x3 opening on rows < 545, full-visibility frames 7–16:
  nose-to-tail extent 1119 (frame 7, near right) → 1101 (frame 11, centred x≈987) → 1095 (frame 16). This is a perspective effect.
  Taken: about 1102 px with the plane centred in the image (the same place where the car is smallest, 166 px).
- Threshold 6 is needed for the semi-transparent nose (scene notes). Motion blur is negligible: the car's length depends only on
  image x, not on speed (carlen.py).
- Length = 1102 × 0.03423 = 37.7 m.

## Checks
- Car at image centre is 166 px → 5.68 m (Cybertruck real length 5.68 m); at rest it is 173 px → 5.9 m. Realistic.
- An A320 is 37.6 m long. This matches.
- Range from the frame choice (1095–1119 px): 37.5–38.3 m.

Confidence: high (about 2%).
