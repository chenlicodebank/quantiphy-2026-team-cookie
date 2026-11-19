# Q2019: length of the red car (red pickup), prior lane width = 3.66 m

Clip: near-nadir drone view of a highway, static camera. "Red car" = red_pickup, lane 4, between the dash rows at y≈989 and y≈1310.
Time base doesn't matter here (it's a size question).

## Scale (lane width)
Divider spacing, centre to centre of the dash rows (scene/static_markings.json; checked in measure.py on frame 10: 310–327 px):
308, 326, **321 (the red car's lane)**, 306, 330 px, mean 318. Dash rows tilt ≈0.4°, so cos correction is negligible.
Scale = 3.66 / 320.8 = 0.01141 m/px (car's own lane). With the 5-lane mean of 318: 0.01151 m/px.

## Car length (bumper to bumper, along x)
- Scene record: 532 px (1760→2292 at frame 15, blur included).
- My check (rear.py, luminance ratio vs median background, rows cy±50, frame 15): the front edge drops to road level
  at x≈2290–2296; the rear dark bumper band starts at x≈1748–1752, ahead of the shadow-to-bed rise at about 1785.
  Length ≈ 540 px. A zoomed crop (frames/car15.png) agrees: the body runs from ≈1760–1777 to ≈2280–2295.
- The front edge matches across frames 8–18 in carlen.py (the rear edge is spoiled by the shadow in that automatic method).
Adopted: 538 ± 8 px (blur included, as the annotators would have clicked it).

## Result
538 × 3.66 / 320.8 = 6.14 m. Range: 532/321 → 6.07 to 545/318 → 6.27. **Answer: 6.15 m.**
Sanity check: about the length of a full-size crew-cab pickup (5.9–6.2 m), so plausible. If the lane is read as the gap
between the inner dash edges (≈310 px), the answer would be ≈6.35 m. I used centre-to-centre.
Confidence: moderate-high (±3%).
