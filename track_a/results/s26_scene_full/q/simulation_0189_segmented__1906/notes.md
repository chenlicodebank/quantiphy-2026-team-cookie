# q1906 — height of the truck at t = 0 (m)

Prior: speed of the box = 0.094 m/s. 2D side view, static camera, fps 120 (= question_fps).

## Box speed (scale)
- Template-matching the cardboard box face (boxtrack.py): the box rises at a CONSTANT 19.19 px/s
  (linear fit residual 0.05 px; cubic fit speed 19.19 at t=0,1,2,3.33 s; net 19.18 px/s).
  The box top edge (measure.py) gives 19.0-19.1 px/s. So the box moves at constant speed, which fits a single prior value
  without a time. (The cargo body underneath accelerates, from ~6-10 to ~30 px/s. It is a separate motion, so the
  scene record's guess that the box rides rigidly on the roof is wrong.)
- Scale = 0.094 / 19.19 = 0.004898 m/px.

## Truck height at frame 0
- Foreground mask of frame 0, excluding the box columns (measure.py): the top is row 308 (the top of the front
  platform cage/pillar, x ~1456-1500). The bottom is row 1027 (stabiliser leg foot); the tyre bottoms are at 1024.
  The extent is 720 px (rows 308..1027 inclusive). Counting only to the tyres gives 717 px.
- Height = 720 x 0.004898 = 3.53 m (tyres only: 3.51 m).

## Checks
- Sanity check at this scale: wheel diameter ~168 px = 0.82 m, wheelbase 879 px = 4.3 m, length 1716 px = 8.4 m.
  These fit a medium truck.
- Box speed by two routes (texture match 19.19, edge 19.0-19.1): about 1% apart.
- Possible error: perspective depth offset between the box and the truck's side silhouette (not measurable here; assumed planar).

Answer: 3.53 m. Confidence: moderate-high.
