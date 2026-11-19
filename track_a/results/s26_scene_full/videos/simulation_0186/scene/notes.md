# simulation_0186 — measurement record

3D Blender render, 24 fps, 40 frames (t = 0 … 1.625 s), 1920×1080. All values are in pixels and seconds. No metric scale is assumed.

## Scene
A white gift box with a yellow ribbon and bow falls vertically, starting near rest at frame 0. It lands on a blue inclined slide (roller-conveyor ramp) and then slides down and to the right, speeding up, toward a wooden floor in the lower right. The camera is **static**: the wall patch shift is ≤0.01 px in every frame. The gift box is the only moving object. Static items:
- a brown "PRODUCT OF ROME ITALY" cardboard box (top left)
- a "SEEDLESS JAFFAS" wooden crate and a shelf board at the top of the ramp
- a blue support post
- the blue ramp
- an orange "TAKE CARE WHEN STACKING CRATES" sign
- the wooden floor
- the grey block wall

The inventory, pixel extents, events and perspective cues are in `scene.json`.

## Files
- `scene.json`: inventory, static extents, camera, events.
- `tracks/gift_box.csv`: one row per frame (0–39) with these columns:
  - `body_cx, body_cy`: **recommended reference point**. This is the centroid of the convex hull of the white paper panels (bow and ribbon pixels removed), which is the best estimate of the projected box centre/origin.
  - `body_x0..y1, body_area`: hull bbox and area.
  - `cx, cy`: centroid of the full silhouette including the bow. It sits about 6 px above the body centre.
  - `bbox_*`: full silhouette bbox, including the bow.
  - `mask_len_main / mask_wid_across / main_axis_deg`: PCA extents of the silhouette. The box looks nearly square, so the axis angle is unstable and should not be read as rotation.
  - `cam_dx, cam_dy`: background shift relative to frame 0.
  - `occluded`, `truncated_by_frame_edge`.
- `scripts/track_gift.py`: segmentation by difference to a median background (frames 0, 8, 16, 24, 32, 39), threshold 40, morphology, largest blob; also does the paper hull and the camera check. It writes overlays to `frames/ov_XX.png`.
- `scripts/body_centre.py`: prints per-frame displacements, used to find events.
- `scripts/static_objects.py`: colour-mask extents of the post, the ramp and the ramp far-edge line.

## Key measurements
- **Free fall, frames 0–8:**
  - x stays at about 554 px.
  - The body centre falls from y = 394.3 (frame 0) to 515.5 (frame 8).
  - Per-frame dy: 1.9, 5.7, 9.7, 13.3, 17.3, 20.9, 24.4, 28.1. That is a constant increase of about 3.7 px/frame², so the box starts near rest at t ≈ 0.
- **Impact on the ramp:** between frame 8 (t = 0.333 s) and frame 9 (t = 0.375 s). There is no visible bounce.
- **Sliding, frames 9–39:**
  - Displacements point along the ramp (dy/dx ≈ 0.6; the ramp far-edge line in the image has slope 0.606).
  - The per-frame step grows from 11.8 px to 54.7 px.
  - At frame 39 the body centre is at (1363, 1014).
- **Apparent size:**
  - Frame 0, silhouette bbox: 144 × 139 px with the bow, 144 × 121 px for the body.
  - The body hull area grows from 11229 (frame 0) to 13146 (frame 38), about 8% in linear size. The box comes slightly toward the camera as it slides, so pixel speeds late in the slide are inflated by perspective.
  - The box is a near-cube tilted about 20–30° in the image, so the bbox is larger than a single face edge. Following the reference convention (world axis-aligned bbox), the projected bbox (`body_x1-body_x0`, `body_y1-body_y0`) is the closest pixel proxy.

## Reliability and ambiguities
- **Centroids:** about ±1 px. Overlays were checked at frames 0, 6, 12, 24, 36 and 39, and the masks follow the box outline closely. There is no shadow and almost no motion blur.
- **Frame 39:** the bottom of the box is cut by the image edge. The bbox and centroid there are biased upward by a few px. Use frame 38 for sizes.
- **Origin vs. silhouette centroid:** the origin of the Blender object is assumed to be the box-body centre. If the origin includes the bow, use `cx, cy`, which is about 6 px higher.
- **Static extents:** values read visually from a grid (crate, cardboard box, sign, floor) are ±5 px. Objects cut by the frame edges are noted in `scene.json`. The colour mask for the sign was broken up by its lettering, so the sign extent comes from the grid image: 215 × 212 px, centre (1570, 684).
- **Depth:** no camera distances are known here. For 3D questions, combine the given depth_info with the pixel sizes and positions above to estimate the focal length.
