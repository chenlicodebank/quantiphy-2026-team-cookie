# simulation_0075 – measurement record (pixels, seconds)

2D simulation, 24 fps, 72 frames (0–71, t = frame/24), 2160x1080. Near-top-down static camera over a
four-way street intersection. Image axes: x right, y down. No metric scale is assumed anywhere.

## Files
- `scene.json` – inventory, layout, sizes, motion summary, events, camera.
- `tracks/<object>.csv` – one row per frame (all 72 frames) for every moving object:
  `frame, time, ref_x, ref_y` (centre of the min-area rectangle of the foreground mask = origin proxy),
  `centroid_x/y` (mask pixel mean), `bbox_x0..y1`, `length_px` / `width_px` (min-area rect along / across the
  main axis), `axis_angle_deg` (main axis, image coords, 90 = vertical, 0/180 = horizontal), `area_px`, `top_y`, `occluded`.
  `pedestrian_sidewalk.csv` also has `torso_x, torso_y, torso_px` (centroid of the white shirt pixels).
  Top-down view, so there is no separate pixel height. The length and width are the ground-plane footprint.
- `static_objects.json` – static items: centre, bbox, length/width, plus road-edge transitions.
- `vehicle_sizes.json` – single-frame vehicle extents at two thresholds (12 = includes soft shadow halo, 25 = body).
- `scripts/` – `track.py` (clean background + tracking), `overlay.py` (visual check), `series.py`, `torso.py`,
  `static.py`, `sizes.py`, `check_dup_zoom.py`, `finalize.py` (occlusion flags, events).

## Objects
Moving (all visible in every frame):
- **white_van**: white van/minibus, vertical road, x≈831. It starts at rest at f0 and speeds up steadily straight up (−y).
  The per-frame step rises about linearly from ~0.5 px to ~20 px at f71. Body is about 236×88 px; track masks run 239–247 × 91–101 because they include some shadow.
- **tan_car**: tan/peach sedan. It starts right of the van heading up and makes a smooth right turn into the
  horizontal road (heading ≈180° from ~f60), at a near-constant ~6.8 px/frame. Body is about 219×82 px.
- **pedestrian_road**: cyclist/scooter rider in dark clothes, between the van and the tan car (x≈917), riding straight
  up at a constant ~8.9 px/frame. Footprint is 62 px along the travel direction and 19 px across.
- **pedestrian_sidewalk**: person in a white top walking right on the SE sidewalk (y≈843) at ~2 px/frame.
  Use torso_x/y as the pelvis proxy, because the mask centre jitters by several px with the legs and the shadow, which extends to the left.

Static: a parked purple sedan (≈196×72, upper lane of the horizontal road), a parked green sedan (≈200×73, lower lane),
a white ball (~20 px disk) and a rock cluster (67×55) on the right of the horizontal road, a dark square grate (89×91, N),
three brown squares (~82 px; NW, SW, SE), a trash bin (25 px, SE), four corner signal posts, and eight three-headed street
lamps (top/bottom sidewalks). Road widths: vertical road x 616–1082 (466 px), horizontal road y 288–756 (468 px).

## Events
- f0: van at rest, starts accelerating.
- f1 is a near-duplicate of f0, so the tan car, cyclist and walker first move between f1 and f2. Their one-frame step at f1 is 0.
- Tan car turn: from f2 to about f60. Heading angles: 105° at f15, 136° at f30, 160° at f40, 172° at f50, ~180° from f60.
- The van draws level with the cyclist (same y) between f70 and f71, about 85 px to its left. No contacts or collisions occur.
- The walker passes under the head of street lamp S2 during f28–53 (`occluded=1`). The torso blob shrinks at f45–47.

## Method and reliability
Clean background: frame 0, with the moving objects' starting regions pasted in from frame 71. Each frame's foreground is
the pixels whose max-channel difference exceeds 25, cleaned with a 5×5 close. Components are kept inside a gate around the
previous bbox. Overlays (frames/overlay.png) confirmed that every track hits the right object over its full extent.
- Vehicle centres: ±1 px, with ~1 px frame-to-frame jitter. The van mask at f34–35 has a glitch (length drops to 234 at f34),
  so its step there reads 6.2/13.9 px instead of ~10/10. Smooth over it.
- Cyclist centre: ±1 px. Its 62 px length may include a short shadow.
- Walker: the mask centre is noisy (±3 px), and the torso centroid is better (±1 px). Sizes vary with stride.
- Sizes: the body extents at threshold 25 are the best estimate of the object footprint. Shadows add ~5 px in length and up to ~17 px
  in width at threshold 12. The parked cars' pale bumpers blend into the asphalt, so allow about ±5 px.
- There is a slight global brightness difference between f0 and f71 (visible as faint patches in the clean background). It is below
  the threshold and does not affect masks.
- The camera is static. Vehicle lengths do not change with image position, so one px scale applies to the whole ground plane.
  The rendered view is not perfectly orthographic (vehicle fronts/windshields are visible), but there is no measurable scale change.
