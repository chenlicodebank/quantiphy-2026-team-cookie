# q_1897 – length of the truck (m)

Prior: truck acceleration 10.757 m/s². Depths to the truck centre: 22.532 m at t=0.5 s (frame 15) and 19.525 m at t=1 s (frame 30).
question_fps = file fps = 30, so frame = round(t·30).

## Method
1. **Motion model** (`recon3d.py`): the truck drives straight with no yaw. I fitted the front-hub track (frames 0–46) and the
   rear-hub track (frames 25–54) from scene/tracks with a pinhole camera (principal point at the image centre, level camera)
   and s(t) = ½·a·t² along a common direction m. Fitting v0 gives v0 = −0.03 m/s, so the truck starts from rest at frame 0.
   Reprojection rms is 0.87 px. The fitted vanishing point is (−3180, 537); the record gave −3040 ± 45 from the box edge.
   The scale along the motion line comes from the acceleration and does not depend on the focal length.
   Wheelbase is 4.19 m.
2. **Focal length from depth_info** (`center_depth.py`, `solve_f.py`): I rebuilt the truck box (side plane through the
   hubs; rear edge, front, top and ground) and put the centre at mid-length, mid-height and half-width.
   f ≈ 2650 px (horizontal FOV ≈ 40°) reproduces both depths: D15 → f = 2654 predicts D30 = 19.522 (given 19.525).
   **Independent check of the scale:** using only the depth ratio (no acceleration), f comes out at 2620–2720, and the
   absolute depths then need a scale factor of 0.99–1.01. So the metric scale from depth_info agrees with the one from
   the acceleration to about 1%.
3. **Rear end** (`rear_consistency.py`): the rear vertical edge of the box (leftmost mask pixel, rows 450–700) was traced
   over frames 34–56. That point must stay fixed relative to the front hub, which happens only when the box side is
   0.10 m outside the hub plane (drift +0.0007 m/frame, against 0.005 m/frame at 0). Then s_rear = −6.92 m relative to the
   front hub. The tail-lift/under-run parts stick out at most about 0.04 m further back.
4. **Front end** (`front_triang.py`): I triangulated the KLT-tracked front bumper corner (the yellow marker light,
   frames 0–43) as a point fixed to the truck. With f = 2650 it lies s = +1.13 m ahead of the front hub, laterally
   2.03 m from the hub plane (the far side), with rms 1.0 px. The result is the same for frames 0–20 (1.05) and 20–43 (1.14).
   A ±30 px change in f moves it by ±0.02 m.
5. **Length** = 1.13 + 6.92 (+ ≈0.02 rear protrusion) ≈ **8.07 m**.

## Second route
The near-side front edge of the cab (the crease between side and front at x ≈ 1105 at frame 36 and 1605 at frame 42) and
the rear box edge were both projected onto the side plane:
- With both on the hub plane: 8.14 / 8.17 m (frames 36 / 42).
- With the box 0.1 m out and the cab 0.1 m out: 8.08 / 8.11 m.
- With the box 0.1 m out and the cab on the hub plane: 8.02 / 8.07 m.

Moving the crease by ±10 px changes the length by ±0.06 m. This route agrees with the triangulation within about 1%.

## Confidence
Expected error is about 2%. The main uncertainties are the exact front-most point (bumper or rounded cab, about 0.05 m)
and the scale (about 1%, set by the fitted vanishing point and the hub tracks).
