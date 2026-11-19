# simulation_0305 – measurement record

3D Blender render, 24 fps, 72 frames (t = frame/24, 0..2.958 s), 2560x1440 with black letterbox bars
(picture rows 80..1359). Camera static. All values in pixels / seconds; no metric scale assumed.

## Scene
- **aircraft** – the only object: one dark-grey jet/sci-fi fighter (twin engine pods, swept wings, fins) flying
  above a featureless light-grey ground plane. Moves smoothly up-left in the image and away from the camera for
  the whole clip; apparent size shrinks from 665 px (main-axis length, frame 0) to 458 px (frame 71), i.e. its
  distance grows by ~1.45x (if size ∝ 1/depth). No contacts, bounces or direction changes.
- **aircraft_shadow** – soft shadow on the ground, below-left of the aircraft; cut by the bottom image edge in
  frames 0-18. Useful only as a ground-plane cue (shadow-to-aircraft image gap shrinks from ~360 px at frame 24 to
  ~250 px at frame 71 as it recedes). Not an object a size question should use.
- **ground** – uniform, no markings, no vanishing lines; brightness gradient (bright near bottom, dark band near
  the top) is the only perspective cue.
- Frames 0 and 1 are identical (duplicated first render frame); motion starts at frame 1→2. Speeds computed with
  a backward difference at frame 1 give 0.

## Files
- `scene.json` – inventory, camera, apparent sizes at frames 0/24/48/71, events.
- `tracks/aircraft.csv`, `tracks/aircraft_shadow.csv` – every frame: `cx,cy` (mask centroid = reference point,
  proxy for the object origin), `bbox_cx,bbox_cy`, bbox `x0,y0,x1,y1,bbox_w,bbox_h`, `len_main_axis` /
  `width_across` (PCA-axis extents of the mask), `axis_angle_deg`, `area_px`, `truncated_by_frame_edge`,
  `occluded` (always 0).
- `scripts/bg.py` (median background → scripts/bg.png, deleted to save space; rerun before seg.py), `scripts/seg.py` (segmentation + tracks + overlays),
  `scripts/check.py`, `scripts/montage.py`.

## Method and reliability
Mask = |frame − per-pixel median background| > 22 grey levels, opened 3x3; components grouped with a 25 px
dilation; upper group = aircraft, lower = shadow. Overlays (every 7th frame) were checked: the masks cover the
full aircraft and shadow and never merge. Aircraft centroid noise is ≲1 px; extents ±2-3 px (thin fin tips and
antialiasing). The mask centroid is a 2D proxy for the origin; the true origin may be offset by a few percent of
the body length (the engine pods/fins make the silhouette asymmetric). Apparent "length" is the projected
silhouette in a 3D oblique view (the aircraft is seen partly from below), so it mixes length with wingspan;
bbox_h includes fins and wing thickness in projection. For depth/focal estimation use len_main_axis or bbox_w
together with given depths. The shadow's soft edge makes its extents ±5 px.
