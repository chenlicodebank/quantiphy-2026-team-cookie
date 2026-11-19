# q_1863 – acceleration of the astronaut at t = 2 s

- 2D segmentation video, 24 fps (the file and the question agree), so t = 2 s means frame 48. The only object is the astronaut. Its pose is rigid; it rises almost straight up the image, starting at about f3 and stopping at f78. It speeds up, cruises at about 5.2 px/frame around f30–f45, then slows down. Frame 48 is early in the slow-down.
- Scale: I re-segmented the figure (`measure.py`) at min-RGB thresholds of 200, 225 and 245. The body length along the main axis is 91.3, 91.4 and 92.8 px, so I used ≈91.8 px = 2.2 m (rest height). That gives 0.0240 m/px.
- Motion: I projected the mask centroid (pelvis proxy) onto the straight path direction (perpendicular wander < 1.5 px) and fitted the arc length s(f) (`fit2.py`, `fit.py`).
  - Global polynomial fits of degree 4–8 over f3–f78, for all three thresholds, give a backward-difference acceleration at f48 of s(48) − 2s(47) + s(46) = −0.0555 to −0.059 px/frame².
  - Second route: local cubic/quadratic fits in windows of ±6 to ±12 frames around f47/f48 give −0.053 to −0.061 px/frame².
  - The smoothed speed slope also agrees: from 5.21 at f45 to 4.83 at f51 is about −0.063, and from f47 to f53 about −0.053.
- Result: a ≈ −0.056 px/frame² × 24² = −32.3 px/s², × 0.0240 m/px = −0.78 m/s². The motion is decelerating; the magnitude is 0.78 m/s².
- Confidence: moderate-to-good, roughly ±8%. Most of the spread comes from the fit window and the edge pixels in the mask. The figure's 25° rotation shifts the centroid against the pelvis by a negligible amount.
