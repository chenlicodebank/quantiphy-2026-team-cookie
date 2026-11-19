# q_3143: height of the bench (internet_0053)

Prior: the rider's average speed is 4.46 m/s. The file and the question both give 30 fps, so I used 30 fps.
Convention: one planar scale factor, prior world value / prior pixel value.

## Pixel speed of the rider (speed.py, scene track; camera drift is under 2 px and changes nothing)
- scooter_cx, frames 0-80: 540 px/s. Frames 0-73 (fully visible): 547 px/s.
- rear wheel, frames 0-80: 543 px/s. Upper-body track, frames 0-80: 538 px/s.
- The rider slows down and the path is slightly oblique (about 12% shrink). Over the whole clip the average is about 543 px/s, ±1%.
- Scale = 4.46 / 543 = 0.00821 m/px.

## Bench height in pixels (frame 0, zoomed crops frames/bench_r2.png and bench.png, and the column profiles in bench.py)
- The top of the back post is at y ≈ 552.5. The thin pole above it belongs to the fence, not the bench.
- The feet are at y ≈ 700-701, on the asphalt edge.
- Height ≈ 148-149 px. This agrees with the scene record's bbox, 552-701 = 149 px.

## Answer
149 px x 0.00821 m/px = 1.22 m.

Check: the alternative speed windows (538-547 px/s) give 1.21-1.24 m.
Sanity: the result is large for a real bench (about 0.8-0.9 m). The prior itself implies a large scale: the rider would be about 2.5 m tall. The benchmark's convention takes the prior as exact, so I keep 1.22.
The bench stands at the fence, slightly farther from the camera than the path, but the convention applies no perspective correction.
Confidence: moderate. The result follows the convention, and the pixel measurements are good to about 2%.
