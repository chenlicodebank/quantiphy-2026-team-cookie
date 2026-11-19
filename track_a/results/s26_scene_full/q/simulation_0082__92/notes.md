# Q92 — distance yellow car ↔ black-and-white car at t = 2.0 s

- 2D top-down render, fps 24 = question_fps → t = 2.0 s is frame 48.
- `measure.py`: mask (dark / white / saturated pixels, as in scene/track.py), body box per truck at frames 47–49.
  Frame 48: yellow centre (1055.5, 400.5), length 304 px; white centre (842.0, 539.0), length 303 px.
  Centre separation dx = 213.5, dy = 138.5 → 254.5 px (mask centroids: 253.7 px).
- Scale from the prior: yellow length 5.67 m / ~305 px (304–306 px around frame 48, near image centre where the
  perspective side-view inflation is smallest) = 0.01859 m/px.
- Second route (kinematics): fronts/centres aligned at frame 0 (dx ≈ 1 px), relative speed 15.96 − 11.40 = 4.56 px/frame
  from frame 1 → dx(48) ≈ 1 + 47·4.56 = 215.3 px (xcorr track gives 215.2); with dy 138.5 → 255.9 px → 4.76 m.
- Answer: ~255 px × 0.01859 = **4.74 m** (routes span 4.70–4.77 m). Confidence: good (±2%); residual uncertainty is
  the perspective in the length scale and origin height vs. top surface.
