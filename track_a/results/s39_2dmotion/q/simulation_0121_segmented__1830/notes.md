# q_1830 — speed of the left first ball at 1 s (m/s)

Prior: ball diameter = 2 m. 2D video, 30 fps (file fps = question_fps = 30), so t = 1 s is frame 30.
Speed = |p(30) - p(29)| x 30, then converted with one m/px scale taken from the ball diameter.

## What happens
The left ball (striker) hits the middle ball between frames 27 and 28. After that it almost stops and drifts back
to the left at about 1 px/frame (y stays constant near 784.7). So at frame 30 the left ball is moving slowly.

## Correcting scene/
In scene/tracks/ball_left.csv, frames 28–30 are wrong: x = 643.47 (f29) and 640.25 (f30). In those frames the left
mask touches the middle ball, so the hull fit took in the light crescent at the contact edge (radius 85 px). That
would give 3.2 px/frame, or 1.17 m/s.
I re-measured in `measure.py`. It cuts the mask at the gap column between the two balls (min column count,
x ≈ 718–720), then fits a circle to the dense convex-hull outline. It also tries a partial-arc fit (right side
excluded) and a fixed-radius fit.
- Full fit: x = 638.51 (f28), 637.56 (f29), 636.46 (f30), 635.59 (f31), 634.50 (f32) ... 626.48 (f42). The steps
  are smooth and about 1 px/frame.
- Diameter: the median circle fit over frames 18–42 (contact frames excluded) gives 164.07 px, so the scale is
  2/164.07 = 0.012190 m/px.

## SAM 3 check
Phrase "grey sphere", no box. (A box prompt at f30 gave a bloated, wrong mask, which I did not use.)
- f29 left ball: centroid x 637.6 (mine 637.56). Box 557.7–719.3 x 702.0–867.7, so 161.6 x 165.7 px.
- f30 left ball: centroid x 636.6 (mine 636.46). Box 556.8–718.2.
- So SAM gives a 1.0 px step from f29 to f30 (centroid and box centre). Mine is 1.11 px.
- SAM extents are 161–167 px against my 164.1 px diameter. That is within 2%, so I keep the circle fit.

## Speed
| route | px/frame | m/s |
|---|---|---|
| backward difference f29→f30, full fit | 1.109 | 0.406 |
| backward difference f29→f30, fixed-r fit | 1.106 | 0.405 |
| backward difference f29→f30, SAM centroid | 1.0 | 0.366 |
| quadratic fit f29–42, derivative at 29.5 | 0.996–1.040 | 0.364–0.380 |
| linear fit f29–36 | 0.91–0.94 | 0.333–0.342 |

The single-frame steps scatter by about ±0.15 px (0.87–1.10 px). I therefore take the smoothed value at the
f29–30 step, about 1.0 px/frame, which agrees with SAM.

Answer: 1.0 px/frame x 30 x 0.012190 = **0.366 m/s**.

Confidence: moderate. The motion is only about 1 px/frame, so the routes span 0.33–0.41 m/s (about ±10%).
