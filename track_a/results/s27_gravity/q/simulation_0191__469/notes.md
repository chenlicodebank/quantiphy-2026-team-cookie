# Q469 — height of the truck (simulation_0191)

Prior: the box's acceleration before 0.6 s = 9.8 m/s². No depth_info. File fps = question fps = 120.

## Scale (fit.py)
- Box centre track (scene/tracks/box.csv, template matched, ±0.3 px). It falls freely from frame 0 and hits the truck roof at frame 61.
- Quadratic fit of cy(t) over frames 0–60: a = 1975.9 px/s² (residual 0.06 px). Other windows (5–60, 10–58, 0–40, 20–60)
  give 1966–1985, about ±0.5 %. The per-frame drops grow linearly, from 0.04 to 8.2 px/frame.
- Scale = 9.8 / 1975.9 = 0.004960 m/px.

## Truck height (truck_ext.py, frame 180)
- Top = top bar of the railing on the cab: the intensity step is at y = 348.0 (the same in columns 1460–1655). Nothing on the truck is higher.
- Bottom = bottom of the tyres: the edge is at y = 1064.2 (both wheels). The stabilizer feet end at about the same level.
- Height = 716.2 px × 0.004960 = **3.55 m**.

## Checks
- Same scale, other parts: truck length 1690 px → 8.4 m; wheel diameter 165 px → 0.82 m (fits the 17.5" wheels of a
  light truck); box 2.0 × 0.95 m. These are realistic sizes for a catering truck.
- Perspective (prof.py, corner.py): the box's underside shows while it is high, so the camera is below the box then. The horizon
  is somewhere around y ≈ 520–650; the mask-based estimates do not agree well. At rest, the bottom edge of the box face shows at y ≈ 407,
  just above the truck side's top edge at y = 410. If the camera is below the roof, this is only possible when the box face is at about the
  same depth as the truck side (within ~2–3 %). So one 2D scale applies to both, and I made no perspective correction.
- Record: scene/ extents (348 → 1062, 714 px) agree with my measurement to 2 px.

Confidence: good. The main uncertainty is a small depth offset between the box and the truck side (a few %).
