# q_214 – velocity of the ice cube at 1.0 s

- 2D render, 24 fps (file and question fps match); t = 1.0 s → frame 24.
- Re-tracked the cube myself (`measure.py`: soft-mask centroid, and the mid-point of the half-max top/bottom edges)
  on frames 22–45 (frame 21 is clipped at the top edge). My track matches scene/tracks/cube.csv to within about 0.2 px.
- Quadratic fit y(t): pixel acceleration 681.7 px/s² (rms residual 0.06 px), so
  scale = 9.8 / 681.7 = 0.01437 m/px. The cube comes out about 0.37 m wide. That is not a realistic ice cube,
  but the gravity prior is exact, so the scene is scaled.
- The fit gives v = 0 at t ≈ −0.014 s, i.e. the cube is released at about t = 0.
- Speed by the benchmark convention (one-frame backward difference, frame 24 minus frame 23):
  - raw centroid: 28.11 px → 9.70 m/s
  - edge mid-point: 9.72 m/s
  - from the quadratic fit: 9.73 m/s
- Check: the instantaneous v(1.0) is 9.94 m/s, and g × (1 − 1/48 + 0.014) = 9.73 m/s, which is consistent.
- Answer: 9.73 m/s. Confidence high: the routes agree within 0.3 %.
