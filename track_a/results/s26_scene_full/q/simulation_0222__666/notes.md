# q_666 — width of the wooden bench (m)

Prior: robot vacuum diameter = 0.438 m. No depth_info. The video is a top-down 2D render; fps = question_fps = 24.

## Measurements (measure_bench.py, frame 77)
- Robot diameter: robust circle fit from scene/tracks (I checked the column): median 117.75 px over all frames,
  117.62 px at rest (frames 69–79). Bbox 119 px.
- Wooden slat bench, segmented by its orange colour (r − b > 45): bbox x 292–583, y 172–293. The edges are clean
  (full coverage between 294–581 and 174–289, with 1–2 px partial rows/columns at the edges).
  - Short (y) extent, measured per column at x = 300…578: 117, 118, 116, 119, 117, 118 px (the 110 px column at
    x = 350 is a slat gap). The edge-to-edge bbox is 120–122 px including the anti-aliased rows. Taken as 119 ± 1.5 px.
  - Long (x) extent ≈ 290 px (about 1.08 m; this is the length, not the width that was asked).
- Width = the shorter horizontal extent = 119 px.

## Scale
One metres-per-pixel value from the prior: 0.438 / 117.75 = 3.720e-3 m/px.
Width = 119 × 3.720e-3 = 0.443 m.

## Checks / caveats
- Second route: using the robot's bbox (119 px) instead of the circle fit gives 0.438 m. Using the bench's
  edge-inclusive 121 px gives 0.450 m. The spread is about ±1.5 %.
- Perspective: the bench top probably sits higher than the robot's top, so it would look slightly enlarged. But I
  can see no side faces at the bench's right or bottom edges (≤ 2–3 px), even though the bench is 300–380 px from the
  image centre. That means the height effect is small, so I made no correction. If there is an effect, the true
  width would be a few percent smaller.
- Confidence: moderate-high, about ±5 %.
