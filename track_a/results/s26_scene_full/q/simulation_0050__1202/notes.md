# Q1202 — height of the walking person (m)

File fps 33 = question_fps 33; t=1 s -> frame 33, t=2 s -> frame 66.

## Focal length (solve.py)
- Pedestrian pelvis pixels (scene track torso_x, pelvis_y_est; checked on zooms of frames 33/66):
  f33 (1370, 521.6), f66 (1194, 523.9). Principal point at image centre (960, 383).
- Back-project with the given human depths 15.8652 / 16.6708 m and require the 1-s displacement = prior speed
  1.236 m/s (constant walk) -> f = 3015 px (hfov 35.3 deg). Smoothed (±2 frame mean) positions: f = 3005.
  Insensitive to a 5-10 px pelvis-x offset (±2 px in f).
- Check (check_bike.py): cyclist apparent-height ratio frames 33/66 vs its given depths gives f ~2700 (weak,
  ±px errors dominate), same order; pedestrian pixel-height ratio 268/256 = 1.047 matches depth ratio 1.051.

## Height (heights.py)
h = Z * height_px / f, Z = depth along optical axis (depth x cos of off-axis angle), f = 3010.
- Frame 33: 268 px -> 1.40 m; frame 66: 256 px -> 1.41 m; local gait maxima near those frames 1.40-1.42 m
  (depth linearly interpolated). Median over all clean frames 1.39, p90 1.41.
- Walking peak height ≈ standing height; answer 1.41 m.

Confidence: moderate (~5%); main uncertainty is f from the speed prior (if the prior's speed includes
pelvis sway, f would be slightly larger and the height slightly smaller).
