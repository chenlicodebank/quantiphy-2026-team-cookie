# simulation_0270 — measurement record (pixels, seconds)

2D Blender render, 2560x1440, 24 fps, 72 frames (t = frame/24). Static camera. One moving object: a
colourful **phoenix** (green head/torso, yellow beak, purple/pink/red wings, long orange-red tail plumes with
peacock-eye spots and a yellow-green flame tip) flying right-to-left in front of a plain grey studio
cyclorama, speeding up, flapping with a ~25-frame (~1.04 s) wingbeat. Its shadow moves along the floor.
No other objects, no contacts/bounces/impacts.

## Files
- `scene.json` — inventory, camera, sizes, events.
- `tracks/phoenix.csv` — one row per frame 0-71. Columns:
  - `bbox_x0,y0,x1,y1,bbox_w,bbox_h,bbox_cx,bbox_cy` — full mask bounding box (beak wisp to tail tip, wing tip to wing tip).
  - `centroid_x/y` — whole-mask centroid; `area_px`; `main_axis_len, across_width, main_axis_deg` — PCA extents of the mask.
  - `green_body_x/y` — centroid of all green pixels (first attempt; jumps when green wing coverts show, e.g. frames 20, 45, 70).
  - `body_x/y` — centroid of the largest green blob (head+neck+torso); `body_blob_x0/x1` its extent.
  - `body_s_x/y` — **recommended origin proxy**: body_x/y, 5-frame median then 5-frame mean.
  - `head_x/y, head_ncc, head_ok` — NCC template track of the head (centre of a 120x90 patch on head/neck, ~35 px behind the beak tip). Trust only `head_ok=1` (lost after frame 66: wing covers head; poor at 9, 17, 34, 42, 45, 59 when the wing sweeps past).
  - `occluded` — 0 always (never occluded by another object; only self-occlusion by wings).
- `tracks/phoenix_shadow.csv` — floor shadow: centroid, bbox, area per frame.
- `scripts/` — `track.py` (background median + masks + shadow), `body.py` (green torso blob), `head.py` (head NCC + smoothing),
  `overlay.py` / `finalize.py` (check images, events, backdrop profile), `probe.py`.

## Method
Background = per-pixel median of 12 evenly spaced frames (bird moves >1000 px so it vanishes). Bird mask =
max-channel |frame − bg| > 18 above y=1100, opened/closed, blobs near the main one. Shadow = darker than bg by >12
below y=1100. Overlays (frames 0, 9, 14, 36, 52, 71) were checked: the mask covers the whole bird incl. tail tip,
wing tips and the faint translucent wisp in front of the beak; bbox fits.

## Key numbers
- Body (body_s) x: 1541 (f0) → 1396 (f24) → 1123 (f40) → 923 (f50) → 315 (f71); y 667-731, bobbing with the wingbeat (lowest ~f13, f39, f64). Leftward pixel step grows from ~0 (f0-1) to ~25-35 px/frame at the end (accelerating).
- Frame 0→1 is almost unchanged; motion begins at frame 2.
- bbox width 536-624 px (wisp/beak to tail tip; varies as the tail plumes swing);
  bbox height 252 (wings level, f71; ~253-260 at f9, 21, 34, 46, 59) to 463 (wings down, f37; 461 at f12-13, 459 at f62).
  Wings are seen side-on, so there is no true wingspan view; vertical bbox extent is the closest "wing" measure.
- Wings up: frames ~2, 26, 52; wings down: 12, 37, 62; wings level: 9, 21, 34, 46, 59, 71.
- Backdrop: wall/floor bend at y≈1062 (ramp 950-1150); shadow at y≈1195-1260.

## Reliability / ambiguity
- Origin: the rig root isn't visible. body_s is the best guess (torso, error maybe ±15 px per frame; raw body_x
  jumps by up to ~20-30 px at wing-level frames 9-10, 20-22, 34-35, 45-47, 59-60, 70 when wings hide or uncover the torso).
  Over long spans (≥5 frames) all point choices agree to within a few px/frame in x. head_x is the sharpest
  rigid feature but the head bobs relative to the body.
- Sizes: mask extents are ±3 px; the faint wisp in front of the beak (~30-50 px) is in the bbox; a size prior
  "length" probably means the bird's world AABB, which includes the tail and changes with the wings — compare to the
  bbox at the frame named, or the frame-0 bbox (566 x 404 px).
- Single-depth 2D clip: one px→m scale should apply to the whole flight.
- Small motion blur on wing tips at fast strokes; no other similar objects.
