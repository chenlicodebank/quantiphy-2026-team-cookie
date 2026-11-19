# Q1815: length of the car (m). Prior: car speed = 6.66 m/s

- 2D scene, static camera, 24 fps (file fps = question_fps, so no re-timing). The car moves uniformly from left to right.
- `measure.py`: median-background difference mask (threshold 40, rows above the platform at y=540), frames 13-36 where the car is fully in view.
  - Silhouette bbox centre: linear fit gives 27.285 px/frame. This matches the scene record (27.29).
  - Front-edge and rear-edge tracks independently give about 27.1-27.2 px/frame.
  - Bumper-to-bumper length: 421-423 px near the image centre, median 422 px. Near the borders it reads 428 px because of the oblique view of the bumpers.
- Scale: 6.66 / 24 = 0.2775 m/frame, so 0.2775 / 27.285 = 0.010170 m/px.
- Length = 422 × 0.010170 = **4.29 m**. A Porsche-911-like coupe is about 4.3 m long, so this is plausible.
- Check: the near-side wheels move about 3.5% faster (28.2 px/frame) because of perspective. Using them as the speed reference would give 4.15 m. The silhouette length and the silhouette speed are measured at the same depth, so they are the consistent pair, and I use them.
- Confidence: good, ±3%.
