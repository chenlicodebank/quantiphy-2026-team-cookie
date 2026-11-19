# q_882 – acceleration of the tennis ball at t = 1.5 s (frame 36)

2D sim, 24 fps (file fps = question_fps, so no retiming). Static camera, one ball moving horizontally left→right at
constant cy ≈ 364 and slowing down steadily; no bounce.

## Tracking (measure.py)
Lab b* mask (>12 above median), largest component, b*-weighted centroid, frames 6–39 (fully visible).
Per-frame dx goes smoothly from 61.0 to 49.3 px/frame: almost constant deceleration.
Quadratic fits for a (px/frame²): all frames 6–39 −0.383; 6–22 −0.388; 22–39 −0.371; 28–39 −0.358; 30–39 −0.333;
cubic fit evaluated at frame 36 −0.369. Used −0.37 px/frame² = −213 px/s² at t = 1.5 s.

## Scale (diam.py)
Ball diameter in px: bbox 34–36 (median 36), equivalent-area diameter 34.7, b* profile edges ≈35–36 (chroma is
4:2:0 so ±1 px). Used 35.5 px → 0.17 / 35.5 = 0.00479 m/px.

## Answer
|a| = 213 × 0.00479 ≈ 1.02 m/s² (the ball is decelerating; magnitude given).
Second route: the global uniform fit (−0.383) gives 1.06; using 36 px diameter gives 1.00. So the range is about 1.00–1.06.
Confidence: moderate-high (~±5%); most of the uncertainty comes from the pixel diameter.
