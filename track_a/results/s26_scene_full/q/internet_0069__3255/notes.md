# q3255 – velocity of the cup at 2.30 s

The prior says the cup's acceleration from 2.00 s to 2.30 s is 0.32 m/s². The question asks for the velocity at 2.30 s.

## Approach

- The video is 2D. The camera is static: the background drifts by no more than a few px, while the mug moves 60-95 px per frame.
- There is one scale, taken from the prior. Scale = 0.32 / (pixel acceleration over frames 60→69), so
  v = 0.32 × v_px / a_px.
- Time base: the question uses 30 fps and the file runs at 30.013 fps, which is negligible. 2.00 s is frame 60 and 2.30 s is frame 69.

## Measurement

I wrote my own tracker (`measure.py`, output in `edges.json`):
- Each frame is compared with the empty background (frame 100) in the band y = 700-780.
- I take the widest run of columns where at least 60% of pixels differ, and find the edges at sub-pixel precision.
- The results match `scene/tracks/mug.csv` to within 1 px.

The body width changes from 453 to 419 to 459 px across the frame because of the cylinder's perspective. So I used the body centre (frames 62-79) as the main point. The leading (right) edge, frames 55-79, was a second route; it is the only edge visible at 2.00 s.

## Results

These come from `analyze.py` and `analyze2.py`.

| Route | a (px/frame²) | v at frame 69 (px/frame) | v (m/s) |
|---|---|---|---|
| Centre, linear fit of v, frames 62-72 | 1.59 | 78.7-79.5 | 0.52-0.53 |
| Centre, frames 62-79 | 1.55 | ≈79 | 0.54 |
| Right edge, frames 57-70 | 1.60 | ≈77 | 0.51-0.52 |
| Right edge, annotator style (forward differences, a = (v69 − v60)/9) | 1.645 | 79.0 | 0.512 |
| Right edge, frames 58-72 | 1.70 | ≈78 | 0.48-0.49 |

The left edge at frames 80-84 is distorted by the frame edge and was not used.

## Sanity check

The scale is about 2.2e-4 m/px. That puts the mug body at about 9.2 cm wide and about 12.4 cm high (570 px), which is plausible.

## Answer

**0.52 m/s.** The routes span about 0.48-0.55. Confidence is moderate: the result depends on the pixel acceleration, which carries about ±7% uncertainty.
