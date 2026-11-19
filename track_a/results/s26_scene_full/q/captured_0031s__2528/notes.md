# q_2528 — length of the table (cm)

Answer: **75 cm**, the front-to-back extent of the table top. This is the longer horizontal side; the left-right side is about 60 cm.

## Inputs
- Lab video, 24 fps (the file rate equals question_fps), 1280x720, f = 0.5959*1280 = 763 px, principal point (640,360).
- Prior: tennis ball (the yellow ball) diameter 6.7 cm.
- depth_info at t=1.6 s (frame 38): "tennis ball 1.19 m, white ball 0.994 m".
  **The labels look swapped.** At frame 38 the yellow ball measures about 50–51.5 px across. With the
  6.7 cm prior that puts it at 0.99–1.02 m, while 1.19 m would mean an 8.6 cm ball. The yellow ball also sits
  lower in the image and appears bigger, so it is the nearer ball. The white ball (about 27–29 px) at 1.19 m comes
  out as a 4.0 cm ball, i.e. a ping-pong ball. I therefore used yellow = 0.994 m and white = 1.19 m.
- Note on the scene record: its yellow diameters (`diam_px`) are about 3 px too large, because the SAM2 white
  outline is included. My half-max G−B widths are in `yellow_widths.json`; a visual check of the profile at frame 39
  gives about 51.5 px, against 55 px in the record.

## Method (`rect2.py`)
1. I took sub-pixel table-top edge points from the mean of frames 46–48 (a half-level crossing for the far edge and the
   two sides, and the gradient peak for the near top-front edge). The rounded corners and the white ball are excluded.
2. I fitted a 3D rectangle lying on a plane n·X = h to all four edge sets, with f = 763 fixed and h = 1. This gives the
   plane normal, W/h = 3.581 (left-right) and L/h = 4.481 (front-back). The fit residuals are 0.14–0.17 px on the sides
   and 0.48 px on the far edge.
3. Scale (the camera height h above the table top):
   - Route A (depth_info, labels swapped): the yellow ball centre is 0.994 m along its ray at frame 38, and the centre
     sits 3.35 cm above the plane. This gives h = 0.1651 m, so **L = 74.0 cm** and W = 59.1 cm.
   - Route B (the 6.7 cm prior and the apparent size): I used the yellow half-max width + 1 px over frames 0–32 (rest and
     rolling, 1.75 m down to 1.28 m). This gives h = 0.1686 ± 0.0023 m, so **L = 75.5 cm** and W = 60.4 cm. The h implied
     by each frame stays constant along the roll, which supports the plane tilt.
4. Checks (`final2.py`):
   - Both balls at rest (frame 5) come out 0.2–1.7 cm inside the far edge. They do visibly sit at the back edge.
   - At frame 41 the yellow ball is 2.4–3 cm from the near edge, and it drops off at frame 42.
   - The white ball at 1.19 m implies a radius of 1.98 cm with Route B's h, i.e. a 40 mm ping-pong ball.
   - Sensitivity: moving the far edge by 1 px changes L by about 3%.

## Result
Front-back 74.0–75.5 cm, left-right 59–60 cm. Length is the longer horizontal extent, so the answer is **75 cm**
(about 60 x 75 cm table top). The other reading (left-right side) would be about 60 cm.
Confidence: moderate-high, about ±4%.
