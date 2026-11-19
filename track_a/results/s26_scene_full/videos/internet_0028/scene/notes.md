# internet_0028 – baggage carousel (measurement record)

All values in pixels of the original 3840x2160 frame (x right, y down) and seconds; t = frame / 20.528302.
No metric scale is assumed anywhere.

## Scene
Close top-down (slightly oblique) 4K view of an airport baggage carousel. Bags ride the carousel **left → right** the whole
clip at a steady ~70-80 px/frame (lower band). In order of appearance: blue_backpack (f0-~46, lower band), red_suitcase
(corner only, top-right, f0-14), orange_suitcase (f4-~90, middle/lower band), black_hard_case (top band, f~6-92, never
fully in view), black_duffel (black with tan crossing straps and red cloth, f~42-92), grey_bag (bottom-left, f~66-92).
Background = grey carousel plates (one embossed logo per plate, pitch ~625 px in the upper band) and dark ribbed rubber
panels. Nothing starts, stops, bounces or is thrown; no people.

## Files
- `scene.json` – inventory, extents, events, camera notes (read this first).
- `tracks/<object>.csv` (final) – per frame: `frame, t_s, ref_x, ref_y, ref_source` (recommended reference point),
  `full_x0..full_y1, full_cx, full_cy` (full-extent box = box measured at a reference frame, translated with the ref
  point; can lie outside the image), `vis_*` (that box clipped to the image, its centre and size), `truncated_by_frame`,
  and `pt_<name>_x/_y` = raw template positions of every tracked mark.
  orange_suitcase.csv also has `mask_*` (colour-mask box and centroid, valid f4-84).
- `tracks/red_suitcase.csv` – red colour mask (visible part only), f0-14.
- `tracks/orange_suitcase_mask.csv` – orange mask every frame (rows f85+ are a WRONG object - duffel strap; ignore).
- `tracks/raw/*_raw.csv` – raw LK-box propagation + template outputs (ncc scores) used to build the finals.
- `global_motion.csv` – per-frame median feature shift of the whole image (dx, dy px/frame), similarity scale/rotation, cumulative shift.
- `speed_map.json` – median image motion in 8x6 position bins for four frame blocks (perspective diagnostic).
- `scripts/` – view.py (grid crops), global_flow.py, orange_mask.py, red_mask.py, profile.py (edge profiles), track.py
  (+objects.json: reference boxes/points), finalize.py, speed_map.py, plate_pitch.py, events.py, overlay.py, diffs.py, cmp_orange.py.

## How measured
- Reference boxes/points chosen by eye on gridded full-res crops, edges refined with HSV row/column profiles (profile.py).
- Box propagation: median Lucas-Kanade shift (forward-backward checked) of features inside the visible part of the box,
  1/3-scale frames, frame to frame from the reference frame forwards and backwards.
- Template points: NCC template matching with sub-pixel peak (ncc 0.93-0.99 for tag/buckle/zip pull/lower wheel).
- ref point per object: orange_suitcase = luggage-tag centre (template f25-69); blue_backpack = hip-strap buckle (f0-22);
  black_hard_case = lower wheel hub (f23-76); black_duffel = white zipper pull (f65-92); grey_bag = LK box centre.
  Outside the template range the ref is continued with LK box increments (`ref_source = lk_extrapolated`), which can
  drift: comparing with the handle template, the orange box drifted ~90 px over f10→f52 (~2 px/frame).
- Visual check: overlays (overlay.py) at f5-f89 – boxes sit on the right bags, edges within ~50 px, points on the marks.

## Key extents (see scene.json for all)
- orange_suitcase @f52: overall length (wheel housing → handle housing) **2455 px** (x 965-3420); orange body only
  **2090 px** (1065-3155); orange + tan grip mask **2348 px** (1036-3384; 2328-2384 over f48-57, shrinking slightly
  as it moves right = perspective). Top edge y 935, bottom beyond frame (width ≥1225 visible). Tag frame ~240x360 px.
  Fully in view about f47-57.
- blue_backpack @f0: body 2600 px (x 490-3090), 2800 px incl. strap tip; top y 1020, bottom beyond frame.
- black_duffel @f86: 2090 px incl. red cloth (x 1400-3490); soft.
- black_hard_case: never fully visible; wheel hubs 640 px apart at f40.
- carousel plate pitch ~625 px (upper band, y~750).

## Motion (raw pixel facts only; no speeds fitted)
- Whole-image median shift 65-81 px/frame in +x (mostly ~72-77), |dy| ≤ 2.
- Per-object frame-to-frame shifts (diffs.py): orange tag 79→71 px/frame (decreasing as it crosses left→right), orange
  handle 75→69, orange LK box 72-81; backpack buckle 72-77, logo 66-70; duffel zip pull 75-83; black case lower wheel
  60-68, upper wheel 45-51; red suitcase edge ~40-44; belt plates upper band 37-50.

## Reliability / ambiguities
- **Camera motion cannot be checked**: no static background is in view; everything rides the belt. Similarity fits show
  no rotation/zoom. If the camera panned slowly, all image speeds include it.
- **Perspective is strong** although labelled 2D: image speed depends on y, x and height above the belt (upper band ~48,
  lower ~75 px/frame; raised bag tops faster). Pick the reference point on the same object/part the question names; a
  single scale from the prior object applies cleanly only to that object.
- Which "length" of the orange suitcase a prior refers to is ambiguous (overall with handle vs body) – both recorded.
- Motion blur ~10-30 px; soft bags (backpack, duffel) deform; bottoms of all bags are cut by the frame edge.
- orange mask x1 early (f4-20) includes a dangling tag beside the handle; mask x0 f41-47 merges with the duffel's strap.
