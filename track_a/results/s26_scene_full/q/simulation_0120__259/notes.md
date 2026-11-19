# Q259 – diameter of the robot cleaner (m)

Prior: speed of robot cleaner = 1 m/s. 2D top-down render; one metres-per-pixel scale from the vacuum's pixel speed.
fps 24.0078 (question_fps 24.0: difference 0.03 %, irrelevant).

- Pixel speed: straight-line, constant motion along row y≈811.5. Linear fit of circle-fit centres (scene track):
  8.401 px/frame (frames 0–32, unoccluded) and 8.410 px/frame (all frames) → 201.8 px/s.
  Scale = 1 / 201.8 = 4.955e-3 m/px.
- Pixel diameter: circle fit 68.89 ± 0.33 px (scene track, frames 0–32); my own check (measure.py, threshold >180
  mask, min enclosing circle, frames 4–32) 68.7–69.3 px, bbox ~69x68 px.
- Diameter = 68.85 px / 201.8 px/s × 1 m/s ≈ 0.341 m.

Second route: my independent mask track gives 0.343 m (its speed fit 8.34 px/frame is pulled down by the partly
hidden mask in frames 0–3, so I kept the record's circle-fit speed). A real robot vacuum is about 0.34 m across, so the value is plausible.
Confidence: high (±2 %).
