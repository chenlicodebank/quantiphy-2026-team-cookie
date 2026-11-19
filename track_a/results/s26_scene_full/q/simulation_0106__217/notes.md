# q_217: distance between the two viruses at t = 2.0 s (frame 48)

Prior: right virus speed = 1.5667 m/s. No depth_info. fps = question_fps = 24, so t=2.0 s is frame 48.

## Observations (from scene/tracks, body-circle centres and radii)
- The scene is not really 2D. The left virus moves up and gets bigger (r 123.8 -> 133 px). The right virus moves down
  and gets smaller (139.1 -> 131 px). The two image paths meet at a vanishing point far below the image
  (y ~ 7300-8400 px past the centre), so both move along parallel 3D lines (world-vertical seen by a camera tilted down)
  in opposite directions.
- Linear fits of (u-cx)/r, (v-cy)/r and 1/r against frame are almost exactly linear (quadratic terms are negligible),
  so both move at a constant 3D velocity. Motion starts at frame 1.
- The right virus is cut by the image edge after about frame 45 (flagged unreliable), so frame 48 is extrapolated
  from the linear fits on untruncated frames (left 1-36, right 1-27).

## Model (dist.py)
P_i(t) = ((u-cx)/r, (v-cy)/r, f/r) x R_i, in camera coordinates, where R_i is the virus's physical body radius.
The scale R_R comes from the prior: |dP_R/dt| = 1.5667 m/s. The focal length f is unknown and cannot be pinned down
from the motion (projective ambiguity), so I scanned it. I also tested two hypotheses for the left virus's radius:
(A) the same as the right one; (B) the value that gives both viruses the same speed, which also puts them at the same
depth at t=0 (k = 0.87-0.89).

| f (px) | A: d(48) m | B: d(48) m |
|---|---|---|
| 1000 | 7.52 | 7.18 |
| 2000 | 7.42 | 7.18 |
| 2667 (Blender default, 50 mm lens) | 7.31 | 7.24 |
| 3500 | 7.15 | 7.44 |

For f between 1000 and 3500 the answer stays within 7.15-7.52 m. **Answer: 7.3 m.**

## Second route
Flat 2D approximation: the separation at frame 48 is about 1260 px (left at (704,-8), right extrapolated to (1223,1140)).
The right virus's image speed gives 0.00604 m/px, so the distance is about 7.6 m. This is about 4% above the 3D value,
because the flat version ignores the depth component of the speed and the depth difference. The two routes agree to within 5%.

Confidence: moderate (about ±5%). The main unknowns are the focal length and the left virus's physical size.
