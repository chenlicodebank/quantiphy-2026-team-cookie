# q_2235 — height of the cup (cm)

The video is 24 fps and question_fps is 24, so the two rates match. The camera is a lab Orbbec with f = 0.5959 x 1280 = 762.8 px and the principal point at (640, 360).
The prior (ball acceleration) is not needed. The scale comes from depth_info: cup distance at t=0 = 1.727 m.

## Pixel measurements (frame 0, plus an average of frames 0/10/20/30/40/48; the cup is static)
Scripts: cup_profile.py, cup_bottom.py. Images: frames/cupgrid_0.png, frames/cup_avg.png
- Top rim ellipse (white tumbler with lid): back edge y=336, front edge ~352, x from 450.5 to 488 (37.5 px).
  Minor/major is about 0.43, so the line of sight is about 26 deg above the rim plane.
- The cookie hides the lower right of the cup. The left edge reaches y~398 at x~466. The bottom front is at y~402-403.
  The cup tapers: the left edge moves 14 px inward over its height, against 6.6 px expected from vertical convergence alone.
  Bottom ellipse centre is about (476.5, 397). Top ellipse centre is (469.3, 344).
- Image bbox height is about 64-66 px (336 to ~402). The scene record says 64.

## Geometry
- Table-plane normal comes from the vanishing points of the table-top edges (geom.py). The table edges meet at 87 deg after
  back-projection, which is consistent with a square top. The camera is tilted about 28.5 deg down. The rays to the cup
  are 26.5-30 deg from horizontal, which matches the rim ellipse ratio.
- Route 1 (cup_height.py, cup_route2.py): the cup axis runs along the table normal between the top and bottom ellipse centres,
  with the axis midpoint at distance 1.727 m. This gives **H = 13.46 cm**. Moving the bottom/top centre by ±2 px gives 12.6-13.9 cm.
- Route 2 (independent scale): the bottom centre lies on the table plane, anchored by the depth of the pen, book or slope_near
  (assumed centre heights 0.5 / 1.0 / 0.6 cm). This gives H = 13.92 / 13.54 / 13.74 cm.
- Card-only reading (bbox pixel height x depth / f, no foreshortening correction): 64-66 px gives 14.5-14.9 cm. This
  overstates the true height, because the cup is seen from about 28 deg above, so the top ellipse adds to the image
  height and the vertical axis is foreshortened.

## Answer
13.9 cm. The geometric routes give 13.5-13.9 cm. I picked the top of that range, which is also within about 7% of the
card-only reading.
Confidence: moderate. The main uncertainty is the bottom of the cup, which the cookie hides (±2 px, about ±0.5 cm).
