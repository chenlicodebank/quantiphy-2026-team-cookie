# q_515 – horizontal length of the droplet

This is a 2D scene: the droplet falls in a plane facing the camera at 60 fps (fps and question_fps agree). The prior gives the droplet's acceleration as 9.7 m/s².

- **Pixel acceleration** (`measure.py`, using the centroid track in scene/tracks/droplet.csv, which I checked):
  - Backward-difference speeds, then the difference of speeds, give a mean of 113,700 px/s² over frames 2–10 and 113,550 px/s² over all frames.
  - A quadratic fit of y over frames 0–10 gives 113,370 px/s², and over frames 2–10 it gives 112,800 px/s².
  - Horizontal acceleration is negligible (about 1,500 px/s²).
  - I used 113,400 px/s². The scale is 9.7 / 113,400 = 8.55e-5 m/px.
- **Droplet width** (bounding-box x extent, measured with full-resolution difference masks against frame 13 in frames 2–8):
  - Threshold 15: 56–60 px. Threshold 25: 49–57 px, typically 55–57. Threshold 10: 59–64 px.
  - In frames 0–1 the box is 57 px wide. PCA minor width is 55–58 px.
  - I took 57.5 ± 2 px.
- **Answer:** 57.5 × 8.55e-5 = 0.00492 m, so about 0.0049 m (a 4.9 mm drop; the height is about 90 px, or 7.7 mm, which is plausible).
- **Second check:** the fit and the finite-difference routes for the acceleration agree within 1%. The width is consistent across frames and thresholds within about ±4%.
- **Confidence:** good, roughly ±5%.
