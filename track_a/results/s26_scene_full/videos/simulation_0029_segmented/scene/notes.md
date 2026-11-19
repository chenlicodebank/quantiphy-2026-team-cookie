# simulation_0029_segmented: measurement notes

The video is 960x960 px, 25 fps, 75 frames (t = frame/25, frame 0 at t = 0). It is a 3D Blender render with the background replaced by plain white.
All values are in pixels (x right, y down) and frames/seconds. No metric scale is assumed.

## Content
- **boat**: a red-and-white fishing boat with a red hull, a white stripe, the name "AH805", a white cabin with a red roof, a stern railing and a thin mast whose upper segment is dark. It is seen roughly side-on with the bow pointing left. It is visible in all frames. It moves left at a nearly constant ~2.6 px/frame (body_cx goes from 544.5 to 352.0). Its image grows by +10.5 %: length 159.6 px in frames 0-4 and 176.4 px in frames 70-74. So it is also approaching the camera. It has no vertical image motion; the keel row stays at y 678-683.
- **bird**: a small dark flying bird that flaps its wings. It is visible in all frames. It flies right at ~7.3 px/frame on average, from x 41 to x 581, with a small up/down undulation (y 519-540). Its apparent size shows no trend and changes only with the wing phase.
- There are no static objects, ground, water, horizon or markings, because the background is white. The image therefore has no perspective cues.

## Files
- `scene.json`: inventory, extents, events and camera summary.
- `tracks/boat.csv` (one row per frame):
  - frame, t
  - full bbox including the mast (x0, y0, x1, y1, bbox_cx, bbox_cy, length_px, height_px)
  - `centroid_x/y`: mask centroid of the cabin+hull
  - `body_*`: bbox of the cabin+hull, i.e. the mask at y >= 568 (body_y0 is sometimes 568 because the lowest part of the mast is included; for the cabin top use `cabin_top_y`, the first row with at least 20 mask pixels)
  - `body_len_px`: bow-to-stern length
  - `mast_x`: estimated mast column. The true pole is at mast_x + 2.45.
  - `mast_px_x`
  - `mast_top_y`: top of the mast mask at threshold 12
  - `mast_tip_lowthr_y`: faint tip, threshold 4
  - `full_height_px`: keel to faint mast tip
  - `bird_overlap`
- `tracks/bird.csv`:
  - frame, t
  - mask centroid (cx, cy) and `cx_best/cy_best`: use these; they equal cx/cy except in frames 48-49, where they are interpolated
  - bbox (x0, y0, x1, y1, bbox_w, bbox_h, bbox centre)
  - `main_axis_len` / `across_width`: from the minAreaRect of the mask
  - area
  - `overlap_mast`: frames 47-50
  - `occluded`: frames 48-49
- `scripts/`:
  - `track.py`: segmentation (mask = 255 - min(RGB) > 12) and tracking
  - `postprocess.py`: bird interpolation and summary numbers
  - `overlay.py`, `crops.py`: visual checks
  - `probe*.py`: exploration

## Method and reliability
- **Segmentation.** The background is exactly white, so the masks are clean. The boat body (cabin+hull) is the largest component below y = 568. The mast is a narrow column at 0.44 of the body width from the bow, a ratio measured on clean frames. The bird is the largest remaining blob above the cabin. Overlays on frames 0, 30, 44-53 and 74 confirmed that the boxes cover the full boat and the full bird.
- **Boat x and length.** Reliable to about ±1 px. The bow and stern are crisp, and the dark keel/shadow strip at the bottom is part of the hull mask. The cabin top is reliable to ±1 px.
- **Boat mast height.** Unreliable. The faint white tip of the mast flickers in the segmentation: its top is found anywhere between y 488 and 512, and in frame 52 most of the mast is missing. The dark mast segment's top (~513-516) is stable. Full keel-to-tip height is ~167-187 px (median 170). For boat height, prefer the cabin+hull height (97 px at frame 0, 105 px at frame 74) unless the question clearly includes the mast.
- **Boat reference point.** The boat's origin is not visible. Its likely position is the hull centre, i.e. body_cx with centroid_y or body_cy. All candidates differ only by a constant offset in x, so speeds do not depend on the choice.
- **Bird centroid.** It jitters by ±2-3 px per frame because of the wingbeat: per-frame dx ranges from 3 to 10 px with a mean of 7.3. Fitting over several frames is advisable.
- **Bird size.** Wingspan-like extent is bbox_w: 15-30 px, maximum 30 at frame 31 and 29 at frame 4. Height (bbox_h) is 5-22 px. Minima with the wings level occur near frames 5, 17-18, 32, 42, 57 and 65-66.
- **Bird crossing the mast (frames 47-50).** This is an image crossing only, with no contact. Frames 47 and 50 are clean. In frames 48 and 49 the bird lies partly on the pole, and its pixels inside the ±2.5 px pole strip were removed, so the measured cx is biased by ~4 px (left at 48, right at 49). Use cx_best there.
- **Camera.** It is assumed static, but this cannot be checked against a background. The boat's constant vertical position supports it. The focal length is unknown and must come from each question's depth_info. The principal point is assumed at (480, 480).

## Events
- There are no starts, stops, bounces, impacts or direction changes: both objects move throughout frames 0-74.
- The bird passes over the bow x at ~frame 41, overlaps the mast at frames 47-50 (pole crossing ~frame 48.5, t ≈ 1.94 s), and passes the stern x at ~frame 59.
