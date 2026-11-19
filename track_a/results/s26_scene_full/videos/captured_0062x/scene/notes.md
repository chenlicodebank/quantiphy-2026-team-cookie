# captured_0062x – measurement record

Lab video (Orbbec, 24 fps, 1280x720, 49 frames, t = frame/24), SAM2-segmented: everything except five
objects is black. Watermark "Modified with Segment Anything 2 Demo" sits at bottom right (x>=1030, y>=690).
3D scene; camera static, oblique view down onto the floor (image-up = farther away). Lab intrinsics per the
benchmark: f = 0.5959 x 1280 = 763 px, principal point about (640, 360). No metric scale was guessed.

## Files
- `scene.json` – inventory, camera, static-object summary, board pixel sizes at key frames, events.
- `tracks/white_board.csv` – one row per frame (0-48) for the only moving object:
  `cx,cy` = centroid of the visible mask (use as the "visible centre"); `rect_cx/cy, length_px, width_px,
  angle_deg` = min-area rectangle of the mask (long axis, short axis, angle in degrees, image y down);
  `bbox_*` = axis-aligned box; `quad_*` = 4-corner perspective outline fitted to the convex hull (FL/FR = far-left/far-right
  corners, NL/NR = near corners, "x;y"), with its centre and the four edge lengths (far/near edge = the board's long
  sides, left/right = its short sides); `area_px`; `truncated_by_frame_edge`; `occluded` (always 0, nothing
  covers it).
- `static.json` – the four static objects at frame 47: centroid, bbox, min-area-rect length/width/angle, area.
- `scripts/track.py` (segmentation, tracking, overlays), `scripts/steps.py` (per-frame step check), `scripts/probe.py`.

## Objects
- **white_board** (moving): flat white rectangular board/tray with two small grey knobs on its far corners.
  At rest frames 0-15, starts moving at frame 16 (t=0.667 s), slides away from the camera toward the upper left
  (image path from about (959,631) to (548,278)), still moving at frame 48. Apparent size shrinks with distance:
  min-rect length 333 px (frame 20) -> 206 px (frame 48), width 178 -> 88 px; the near long edge 306 -> 194 px,
  far long edge 240 -> 165 px. Its orientation stays about 13 deg (long axis falling to the right).
- **blue_bin** – blue confetti-pattern waste bin, top left, centroid (337.5,156.3), bbox 91x100 px.
- **blue_tote_bag** – blue tote bag with pink round logo, lying flat, centroid (837.3,329.2), bbox 125x77 px.
- **small_white_box** – small printed white carton, centroid (516.7,495.5), min-rect 68.7x30.7 px. It is white like the
  board but much smaller and does not move.
- **teddy_bear** – brown teddy bear lying down, centroid (635.0,623.8), bbox 113x86 px.
All static centroids move by less than 1 px over the clip, which confirms the camera is static.

## Events
Rest 0-15; motion starts at 16; near edge enters the frame fully at 20; the largest image step is about 25.6 px/frame
at 21; the step falls to about 16 px at 25-26, rises again to about 20 px at 28-29, then decays to 12.3 px at 48.
Frame 35->36 shows a double step (31 px, against about 15 px for neighbours), which looks like a dropped frame in the recording.
Treat it as two frame intervals, or smooth over it. The board passes left of the tote bag (frames 36-40)
without touching it. No bounce or impact.

## Reliability / ambiguities
- Mask: thresholding on white is clean, and overlays (frames/ov_*.png) confirm it covers the full board. Centroid noise is
  about 0.3 px at rest.
- Frames 0-19: the near part of the board is cut by the image bottom (and in frames 0-~19 a little by the grey
  watermark box). The centroid, bbox, length/width and near edge are biased there (the centroid sits too far
  up). Use the far edge or the far corners FL/FR for position and size in those frames, or use frames >= 20.
- The quad corners are approximate (±3-5 px): the corners are rounded and carry knobs.
- The board is a rigid flat object on the floor. Its true centre lies a little nearer the camera than the mask
  centroid would suggest under strong perspective, but the effect is small at this size.
- For metric work, use the given depth_info with f = 763 px. Pixel size scales roughly as 1/depth (length ratio
  333/206 = 1.62 from frame 20 to frame 48).
