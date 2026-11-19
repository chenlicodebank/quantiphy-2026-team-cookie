# q1514 – width of the vehicle (HIMARS-style launcher truck), simulation_0144

The file and the question both run at 24 fps (35 frames). Prior: rocket length = 2.9 m. Depths: rocket 43.064 m at t=0 (f0)
and 41.127 m at t=0.5 s (f12). The camera is static. I assume the principal point is at the image centre (960, 540).

## Focal length (geom.py, fscan.py, truck.py)
- Rocket origin pixels: f0 = rest position in the tube, s = -520 on the scene/ flight line -> (1331.8, 761.1). f12 = (1239.0, 656.0)
  from scene/tracks/missile.csv. For a trial f, back-projecting these with the two depths gives the 3D flight line, and every
  tracked frame (13-30) is placed on that line.
- Route A: the rocket's apparent width (blur-free) x depth should stay constant. Its slope over f13-30 is zero at f ≈ 2230 px.
- Route B: apparent length = projected 2.9 m + c x image speed (motion blur). At f = 2200, c = 0.44, which is close to
  Blender's default shutter of 0.5. With c = 0.5 the length fit gives f ≈ 2150.
- Route C (truck geometry): b, the truck's lateral axis, is perpendicular to the rocket/pod axis, and its direction was fitted
  to the lateral edges (cab front edges, tube-face edges). "Up" was fitted to the vertical cab edges, and a = up x b.
  The predicted longitudinal edge directions (bed edges, wheel-hub line) match the image exactly at f ≈ 2200-2210
  (residual about 0.1 deg). That is an orthogonality check.
- Adopted f = 2200 ± 50 px (horizontal field of view about 47 deg). The camera is almost level and the pod is raised about 39 deg.

## Width
- Anchor: the tube mouth the rocket leaves from (top row, near-side column, (1285.6, 707.5)) is placed on the 3D rocket line.
  The tube-face plane has the pod axis as its normal. The middle-column tube (1268.75, 706.25) back-projected onto that
  plane gives the truck's centre plane (normal b). The middle column also coincides with the midpoint of the pod face,
  so the pod is centred on the truck.
- Cab front face (frontw.py): the far-side corner edge is at x = 1002.5 and the near-side corner edge at x = 1096.5, taken
  from intensity steps along rows y = 923-947 (94 px). I solved for the two 3D points: their difference is parallel to b
  and their midpoint lies on the centre plane.
  Result: 2.465 m at f = 2200 (2.645 at f = 2100, 2.308 at f = 2300). The roof front edge and front bottom edge give
  2.43 / 2.46 m.
- Bumper ends (x ≈ 1001 and the side block at ≈ 1100) and the front fender/tyre look flush with the cab sides. No mirrors
  stick out, so the overall wheel-to-wheel / body width ≈ the cab width.
- Second route: a simple pinhole estimate, 94 px x 38.7 m / 2200 / sin(angle between b and the viewing ray = 0.667),
  gives 2.48 m.

Answer: 2.47 m. Uncertainty is about ±4 %, mostly from f. It also assumes the pod is centred on the truck and that the
tyres do not stick out past the cab.
