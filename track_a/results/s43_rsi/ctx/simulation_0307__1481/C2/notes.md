# Q1481 – length of the plane (m)

Prior: speed 22.16 m/s. depth_info: 102.6664 m at t=1 s (frame 24) and 121.8263 m at t=2 s (frame 48).
question_fps = file fps = 24. The camera is static. Frames 0 and 1 are identical, and the motion starts after frame 1.

## Geometry
- The aircraft is a VTOL gunship with twin engine pods, a central fuselage with a canopy, and wings with ducted fans
  and wingtip fins. It flies nose-first, up-left in the image, away from the camera, with a constant attitude.
- Constant 3D velocity is confirmed: a projective (constant-velocity) fit to the hull-centroid track has 2.3 px rms.
  Its vanishing point combined with the two depths gives f ≈ 3460 px, and the speed implied there is 22.10 m/s (the prior is 22.16).
  Fitting speed and depths alone gives f ≈ 3430 px (hfov ≈ 41°). (geo.py, vp.py)
- The body axis is **not** parallel to the velocity. The pods appear at 42–43° in the image while the motion runs at 29°.
  The 3D body axis is about 7.5° off the flight path, nose up. So length can't come from "pixel length ÷ pixel speed".

## Length measurement
- I measured the extreme points along the body axis. These are the front corner of the left pod (LF) and the rear tip of
  the same pod (LR, the dark tip just beyond its light). I clicked them on contrast-enhanced zooms at frames 2, 24 and 48
  (plus 71 for LR). Then I tracked them in every frame by template matching (track.py, tracks_feat.json). I also tracked the
  canopy (CL) and the right-element front (RF).
- An oblique-coordinate check on frame 2 shows that the canopy front, a nose probe and the right element front all sit at or
  behind the pod fronts, and that the pod rear tips are the rear-most points. In 3D, the canopy is 3.4–3.6 m behind LF and RF
  is 1.4–2.4 m behind it. So pod front to pod rear is the nose-to-tail extent.
- Bundle adjustment (ba.py) fits a rigid aircraft translating at constant V with |V| = 22.16, using:
  - an unknown focal length f
  - the 3D feature points
  - an origin point (image = hull centroid, distances = depth_info)

  The feature reprojection rms is 0.7–1.4 px, f = 3300–3360, and the given distances are reproduced to 0.06–0.15 m.

  | Run | Pod length L (m) |
  |---|---|
  | thr 0.8, LF+LR+CL | 10.67 ± 0.09 |
  | thr 0.9 | 10.97 ± 0.15 |
  | LF+LR only | 10.62 |
  | with RF | 10.69 |

- Second route (tri.py / sens.py): direct triangulation of the clicked keyframe points with V taken from the hull centroid
  and the depths (f = 3300–3550) gives 10.45–10.72. A bootstrap with ±2 px click noise gives 10.59 ± 0.42.

## Answer
L ≈ 10.7 m (range of methods 10.5–11.0).

Caveats:
- This is the body (local) nose-to-tail extent. If the reference were a world-axis box of a pitched or diagonal plane, it
  would differ by a few percent.
- The pod front corner has low contrast, and that is the main uncertainty (about ±4 %).
- The origin lies about 8.4 m behind the pod front along the axis, so the model origin is not at the visual centre. This does
  not affect the length, because the scale comes from the speed plus the radial velocity from the two depths.

Confidence: moderate-good.
