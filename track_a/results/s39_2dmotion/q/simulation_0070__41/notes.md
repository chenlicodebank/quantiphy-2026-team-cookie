# Q41: speed of the yellow car at 2.5 s (m/s)

- 2D top-down orthographic render, 24 fps (file fps = question_fps = 24). t = 2.5 s -> frame 60.
- Only one car in the scene (peach/"turing yellow" sedan); it has finished its right turn and is driving
  right along the horizontal road at frame 60 (axis ~1 deg).
- `measure.py`: median background, paint-colour mask inside the difference mask, convex hull (excludes shadow),
  centroid = origin, PCA length. Output in `my_track.json`.

## Scale (prior: car length 5.44 m)
- My mask length at frames 55-65: 218-220.8 px, 220.3 at f60; scene record 220 (218-221).
- SAM 3 "yellow car": f60 length 220.3 px (horiz 220), f59 218.4 px (slightly tight). Agrees within 1 pct.
- L = 220 px -> 0.024727 m/px.

## Speed
- Centroid step f59->f60: 6.88 px (mine), 6.92 px (SAM centroids 1291.5,633.2 -> 1298.4,632.7), 6.94 (scene csv).
- Per-frame steps jitter ±0.15 px from mask noise; motion is essentially constant (whole clip 6.83 ± 0.18 px/frame).
  Mean of steps 55-65: 6.79; chord f54->f66: 81.62/12 = 6.80 px/frame.
- Used 6.82 px/frame -> 6.82 x 24 x 0.024727 = 4.05 m/s (raw single step 6.88 -> 4.08; within 1 pct).

## Checks
- SAM vs my mask: length 220.3 vs 220.3 px at f60, centroid differs by ~1.5 px in x (SAM slightly wider mask on
  the front); difference < 3 pct, no conflict.
- Second route (long-baseline chord, f54-66) gives 4.03 m/s; the single step gives 4.08 m/s.

Answer: 4.05 m/s. Confidence: high (about ±2 pct).
