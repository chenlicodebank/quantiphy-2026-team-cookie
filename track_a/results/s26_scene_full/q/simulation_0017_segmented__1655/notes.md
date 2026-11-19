# q_1655 — length of the bench seat (m)

The file fps and question_fps are both 33. Frame 0 = t 0 and frame 33 = t 1.

## Camera calibration from the person (prior 1.3 m/s, depths 5.424 m at t=0 and 4.886 m at t=1)
- The pelvis x comes from scene/tracks/person.csv (pelvis_x_smooth): -1.5 px at frame 0 and 252.0 px at frame 33. The
  apparent size is constant, so the person walks parallel to the image plane at a constant depth Z.
- Route 1 uses only the two distances: f = 906.7 px and Z = 4.657 m. It reproduces the 1.3 m/s speed (1.302).
- Route 2 uses the speed prior plus each distance: Z = 4.659 / 4.657 m and f = 908.6 / 908.2 px. All routes agree,
  giving f ≈ 905-908 px and person Z ≈ 4.66 m.
- Horizon: the pedestal's top tier is seen edge-on at y≈549, and the base outline converges at y≈549, so y_h = 549.
  The planted shoe sole (frames 0-13) is at y≈730, so the camera is h ≈ 0.934 m above the floor.

## Bench (compute.py, slab_edges.py, bench_edges.py, profile.py)
- The widest part is the seat slab: x 13 to 1058 at y 785-790, so 1046 px. Its two ends are almost symmetric about
  cx. The pointed slab ends lie on the slab's front face, so the length is Z_front x 1046 / f.
- Column profiles: slab front-top edge at y≈781, cushion top front edge at y≈752, cushion top back edge at y≈699, and
  the base's front bottom on the floor at y=967 (Z = 2.02 m).
- The bench origin is taken to be the centre of its bounding box (distance 2.267 m). The front is at z, the back at
  z x 203/150, and the top at h - 203 z / f. Solving gives z_front = 1.84 m, seat top 0.52 m and depth about 0.65 m.
  The base front at 2.02 m sits behind the seat front, which is consistent.
- **Length = 1.84 x 1046 / 905 ≈ 2.13 m.**

## Alternatives and sensitivity
- Origin at the bottom centre instead: 2.03 m.
- Seat front aligned with the base front, ignoring the bench distance: 2.34 m.
- Naive 2.267 x 1046 / f: 2.62 m. This is rejected because it ignores the vertical offset and the depth extent.
- Confidence: moderate, about ±8%. The main uncertainty is where the bench origin sits within its depth.
