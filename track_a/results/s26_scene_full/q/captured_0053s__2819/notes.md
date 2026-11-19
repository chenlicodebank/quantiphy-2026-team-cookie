# q_2819 – height of the trashbin (cm)

File fps = question fps = 24. t=0.4 s → frame 10.

## Object
The trashbin is the record's "blue_object": a blue patterned, slightly tapered round bin lying on its side,
sliding (print does not rotate) up-left along its own axis. The wider open end (rim lip visible) is the far,
upper-left end; the narrower bottom is the near, lower-right end. Its standing height = its axis length.

## Geometry
- f = 0.5959·1280 = 762.75 px, principal point (640,360).
- Back-projected the given depths at t=0.4 s (bin 2.730, cup 2.516, book 2.082, ball 2.925 m).
  Ground-plane normal from cup/book/ball centres: tilt 41° (`geom.py`). Check: bin centre moved on a plane
  parallel to it gives speed ≈0.97–0.98 m/s at frames 9–11 vs prior 0.9962 m/s, and depth ratio f47/f0 1.39 vs
  apparent-size ratio 1.33. (A height-corrected plane with 33° tilt gave 1.17 m/s – worse – and worse silhouette fits.)
- Silhouette model fit (`frustfit.py`): a 3D solid lying on that plane at the back-projected centre, projected with the
  pinhole camera; IoU against the background-difference mask; shared size over 5 frames, per-frame yaw/offset.

## Results (axis length L = height)
| model / plane / frames        | IoU loss | L (m) | diameters |
|-------------------------------|---------|-------|-----------|
| frustum, 41°, 16,24,30,40,47  | 0.068   | 0.329 | 0.347 / 0.280 |
| frustum, 41°, 20,26,34,42,46  | 0.066   | 0.330 | 0.346 / 0.279 |
| frustum, 41°, 6,9,10,11,14    | 0.048   | 0.333 | 0.333 / 0.273 |
| cylinder, 41°                 | 0.091   | 0.334 | 0.312 |
| frustum, 33° plane            | 0.098   | 0.350 | 0.363 / 0.303 |
| box, 41°                      | 0.099   | 0.371 | 0.229 × 0.212 |
Best-fitting model (frustum) is stable at 0.33 m across frame windows (second route); overlays in
frames/jfit_frust_*.png match the outline closely.
Simple card estimate (depth × image long side / f = 2.73×120/763 = 0.43 m) overestimates, because the oblique
silhouette's long side includes the end ellipses and the axis is foreshortened differently.

Answer: 33.1 cm. Confidence moderate (±10%): the main uncertainty is the axis-length vs diameter trade-off in the
silhouette and the plane tilt (a 33° plane would give ~35 cm).
