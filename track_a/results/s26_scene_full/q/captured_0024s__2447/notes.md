# q_2447 - width of the book (cm)

Answer: **10.7 cm** (the shorter side of the teal hardcover's cover; length ≈ 15.6-16.0 cm).

File fps = question fps = 24, so frame = round(t*24). Camera f = 0.5959*1280 = 762.8 px, principal point (640, 360).

## Why a plain depth*pixels/f estimate is not enough
On the ramp the book's short side runs down the slope, which recedes strongly in depth (slope ends at 1.243 m and
0.990 m), so its image length (~46 px) is heavily foreshortened. Using depth*px/f naively gives ~6.4 cm, which is wrong.
So I built 3D geometry.

## Route 1 (main): ramp plane from depth_info, then cover corners -> 3D (geom.py, edges.py)
- Ramp corners at frame 44 (zoomed): TL (750,359), TR (860,361), BL (609,468), BR (706,490). Back-projected the
  far/near edge midpoints with 1.243 / 0.990 m -> slope vector, length 0.370 m. Width direction w = perpendicular to the
  slope and projecting onto the top-edge image line (w = (0.707, 0.016, -0.707): the board is seen about 45° oblique).
  The bottom edge gives the same w to within 2.7°.
- The book's cover edges in the image are parallel to the ramp edges. Cover-top plane = parallel to the ramp, passing
  through the book centre at t=1.0 (pixel (751.0, 397.7), depth 1.0685 m). Check: the same plane puts the frame-29
  centre at 0.971 m (given at t=1.2: 0.977 m).
- Sub-pixel cover-top edges on the mean of the static frames 0-16. Each edge is a line fit (rms 0.1-0.6 px). Corners:
  BL (754.4,352.2), BR (846.8,351.9), FL (715.5,380.6), FR (804.9,384.5).
- 3D sides: back 16.3 / front 15.8 cm, left 10.6 / right 11.0 cm, corner angle 91.7° (so the model looks
  self-consistent). Moving the plane 0.5-1 cm higher to reach the cover top gives 15.6-16.1 x 10.4-10.9 cm.
  **Width ≈ 10.7 cm.**
- Slope-direction scale check against the prior: book centroids (scene track, frames 18-28) intersected with the same
  plane give a per-frame acceleration of about 2.6-3.1 m/s² for frames 19-23, which matches the prior's 2.8 m/s². Later frames
  (motion blur) and whole-run quadratic fits give about 2.0-2.2 m/s². So the prior agrees with the slope-direction
  scale to within about 5-25%. The early frames, which are the cleanest, agree best.

## Route 2 (cross-check): book resting on the table (table3d_b.py)
- Table plane normal from two conditions: the table's front corner edges are perpendicular, and the plane is
  perpendicular to the ramp's horizontal edge. This puts the camera nearly level (1.4° pitch). The plane passes
  through the ramp's near-edge midpoint (0.990 m). Cover corners at frame 44: (497,468), (557,462), (640,477), (586,486).
- Result: long side 15.0-16.2 cm (agrees with route 1), short side 8.7-9.4 cm. This view grazes the table, so the
  short side is very sensitive to the plane height and to the corner pixels (the mask variant gives 7-9 cm). It
  supports the length but only roughly the width, so I give it little weight.
- The given table_left/right depths (1.035 / 0.573 m) do not fit the table corners. A corner-based table plane would
  put the ramp foot at 0.73 m, which contradicts 0.99 m, so I did not use those depths.

## Scene record check
The scene track covers the right object (the teal book) on all frames. Its minrect "width" (~45 px on the ramp, ~30 px on
the table) is foreshortened and is not a size.

## Confidence
Moderate. Width is 10.7 ± ~0.6 cm. The main uncertainties are the slope direction from two depths, the plane height
(centre vs. cover top), and where the cover edges are placed (~1 px ≈ 2.3 mm along the slope).
