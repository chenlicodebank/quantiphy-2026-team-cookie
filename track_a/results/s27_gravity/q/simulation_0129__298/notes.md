# q298 – diameter of the ball (m), prior g = 9.8 m/s^2, 2D video, 24 fps (file fps = question fps)

Method: one metres-per-pixel scale from the ball's own pixel acceleration under gravity.
- measure.py: red-blob centroid per frame (x stays 955.6–956.3, purely vertical fall). Quadratic fit of y vs frame,
  frames 2–36: a = 0.4463 px/frame^2 *2 *576 = 514 px/s^2 (rms 0.29 px). Sub-windows: frames 2–19 → 505,
  19–36 → 511, 2–38 → 514; mean second difference 508. Adopted a = 511 px/s^2 (±1 %).
  Scale = 9.8 / 511 = 0.01918 m/px.
- Diameter in pixels: red-threshold blob bbox ~20 px, area-equivalent diameter 19.8–20.6 (mid-clip);
  diam.py half-max widths of the background-difference profile: horizontal median 19.4 px (unaffected by vertical
  motion blur), vertical 18.6 (top shading/blur lowers it), area-equivalent 19.2. Visual edge-to-edge 20–21.
  Adopted D = 19.8 px (±0.6).
- D = 19.8 × 0.01918 = 0.380 m. Range 0.372–0.391 m over the pixel-diameter estimates.

Second route: scene record's independent fit (519 px/s^2, 20 px) gives 0.378 m — consistent.
Confidence: good (±3 %), dominated by the ~20 px diameter's edge definition.
