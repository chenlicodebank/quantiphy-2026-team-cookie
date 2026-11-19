# Q1001 – height of the plane (prior: speed 22.16 m/s)

2D simulation: a jet flies horizontally from right to left at a constant height (y ≈ 417 px). The camera is static.
I used one metres-per-pixel scale, taken from the prior speed.

## Measurements (`measure.py`, my own masks: background difference > 22, then a close, then the largest component)
- **Height (vertical bbox extent, fin top to wheel bottom).** 224 px in every fully visible frame, 13-55
  (median 224.0, mean 224.1). This matches the scene record.
- **Pixel speed of the origin proxy (bbox centre = midpoint of nose and tail, on the fuselage centreline).**
  - From 2156 px at frame 13 to 393.5 px at frame 55: 1762.5 px / 42 frames = 41.96 px/frame.
  - The nose edge gives 42.3 px/frame and the tail edge 41.6 px/frame.
  - Template matching gives ~43.4 px/frame. It is biased because the textured near-side parts are closer to the
    camera, and the template correlation drops to 0.83 as the view rotates. I did not use it.
- **Scale.** 22.16 m/s / (41.96 px/frame × fps).

## Time base
The file is 24 fps; question_fps is 25. Both rates give a plausible jet, so physics cannot decide between them:
- at 24 fps: height = 224 × 22.16 / (41.96 × 24) = 4.93 m, and the length (~707 px) is 15.6 m;
- at 25 fps: height = 4.73 m, and the length is 14.9 m.

Both are close to fighter-jet proportions (e.g. 15 m long and 4.9 m high). Since I cannot decide, I answer the
midpoint, 4.83 m, which is within about 2.1% of either reading.

## Second-route check
The nose-edge and tail-edge speeds (42.3 and 41.6 px/frame) bracket the centre speed. They change the result by
less than 1%.

Confidence: moderate-high on the pixel ratio. The main uncertainty is the 24 vs 25 fps time base (±2% around the
answer).
