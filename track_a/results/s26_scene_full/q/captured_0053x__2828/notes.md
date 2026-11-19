# q_2828: distance between the white cup and the basketball (m)

The file and the question both run at 24 fps. t = 0.4 s is frame 10.
Method (lab card): f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Each centre is back-projected along its
pixel ray, and the point is placed at the given Euclidean camera distance (depth_info is the distance to the object
centre).
- cup (white tumbler): mask centroid (564.4, 423.9), distance 2.516 m.
- basketball: mask centroid (985.8, 369.6), distance 2.925 m.
I checked both on the frame at t = 0.4 s, and the scene-record masks cover the right objects. Both objects are static.
- 3D distance = **1.475 m**. Using the bbox centres instead of the centroids gives 1.4747 m.
- Sensitivity: if depth_info were read as z-depth instead of ray distance, the result would be 1.637 m. The
  convention is camera-centre distance, so I answer 1.475.

Prior check: the trashbin is the moving blue object. Its image speed near frame 10, at 2.73 m, gives
0.96-1.07 m/s per frame (about 0.99 at frames 9-10), which matches the prior of 0.9962 m/s. This supports f and the
depth convention.
Confidence: high (±3%).
