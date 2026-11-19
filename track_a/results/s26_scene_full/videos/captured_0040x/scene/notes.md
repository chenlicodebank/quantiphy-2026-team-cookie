# captured_0040x — measurement record (pixels, seconds; t = frame/24, frame 0 at t = 0)

Lab video (3D), 1280x720, 24 fps, 49 frames (0-48, 2.04 s). It went through SAM2 segmentation: everything except the
table, the things on it and the thrown object is black. The watermark "Modified with Segment Anything 2 Demo" is at the
bottom right. The hand holding the object has also been masked out.
Lab conventions: fx = 763 px, principal point about (640, 360). Use the depth_info given with each question to back-project.

## Files
- `scene.json`: inventory (pixel boxes and sizes of the static objects at frame 0), events, camera, size trend.
- `tracks/white_toy.csv`: the only moving object, every frame 0-48. Columns:
  - `cx, cy` = mask centroid (the visible centre; use this as the reference point).
  - `bbox_cx, bbox_cy` = bounding-box centre.
  - `x0 y0 x1 y1` = bounding box (inclusive). `bbox_w, bbox_h` = box width and height.
  - `mask_len_major, mask_width_minor` = side lengths of the minimum-area rotated rectangle (length along the main axis and width across it).
  - `major_angle_deg_minAreaRect` = OpenCV angle of that rectangle. `mask_area_px` = mask area in pixels.
  - `occluded`: 0 = clear, 1 = partly hidden, 2 = mostly hidden. `note` = reason.
- `scripts/`:
  - `track.py`: difference from the per-pixel median background, threshold 40, open/close, keep the component nearest the previous position. Writes `raw_track.json`.
  - `build.py`: writes the CSV and scene.json.
  - `overlay.py`: draws the boxes and centroids on frames for checking.
  - `static_check.py`: camera shift and whether static objects moved.
  - `table.py`: table outline.

## Moving object: white_toy
- **What it is:** a white/cream oblong soft object, capsule or bean shaped (a plush or stress toy). It is the only thing that moves. Its size is unknown here; a question will give it.
- **Motion:**
  - Frames 0-22: held in a hand at the far left, off the table (x ≈ 125-190, y ≈ 460-550). It swings in a small wind-up: down to frame 8, up to frame 12, down to frame 20, then up.
  - Release between frames 22 and 23. Per-frame displacement goes 13 → 33 → 55 → 62 px.
  - Flight to the right in three arcs, with apexes at frame ~28.5 (cy ≈ 332), frame ~36.3 (cy ≈ 358) and frame 45 (cy ≈ 385).
  - Two bounces on the table top:
    - Frame ~33, behind the tape roll and card tent (hidden).
    - Frame 41, right of the white cup (cy 487).
  - At frame 48 it is still visible at the right (cx 1183), coming down.
  - Horizontal image speed after release is roughly 31-51 px/frame (frames 26-32 ≈ 45-51, frames 37-48 ≈ 31-44).
- **Getting closer:** the apparent size grows, so the object moves toward the camera.
  - Width across the main axis: ≈ 36 px in the hand (frames 0-22), 37-40 px in frames 25-30, 39-46 px in frames 34-38, 47-56 px in frames 42-48.
  - Mask area: ≈ 1300 px² in the hand, ≈ 2300-2500 px² in frames 26-29, ≈ 3000-3400 px² in frames 43-46, 5348 px² at frame 48 (blur included).
  - Best pixel-length frames (least blur, long axis near the image plane): frame 29 (major axis 73.7, minor 36.8, box 73x39, axis nearly horizontal) and frames 44-45 (≈ 78-79 x 47-49).
- **Reliability:**
  - Centroids are about ±1-2 px in clear frames.
  - Frames 0-22: the hand cutout takes a bite out of the left/lower-left of the mask, so the centroid is pulled ~2-4 px right and the mask is smaller than the toy.
  - Frames 32, 34 and 35 are partly hidden (tape roll, card tent), so their centroids are biased by several px.
  - Frame 33 is mostly hidden: only a blurred fragment shows, at (630, 483). Do not trust that centroid. The true centre is probably slightly higher and left, near the impact point.
  - Frames 40-41: the segmentation leaves the toy's lower half semi-transparent over the table, so the mask extent is approximate.
  - Fast frames (23-25, 30-31, 39, 47-48) are motion blurred. The major axis and box are stretched along the motion; the minor width is less affected.
  - Frames 36-38: the toy passes just above and in front of the cup's top rim (white on white).

## Static objects (frame 0; boxes are x0, y0, x1, y1 in px; read from zoomed grids, ±2 px)
- **glass_jar:** clear jar with white lid, leftmost on the table. Box [482, 416, 543, 497], 61 wide x 81 tall.
- **tape_roll:** wide translucent tape roll lying flat. Box [551, 437, 629, 484], 78 x 47.
- **card_tent:** playing cards leaned into a tent. Box [663, 417, 712, 500], 49 x 83.
- **white_cup:** tall white tumbler, the tallest object. Box [740, 377, 814, 503], top diameter 74, height 126.
- **flat_cards:** card(s) lying flat in front of the tent. Box [645, 500, 745, 515].
- **dark_card:** navy card or booklet near the table front, with a yellow sticky note at its right end. Box [510, 529, 617, 551].
- **table:** wooden top seen obliquely.
  - Approximate corners: front-left (210, 542), front-right (1138, 588), back-left (~450, 452), back-right (~905, 465).
  - The front edge is about 25-30 px thick.
- **table_leg:** dark pedestal. Box [629, 620, 688, 719], cut off by the image bottom.
- None of these move (static_check.py). The objects all stand on the back half of the table, at roughly similar depths.

## Camera
Static: phase-correlation shift < 0.15 px in every frame. The camera is a little above the table and looks slightly
down. There is no horizon; the black background removes all cues outside the table.

## Ambiguities
- There are two kinds of white object: the toy and the white cup. The track never jumps to the cup (checked on overlays).
- The hand is invisible, so contact with the hand cannot be seen directly. Release is taken from the jump in speed, and from the hand bite on the mask disappearing after frame 22.
- Bounce 1 at frame ~33 is inferred from the turn in the trajectory and is hidden.
- There are no shadows (segmented footage).
