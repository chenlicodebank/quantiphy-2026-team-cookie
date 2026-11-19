# q83: distance walker–bike at t = 1.0 s (frame 24)

2D top-down render, 24 fps (file fps = question fps), so t = 1.0 s is frame 24. The scale comes from the prior (bike length 1.7 m).

- Bike length: I measured the cyan bike-only mask in code (measure.py) over frames 2–16. It is 376.4 ± 1.5 px; the record gives 378 px. Using 377 px gives 0.004509 m/px.
- Bike centre at frame 24: by then the bike is almost out of frame (only the rear tip, x ≤ 25, is visible).
  - Route A: a linear fit of the bbox centre over frames 2–16 (−47.46 px/frame, residuals ≤ 1.1 px), extrapolated to frame 24, gives x = −163.1.
  - Route B: the measured rear edge at frame 24 (x1 = 25) minus half the bike length gives −162.7.
  - The record's value is −166.7. I use x = −163 and y = 644.
- Walker pelvis at frame 24: the record's torso-bbox centre is 1246.5 and its filled-mask centroid is 1255. On a 3× crop, the hips (where the thighs leave the shirt) are about midway between x 1220 and 1290, i.e. about 1255. I use (1252, 441), about ±8 px.
- Pixel distance: Δx = 1415, Δy = 203, so 1429.5 px. Multiplied by 0.004509 m/px, that is **6.45 m**.
  - Sensitivity: a bike length of 376 to 378 px gives 6.43 to 6.46 m. ±8 px on the pelvis changes the result by ±0.04 m.

Confidence: high (about ±2%). The main assumption is that the bike's origin is its bbox centre.
