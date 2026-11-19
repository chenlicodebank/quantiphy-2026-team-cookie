# q 858 – speed of the box at t = 1.75 s (frame 42, 24 fps)

Prior: box width (side parallel to the slope) = 0.611 m. No depth_info. fps = question_fps = 24, so no re-timing issue.

## Findings
- scene/ track (tracks/box.csv) covers the right object (the only moving thing, a cardboard box sliding down a
  ramp). Centroid steps were checked; frame 27 shows frame 28's position (a duplicated frame), so it is excluded from fits.
- **The ramp is not parallel to the image plane; it recedes from the camera.** Evidence:
  - The ramp band in frame 0 narrows smoothly from ~49.5 px (top-left) to 46.5 px (bottom-right) (`band.py`).
  - The box's front-face along-slope edge length (luminance edges in a slope-aligned crop, `profile2.py`):
    93 px (frames 15–21) → 91 (22–31) → 80–82 (37–43). The across-slope front-face height also drops, 57 → ~54 px
    (`profile3.py`). The downhill end face is visible at the top of the ramp and the uphill end face at the bottom.
  - Pixel acceleration falls from ~1.55 px/frame² to ~1.0 px/frame² even though a sliding box should
    accelerate uniformly.
  So one global m/px scale (the "2D" assumption) would underestimate the late speed by ~12%.
- The front-face and top-face (far edge) along-slope lengths agree (~91 px at frames 27–30), so the box's own depth adds
  no measurable perspective difference; front-face length can stand in for the centre plane.

## Method (fit.py)
Joint least-squares fit:
u_i (centroid projected on the path, px) = u0 + A·s/(1+C·s), with the 1D projective image of a straight line;
s = τ + qτ² (constant world acceleration, τ = frame − 15); box length L_i = u(s+W/2) − u(s−W/2);
metric W ↔ 0.611 m. Frames 15–44 without 27; 22 front-face length measurements.
Result: rms 0.66 px on u, 1.6 px on L. World acceleration ≈ 6.4 m/s² (plausible for a slope with friction).
Speed(42) = |s42 − s41|·24·(0.611/W) = **10.73 m/s** (10.67–10.76 for L weights 0.3–3).

## Second route (local scale)
Centroid step 41→42 = 59.06 px; front-face length at frames 40–42 ≈ 80–81 px → 0.611/80.5 m/px →
59.06·24·0.611/80.5 = 10.76 m/s. Agrees with the fit.
Check of the alternative: a single global scale (91–93 px early) would give 9.3–9.5 m/s. But then world speed would not
rise linearly (slope 0.0178 → 0.0133 per frame in step/L units), while the local-scale speeds rise linearly
(0.0178 vs 0.0181), so I rejected the global scale.

## Confidence
Moderate to good. Main uncertainty: ±1 px in the late front-face edges (blur), which is about ±1.5% in the answer,
plus small centroid bias from end faces coming into view. Answer 10.73 m/s.
