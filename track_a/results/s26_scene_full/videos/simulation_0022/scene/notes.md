# simulation_0022 – measurement record

Video: 960x960 px, 25 fps, 75 frames (t = frame/25, 0–2.96 s). Simulation (Blender), labelled 2D. Units are pixels
(x right, y down) and seconds; no metric scale has been assumed.

## Scene
There is one moving object: a red fishing boat (white cabin with a red roof trim, a tall white mast with a black
vertical element, white aft railing and "AH805" on the hull). Its bow points left and it sails left across the
right half of the frame. The static items are a beige dome-shaped rock island on the left, a sand flat under it, a
thin far shore on the horizon (y ≈ 614–626), sea with animated ripples and the boat's red reflection, and sky with
clouds. The camera is static: sky and island pixel differences across frames are only compression noise, so there is
no pan.

## Files
- `scene.json`: inventory, camera, static objects, events and a summary of the boat's pixel sizes.
- `tracks/boat.csv`: one row per frame (0–74). Columns:
  - Full mask bbox (`bbox_*`, including the mast), with `bbox_cx/cy`, `mask_cx/cy` and `mask_area`.
  - `length_px` and `height_px` (full bbox).
  - Red hull bbox (`hull_x0..y1`, `hull_len_px`, `hull_cx/cy`). `hull_x0` is the bow tip.
  - `mast_x` and `mast_top_y`.
  - `clipped_right_edge` (1 for frames 0–34, when the stern is cut off by the image edge).
  - `est_full_hull_len_px` and `est_center_x`: the hull centre. In clipped frames it is extrapolated from the bow
    using the length fit L = 274.9 + 0.235·frame.
  - `occluded` (always 0).
- `scripts/`:
  - `track_boat.py`: segmentation and track. Writes overlays to `../frames/ov/`.
  - `finalize.py`: adds the centre estimate and prints the summaries.
  - `static_island.py`: island extents.
  - `probe*.py`: checks for camera stillness and colour.

## Method
- **Background:** frame 0 for x < 820 and frame 74 for x ≥ 820. The boat is never in both regions at once.
- **Boat mask:** the union of:
  - the red hull colour (rows < 689; red pixels lower down are the reflection);
  - background difference above y = 622, where sky, island and far shore are static;
  - a downward extension over the dark underside (≤ 10 px);
  - a thin-mast detector (column of small sky differences).

  I checked the overlays at frames 0, 40, 48 and 72: the mask covers the hull, cabin and mast, and the bbox fits the
  boat. It does not include the thin white stern legs/rudder that reach into the water, or the reflection.

## Reliability
- **Bow x (`hull_x0`), mast x and mast top:** ±1–2 px. These are the best features for displacement and speed.
- **Hull top (y = 586, constant):** reliable.
- **Hull bottom/waterline (679–688):** ±4 px. The dark underside merges with dark water.
- **Hull length when fully visible (frames 35–74):** 282–292 px, ±2 px.
- **Overall height from mast top to keel:** about 293 px (frame 48).

## Motion and ambiguities
- **Motion:** the boat moves purely horizontally and leftward through the whole clip, with no vertical motion. It is
  already moving at frame 0 and still moving at frame 74. There are no stops, bounces or contacts.
- **Distance covered:** about −4.6 px/frame. The bow goes from 832 to 486 and the mast from 952 to 612, so about 340
  px over 74 frames.
- **Pixel speed rises slightly:** the mast moves at −4.51, −4.60 and −4.68 px/frame over frames 0–24, 24–49 and
  49–74. The apparent hull length grows by the same ~3.5% (282 → 292 px), and so does the bow-to-mast offset
  (122 → 127 px). This fits a constant world speed with the boat slowly approaching the camera. It could also be a
  slight acceleration; the pixels alone can't tell these apart. If a single 2D scale is used, take the boat's pixel
  length at the time the question refers to.
- **Clipped frames:** before frame 35 the stern is out of frame, so bbox and centre there are clipped or
  extrapolated. Prefer the bow or mast for motion.
- **Reference point:** the Blender origin isn't visible; it is presumably near the hull's mid-length (`est_center_x`,
  `hull_cy`).

## Static objects
These are approximate (±5 px):
- **Rock island:** x 30–557, y 528–655 (527 × 127 px).
- **Sand flat:** x 0–640, y 615–680.
