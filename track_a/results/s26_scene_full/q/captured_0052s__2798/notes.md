# q_2798 — distance between trashbin and basketball (m)

The file runs at 24 fps and so does question_fps. Lab camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).

## Measurements
- Basketball (static, measured in code with an orange saturation mask on frame 24): bbox x 756–847, y 624–719,
  centre (801.5, 671.5), 92 px wide. This matches scene/static_objects.json.
- Recycling bin (static): scene record, frame 48 (no hand overlapping it): bbox x 681–775, y 485–591, centre (728, 538).
  At frame 24 the person's hand overlaps the bin, so my frame-24 mask is too big there (centre 722.5, 530.5). I used
  that mask only as a sensitivity check.
- Depths at t = 1.0 s: bin 2.977 m, basketball 1.9365 m.

## Computation
Each centre is back-projected along its unit ray to the given Euclidean depth, and the result is the 3D distance between the two points.
- Record centres: 1.123 m. With the basketball centre at y = 669.5: 1.122 m. With the frame-24 bin mask: 1.134 m.
- If depth_info were read as z-depth instead: 1.047 m. I rejected this reading, since depth_info is defined as Euclidean distance.
- Sanity check: the basketball diameter comes out as 1.9365 × 92 / 762.8 = 0.234 m, close to a real basketball
  (0.24 m). Most of the separation is along the depth direction (~1.04 m).

Answer: 1.12 m. Confidence is good, about ±3%.
