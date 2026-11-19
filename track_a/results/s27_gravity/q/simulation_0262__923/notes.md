# Q923 – speed of the red cup at t = 0.5 s

2D scene (single cup falling straight down, camera static), file fps = question_fps = 24. t = 0.5 s -> frame 12.
Prior: acceleration before 0.75 s = 9.8 m/s^2 -> scale from pixel acceleration.

Method (measure.py): body mask = HSV saturation > 90 (red body); tracked its centroid y and sub-pixel bottom edge
per frame, fitted a quadratic over the fully visible free-fall frames 6–18.
- Centroid: a = 11.21 px/frame^2, residuals < 0.9 px. Backward-difference speed at f12 = 129.5 px/frame (raw) / fit 129.3.
  v = d/a * 9.8/24 = 4.72 (raw) / 4.70 (fit) m/s.
- Bottom edge (second route): a = 11.36 px/frame^2, v = 4.55–4.59 m/s (edge shifts slightly with viewing angle; residuals ~1.9 px).
- Top edge (lid, noisier): ~5.0 m/s – least reliable.
Consistency check: centroid result implies the cup was released from rest at frame 0 (v/a = 11.5 frames = f12 - 0.5),
the natural simulation set-up; then v = 9.8 * 11.5/24 = 4.696 m/s.

Answer: 4.70 m/s. Confidence: high (±3%).
