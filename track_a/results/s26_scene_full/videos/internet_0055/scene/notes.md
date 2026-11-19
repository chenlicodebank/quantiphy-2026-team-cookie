# internet_0055 – measurement record (pixels and seconds only)

Real footage, 1920x1080, 30 fps, 75 frames (t = frame/30, frame 0 at t = 0). Marked as a 2D scene.
Eye-level view along a two-lane bike path into a roundabout (Stanford campus). No metric scale is assumed anywhere.

## Files
- `scene.json` – inventory, per-object summaries, events, camera, perspective cues, static object extents (frame-0 pixels).
- `tracks/pedestrian.csv` – woman walking right to left, all 75 frames.
- `tracks/white_car.csv` – white SUV on the far side of the roundabout, frames 0-59 (visible=0 afterwards).
- `tracks/bus.csv` – Marguerite shuttle bus at the right edge, all frames (always cut by the edge).
- `camera_transforms.json` – per-frame 2x3 similarity matrix `a` (frame-i pixel -> frame-0 pixel), scale, roll, centre shift dx/dy.
- `scripts/` – camera.py (camera motion), background.py (stabilised median background), segment.py (pedestrian + car masks
  and tracks), buses.py (bus edges), static_objects.py, parallax_check.py, draw_tracks.py, build_scene.py.
  Run order: camera -> background (writes scratch frames/bg_stab.png) -> segment -> buses -> static_objects -> build_scene.

Track columns (pedestrian, white_car): `cx,cy` = mask centroid; `bbox_*` = mask bounding box; `bbox_cx,bbox_cy` = bbox centre
(the "visible centre"); `top_x,top_y` = topmost mask point (head top for the pedestrian); `mask_len_main_axis` /
`mask_width_across` / `main_axis_angle_deg` = PCA extents of the mask; `stab_*` = same quantities in frame-0 (background-fixed)
coordinates; `occluded` = 1 if partly hidden. All other columns are in the original frame.
Bus columns: `rear_left_edge_x` (left edge of the white rear panel / rear corner), `rear_top_y`, `rear_bottom_y` (rear panel roof
and bumper bottom), `front_end_x` (leftmost bus pixel once the side is visible, frames 47-74), `side_top_y_at_front`,
`side_bottom_y_at_front` (bottom includes some ground shadow).

## How it was measured
- Camera: KLT features from frame 0 tracked to every frame, RANSAC similarity fit. The camera is handheld but almost still:
  smooth drift, by frame 74 background moved ~+5..+12 px (x) and ~+11..+17 px (y), roll ~0.27 deg, no zoom (<0.2%).
  Template-tracked static points at near and far depths fit the model within ~2 px, so no parallax. For motion of the
  pedestrian (~600 px) the drift is ~1-1.5%; use `stab_*` columns if you want background-fixed coordinates.
- Pedestrian and car: every frame warped to frame 0, differenced against a median background (very clean), thresholded,
  cast shadow at the feet removed (dark, unsaturated pixels in the bottom 45 px of the mask), largest blob + nearby parts.
  Overlays were checked by eye at frames 0,10,20,30,36,40,42,48,50,60,67,74: masks cover head (cap) to shoes; bbox
  extents are good to ~±3 px. Small leftovers: some low-contrast pants pixels missing inside the mask (does not affect bbox),
  a few px of shadow between the feet in some frames (affects `cx,cy` slightly, bbox hardly).
- Bus: colour (white rear panel) for the rear corner; difference to a bus-free background (frames 22-34) for the front end.
- Static objects: colour masks on the stabilised background (= frame-0 coordinates) plus readings on zoomed frames.

## Objects and reliability
- **pedestrian** (the main subject): woman, light-pink cap, white long-sleeve top, khaki cargo pants, pink/orange shoes.
  She walks steadily right to left across the far end of the bike path, in front of the splitter island, all 75 frames
  (already moving at frame 0, still moving at frame 74; no stops). bbox centre x goes from ~1220 to ~610 px (~8.2 px/frame).
  She also comes slightly toward the camera: pixel height (bbox_h, cap top to the lowest shoe) grows from ~261 (frame 0)
  to ~315 (frame 74), and feet go from y≈686 to y≈733. So a single px->m scale taken at one time differs by up to ~±10% from
  another time; the annotators used one scale (planar assumption). Height is best read at legs-together frames
  (mid-stance, bbox width minimum): frames 4, 21, 35, 50, 67 (bbox_h ≈ 272, 283, 291(occluded), 303, 312). Feet-apart
  (double support, max stride width) frames: 12, 28, 43, 58 (and ~73-74). Each step takes ~15-16 frames (~0.5 s).
  Frames 34-52: her lower legs/feet are near or behind the black bollard (occluded=1, conservative flag); in some of those
  frames bbox_y1 may be ~2-6 px short. She passes in front of the bicycle-sign pole around frames 36-37 (pole is behind her).
- **white_car**: white SUV (Tesla Model Y-like), side view, nose to the left, on the far side of the roundabout (far away,
  ~65 px tall). Moves left ~5.5 px/frame. Full bumper-to-bumper length visible only in frames 0-17 and 21-28:
  bbox_w ≈ 167-174 px (frames 0-17), 177-183 px (21-28); it grows slowly because the car comes around the curve slightly
  toward the camera. Frames 0-17 the DO NOT ENTER pole crosses the car body (mask bridged across it, flagged occluded);
  frames 18-20 its rear end is hidden behind that pole (bbox_x1 stuck at ~233, length too short); from frame 29 the front is
  cut by the left image edge (only the rear bumper bbox_x1 is valid); gone from frame 60.
- **bus**: ONE white/red Marguerite shuttle (#3428), not two buses. Frames 0-~45: its rear is seen, the rear corner moves
  right from x=1753 to ~1902, decelerating (≈6 px/frame at start, ≈0 by frame ~44). Then the bus turns around the roundabout:
  its rear stays at the right edge (x≈1890-1909) and its left side swings into view, front end moving left from ~1843
  (frame 47) to ~1775 (frame 74); `front_end_x` is noisy (±6 px). Never fully visible, so no length.
  `rear_top_y` is blank in frames 72-74 (detector jumped to the red banner).
- Static (frame-0 px, see scene.json for full list): bollard 66 w x 380 h (x 857-923, y 655-1035), red no-pedestrian disc on
  it 96 px; DO NOT ENTER panel 153 x 150; bicycle diamond 161 x 166 (diagonals), arrow plaque 97 x 56; YIELD triangle
  120 x 102; TO TRAFFIC IN CIRCLE plaque 93 x 67; chevron signs ~52-56 x 46-47; delineators ~13-25 x 49-60; Stanford banner
  51 x 70. These are at very different depths from the moving objects – only use them as a scale if the question does.

## Ambiguities
- The pedestrian's "length" in the motion direction is her stride width (bbox_w, 67-186 px, oscillating with gait), her
  main axis length (`mask_len_main_axis`) is ≈ her pixel height. A person-height prior pairs with bbox_h.
- Car and pedestrian are at very different distances: one scale cannot fit both physically, although the annotators'
  convention is one scale from the prior object.
- Motion blur is mild; shadows: the pedestrian casts a dark shadow down-right on the path (removed from the mask);
  the bus casts a shadow on the road to its lower left.
