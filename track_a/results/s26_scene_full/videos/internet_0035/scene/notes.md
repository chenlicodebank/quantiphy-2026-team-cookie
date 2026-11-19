# internet_0035 — measurement record

Internet clip, labelled 2D. 3840x2160, 22.297248 fps, 36 frames (0–35, t = frame/22.297248, last frame t = 1.570 s).
All values are in pixels of the full-resolution frame (x right, y down) and seconds. No metric scale is assumed.

## Scene
A static close-up of a white tiled wall (large rectangular tiles with dark grout, laid in a staggered pattern) with a white
suction-cup toilet-roll holder mounted on it. A right hand (forearm and dark grey-green sleeve come in from the right
edge) holds an **empty cardboard toilet-paper tube** that is sitting on the holder's horizontal arm. The hand slides the tube right
along the arm. The tube clears the arm's end-plate between frames 24 and 25. Then the hand carries it down and to the
right, and both leave the frame at the bottom right: the tube is last seen (partly) in frame 32 and the hand in frame 33.
Frames 34–35 show only the wall and the holder.

## Files
- `scene.json`: inventory (tube, hand, holder, tiles, sleeve), static sizes and positions, events, camera.
- `tracks/tube.csv`: one row per frame. `visible` is 1 for frames 0–32. Columns:
  - `left_end_x`, `left_end_y`: leftmost mask point, i.e. the tube's free left end. **This is the most reliable coordinate.**
    Its y jumps by about ±20 px because the leftmost point slides around the end ellipse, so don't use left_end_y for motion.
  - `ctr_est_x`, `ctr_est_y`: estimated centre of the whole tube. x = left_end_x + 277.5 (half of 555 px). y is the middle
    of the top and bottom silhouette edges, or bottom − 131 when the top edge wasn't found.
  - `cx_mask`, `cy_mask`: centroid of the visible mask. It's biased left because the fingers hide the right part.
  - Mask bbox, plus `mask_len_axis`, `mask_wid_axis`, `mask_angle_deg`: PCA extents of the visible mask.
  - `bottom_y`, `top_y`, `diam_px`: silhouette edges measured on the column at left_end_x + 130.
  - `occluded` (always 1: the right end is in the fingers), plus an occlusion text and `on_holder_arm` (left end still left of the
    end-plate at x 2339).
- `tracks/tube_raw.csv`: raw output of segment.py. Its frame-33 row is a false detection (a blurred finger).
- `tracks/hand.csv`: mask of skin pixels (hand and forearm). Columns: centroid, bbox, PCA extents, `leftmost_x/y`
  (finger or thumb tip), `at_frame_edge`, and the sleeve's top-left corner. Visible in frames 0–33.
- `camera_shift.json`: positions of 7 grout lines in every frame, plus mean brightness.
- `scripts/`:
  - `camera.py`: camera-stability check.
  - `probe_colors*.py`: chose the colour thresholds.
  - `segment.py`: masks, raw tracks and overlays.
  - `tube_dims.py`, `build_tube.py`: tube size and the final tube.csv.
  - `static_profiles.py`, `tiles.py`: holder and tile edges.
  - `draw_tracks.py`: track overlay for checking.

## Methods
- **Camera:** static. Grout lines move less than 1.2 px over the clip (a jump of about 0.5 px at frame 17 is compression or a tiny
  shake), so motion can be measured directly in image coordinates. Exposure brightens steadily (mean grey 175 → 189).
- **Segmentation** (Lab colour, full resolution):
  - Tube: b ≥ 131, b − a ≥ −0.5, a < 134, L > 90, with skin dilated by 15 px and removed. The wall and holder are neutral
    (b ≈ 126–128).
  - Skin: a ≥ 136.
  - Then: morphological open/close, largest component, hole fill.
  - I checked the overlays (frames/ov, not part of the record) at frames 0, 16, 24, 28, 31, 32 and 33. The tube outline hits the
    cardboard in frames 0–32. Frames 28–32 are motion-blurred. In frame 32 the tube is cut off by the bottom edge.
- **Tube length (bumper-to-bumper equivalent): 555 px** (±10). This is the horizontal extent at frame 0, row y = 1300, from the
  left end at x 1716 to the open right end at x 2271. Frame 0 is the only frame where the right end is visible, between
  thumb and index finger. The axis tilts about −4°, so the length along the axis is about 557 px. It is consistent with
  frame 22 (left end 2196, right end near 2755).
- **Tube diameter: ≈ 260 px.** Frames 15–25 give 258–264 px. Earlier frames are partly covered by fingers (240–250 px, low
  reliability). Motion blur inflates frames 26–31 to 265–280 px.
- **Mask PCA length** is 564–610 px. It includes the end ellipse and finger notches, so don't use it as the tube length.
- **Tube motion** (left_end_x, px per frame):
  - Frames 0→1: +2. Frames 1→10: +12 to +18. Frames 10→20: +20 to +40, roughly accelerating. Frames 20→26: +28 to +64.
  - Frames 26→32: about +75 to +104 in x and +50 to +180 in y. The path turns down-right after leaving the arm, at about
    50–60° below horizontal by frames 28–32.
  - While on the arm (frames 0–24) the path is nearly horizontal: ctr_est_y 1374 → 1306 → 1318. Most of the early y change is
    the tube rotating slightly and the noisy top edge in frames 0–9.
  - For an "annotator style" reference point, use left_end_x for x, or ctr_est for 2D position.
- **Holder (frame 35, from edge profiles):**
  - Suction cup: x 1451–1740 (diameter about 290 px), top y 905.
  - Horizontal arm: base left edge x 1516 to end-plate outer face x 2339 (823 px). Visible arm band y 1291–1418.
  - End-plate: x 2326–2339, y 1233–1434 (about 200 px).
- **Tiles:**
  - Width: 1550 / 1629 px (top row), 1608 px (middle row), 1547 / 1630 px (bottom row).
  - Height: 1046–1091 px. It grows from left to right because the lower grout line slopes from y 1733 to 1772.
  - So the scale varies by a few percent across the frame (uneven tiles or lens). The tube and holder sit near the frame centre.

## Reliability and ambiguities
- **Occlusion:** the hand covers the tube's right end in every frame, so the mask centroid and bbox understate the tube. Use the
  left end and the 555 px length.
- **Holder hidden:** the tube hides part of the holder arm until frame 24. Holder sizes come from the clean frame 35.
- **Motion blur:** strong in frames 27–33. Edge positions there are uncertain by about ±10–20 px. The frame-29 bottom edge is
  probably inflated by blur.
- **Depth:** the tube is a few cm in front of the wall, while the tiles are on the wall. Under the single-scale planar convention
  this is ignored, but it means tile-based and tube-based scales are not identical.
- **Hand:** the hand mask includes the forearm and is truncated by the image edge, so its bbox and centroid describe only
  the visible part. Use leftmost_x (the fingertips) for a hand position.
- **Shadows:** there are soft shadows of the holder and hand on the wall. They are neutral grey, so they're excluded from the
  tube mask.
- **No other moving objects.** There's only one tube and one holder, so similar objects can't be confused.
