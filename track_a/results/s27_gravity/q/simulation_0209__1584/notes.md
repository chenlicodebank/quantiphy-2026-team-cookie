# Q1584: length of the table (m). Answer: 2.36

The file and the question both use 24 fps. This is a 3D Blender scene: a typewriter falls onto a large pedestal desk, and a revolver lies on the desk.

## Geometry (principal point at the image centre, no roll)
- **Vertical vanishing point** (`vert.py`): I fitted lines to the desk's left and right vertical silhouettes against the wall
  (fit residual 0.3 and 1.2 px). They meet at (1030, 11015), so roll is about 0 and f / tan(tilt) = 10475 px.
- **Gravity fall** (`track.py`, `fit2.py`, `scanf.py`): I re-segmented frames 0-10 myself. Frame 10 is still in the air and
  contact comes at about 0.435 s, which fits the prior's "before 0.45 s".
  - The scene record's bbox centre is biased: the top face comes into view during the fall (bbox_h grows from 117 to 150 px).
    I therefore fitted the bottom edge with a pinhole model under 9.8 m/s² free fall, with the tilt tied to the vanishing point.
    The bottom-front edge is about 0.15-0.2 m nearer than the origin, so its distance is about 4.15 m.
  - The best fit is f = 2650-2700 px (residual 0.25 px).
- **Second route, depth versus timing:**
  - Start origin: 4.32 m along the ray at pixel (1247, 46). Origin at t = 0.5 s: 4.501 m along the ray at (1234, 607).
  - The vertical drop between them must equal 0.5 g t² for the observed fall time (rest at t ≈ -0.01 s, contact at 0.435 s).
    This holds for f of about 2600-2650 px (drop about 0.95 m).
- **Adopted values:** f = 2650 ± 70 px, tilt 0.248 rad.

## Desk
- **Plane:** normal along gravity. I placed it with the revolver: its origin is 4.704 m along the ray at (1448, 625), and the desk top is 1.5 cm below it.
- **Corners:** I picked the outer corners of the top on zoomed crops: L (459, 697), FL (698, 888), FR (2000, 656), B (1595, 525), each ±3-5 px.
- **Back-projection at f = 2650 px:**
  - Front long edge 2.336 m, back long edge 2.374 m, extent along the long axis 2.38 m. Width is about 1.0 m.
  - At f = 2600 px the length is about 2.40 m; at f = 2700 px it is about 2.31 m.
- **Answer:** 2.36 m.

## Checks
- The typewriter origin comes out 0.09 m above the desk at rest. That is half the height of a box about 0.18 m tall and about 0.5 m wide, a plausible ratio for a typewriter.
- The objects are about 1.4 times the size of typical real ones (a 0.5 m typewriter, a 2.4 m desk). The scale is still fixed by the given distances together with g: the drop computed from the distances matches the gravity fall time. A smaller scale would need a much shorter fall.
- The four corners are not quite a rectangle (about 94° at FL) because of corner-picking error on the short edges. The long edges agree within 2%.
- **Confidence:** about ±5%.
