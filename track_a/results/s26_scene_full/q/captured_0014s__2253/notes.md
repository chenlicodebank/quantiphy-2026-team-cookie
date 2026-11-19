# Q2253 — width of the slope (cm)

The slope is the white board on the table. The ball rolls down it toward the camera. File fps = question fps = 24.

Method (measure.py): I segmented the white board at frame 48, when the ball is gone (min RGB > 200, then the largest
component), and fitted a 4-corner polygon. The overlay is in frames/ov.png and fits the board edges to about 1 px.
Corners: (592,303), (501,312), (609,407), (509,422).
I back-projected with f = 0.5959 x 1280 = 763 px and principal point (640,360), using the depth_info values:
slope_far = 1.854 m for the far edge and slope_near = 1.701 m for the near edge.

- Far (top) edge: 91.4 px, which gives 21.8 cm.
- Near (bottom) edge: 101.1 px, which gives 22.2 cm.
- Length down the slope (between the edge midpoints): about 29.2 cm. It is longer than the width, so width is the
  shorter, side-to-side extent.

Second route: the two edges are independent, each with its own depth, and they agree to within 0.4 cm. The mask may
be about 1 px tight on each side; correcting for that gives about 22.4 cm.
Answer: 22.0 cm. Confidence: good (±3%).
