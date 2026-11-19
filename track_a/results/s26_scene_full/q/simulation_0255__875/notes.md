# Q875 – acceleration of the tennis ball at t = 1 s (frame 24)

The video is a 2D render at 24 fps. The file and the question use the same rate. The ball rolls right along a constant row, slowing steadily the whole time. There is no bounce or occlusion, and the camera is static.

## Scale (prior: diameter = 0.17 m)
- `measure.py`: half-max widths of a background-difference mask across the ball's centre row and column. Width ≈ 23.0 px in the middle frames. Height ≈ 24.0 px, which may include a faint contact shadow.
- `diam.py`: a circle fitted to the radial half-max edge points, leaving out the bottom (shadow) side. This gives D = 23.5–23.9 px for frames 10–28 and 24.0–24.2 px for frames 36–40.
- Adopted D = 23.7 px, so the scale is 0.17 / 23.7 = 0.007173 m/px.

## Pixel acceleration
- `measure.py`: x is the intensity-weighted centroid of the background-difference mask.
- Fitting a quadratic to x(frame) gives a = −0.267 px/frame² (frames 0–40), −0.2655 (12–36), −0.2637 (16–32) and −0.2525 (20–28, the shortest and noisiest window). Residuals are about 0.07–0.13 px.
- Second route: the record's chroma-mask track in `scene/` fitted independently gives −0.2661 px/frame².
- The per-frame dx falls linearly from 44.3 to 33.8 px/frame, which is consistent with uniform deceleration.
- Adopted a = 0.2655 px/frame² × 576 = 152.9 px/s².

## Answer
|a| = 152.9 × 0.007173 = **1.10 m/s²** (deceleration).
- Uncertainty: the pixel diameter (23.0–24.2 px) contributes about ±3%, and the acceleration about ±1%.
- Confidence: good.
