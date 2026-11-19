# q1628: length of the rabbit (m)

Prior: deer speed = 1.277 m/s. The "deer" is the horned quadruped in scene/. The camera is static and the time base is 30 fps (file rate = question rate).
depth_info: rabbit is 15.798 m from the camera at t=0 and 15.852 m at t=1.0.

## Rabbit pixel length
- The rabbit faces right (+x) and moves along x, so its length is its horizontal pixel extent along x.
- A pale disc (render artifact) covers its head. The disc's right edge is taken as the nose.
- Zoomed, gridded frames (zoom.py, frames/z*.png):
  - f0: rump 937 to disc edge ~1016, about 79 px.
  - f28: rump 1144 to ~1222, about 78 px; about 87 px with the hind feet stretched.
- The scene record's bbox_w over all 75 frames: median 82 px (10–90 pct: 70–92).
- I tried a background-difference segmentation (seg.py). The deer's shadow and the brownish floor contaminated it, so I rejected it.
- Used length = 82 px.

## Scale
1. Prior route (2D):
   - Deer pixel speed: mask centroid net 7.80 px/frame; trunk 7.65; mean 7.72 px/frame = 231.7 px/s.
   - Deer hooves (y≈798) and rabbit feet (y≈800) are on the same floor line, so both are at about the same depth.
   - Scale = 1.277 / 231.7 = 0.00551 m/px, giving 82 px → 0.452 m.
2. Depth route:
   - The rabbit moves mostly sideways (centroid (975,772) at t=0, (1199,771) at t=1, principal point (960,540)).
   - Its distance grows 15.798 → 15.852 m. Assuming constant Z, this gives f ≈ 2958 px and Z ≈ 15.75 m.
   - Scale = Z/f = 0.00533 m/px, giving 82 px → 0.437 m.
   - Cross-check: at this f the deer would move 7.99 px/frame, against 7.65–7.87 measured, which agrees within 3%.

## Answer
0.445 m: the average of the two routes, which differ by 3%.

Confidence: moderate.
- The disc hides the exact nose position.
- The length changes with the hop pose (70–92 px), about ±8%.
