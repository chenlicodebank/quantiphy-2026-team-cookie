# simulation_0263 — measurement record (pixels, seconds)

Video: 2560x1440, 24 fps, 72 frames (t = frame/24), Blender render, 2D scene.
Content: top-down view of a plain light-grey floor. A single dark-grey sports car (nose pointing left) is at rest at
frames 0-1, then drives straight LEFT along image row y ≈ 718, faster every frame, and leaves through the left edge
(nose crosses x = 0 at frame 61; by frame 71 only the rear ~118 px is still visible). No other objects, people,
markings or props. The car's cast shadow (a mid-grey band ~38 px toward the image top and ~15 px ahead of the nose)
moves with it. The camera is static (car-free bands drift ≤ 0.08 px over the clip).

## Files
- `scene.json`: inventory, sizes, key positions, events, camera.
- `tracks/car.csv`: one row per frame (0-71). Columns:
  - `ref_x, ref_y`: **recommended reference point** (car centre ≈ vehicle root seen from above).
    ref_x = 1596.5 + `tm_dx_vs_f30`, where tm_dx_vs_f30 is the sub-pixel shift of a rigid template of the car's
    rear end (from frame 30) found by normalised cross-correlation. 1596.5 is the body-bbox centre x at frame 30.
    ref_y = 718.0 (template dy = 0 in every frame, so the car never moves vertically). This stays valid in the
    truncated frames 61-71, where ref_x goes negative (the centre is off-screen).
  - `step_px`: |ref_x(i) − ref_x(i−1)| (one-frame backward step in px; multiply by 24 for px/s).
  - `ref_x_bboxcentre, ref_y_bboxcentre, cx, cy`: centre of the body-mask bbox and the mask centroid (alternatives;
    wrong once the car is truncated, frames ≥ 61).
  - `bbox_x0..y1, len_x, wid_y, pca_len, pca_wid, axis_deg, area`: body mask (car without shadow: pixels darker
    than 0.45 × background, closed with a 41 px disc, holes filled, largest component).
  - `full_x0..y1`: mask of |frame − background| > 25 (car + shadow).
  - `truncated_by_frame_edge` (1 from frame 61), `occluded` (always 0), `tm_score` (match quality 0.86-1.0).
- `scripts/`: `track_car.py` (background, masks, template tracking, overlays), `finalize.py` (ref point,
  camera check, track overlay), `profile_check.py` (nose/length check), `probe.py` (intensity probe).
  Run from the scene_ws folder.

## Key numbers
- Rest: frames 0-1 identical (ref_x 2001.5). First motion 1→2 (1.3 px). Steps grow smoothly by ~0.9 px/frame
  each frame: 26.6 px at 29→30, 35.5 at 39→40, 53.6 at 59→60, 63.4 at 70→71. Positions frame 0: 2001.5;
  f30: 1596.5; f40: 1281.8 (≈ image centre); f60: 382.0; f71: −265.3. Net displacement f0→f71 = 2266.8 px
  (straight line along −x, so path length = net displacement).
- Car width (across motion, y): 366 px (y 536-901) in all frames; it is very reliable (±2 px).
- Car length (along motion, x, body mask, untruncated frames): 788 px at frames 0-9, 776 at f30, 767 at f40,
  742-744 at f58-60. The apparent length shrinks ~6 % as the car moves from the right of the image to the left,
  probably mild perspective (parts at different heights shift differently) and changing lighting at the nose.
  Recommended single value 776 ± 15 px (≈ median of frames 0-60). If a question gives the car's real length or width,
  pixel scale = 776 px (length) or 366 px (width); the width-based scale is more stable.
  Length/width ratio ≈ 2.12.
- Height: not visible (top view).

## Reliability and ambiguities
- Track: the template shift is consistent to ≈ 0.1-0.3 px per frame (smooth step sequence). The bbox centre differs
  from the template reference by up to ~15-30 px late in the clip because the apparent front edge creeps back; for
  speeds and distances use `ref_x` (step differences between the two agree within ~1 px/frame).
- The shadow is excluded from the body mask by brightness. A faint grey fringe ~15 px ahead of the nose may be
  shadow or a light-coloured bumper edge (±15 px on length).
- Frame 71: body-mask bbox/centroid columns are wrong (only a fragment, y 710-901); ref_x from the template is fine.
- No motion blur visible; car brightness darkens slightly toward the left of the image (lighting vignette).
- One scale for the whole frame is appropriate (2D, motion purely along x at constant y).
