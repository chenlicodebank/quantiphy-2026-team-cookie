# captured_0015 - measurement record

Lab clip (24 fps, 73 frames, 1280x720, labelled 2D). A person stands still at the left of the image and tosses a
small plush toy (brown/orange, white face/paws, striped tail) straight up twice, catching it with both hands each
time. The camera is static. The background is artificially blurred (SAM2 demo watermark at bottom right); the
person and toy are sharp. All values are in pixels and frames/seconds (t = frame/24). No metric scale was assumed.

## Files
- `scene.json`: inventory, size summary, static objects, events, camera.
- `tracks/toy.csv`: toy track for all 73 frames. **Use `best_cx, best_cy`** (visible centre). Other columns:
  `best_x0..y1, best_w, best_h` (bbox), `best_len/best_wid/best_axis_deg` (mask extent along/across its PCA main
  axis, axis angle in image degrees, about 90 = vertical), `method` (diff / diff_win / colour), `contact`
  (held / release_contact / free / catch), `occluded` (1 = partly hidden by hands or merged with them).
  `core_cx, core_cy` = centroid of dark-brown fur pixels only (consistent across all frames, but biased toward the
  brown body, a few px below the true centre). `col_*` = colour-mask measurements (warm saturated pixels clipped to
  a 70x100 window around the core when merged with skin; `col_merged`=1).
- `tracks/toy_flight_diffmask.csv`: raw background-difference masks for frames 14-23 and 48-60 (with flag for
  frames where the mask is merged with an arm, those rows are not toy-only).
- `tracks/person.csv`: per frame `head_top_y`, `feet_bottom_y`, `height_px` (top of hair to bottom of shoes),
  plus a sharpness-mask bbox (`bbox_*`, `mask_c*`), which is NOT a full-body box (it misses the low-texture
  trousers/shoes below y~500; ignore its bottom edge). `trouser_*` columns are unreliable (dark background pixels).
- `tracks/camera_shift.csv`: phase-correlation shift of the background vs frame 0.
- `scripts/`: probe.py, toymask*.py (diagnostics), track_toy.py (colour tracking), bgdiff.py, finalize_toy.py
  (final toy.csv), person.py, person_extent.py, camera.py, cropsheet.py.

## Methods
- Toy, free in the air (frames 17-21, 53-58, method `diff`): per-pixel median background of the region over all
  frames, |frame - background| > 28 -> mask component at the toy. Captures the whole toy including the white
  parts. Checked visually on overlay sheets: masks cover the full toy and nothing else.
- Toy near the hands (15, 16, 22, 51, 52, 59, method `diff_win`): same mask clipped to a toy-sized window around
  the fur core. Reliable to a few px.
- Toy held / being carried (other frames, method `colour`): colour mask of the fur, clipped around the core;
  centre ~±5-10 px (fingers cover part; white face missed). Frames 12-14, 23-28, 46-50, 60-62 are strongly
  motion blurred. Frame 23 (catch): by eye the blurred toy spans about x 420-470, y 205-300 (centre ~(445,250)),
  while the table gives (438,268): treat as ±15 px.
- Toy size (free flight, full mask): toss 1 bbox 49-61 w x 98-102 h; toss 2 53-58 w x 101-107 h. The width
  changes with rotation (tail sticks out sideways in frames 18-21). A good single value is about 103 px tall x
  57 px wide (main-axis length ~100-107 px). Blur makes the bbox of moving frames longer along the motion.
- Person: head top = first dark (hair) row above the head; feet bottom = lowest row where the shoes differ from
  the floor. Height 507 ± 1 px (y 134.5 -> 641) in every frame; she does not move her feet. Torso/trouser x about
  285-405, shoes about 305-400; approximate image centre (350, 388), pelvis roughly (350, 345) by eye.
- Camera: static (max |shift| 0.5 px).

## Motion summary (pixels, for orientation only)
- Toy at rest at waist, frames 0-8, centre about (421, 365-369).
- Toss 1: rises from frame 9, release ~15 (y ~223), free 16-22, apex frame 19 (y 175.7), catch ~23, carried down
  to the lowest point ~frame 31 (y ~374), small bob 33-41 (up to y ~344 at 36).
- Toss 2: rises from frame 43, release ~50 (y ~218), free 51-59, apex frame 55 (y 149.1; 54: 149.5), catch ~60,
  back at waist ~66-72 (y ~352).
- Horizontal motion of the toy is small (x 413-449); the motion is essentially vertical.
- Free flight is short (7-9 frames), so a fitted parabola uses few points; the y positions in `diff` frames are
  good to ~1-2 px.

## Ambiguities
- Release/catch frames are ±1 frame (hands stay close to the toy).
- The scene is labelled 2D; one px scale should hold for the toy and the person (the toy is roughly at the
  person's depth, slightly in front of her). If a depth is given, use f = 763 px.
- Only one toy, one person; no other moving objects. The background stands/TV/panels are blurred, so their
  positions in scene.json are approximate (±10 px).
