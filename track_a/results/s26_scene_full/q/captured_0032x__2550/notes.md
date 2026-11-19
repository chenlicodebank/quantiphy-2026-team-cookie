# q 2550 — width of the table (cm)

Lab video, 24 fps (file and question_fps both 24). f = 0.5959 x 1280 = 762.8 px, principal point (640,360).
Prior: tennis ball diameter 6.7 cm. depth_info at t=1.5 s (frame 36): tennis ball 1.183 m, ping-pong ball 1.353 m.

## Method (edges.py, geom.py)
1. edges.py: fitted the four table-top edges in code (frames 0 and 48; overlay frames/edges_f48.png):
   back edge (top of the non-black mask), left/right side edges (row-wise mask extents), front-top edge
   (strongest brightness drop between the top surface and the front face, per column).
2. geom.py: vanishing point of the side edges (718,350) gives the depth direction; the intersection of the back and
   front edges (x ≈ -5000) gives the lateral direction; the plane normal is their cross product.
   The plane offset comes from the tennis-ball centre at frame 36 (track ccx,ccy = 582.5,436.5) back-projected
   to a Euclidean distance of 1.183 m, minus the 3.35 cm radius along the normal.
3. Table corners were found by intersecting the edge lines and back-projecting them onto that plane.

## Results
- frame 48 edges: left-right extent (front and back edge) 60.08 cm. Front-to-back (side edges) is 74.97 cm. Corner angle is 89.0°.
- frame 0 edges: left-right extent 59.90 cm. Front-to-back is 74.0 cm. Corner angle is 87.2°.
- The table is roughly 75 cm (front-to-back) x 60 cm (left-right). The record's 501 px front edge vs 282 px back edge comes from strong foreshortening, because the camera
  is only about 17 cm above the table plane.

## Checks (second route)
- The ping-pong centre, back-projected independently to its own given 1.353 m, lies 1.98 cm above the reconstructed
  plane. A ping-pong ball's radius is 2.0 cm, so the plane and scale agree with the second given depth.
- The reconstruction comes out rectangular (front = back length, corners about 88–89°), so the vanishing-point normal is consistent.
- A rejected variant (a plane forced through both ball contact points) gave a non-rectangular table, so it was discarded.
- The tennis ball's pixel diameter at frame 36 (42 px) implies a distance of 1.217 m rather than 1.183 m (+3%). If that were used, the result would be about 61.8 cm.
  I kept the given depth, as the convention requires.

## Naming
Width = the shorter horizontal extent. Here that is the left-right extent, 60 cm. The longer front-to-back extent,
about 74–75 cm, is the length. (If "width" were read as front-to-back depth, the answer would be about 74.5 cm.)
Answer: 60.0 cm. Confidence: good, about ±3%.
