# Q211 – height of the ice cube (m)

Prior: gravity = 9.8 m/s^2. 2D scene (static camera, plain background), file fps = question_fps = 24.

## Scale (from the prior)
- `measure.py` re-tracks the falling cube (|grey − bg| > 25, largest blob, centroid) in frames 22–45
  (frame 21 clipped at the top, frame 46 inside the cup). Track matches scene/tracks/cube.csv.
- Quadratic fit y(t): a = 682.4 px/s^2, residual rms 0.12 px. First half (f22–33) 682.0, second half (f34–45)
  683.0 → consistent free fall.
- Scale = 9.8 / 682.4 = 0.01436 m/px.

## Cube size in pixels
- Subpixel edge-profile extents (coverage-weighted, mean over 24 frames): vertical 25.9 px, horizontal 25.2 px;
  sqrt(area) 25.9 px; bbox 26 x 26–27 (incl. anti-aliased edge). Raw pixel dump of frame 38 (`look.py`) gives
  ~25.5–26 px tall and ~25.6 px wide. Face seen square-on. Adopted 25.6 ± 0.4 px.

## Answer
height = 25.6 px x 0.01436 m/px = 0.367 m (range 0.362–0.372 across the size estimates).
The cube is large for an ice cube (the cup is ~1.1 m tall at this scale), so the scene is scaled up; the gravity
prior is exact and fully observed in the fall, so it sets the scale. Confidence: good (~±3 pct).
