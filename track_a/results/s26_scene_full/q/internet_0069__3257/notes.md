# q_3257 – cup displacement from 2.10 s to 2.30 s (cm)

Prior: the cup's acceleration from 2.00 s to 2.30 s is 0.32 m/s². Internet video, so I used a planar model with one scale taken from the prior: scale = 0.32 / a_px.

Time base: the file's rate (30.013 fps) and question_fps (30) give the same frames: 2.00 s → frame 60, 2.10 s → 63, 2.30 s → 69.
Camera: static. The background drifts by only a few px over the clip (scene/tracks/camera.csv).

## Measurements
- Body edges come from scene/tracks/mug.csv, band y 720–760. I re-measured them independently in measure.py (sub-pixel, edges.csv). In the clean frames 67–73 they agree to within about 1 px.
- Reference point: the body centre, (left + right)/2. This cancels the cylinder's perspective widening (width 452 px at frame 62 → 419 at 70).
- Pixel acceleration, from a quadratic fit (fit.py):
  - centre, frames 62–79: 1.565 px/frame²
  - centre, frames 62–69: 1.613 px/frame²
  - leading (right) edge, frames 60–69: 1.500 px/frame²
  - trailing (left) edge, frames 62–69: 1.643 px/frame²
- Adopted a_px ≈ 1.56 px/frame² = 1405 px/s², so scale = 2.28e-4 m/px. As a sanity check, the mug body is about 420 px ≈ 9.6 cm wide, which is plausible.
- Centre displacement from frame 63 to 69: 809.0 − 365.0 = 444 px (left edge 458, right edge 430).

## Answer
444 px × 0.32 / 1405 = 0.101 m → **10.1 cm**

Second-route check: using each reference point consistently for both the acceleration and the displacement:
- right edge: 430 × 0.32 / (1.50 × 900) = 10.2 cm
- left edge: 458 × 0.32 / (1.643 × 900) = 9.9 cm

The routes agree within about 3%.

Confidence: moderate-to-good. The main uncertainty is how the annotator estimated the pixel acceleration (±5%).
