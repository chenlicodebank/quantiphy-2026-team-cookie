# q1359 — width of the purple car (simulation_0067)

Answer: **1.73 m**

The purple car is the parked dark-purple classic sedan (W123-like) on the far side of the intersection, pointing left.
It does not move, so I used frame 0. File fps = question_fps = 24.

## Camera (3D scene)
- Principal point at the image centre. The three vanishing points from scene.json are VP1 (road, 2697,-43), VP2 (diagonal
  road, ~110,-47) and the vertical VP (1075,2604). All three orthogonal pairs give f ≈ 1098–1107 px, and the
  orthocentre lands on the image centre. I used f = 1100 (`cam.py`).
- Metric scale: the pedestrian's pelvis pixel and the given depths (21.677 m at f14, 22.7825 m at f38), together with
  the feet directly below the pelvis, give a camera height of 7.088 / 7.089 m above the sidewalk (`ground.py`). The
  far curb face is ~4.5 px tall, which works out to a curb ≈0.10 m, so the camera is ≈7.19 m above the road.
- Check against the prior: I tracked the van's lowest mask point (a ground contact) over frames 16–71, mapped it onto
  the road plane and fitted a quadratic. The acceleration comes out at 4.04 m/s² against the prior of 4 m/s²
  (`vanacc.py`), so I rescaled the road height by 0.99 to 7.116 m. The van moves along VP2, which is the same
  direction as the sedan's width, so this check covers the axis the answer depends on.

## Sedan
- Near-side wheel ground contacts are (1331,334.6) front and (1418,311.7) rear. The car's axis lies 1.1° from the road
  direction, and the wheelbase is 2.87 m.
- The width runs along the lateral axis, which points almost straight away from the camera, so measuring y in pixels
  is very sensitive. Instead, each left/right feature pair is placed on the image line through VP2 (the image of a
  lateral 3D line), so only their x-coordinates matter (`sedan3.py`). At f = 1100 the lateral line agrees with the
  VP2 direction: the leftover axial component is only 0.04 m.
  - Bumper ends, x 1253.5 → 1314, at h 0.40–0.50 m: **1.72–1.75 m**. The near end sits on the wheel line at h ≈ 0.46.
  - Front fender corners, x 1260 → 1320, at h 0.70–0.80: 1.69–1.71 m.
  - Headlight outer edges (narrower than the body): 1.60–1.62 m.
- Far-side door mirror (`mirror.py`): at the A-pillar's axial position (h ≈ 1.0 m) its tip reaches lateral ≈ -1.55
  to -1.63 m. That is inside the far bumper end (-1.67 m), so the mirror does not widen the bounding box.
- Sensitivity: with f = 1000 the bumper width is 1.79 m, and with f = 1200 it is 1.68 m. One pixel in x changes the
  width by about 0.03 m.

## Second route
- The far front tyre, visible under the bumper, gives an outer track width of ≈1.6 m on the ground. This is only
  consistent, not precise: the tyre's lowest visible point sits 0.35 m ahead of the axle, so it is not the true contact.
- Proportions: a real W123 has width/wheelbase ≈ 0.64. Here it is 1.73/2.87 = 0.60, which is plausible for an asset
  model.

Confidence: moderate. Expected error is about ±4%, mainly from f and from where the bumper and corner ends were placed.
