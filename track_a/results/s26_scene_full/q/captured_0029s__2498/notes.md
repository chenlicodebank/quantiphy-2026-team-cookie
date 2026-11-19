# Q2498: length of the table (cm)

The file and question both run at 24 fps. Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
Depth frames: t=1.00 -> frame 24 (0.901 m), t=1.24 -> frame 30 (1.144 m; the ball is at the back edge and touches the whiteboard), t=1.6 -> frame 38 (1.027 m).

## Method
- `edges.py`: I made table masks for frames 30 and 48 and took their union, so the ball doesn't hide the edge. I fitted lines to the back edge (mask top), the front top edge (the brightness step between the top surface and the slab face), and the left and right sides (mask extremes). Corners are the line intersections (`corners.json`): BL (443, 452), BR (918, 471), FL (212.5, 536), FR (1139, 587). Because these are line intersections, rounded corners don't shorten the result. The overlay is `frames/edges.png`.
- `plane.py`: I back-projected the ball centres from `scene/tracks/ball.csv` at frames 24, 30 and 38 using the given depths.
  - **Route A (main):** the plane normal comes from the vanishing points of the table rectangle. They are 88 deg apart, against 90 for a perfect rectangle. The ball centres sit on a plane parallel to the top, 3.35 cm above it. Their three offsets agree within 4 mm (-0.1205, -0.1204, -0.1242 m), so the camera is 15.5 cm above the table top. Intersecting the corner rays with that plane gives a front length of 70.6 cm and a back length of 70.6 cm (70.1 to 71.8 cm using each ball point alone). The width is 55.4 cm.
  - **Route B (check):** the normal comes from the three ball centres alone, which is poorly conditioned. It gives 73.9 cm front and 72.1 cm back; the sides come out at 55.6 and 51.3 cm, so the shape is not a rectangle. The two normals differ by 1.3 deg.
- **Consistency check:** the slab is 30 px thick on the left and 34 px on the right. At route A's depths (Z_FL = 0.62 m, Z_FR = 0.54 m), both edges come out about 2.4 cm thick. Route B's depths give 2.7 vs 2.4 cm, which favours route A.
- **Ball-size check:** the apparent ball diameter puts the depths about 3 to 5 % above depth_info (likely because the mask shrinks by 1 to 2 px). I used depth_info.

## Answer
The length (long horizontal side) is about **70.6 cm**, with a likely range of 70 to 74 cm. The width (front to back) is about 55 cm. Confidence: moderate. The camera views the table at a grazing angle, so the result scales directly with the camera height above the top, which is set by the depth_info.
