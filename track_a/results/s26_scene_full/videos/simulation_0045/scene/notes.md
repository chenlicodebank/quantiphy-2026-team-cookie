# simulation_0045 — measurement record (pixels, seconds)

Blender render, 3D scene, 1920x766, 33 fps, 99 frames (t = frame/33, 0 … 2.970 s). Static camera.
A city street runs away from the camera. A **cyclist** (dark jacket, blue bike, on the road) and a **pedestrian**
(white T-shirt, light jeans, on the right sidewalk) both move straight away from the camera for the whole clip.
Nothing else moves.

## Files
- `scene.json`: inventory (moving + static objects with pixel extents), camera info, events, file list.
- `tracks/cyclist.csv`, `tracks/pedestrian.csv`: one row per frame 0–98. Columns:
  - `frame, time`
  - `ref_x, ref_y`: reference point = estimated **pelvis** (pedestrian: hip-joint level; cyclist: rider's pelvis on the saddle).
    x = median x of the torso band (15–40 % of height below the head top); y = head_top_y + k·height_smooth_px,
    k = 0.47 for the pedestrian (hip joint ≈ 53 % of stature above the soles), k = 0.44 for the rider (saddle top measured at
    ≈ 0.47·h below the head top in a zoom of frame 30; pelvis just above).
  - `head_top_x, head_top_y`: top of the head (centre x of the top 8 % of the mask).
  - `ground_x, ground_y`: lowest mask point row (pedestrian: lowest foot; cyclist: bottom of the rear (nearer) wheel = ground contact).
  - `bbox_x0, bbox_y0, bbox_x1, bbox_y1`: mask bounding box (inclusive).
  - `height_px` = bbox height (head top to lowest point); `height_smooth_px` = smooth fit (1/h quadratic in frame) — use it
    for sizes; it removes the gait wiggle and fills in the truncated cyclist frames 0–4.
  - `width_px` = bbox width; `torso_width_px` = shoulder/torso width (2–98 percentile of x in the torso band; reliable).
  - `mask_cx, mask_cy, area_px`, `occluded` (always 0), `truncated_by_frame_edge` (cyclist frames 0–4: rear wheel cut by the bottom edge).
  For upright figures the main axis is vertical: length along the main axis = height_px, width across = width_px/torso_width_px.
- `tracks/*_mask.csv`: raw mask statistics from `seg.py`.
- `bg.jpg`: median background (camera static, movers removed).
- `scripts/`: `bg.py` (median background + camera-shift check), `seg.py` (segmentation/tracking), `finalize.py` (reference
  points, smoothing of heights, step events, vanishing points, check for other motion), `overlay.py`/`tile.py`/`plot_series.py`/
  `crop.py`/`dbg.py` (visual checks), `check_record.py`, `shrink_bg.py`.

## How measured
Background subtraction against a median of every 3rd frame. Cast shadows (to the right / up-right of each figure on the
ground, and on the railing/hedge for the pedestrian) were suppressed by a brightness-ratio + chromaticity test, applied only
below mid-height for the cyclist (his dark jacket over the white phone booth otherwise looks like shadow) and below the head
for the pedestrian (light jeans need a low threshold of 16). Contours and boxes were drawn on frames 0–98 (every 10th) and
checked by eye: head tops, feet/wheel bottoms and left edges hit the figures; reference points sit at belt/hip level
(pedestrian) and on the saddle (cyclist).

## Reliability
- Camera: static (≤ 0.015 px shift). No other motion anywhere (residual foreground = 0 outside the two movers).
- head_top_y, ground_y, bbox_x0: ±2 px. ref_x: ±2 px. ref_y: depends on the pelvis-fraction assumption (±0.03·h ≈ ±10 px near,
  ±5 px far); the frame-to-frame changes are much better than that because the same fraction is used throughout.
- bbox_x1 / width_px: the right edge can include residual shadow (pedestrian frames ≈ 0–30 next to the hedge; cyclist a few
  px of wheel shadow). Prefer torso_width_px for widths.
- Pedestrian height_px oscillates ±10 px with the walking gait (head bob and stride); the lowest point switches between feet
  (step transitions ≈ frames 9, 26, 43, 61, 78, 95, i.e. ~17 frames ≈ 0.52 s per step). For max/min walking height use the
  raw height_px; for rest height use height_smooth_px (≈ standing height in px at that depth).
- Cyclist height = head top to rear-wheel bottom (rider + bike, ≈ total height of the rig). Frames 0–4 truncated
  (frame 0 visible 437 px, estimated full 468 px).
- Apparent size shrinks steadily: cyclist 468→145 px (×3.2), pedestrian 353→251 px (×1.41) — both move away from the camera
  (along the street), the cyclist faster.

## Perspective / 3D
- Street vanishing point ≈ (585, 200) ± 25 px (curb lines meet at (586,194); the cyclist and pedestrian head paths extrapolate
  to (580,208) and (609,215)), so both move almost parallel to the street axis, straight away from the camera.
  The road rises to a crest near y≈350, so the true horizon is not visible; verticals appear vertical (no roll, little tilt).
- Focal length unknown. With given depth_info d (camera→origin) for a mover at two times and a known size S:
  f ≈ h_px·d/S (for a size facing the camera); back-project pixel (u,v) with principal point ≈ (960, 383):
  ray = ((u−960)/f, (v−383)/f, 1), position = d·ray/|ray|. Check f by reproducing the other given depths
  (h_px ∝ 1/depth: cyclist 1/h grows 3.2× over the clip).
- Static references (scene.json): telephone booth 118×288 px (x 795–913, y 114–402) at the far end of the right sidewalk;
  parked cream bicycle with basket on the left sidewalk, ≈127×210 px (x 38–165, y 370–580), seen head-on; two manhole covers
  (near one ≈267 px wide at the bottom edge, far one ≈102 px wide at y≈407). Coordinates of tree, shop sign/door, railing are
  approximate (read off a 100-px grid, ±10 px).

## Ambiguities
- Two people: "cyclist/rider/man on the bike" = dark jacket on the road; "pedestrian/walking man" = white T-shirt on the sidewalk.
  A question about "the bicycle" most likely means the moving blue bike; the parked cream bicycle (left sidewalk) is static.
- Cyclist origin: rider pelvis (ref) vs bike root (near ground_x/ground_y, or between the wheels). Both move together, so speeds
  agree up to perspective; pick per question.
- No events other than continuous motion: no start/stop, no contact, no turn, both visible in all frames.
