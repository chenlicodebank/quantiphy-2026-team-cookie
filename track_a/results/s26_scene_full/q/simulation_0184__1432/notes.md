# q_1432 – length of the box (simulation_0184, 3D Blender render)

Question: length of the box (m). Prior: acceleration of the box at t=1.25 s = 1.58 m/s². depth_info: camera→box
origin 9.194 m at t=0 and 9.096 m at t=0.5 s. question_fps = file fps = 24 (no time-base mismatch).

## Geometry / camera
- Static camera, principal point assumed at the image centre (960,540).
- **Focal length, route 1 (gravity)** – `fall_fit.py`: the box falls from rest at frame 0 (first step 2.1 px, about half of
  the 4.0–4.1 px/frame² second difference). Projecting a free fall (g = 9.81) from the 3D start point (ray through the
  centroid, distance 9.194) and fitting the cy track for frames 0–7 gives f ≈ 2153–2175 px for camera pitch between -0.1
  and +0.2 rad; at the measured near-level pitch (horizon y ≈ 555) f ≈ 2155 px.
- **Camera yaw relative to the world** – `wall_vp.py`, `vp_solve.py`: the block-wall mortar lines are not horizontal
  (slopes -0.087 at the top down to -0.012 near y=480). Their vanishing point is (-5343, 555), so the wall lies at 19.1°
  to the image plane (right side nearer the camera) and the camera is almost level. A free cuboid fit put the box at
  17.7° yaw (`box_fit2.py`), so the box is aligned with the wall, i.e. with the world axes. Its world AABB length is
  therefore its long-side extent L. This also means the region x≈653–751 on frame 0 is mostly the box's right end
  face, not the front face. That end face carries the "504"/vent panel and the "^ N2054/B" lid end, which are seen on
  the end face on later frames.

## Size measurement
- `box_fit3.py` / `box_fit4.py`: a cuboid with yaw fixed to the wall direction is fitted to the convex-hull
  silhouettes of frames 0–3 (IoU fit, centre at distance 9.194 on its ray). Scale comes from the distance. The fit
  alone trades length against depth (W), so the depth W is chosen with the ramp frames 18–42. Those frames are fitted
  with one shared orientation and a free centre per frame, which pins down the L:W:H shape.
  Profile at f=2180: W .55/.60/.65/.70 → L 1.211/1.194/1.167/1.142. The early-frame cost is lowest at W≈0.65 and the
  ramp cost at W≈0.60, so W≈0.62. **Fit: L≈1.19 m, H≈0.71, W≈0.62 at f=2165.**
- `extent_check.py`: the fitted cuboid spans x 420–747 on frame 0, but the silhouette spans 416–751. The lid is wider
  than the base: the base is 428–741 and the lid band is 416–751. The fitted cuboid sits between them, while the AABB
  includes the lid. Matching the silhouette extremes gives L≈1.21–1.23 m.
- Answer: **L ≈ 1.21 m** (between the cuboid compromise of 1.19 and the lid-extreme value of 1.22–1.23).

## Second route / checks
- **Focal length from the prior (route 2)** – `ramp_line.py`: with f=2180 and the fitted shape, the 3D centres on the
  ramp define a straight line (slope 29°, heading toward the camera). Projecting the image positions onto that line gives
  arc length s(t). Quadratic fits over frames 16–42, 20–42 and 24–42 give 1.45–1.61 m/s². The prior is 1.58 m/s², so
  the prior is reproduced with f ≈ 2100–2220, consistent with the gravity value of 2155. (An earlier size-ratio
  depth model in `ramp_accel.py` gave 1.61–1.67 at f=2160, also consistent.) Used f = 2165. L scales about as 1/f, so
  this adds about ±1.5 % uncertainty.
- The fitted height (0.71 m) reproduces the silhouette height exactly: cuboid y 240.6–431.0 against silhouette 241–431.

## Confidence
Moderate: about ±5 %. The main uncertainties are the box depth W (length–depth trade-off, ±1.5 %), the lid overhang and
non-cuboid shape (±2 %), and f (±1.5 %).
Other reading: if the reference took the box's AABB along the camera's horizontal (not the world axes), the value would
be about L·cos19° + W·sin19° ≈ 1.34 m. The wall alignment strongly suggests the world-axis value of 1.21 m.
