# simulation_0019_segmented — measurement record

3D scene, segmentation video (Blender render with background replaced by white), 1080x1080, 33 fps, 97 frames
(t = frame/33, frames 0-96, t 0-2.909 s). All values are pixels / seconds; no metric scale is assumed.
Pixel coordinates: origin top-left, x right, y down.

## Scene
A man walks right-to-left (-x) behind a grey abstract flame-shaped sculpture standing on a two-tier plinth
(light upper tier, dark lower block). Two framed abstract paintings on dark stand bases flank the sculpture
(left and right); a brown sculpture is cut off at the right image edge. The man is the only moving object.
Camera is static (median-background subtraction leaves only the man; no background shift). No ground, horizon
or floor texture is visible (white background), so perspective cues are limited to object bases/occlusion:
depth order front->back = plinth/sculpture (base y 895), man (feet y 777-787), painting stands (base y 686),
right-edge object (base y 659). The pedestal top face is seen from above (camera higher than the plinth top).

## Files
- `scene.json`: inventory (appearance, pixel bboxes/extents of static objects), man summary (apparent size range,
  gait), events with frame/time, camera notes.
- `tracks/man.csv`: one row per frame 0-96. Columns: frame, t, visible (any mask pixels), occluded (1 = partly or fully
  hidden), pelvis_x/pelvis_y (reference point, see below), pelvis_src (measured / from_head / interp), bbox_x0..y1,
  bbox_w, bbox_h (visible mask bbox), centroid_x/y (visible mask centroid), head_top_x/y (mean x of top 20 mask rows,
  topmost row), feet_y (lowest mask row, only when unoccluded), mask_area, pelvis_meas_x/y (hip-band measurement).
- `scripts/bg.py` (median background -> scripts/bg.png, change-region listing), `scripts/track_person.py` (mask,
  track, overlays to frames/ov_*.png), `scripts/static.py` (static extents), `scripts/write_scene.py` (scene.json).

## Method and reliability
- Mask = max-channel |frame - median background| > 30, opened/closed, components gated near previous position.
  Overlays (frames/ov_*.png) checked at frames 0-96 every 6 plus transitions: masks cover the full man.
  Small holes where his white shirt matches the right painting (frames ~20-30) do not change the bbox.
- Pelvis (reference point for simulation answers = human pelvis):
  * frames 0-40 (`measured`): x = mean mask x in a 24-row band at head_top + 0.47*bbox_h, y = that row. Arms swinging
    through the band add ~±3 px jitter to x. y ≈ 643-650.
  * frames 41-57 and 78-96 (`from_head`): head_top + median offset (dx -1.2, dy +122.2) from frames 0-40. Head
    stays visible there, so x is good to a few px; y assumes constant posture.
  * frames 58-77 (`interp`): man fully hidden behind sculpture (58 shows only a hand fragment); linear interpolation
    between frames 57 and 78 (~6.4 px/frame vs ~5.5 px/frame when visible — treat with care; times there are
    unobserved).
  Pelvis x moves ~883 (f0) -> 651 (f40) -> 570 (f57) -> 435 (f78) -> 341 (f96), y ~645 throughout; per-frame steps
  vary with gait (≈3-10 px). Prefer fitting over several frames than single-frame differences.
- Apparent size of the man: full-view bbox height 257-268 px (median 261) over frames 0-40, varying with gait;
  feet_y 781-787; frames 94-96 height 253-257 with a foot partly hidden behind the plinth. Near-constant size ->
  roughly constant camera distance (walk nearly parallel to the image plane; maybe very slightly farther at the end).
  Bbox width 61 (legs together) to 139 (full stride): step period ~16-17 frames.
- Static extents (from background, ±2 px): sculpture bbox (376,391)-(602,693), 302 px tall, 227 wide; plinth upper
  tier (355,672)-(627,768); lower block (332,768)-(632,895) 301x128; whole plinth 224 px tall; left painting stand
  (249,518)-(377,686) 129x168; right painting stand (656,519)-(783,686) 128x167; right-edge object visible part
  (1034,548)-(1079,659), truncated.
- Occlusion flag: occluded=1 when the man's left silhouette edge abuts sculpture/plinth pixels in >=4 rows, or the
  visible height < 240 px. Partial occlusion starts at frame 41 (hand/foot at plinth edge; arm and legs clearly
  hidden from ~46-50), full occlusion 59-77, partial 78-96.

## Ambiguities
- Pelvis is an image-based estimate (no skeleton); for 3D questions answerers need depth_info + focal length.
- The man is not at the same depth as the sculpture/paintings (he is between them), so a single pixel scale from a
  static object does not transfer to him without depth information.
- No start/stop, bounce or contact events: he walks continuously and does not touch any object.
