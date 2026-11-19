# Q873: speed of the tennis ball at t = 1.5 s (m/s)

- 2D render at 24 fps (file fps = question_fps = 24). t = 1.5 s is frame 36. The camera is static and there is one ball,
  rolling right along y ≈ 563 px and slowing steadily.
- Scale prior: ball diameter = 0.17 m.

## Measurements (scripts in this folder)
- `measure.py`: centroid of the background-difference mask (diff-weighted) in every frame.
  - dx(35→36) is 34.99 px/frame raw.
  - A quadratic fit to x(frame) over frames 0–40 (residual 0.13 px) gives dx(36) = 34.75 px/frame.
  - Adopted: 34.8 px/frame = 835 px/s. The scene record's chroma centroids give 35.0 px/frame, which agrees.
- `diam.py` and `prof.py`: ball diameter in pixels.
  - Subpixel half-max widths over frames 20–40: horizontal 23.1 px and vertical 24.7 px. The vertical value includes
    the dark lower rim and perhaps a little contact shadow.
  - Raw colour profiles at frame 36: horizontal edges at 1475.5 and about 1499.3 (23.8 px); vertical edges at 551.5
    and about 576.3 (24.8 px).
  - Adopted D = 24.3 ± 0.5 px. The scene record's estimate is 24.5 px.
- Scale = 0.17 / 24.3 = 0.00700 m/px.

## Answer
Speed = 835 px/s × 0.00700 m/px = **5.83 m/s**.

## Check
- The raw one-frame difference gives 5.87 m/s and the fitted value gives 5.83 m/s.
- With D = 24.5 px the answer is 5.80 m/s; with D = 23.8 px it is 5.96 m/s.
- The main uncertainty is the pixel diameter, about ±2–3 %. Confidence is fairly high.
