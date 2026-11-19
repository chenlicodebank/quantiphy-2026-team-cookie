# q_2539 — length of the table (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 762.8 px, principal point (640, 360).
Prior: tennis ball diameter 6.7 cm (r = 3.35 cm). depth_info at t=1.5 s (frame 36): tennis 1.183 m, ping-pong 1.353 m
(ping-pong radius taken as 2.0 cm).

## Method (scripts: table_edges.py, draw_lines.py, geom.py, check.py)
1. Tabletop edges fitted on frame 12 (static): wood colour mask boundary, plus the top/front-face gradient for the
   near edge. Far edge uses only columns free of hands/head. Overlays (frames/lines_L.png, lines_R.png,
   table_fit_12.png) show the lines on the edges. A gradient-based refit agrees to <1.5 px at the VP.
   Corners: FL (572,425), FR (844,427), NL (462,483), NR (958,495). The scene record's far corners (560/850, 428) were
   approximate; corrected here.
2. Table plane: normal from the two vanishing directions. Depth VP = (714, 350); lateral VP far off at x ≈ -3700.
   The plane offset comes from the 3D ball centres at frame 36, back-projected with the given depths and lowered by
   their radii. Tennis ball gives h = 0.1628 m; ping-pong gives 0.1613 m, independent and consistent within 1 %.
3. Back-projected corners onto the plane: the depth-direction sides are 73.4–73.7 cm (left = right) and the
   lateral sides are 57.5–58.1 cm. The table is longer front-to-back, so length = 73.7 cm and width = 58 cm.

## Checks
- Variant forcing the lateral axis perpendicular to the depth axis (measured angle 85.6 deg): length 74.1 cm,
  width 58.2 cm.
- Sensitivity: a ±2 px shift of the depth VP gives ±1.5 cm of length. That shift is the main uncertainty, because the
  camera is only about 16 cm above the tabletop.
- Second route, the yellow ball rolling over frames 30–41: its plane-predicted depth (centre 3.35 cm above the
  plane) matches the depth from its apparent size (eq_diam ratio, anchored at frame 36) to within about 1–2 %. Size
  suggests slightly more depth range, so the length is if anything ~1–2 % larger. The white-ball size is
  unreliable: its mask includes the reflection and blur.
- Sanity: 74 x 58 cm is close to a standard 75 x 60 cm table.

Answer: 74 cm (range about 73–76). Confidence: moderate-high.
