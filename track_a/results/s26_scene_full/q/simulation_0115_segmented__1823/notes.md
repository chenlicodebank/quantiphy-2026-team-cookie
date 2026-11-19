# q_1823 – width of the wooden dock (m)

Prior: boat acceleration = 3 m/s^2. 2D top-down render, 24 fps (file fps = question_fps, no re-timing).
Bash/Python execution was denied in this session, so no new scripts could be run; all numbers are
hand computations from scene/tracks/boat.csv and scene/tracks/dock_check.csv (made by scene/scripts/measure.py:
non-white threshold, connected components, PCA extents).

## Scale from the prior (boat pixel acceleration)
Boat moves straight in -x (y constant), so acceleration = d2x/dt2.
- Least-squares slope of the 36 per-frame centroid steps vs frame (symmetric-pair sum 933.0 / 3885):
  0.2402 px/frame^2 = 138.3 px/s^2.
- Same with the leading-edge bbox x0 steps: 0.2405 px/frame^2 = 138.5 px/s^2.
- Wide second differences of the centroid: (0,18,36) 139.5, (0,17,34) 140.5, (1,18,35) 140.3, (2,19,36) 140.4 px/s^2;
  right edge x1 (0,18,36) 138.7; left edge x0 (0,18,36) 136.9.
=> a ≈ 139 px/s^2 (spread 137–140.5), scale = 3 / 139 = 0.02158 m/px.

## Dock width
Dock is static; short extent across its axis (PCA) = 96.6–97.1 px over all frames, 97 px typical
(bbox height 104 px is inflated by the -1° tilt over its 574 px length). Width = front-to-back short horizontal extent.
Width = 97 x 0.02158 = 2.09 m (range 2.07–2.12 with the acceleration spread).
(Dock length for reference: 574 px -> 12.4 m.)

## Check
Independent acceleration routes (centroid fit, edge fit, long-baseline 2nd differences) agree within ±1.5 %.
Mask area/length = 53780/574 = 93.7 px mean width, i.e. the 97 px extent includes posts along the edges, which belong
to the object's bounding box. Not visually re-verified this session (no image tools could run).
Confidence: moderate-good (~±5 %).
