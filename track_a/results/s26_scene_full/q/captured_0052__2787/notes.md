# q 2787 — basketball diameter (cm)

Lab video, 24 fps (file and question_fps agree). The basketball is static at the lower right (orange), so the
same pixel size is seen at frames 0, 24 and 47. Scale: lab f = 0.5959 x 1280 = 763 px, with depth_info
distance_basketball_camera = 1.9365 m at t = 1.0 s (frame 24). The prior (the yoga ball's velocity) is not
needed for a size.

## Measurement (extent.py, edge.py, measure.py)
- Radial saturation-edge profiles (half-level crossing, every 2°) around the ball at frame 24, overlay in
  frames/extent_24.png: the rim fits within about 1 px.
- Horizontal diameter 91.1 px. Diameters along directions run from 88 px (tangential, ~150°) to ~100 px (radial,
  ~58°, toward the image corner). The ellipse fit without the bottom shadow sector gives 88.0 x 99.8 px, with the
  major axis at about 59°. This matches the expected off-axis stretch of a sphere (the centre is about 350 px from
  the principal point, theta ~24.6°, 1/cos theta ~1.10). The shadow inflates the major axis a little.
- The colour-mask method (measure.py) misses the darker rim (eq. diameter 89 px). The edge circle fit gives 93 px.
  The scene record gave 92 x 86 px, which is consistent horizontally.

## Size
- Method card, D x px / f: horizontal 91.1 px -> **23.1 cm**; minor axis 88 px -> 22.3 cm; circle 93 px ->
  23.6 cm; major axis -> 25.3 cm.
- Second route: exact sphere geometry. If the depth is the Euclidean distance to the centre, the minor axis gives
  20.3 cm. If the depth is a z-depth (the back-projection convention multiplies the (x, y, 1) ray by the depth),
  the minor axis gives 22.3 cm at the centre and ~23.4 cm if the depth is the front-surface z. Real basketballs
  are 22-24.3 cm (size 5-7).
- Answer: 23.1 cm (method card, horizontal extent), which sits in the middle of the plausible readings.
  Confidence moderate (±5-10 %). The main uncertainty is the convention behind the depth value, not the pixel
  measurement (±1-2 px).
