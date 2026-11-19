# simulation_0039 – measurement record (pixels / seconds only, no metric scale)

Video: 1536x1536, 25 fps, 75 frames (t = frame/25, 0 … 2.96 s). Simulation (Blender), 3D scene.
High-angle, nearly top-down aerial view of a beach: sand (top 2/3), rock outcrop top right, green water
bottom and right. **Camera static** (phase correlation shift < 0.05 px over the whole clip).

## Files
- `scene.json` – inventory (names, distinguishing features, visibility, motion, pixel sizes), camera, events.
- `tracks/<obj>.csv` – one row per frame the object is visible: `frame,t,ref_x,ref_y` (reference point =
  mask centroid), `bbox_cx,bbox_cy,x0,y0,x1,y1,bbox_w,bbox_h` (inclusive pixel box), `len_main_axis,
  width_across,main_axis_deg` (min-area rectangle of the mask; angle of principal axis, image coords,
  y down), `area_px`, flags `occluded, truncated_by_edge, merged_with_other, duplicate_frame`.
  boat.csv adds `hull_*` (hull-only mask: mast, rails, antennas removed by a 21 px morphological opening).
  person.csv adds `head_top_y, feet_bottom_y`.
  Objects: person (f0–74), bird (f2–70), bird_shadow (f0–42, low reliability), boat (f0–74).
- `tracks/*_raw.csv` – raw tracker output (same numbers, fewer flags).
- `track_summary.json` – start/end positions, median per-frame step, size ranges, size every 10 frames.
- `static_raw.json` – automatic sand / rock masks: extents, shoreline lower-edge samples every 64 px.
- `scripts/` – cam.py (camera shift), bg.py (median background), dups.py (duplicate frames),
  track.py (all tracking), finalize.py (clean CSV + summary), static.py, overlay/zoomcheck/montage/dbg (checks).

## IMPORTANT: duplicated frames
Frames 1, 26, 51 are pixel-identical to frames 0, 25, 50 (render/encode artefact). Every object has a
zero step at those frames and a ~double step at the next frame (2, 27, 52). A one-frame backward
difference at those frames is therefore 0 / doubled; the reference answers (computed from the true
3D positions) will not show this, so when a question asks for speed at such a frame, average neighbouring
steps (e.g. use (p(i+1)-p(i-1))/2 or a short fit) instead of the literal one-frame difference.

## Objects and how they were measured
- **person** (man, white T-shirt, grey/blue jeans, left of centre on dry sand, long shadow up-right):
  background difference (median of every 3rd frame) inside a window following him; his shadow (largest
  dark blob) and its soft edge are removed, shoes inside the shadow added back if in the body column.
  Walks slowly toward the bottom of the image (toward the water): centroid (512,549) → (524,705), ~2.0
  px/frame, fairly steady. Image "height" head-top→feet-bottom 55–71 px (median 63; stride-dependent and
  foreshortened by the steep view), width 27–29 px. Centroid ≈ shirt hem/belt = pelvis region. Feet
  bottom ±4 px (feet touch the shadow). f24–26 flagged occluded: the bird passes just below his feet.
  Checked visually on zoomed overlays (f0,10,24,25,27,40,60,74).
- **bird** (large black/dark-brown bird of prey): dark foreground blob followed with a constant-velocity
  predictor. Enters at the left edge f2 (partial), fully in f3, flies right with a slight downward curve,
  ~24 px/frame almost constant, crosses the beach→water edge around f45–50, partial at right edge f70,
  gone from f71. When it touches the person's shadow (f24–26) the shadow pixels are removed using frames
  i±4; extents there slightly less reliable (flag merged). Wings flap: main-axis length 45–91 px (largest
  ~88–91 px at f56–58 with wings spread; the wingspan is drawn roughly vertical in the image), width
  25–40 px; centroid jitters a few px with wing pose (bbox centre also given). Over the dark water the
  bird stays well separated (checked f57, 66, 69).
- **bird_shadow**: blurry, only the dark core (V<75) is segmented; merged with the person's shadow
  f7–23, fades over wet sand/water from f31 (flagged occluded). Moves with the bird ~450–600 px up-right
  of it. Use only for rough checks.
- **boat** (fishing boat: red hull, white deck/cabin, red cabin roof, mast, green hatch, text on hull;
  bow upper-left, stern lower-right; dark shadow on water to the right): colour segmentation (not
  water-green, restricted to pixels that are water in a boat-free background). Translates bow-first to the
  upper-left: full-mask centroid (743,1414) → (188,1259), ~8.2 px/frame (per-frame hull-centroid steps
  6–10 px, i.e. ±1.5 px noise – average over several frames). Heading constant (hull axis ≈ 20.5°,
  i.e. bow up-left), no rotation. Hull main-axis length median 495 px (490–512 full mask), hull width
  ~194 px (top view of deck + visible side; noisy 190–260 with mast). bbox height with mast ~300 px but
  the thin mast top is not segmented in every frame (e.g. f40) – use hull_* for size. Stern touches the
  bottom edge at f0; bow cut by the left edge from f66 (mask) / f67 (hull): centroids after f65 are
  biased (steps drop to 4–6 px) → use the stern side (x1, hull_x1) for motion there.
  The boat's "root" is unknown; hull centroid is the best proxy.
- **static**: rock outcrop top right x≈685–1450, y 0–320 (cut by the top edge; auto mask x 744–1475,
  y 0–323, centroid (1112,113)); dry-sand plateau with jagged lower edge, lowest tip ≈ (570,1030); wet
  sand/water line lowest at ≈ (647,1159); water fills the lower part and the right side. Person's
  shadow is long (~120 px) pointing up-right (sun low, from lower-left).

## Perspective / 3D
No horizon; steep top-down view. Upright objects appear as short strokes pointing up the image (person's
head above his feet, mast top above its base). Apparent sizes do not change measurably over the clip
(person width 27–29 px over 156 px of travel; boat hull length constant within ±2 % while travelling
~560 px), so all objects keep ~constant camera distance; bird size changes are wing-pose, not depth.
The bird flies above the ground (its shadow is far from it), so the bird is closer to the camera than
the sand; its pixel scale differs from the person's/boat's – use depth_info per object when given.
Focal length unknown; with depths given, f_px = pixel size × depth / true size; principal point
assumed (768,768).

## Reliability
Positions: person ±1–2 px, bird ±2–3 px (pose jitter), boat ±1.5 px per frame (hull), bird shadow ±5 px.
Sizes: boat hull length ±5 px, person height ±4 px, bird extents vary with flapping (report min/max).
