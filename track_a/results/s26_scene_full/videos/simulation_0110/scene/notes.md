# simulation_0110 – measurement record

Scene: 3D Blender render, 1920x1080, 24 fps, 72 frames (t = frame/24). Two identical red blood cells
(red biconcave discs seen obliquely from slightly above) on a flat uniform grey background (BGR 206).
Nothing else is in the scene: no ground plane, horizon, markings or static objects.

## Files
- `scene.json` – inventory, camera, events, summary numbers.
- `tracks/cell_left.csv`, `tracks/cell_right.csv` – one row per frame (0–71) per cell:
  `cx,cy` mask centroid (reference point = cell centre / origin), `bbox_cx,bbox_cy` bbox centre,
  `x0,y0,x1,y1,bbox_w,bbox_h` bounding box (px, inclusive), `mask_len,mask_wid,mask_angle` min-area
  rectangle (long axis is horizontal in the image = the disc diameter; the short side = projected
  thickness+tilt of the disc), `area` (px), `touches_edge`, `occluded` (always 0),
  `rel_depth_area` = sqrt(area0/area) ≈ Z(i)/Z(0), `rel_depth_len` = len0/len, `u_minus_cx0, v_minus_cy0`
  = centroid offset from assumed principal point (960,540).
- `scripts/track.py` (segmentation + tracks + check images), `scripts/augment.py` (relative-depth columns),
  `scripts/analyze.py` (summary printout). Check overlays were in `frames/check_*.png`.

## Method
Colour threshold (R−G>40 and R−B>30), 5x5 closing, connected components >200 px, sorted left→right.
Overlays at frames 0, 35, 71 confirmed the contours follow the full cell outline (including the lighter
upper rim) and the centroid sits at the cell centre. Cells never touch or overlap, never leave frame.

## Findings
- Camera static (background uniform and constant; nothing to pan against).
- Both cells are motionless from frame 0 to frame 1; motion starts at frame 1 (t=0.042 s) and continues
  smoothly to the last frame. No bounce, contact or direction change.
- Both cells recede from the camera at the same constant rate: relative depth from apparent size is linear,
  Z/Z0 ≈ 0.9858 + 0.01505·frame (frames 1–71, residual < 0.004), reaching ≈2.05 at frame 71. Apparent
  size halves: bbox width 330→164 px (left), 328→160 px (right); bbox height 182→86 / 180→86.
- Image motion: left cell centroid (816,585)→(627,503) – left and up; right cell (1185,585)→(1162,517) –
  mostly up. Per-frame image step shrinks over time (as expected for a receding object).
- Centroid pixel separation 368.5→535.4 px; since both cells are at equal depth, world separation ∝
  separation·Z: grows from 368.5 to ≈1099 "frame-0 pixels" (≈3x) – the cells move apart in 3D.
- Since both cells share depth and size at every frame, any size prior on one cell transfers to the other.

## How to get metric values (in the answering session)
Back-project: X = (u−960)·Z/f, Y = (v−540)·Z/f, with Z from depth_info (origin distance) and
f from depth_info + a known size (e.g. f ≈ bbox_w·Z/diameter, using the cell's horizontal extent ~ its
diameter). Relative depth columns give Z(i) at other frames from one given depth. Note depth_info is
camera-to-origin Euclidean distance, not Z; correct with sqrt(1+((u−960)²+(v−540)²)/f²).

## Reliability / ambiguities
- Centroids ±0.3 px (per-frame differences are noisy at the ~0.2 px level late in the clip; smooth if needed).
- The mask centroid of an obliquely viewed disc is a good proxy of the origin but may differ by a few px
  vertically from the true projected centre (shading/rim visible on the upper face). bbox centre agrees
  with the centroid within ~1–2 px.
- Mask height in the image mixes disc thickness and tilt; it is not the world height. The horizontal
  extent (bbox_w ≈ mask_len) best represents the disc diameter. Soft anti-aliased edges: extents ±1–2 px.
- Relative depth from area assumes no rotation; cell shape appears constant (aspect ratio ~1.8–1.9 throughout).
- Principal point (960,540) assumed; focal length unknown.
