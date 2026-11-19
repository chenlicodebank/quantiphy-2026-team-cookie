# simulation_0070 – measurement record (pixels, seconds)

2D simulation (Blender render), 2160x1080, 24 fps, 72 frames (t = frame/24, t = 0 to 2.958 s).
The scene is a **static top-down (bird's-eye) view of a street intersection**. Two objects move: a
**peach sedan (car)** that drives up the vertical road and turns right into the horizontal road, and a
**cyclist** (person on a bicycle, seen from above) riding straight up the vertical road, left of the car.
Everything else is static. No metric scale is assumed anywhere.

## Files
- `scene.json` – inventory (moving and static objects with pixel sizes and positions), camera, events.
- `tracks/car.csv` – car, every frame 0-71. Columns: frame, t, cx, cy (centroid of the tight body mask = origin
  estimate), bx0..by1 (axis-aligned bbox), len/wid (minAreaRect of the mask), rect_cx/cy/angle,
  pca_len/pca_wid (extent along/across the principal axis, +1 px), axis_deg (body axis, mod 180, CCW from +x,
  90 = up), area, edge (touches the frame border: never), occluded (never), heading_deg (front direction),
  front_x/y and rear_x/y (bumper midpoints on the axis).
- `tracks/car_with_shadow.csv` – the same from the loose difference mask (body + soft drop shadow, ~222 x 91 px).
  For reference only. Do not use it for sizes.
- `tracks/cyclist.csv` – cyclist, every frame 0-71, the same columns as car.csv without heading/front/rear.
- `scripts/` – `motion_scan.py` (finds the movers), `track.py` (masks and tracks, writes the CSVs and the overlays),
  `car_axis_points.py` (heading and bumper points; also tests a rear-axle pivot model, which was rejected),
  `static_objects.py` (static inventory from the median background), `events_camera.py` (camera-shift check,
  per-frame steps and direction), `zoom_check.py` / `crop.py` (visual checks).

## Method
Background = per-pixel temporal median of every 4th frame. Moving mask = RGB distance to the background > 30,
closed and hole-filled. A 10 px column (x 934-943) is cut out so that the cyclist (x ≈ 907-930) and the car
(x ≥ 950) never merge. Car body = peach-paint pixels (R−B > 22, R > 180) inside the moving mask, followed by the
convex hull (adds the dark windows and excludes the grey shadow). Overlays (car body box, bbox, centroid) were
checked by eye at frames 0, 12, …, 71 and zoomed at frames 30 and 71. The box hugs the bumpers and sides.

## Key numbers (px)
- Car body: length 220 (218-221), width 82 (80-83), from PCA extents; minAreaRect gives about 1 px less.
  The size is constant over the clip (orthographic top view, no perspective scaling).
- Car centroid: (990.4, 851.5) at f0 → (1371.8, 636.5) at f71. Path length 478.4 px, net 437.8 px.
  The per-frame step is nearly constant: 6.83 ± 0.18 px/frame over frames 2-71.
- Car heading: 89.8° (up) at f0-1 → 45° at f29 → <1° at f61 → 0° (right) from f66.
- Cyclist: length 63 (57-68; oscillates with the pedalling), width 21. Moves straight up at x ≈ 917-918.
  Mean step 8.93 px/frame (frames 2-71); single steps vary 7.5-10.3 because the legs move inside the mask.
  Centroid (918.6, 810.3) at f3 → (917.2, 203.9) at f71. Path ≈ net ≈ 625 px over frames 1-71.
- Both objects are stationary between frames 0 and 1, and both start moving at frame 2 (t = 0.083 s).
  No contact or collision occurs. The closest approach is at the start (about 20 px gap between the cyclist's
  right edge and the car's left side).
- Static objects (scene.json): roads ~470 px wide; 4 sidewalk blocks; manhole 87x90; three brown squares
  ~82x80; 8 two-headed lamp fixtures; 4 dark corner fixtures; a teal round object (Ø19); a white ball on the
  road at (2028.8, 432.4), Ø ≈ 19 px, static; a grey rock cluster 68x56 at (2062, 623), static.

## Reliability and ambiguities
- Camera static: the phase-correlation shift is < 0.01 px. The background is stable.
- Car origin: the body-mask centroid is the best origin estimate (±1 px). I tested a fixed non-slipping pivot
  (rear-axle root) model and rejected it. The direction of motion differs from the body heading in a way no
  rigid pivot explains: early in the turn the path direction leads the heading by ~26°, and late in the turn it
  trails by ~14°. The car's rotation and translation are evidently keyed independently, so the centroid moves at
  a near-constant pixel rate. If a question's root is a different point, front_x/y and rear_x/y bound it.
- Cyclist identity: very small and thin from above. I read it as a rider on a bicycle (front wheel with a white
  tip at the top, shoulders and arms at the middle), but "pedestrian" / "person" probably means the same object.
  The reference point is the mask centroid (±2 px per frame, jittery). Smoothing over several frames or using
  long baselines is advisable. In frames 0-2 the car's shadow touches its mask (occluded = 1, cx biased by
  about +2-3 px, width inflated to ~25).
- The car's soft drop shadow widens the loose mask by ~10 px. The tight body mask excludes it. Car side mirrors
  stick out ~1-2 px beyond the body box.
- Scale: the scene is 2D and orthographic, so one m/px factor from the given prior applies to every object
  (the car length 220 px is the natural prior carrier).
