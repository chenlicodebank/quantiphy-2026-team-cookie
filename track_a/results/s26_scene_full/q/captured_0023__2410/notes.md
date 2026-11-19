# q_2410: width of the book (cm)

Answer: **8.4 cm**. "Width" here means the book's shorter horizontal side, i.e. the short side of the cover. The long side
(length) comes out at about 19.3 cm.

The file runs at 24 fps and question_fps is also 24, so frame = round(t*24).
Camera: lab card f = 0.5959*1280 = 763 px, principal point (640, 360).

## Why it needs geometry
The book's long side runs left-right in the image. Its short side points along the line of sight, which squashes it
strongly in the image: up the ramp it is seen at about 32 deg, and on the table at about 11 deg. So width = depth*px/f
cannot be used directly. Instead I back-project the cover's edges onto the 3D plane the cover lies in.

## Route A (main): the cover face on the ramp (`geom.py`, `check_ramp.py`)
- Ramp plane: it passes through the ramp top-edge centre (588.5, 356) at distance_slope_far = 1.201 m and the ramp foot
  centre (585, 482) at distance_slope_near = 0.9555 m, and it contains the horizontal edge direction.
  The ramp makes a 31.4 deg angle with the camera axis, i.e. about 30 deg inclination. The cover lies in this plane,
  raised by the book's thickness (about 1.3 cm).
- Checks on the plane:
  - The ratio of the ramp's top and bottom edge widths in pixels (183/145 = 1.262) matches the ratio of the given
    depths (1.257).
  - The book centroid at t = 1.2 s (frame 29, (585.4, 435.4)) lands on the plane at 1.019 m. The given value is 1.02 m.
  - The book at the ramp top lands at 1.158 m. Scaling its apparent length (173 px at rest at 0.851 m vs 127 px at the
    top) gives 1.159 m.
- Cover face in code-read column profiles (x = 560/590/620): the light-blue cover runs from y = 350.5 to 379.5 at
  frame 10 (book held still) and from 353.5 to 382.5 at frame 22 (just released). Both are 29 px. A thin page edge
  follows below it.
- Width: 8.33 cm at frame 10 and 8.23 cm at frame 22 with the thickness offset; 8.5 / 8.4 cm without it.
- Sensitivity: an error of ±1.5 deg in the ramp angle moves the result by ±0.45 cm. The two depth checks above hold
  the angle to about that accuracy.

## Route B (check): the book at rest on the table, frame 46
- The top face runs from y ≈ 481.5 to 496.5 at x = 560, i.e. 15 px (14-15 px over x = 520-630). The front face (page
  block) is about 12 px, which gives a thickness of about 1.3 cm.
- I put the table plane through the ramp foot line and the bottom of the book, with the book centre at 0.851 m
  (t = 1.6 s). The result depends heavily on which pixel is taken as the book centre:
  - y = 493: pitch 0.8 deg, width 8.9-9.1 cm
  - y = 490: 10.4 cm
  - y = 496: 7.9 cm
- If I use the table vanishing point (horizon at y ≈ 338, camera pitch 1.65 deg) instead, the width is about 8.5 cm.
- Length check along the top face: 18.9-19.7 cm, which agrees with 173 px * 0.851 / 763 = 19.3 cm.
- Route B agrees with route A, but its error bars are much wider (±1.5 cm). Route A is better constrained.

## Confidence
Main value 8.3 cm (route A), checked by route B at about 8.5-9 cm. Answer: 8.4 cm. I expect it to be within about
±0.6 cm.
