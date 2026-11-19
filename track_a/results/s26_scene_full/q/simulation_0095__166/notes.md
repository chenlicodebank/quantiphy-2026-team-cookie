# Q166 – height of the car (m)

2D simulation, 24 fps (file fps = question_fps, so there is no re-timing). Prior: car acceleration = 10 m/s^2. Scale = 10 / (pixel acceleration).

## Pixel acceleration (measure.py)
I segmented the car in every frame (|rgb-bg| > 6 below y = 545) and fitted x(frame) with a quadratic:
- Mask centroid, frames 2-71: 0.5065 px/frame^2. Frames 10-71: 0.5062. Frames 20-71: 0.5058. Residual RMS 0.13 px.
- Bbox centre: 0.504. Front edge: 0.509. Rear edge: 0.499. The front/rear difference comes from slight perspective and blur.
- Second route: the mean of the per-frame speed differences of the centroid (frames 10-71) is 0.508.
- I used 0.506 px/frame^2, which is 291.5 px/s^2. Scale = 10 / 291.5 = 0.0343 m/px.

## Car height in pixels
- Roof to wheel bottom: 56 px with threshold 6, 55 px with threshold 20, at frames 0, 24, 48 and 71. The mean over all frames at threshold 6 is 55.9.
- A zoomed crop of frame 0 shows a clean silhouette with no shadow. I used 55.5 px, which allows for antialiasing.

## Answer
55.5 px x 0.0343 m/px = 1.90 m. The range is 1.89-1.92, depending on the height in pixels (55-56) and the acceleration (0.504-0.509).
This is plausible for a Cybertruck-like pickup (real one is about 1.8-1.9 m). Confidence: good, about 3% uncertainty.
