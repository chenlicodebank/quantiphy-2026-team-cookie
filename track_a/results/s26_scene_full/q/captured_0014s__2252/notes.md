# q_2252 — length of the slope (cm)

Slope = the white board the ball rolls down (far edge at top, near edge at bottom of the image).
File fps = question_fps = 24.

Method (measure.py): white colour mask of the board at frame 48 (no ball), contour + polygon corners:
far edge (500,313)-(592,303), near edge (509,422)-(609,408) (they match scene/ to within 2 px).
Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640,360).
Far-edge midpoint (546, ~307) back-projected at depth 1.8540 m; near-edge midpoint (559, ~415.5) at 1.7010 m.
- Using the polygon corner midpoints (308 / 415): 0.292 m
- Using the mask's outer boundary at the centre column (306 / 418): 0.300 m
- Answer: the mean, 29.6 cm (±1 cm, depending on which side of the edge pixels you take).

Second-route check: the board's width, measured at its near edge (depth 1.701) and at its far edge (depth 1.854),
gives the same value both times: 22.1 cm. That shows the two given depths agree with the geometry. A 22.1 x 29.6 board
has about the proportions of A4 (21 x 29.7), which is a plausible size for the board.
The ball-acceleration prior is not needed to get this length.
Confidence: good (about 3%).
