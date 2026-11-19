# Q1029 – butterfly displacement, 0.5 s to 1.0 s

- Time base: the file and the question both use 24 fps, so the interval is frames 12 to 24.
- Prior: the butterfly's speed is 0.32 m/s. This is a 2D scene: a static camera, with the butterfly flying right to left in a near-straight, near-horizontal line.
- Measurement (m.py, using scene/tracks/butterfly.csv):
  - The pixel motion is very close to uniform.
  - Linear fit of the mask centroid over frames 2–63: −31.06 px/frame. Adding a quadratic term changes it by only −0.006 px/frame².
  - Linear fit of the raw body points: −30.78 px/frame.
  - Body quadratic fit: 30.27 px/frame over frames 12–24, against 30.79 px/frame on average over the clip.
  - Vertical drift is negligible, so the path is straight.
- Scale: speed is constant and the path is straight, so displacement = speed × Δt = 0.32 × 0.5 = 0.160 m.
- Second route: suppose the prior is instead the clip-average speed. Using the body fit, displacement = 363.2 px over frames 12–24 and 0.32 m/s ↔ 30.79 px/frame × 24 fps. That gives a scale of 4.33e-4 m/px and a displacement of 0.157 m. The centroid route gives 375.6 px, which is about 0.163 m. Both agree within 2 %.
- Answer: 0.16 m. Confidence: high.
