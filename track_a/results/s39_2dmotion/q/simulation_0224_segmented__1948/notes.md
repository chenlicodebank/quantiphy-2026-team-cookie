# q_1948 — speed of the red general chess piece at t = 1.5 s (m/s)

Prior: diameter of one Chinese chess piece = 0.097 m. 2D video, no depth_info. question_fps = file fps = 24,
so t = 1.5 s -> frame 36.

## Object
The scene/ record calls it a "block": it is the chess piece (cream disc, seen from a low angle as a stadium shape)
sliding down a tilted chessboard/trough (grid lines visible on the board). It is the only moving object, so the
asked object and the prior's object are the same piece. Record track (tracks/block.csv) covers it, frames 0-39.

## Scale (pixel diameter) — scripts profile.py, edge.py, measure.py, air43.py
- Long extent of the silhouette along its axis (= disc diameter; the disc's projected major axis lies within
  ~1.5 deg of the motion direction, so the motion along the board is foreshortened by < 0.5 pct).
- edge.py: half-contrast edges of the difference-to-empty-ramp (frame 44) profile along the axis, max over parallel
  lines: 76.0-77.0 px (frames 15, 20, 24, 30, 33, 36). profile.py chords at diff thresholds 90/60/40:
  medians 77.3 / 78.0 / 80.0 px; constant along the whole ramp (no depth change). Lower-left end has a shaded
  rounded edge (gradual contrast), so I take D = 77.5 px (+-1.5).
- SAM 3 ("beige object", box prompt) frames 24/34/36: length 86.8/86.0/86.5 px, width 35 px — 11 pct larger than
  mine. On zoomed overlays (frames/cmp_24.png, cmp_36.png; red = SAM, green = light top-face mask, blue = diff mask)
  the SAM outline runs 1-3 px outside the piece onto the dark rim/trough at the ends and the upper edge, so SAM is
  too large; my half-contrast edges are right. The record's 81.3 px is a thresholded/closed mask extent (+1 px
  convention), also inflated by ~3-4 px.
- Check: frame 43 (piece in the air, clean silhouette on white): max Feret 82-83 px; the tumbling disc's silhouette
  can reach sqrt(D^2 + t^2) (~1.08 D for a typical piece), consistent with D ~ 77-78 px.
- Scale = 0.097 / 77.5 = 1.252e-3 m/px.

## Speed at frame 36 — speed.py
Own template track (masked NCC, sub-pixel) agrees with the record within ~0.4 px. The clip has repeated frames
(6, 13, 25, 28, 35, 38) and double steps (5, 10, 23, 27, 34, 37); frame 35 repeats 34 (= render index 35), so
the backward step 35->36 is one true frame step:
- raw step video 35 -> 36: 34.54 px/frame (SAM centroids 34 -> 36: 34.7 px)
- quadratic fit of path position vs true render index (rms 0.4-0.6 px, a ~ 0.95-1.0 px/frame^2):
  s(36) - s(35) = 35.07-35.34 px/frame
- neighbours: half of 33->34 double step 34.1, half of 36->37 double step 36.3 (consistent with steady acceleration)
Adopted 34.9 px/frame -> 837.6 px/s.

## Answer
v = 837.6 px/s x 1.252e-3 m/px = 1.048 m/s  -> 1.05 m/s.
(With the record's 81.3 px it would be 1.00; with SAM's 86.5 px 0.94 — both rejected above.)
Confidence: moderate-high; main uncertainty is the pixel diameter (+-2 pct) and step definition (+-1 pct).
