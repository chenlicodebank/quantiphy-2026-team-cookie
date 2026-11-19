# Q880 – acceleration of the tennis ball at t = 0.5 s (frame 12)

fps = question_fps = 24 (no re-timing). 2D scene, static camera, ball moves horizontally left→right at constant y≈364.

## Method (measure.py → my_track.csv)
- Re-tracked the ball myself: Lab b* > median + thr (thr 8 / 12 / 18), largest component; centroid and bbox centre.
- Fully visible frames 6–39 (5 and 40 are cut by the image edge, excluded).
- Fitted x(frame) with a quadratic (whole range), a cubic (accel evaluated at frame 12) and a local quadratic on frames 6–18.
- Per-frame dx falls smoothly from ~61 to ~49 px/frame: uniform deceleration, no bounce.

## Key numbers
- Acceleration: -0.381 to -0.400 px/frame² across thresholds/methods; best (centroid, thr 8–12, global quadratic,
  rms 0.23–0.27 px) = -0.3845 px/frame² → -221.5 px/s².
- Ball diameter: bbox 36 × 36 px (thr 8 and 12), confirmed on a zoomed crop of frame 12 (x≈396–431, y≈346–382).
  Scale = 0.17 m / 36 px = 0.004722 m/px.
- a = 221.5 × 0.004722 ≈ 1.046 m/s² (deceleration; magnitude reported).

## Second route
Cubic fit with accel evaluated at frame 12 (-0.395..-0.400 px/frame²) and a local 6–18 fit (-0.36..-0.40) give
1.03–1.09 m/s²; consistent. Scene record (notes: ~-0.35 px/frame² rough) agrees roughly.

## Answer
1.05 m/s² (magnitude; the ball decelerates). Confidence: good, about ±4 % (mostly diameter ±1 px).
