# q3114 — length of the brown table (m)

Prior: average speed of the scooter rider = 3.8 m/s. Internet video, 30 fps (file = question fps), planar single-scale convention.

## Scale from the prior (measure.py)
- Rider torso-centroid track (scene/tracks/rider_scooter.csv, unflagged rows, frames 143–259; the rider moves only left to right).
- Raw image x: linear fit 31.27 px/frame, net 30.92 px/frame. Background-relative x: fit 31.71, net 31.37 px/frame.
  The camera drifts very slowly, about 0.2 px/frame.
- Mean pixel speed ≈ 31.2 px/frame = 936 px/s → scale = 3.8 / 936 = 0.00406 m/px.
- Sanity check: the scooter (264 px) comes out at 1.07 m and the rider's height (420 px) at 1.71 m. Both are plausible.

## Table
- "The brown table" = the large wooden-top picnic table at front centre, which is the most prominent one.
  The other front table on the right is also brown (580 px → 2.36 m). The grey one is metal.
- Frame 0, brown-colour run along the table top at rows y = 1262–1274: x = 1707 → 2407, **700 px** (±3 px).
  This agrees with scene.json (697 px) and with the gridded zoom frames/table_c.png.
- Length = 700 × 0.00406 = **2.84 m**.

## Second route / confidence
- Range of the speed estimate: 30.9–31.7 px/frame, which gives 2.80–2.87 m.
- The table is in the front row, closer to the camera than the rider's path, so its real length is probably shorter (about 2.4 m).
  The benchmark's convention is one planar scale with no perspective correction, so the answer is 2.84 m.
- Main uncertainty: which table the question means. Moderate confidence.
