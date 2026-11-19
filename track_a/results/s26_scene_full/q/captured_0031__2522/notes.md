# Q2522: length of the table (cm)

Answer: **79 cm**. This is the table's longer horizontal extent, which runs front to back (away from the camera). The side facing the camera measures about 59 cm.

## Method (table3d.py)
- Frame 48, where the table is unobstructed. The top surface was segmented by HSV colour. Lines were fitted to its four edges in code: the side edges from the extreme pixels in each row, the back edge from the topmost pixels (avoiding the hands and head), and the front edge from the strongest brightness drop between the top surface and the front face. Fit RMS was 0.4 to 1.0 px.
  Corners: BL (577.4, 423.1), BR (842.1, 427.8), FL (463.8, 482.6), FR (956.6, 494.8). The overlay is in frames/corners.png.
- Camera model from the lab card: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- The two vanishing points (side edges and front/back edges) back-project to directions 89.6 degrees apart. That fits a rectangle under this focal length, so it checks f. The plane normal is the cross product of the two directions. The camera is about at table height with roughly 0.6 degrees of downward tilt.
- Scale comes from the tennis ball (D = 6.7 cm, the prior). Its centre lies 3.35 cm above the plane along the normal. The plane offset is n·(C − r n), and each corner ray is intersected with the plane.

## Depth_info inconsistency
- depth_info says tennis ball 1.19 m and white ball 0.994 m at t = 1.6 s (frame 38).
- In frame 38 the tennis ball is 50.8 px across. At 0.994 m that implies 763 × 0.067 / 0.994 = 51.4 px, which matches. At 1.19 m it would imply a 7.9 cm ball, which contradicts the exact prior.
- The white ball is 24.5 px across and sits higher in the image, so it is the farther ball. At 1.19 m it would be 3.8 cm (ping-pong size), which is plausible.
- So the two labels appear swapped. I used tennis ball = 0.994 m and white ball = 1.19 m.

## Results (front / side lengths, cm)
- A: tennis ball at frame 38, depth 0.994: 58.7 / 78.9
- B: tennis-ball range from apparent size over frames 20-42: 58.9 / 79.2. The plane offset is very consistent across frames (sd 1.9 mm while depth goes from 1.4 to 0.9 m), which also confirms the plane tilt.
- C: white ball at depth 1.19, with its radius taken from its pixel size: 58.2 / 78.3
- Labels as written (tennis ball at 1.19, which is inconsistent): 67.8 / 91.2. Rejected.

## Second-route check (check_ball.py)
- At rest (frames 10-15) the tennis ball's contact point is 79-82 cm from the front edge. Its diameter there is about 1 px too small because the hands cover part of it; correcting for that gives about 77 cm, a few cm inside the far edge where it was held.
- At frame 42, as it rolls off, the contact point is at about −1 cm, i.e. right at the front edge.
- Both agree with a table about 79 cm deep.

## Other readings
- Length (longer horizontal side, front to back) = 79 cm.
- Width (side facing the camera) = 59 cm.

Confidence: moderate to good, about ±4%. The grazing view makes the depth-direction length sensitive to about 1 px in the back-edge row, which is roughly 2 cm.
