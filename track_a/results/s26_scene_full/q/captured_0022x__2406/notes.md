# q_2406: length of the table (cm)

The file and the question both run at 24 fps. The depth_info times map to frames 14, 19 and 29.

**Method (3D, lab camera f = 0.5959 x 1280 = 763 px, principal point (640,360)).**
1. `edges.py`: I took a median background of every 3rd frame, which removes the ball, and segmented the table top. I fitted Huber lines to the back, left and right silhouette edges and to the top-face front edge. For the front edge I used the strongest brightness drop between the top face and the front slab face, not the silhouette bottom; the slab is about 11.5 px thick. The fits have rms 0.3–0.8 px. Top-surface corners: BL (281.5,417.5), BR (600.1,361.9), FR (671.0,513.5), FL (224.7,613.9). The overlay is in frames/edges.png.
2. `recon.py`: the two pairs of opposite edges give two vanishing points, which give the 3D directions of the long and short edges. They are 88.7° apart, so the rectangle is consistent with f = 763. The plane normal is their cross product. I back-projected the ball centre at frames 14, 19 and 29 with depths 1.751, 1.687 and 1.526 m. The table surface is the plane 2 cm (the ball radius) below the ball centres. Plane offsets: -0.863, -0.864 and -0.847 m. I intersected the corner rays with this plane.
   - Result: long edges 71.3 cm and short edges 58.3 cm. The diagonals are 91.2 and 93.2 cm.
   - The result changes by ±0.1 cm depending on which ball-centre definition is used.

**Second route (`route2.py`).** I took the plane normal from the long-edge vanishing direction x the 3D ball path (frames 14→29), which does not use the short-edge vanishing point. This gives back and front edges of 72.2 and 68.9 cm (mean 70.5) and a width of 63.8 cm. This route is more sensitive to depth noise: the ball path tilts 3.6° out of the vanishing-point plane. The ball's apparent diameter (18–19 px) matches 40 mm at the given depths (17.4–20 px).

**Answer:** length = 71.3 cm, the long horizontal extent. The width (front to back) would be about 58 cm. Confidence is moderate, about ±4%.
