# q_2492 — length ("long") of the table, cm

File fps 24 = question_fps 24, so frame = round(t*24). The depth_info times are frame 24 (t=1.00, 0.901 m; the "s" is a typo for m),
frame 30 (t=1.24, 1.144 m, board hit) and frame 38 (t=1.6, 1.027 m).

## Method (measure.py, fscan.py, table_edges.py, sides.py, ballsize.py)
- Ball centres from scene/tracks/ball.csv (frames 24, 30, 38). I checked them against the frames.
  Back-projected with f = 0.5959*1280 = 763 px, (cx, cy) = (640, 360) and the given Euclidean distances.
- These 3 ball centres give a plane that is almost horizontal (normal (0.00, -1.00, -0.02), so no camera roll).
  I moved it down by the ball radius (3.35 cm) to get the table top: camera is about 0.17 m above the table.
- Table-top corners on frame 48, measured in code (the drop in brightness from the top surface to the dark front edge, and
  the R-B colour edge for the side edges): FL (209,537), FR (1140,588). The side edges go behind the white board at about x=424 and x=905
  (y≈456-461), so the real back edge is hidden. The front edge is the long, fully visible side.
- Intersecting the corner rays with the table plane gives **front edge = 0.750 m** (the visible back segment between the side edges, where they meet the board, is 0.725 m;
  the visible side depth is ≥0.50-0.59 m, so the front edge is the long side).

## Second route / conflict
- The ball's apparent size does not match the given depths. The diameter is 40 px at frame 30, 44 px at 38 and 48 px at 24
  (diam_px; my own FWHM measurements are even smaller, 33-44 px). The given distance divided by the size-based distance (0.067*763/diam)
  is 0.85, 0.90 and 0.88 (mean 0.875). So either the given depths are about 12 % short or the effective focal length is about 12 % smaller.
- If the ball size (the prior) sets the scale instead of depth_info, the front edge is 0.750/0.875 = **0.857 m**.
- Front-edge length goes as 1/f (fscan.py: f 650 → 0.844, 700 → 0.799, 763 → 0.750, 820 → 0.712).
- A rectangle check from vanishing points was not reliable (it gives f≈490, which neither the ball nor the depth supports).
  This is probably lens distortion or a table top that is not quite rectangular, so I did not use it.

## Answer
The two scale routes give 75.0 cm (depth_info + f=763) and 85.7 cm (prior ball size + f=763).
I answer with their geometric mean, about **80 cm**, which is within about 7 % of both.
Confidence: moderate. The scale conflict dominates the uncertainty; the pixel geometry itself is good to about ±2 %.
