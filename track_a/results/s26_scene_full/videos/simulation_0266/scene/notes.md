# simulation_0266 — measurement record

2D simulation (Blender), 2560x1440, 24 fps, 72 frames (t = frame/24). Top-down view of snowy mountain
terrain. **One moving object: a black snowmobile** (nose pointing left) that starts at rest and speeds up
in a straight line toward the left (-x) at constant image row y ≈ 719.5. Camera static.

## Files
- `scene.json` – inventory, pixel sizes, events, camera.
- `tracks/snowmobile.csv` – one row per frame 0-71:
  - `cx_bbox, cy_bbox` bbox centre of the segmentation mask; `cx_mask, cy_mask` mask centroid;
  - `x0,y0,x1,y1, bbox_w, bbox_h` bbox; `len_main_axis, width_across, angle_deg` from minAreaRect (main axis = x);
  - `area` mask px; `occluded_or_cut` = 1 when the vehicle touches the image border or is in the glitch (61-71);
  - `rear_x` rear (right-most) edge; **`cx_est, cy_est` = recommended reference point (vehicle origin)**,
    `cx_method` how it was obtained.
- `scripts/` – bg.py (median background + camera-shift check, cam_shift.json), track.py (segmentation),
  rear_edge.py (rear edge + centre after the nose leaves the frame), draw_track.py (check images).

## How measured
- Background = frame 66 for x≥1000 and frame 0 for x<1000 (vehicle absent there). Mask = max-channel
  |frame − bg| > 40, open/close, largest component, holes filled. Overlays (frames 0, 6, …, 60, 66, 68) were
  inspected: masks follow the full silhouette incl. front ski tips and rear fins; no shadow included.
- Frames 0-60: whole vehicle visible; reference = bbox centre (±1 px).
- Frames 61-71: nose cut by left border. cx_est = rear_x − offset, offset = linear fit of (x1 − cx_bbox)
  over frames 40-60 (370.4 px at frame 60 → 363 px at 71). Frames 67-71 contain a render glitch (soft white
  blob over the left of the image) that inflates the mask ~20 px, so rear_x there uses dark pixels
  (gray<90). cx_est for 61-71 is extrapolated: maybe ±3 px; cx_bbox/x0 in those frames are NOT the centre.
- Static landmarks measured by eye on zoomed grid crops (±10 px).

## Key numbers (pixels)
- Snowmobile silhouette length (along motion, x): 785-787 px at frames 0-9, slowly falling to 740 px at
  frame 60 (≈ −0.75 px/frame; probably perspective of the 3D model, since the width stays constant).
  Width across: 365 ± 2 px (y 536-902). If a question gives the vehicle length, the measurement at the frame in
  question (or the mean ≈ 770 px over 0-60) sets the m/px scale; the spread is ±3 %.
- Positions: cx_est 1995.5 (f0) → 399.0 (f60) → −245 (f71, extrapolated; centre beyond the left edge).
  Per-frame step grows roughly linearly (~1 px at frame 2, ~25 px at f28, ~53 px at f60, ~61-63 px at f67-71),
  consistent with uniform acceleration from rest beginning at frame 1. Small noise (±1-2 px) in the per-frame
  step from the bbox edges; smoothing over a few frames is recommended for pixel speeds/accelerations.
- Events: rest frames 0-1; motion starts at frame 1 (t=0.042 s); nose touches left border at frame 61
  (t=2.542 s); no bounces, impacts or direction changes.
- Static: small rock with shadow ~x 1850-1965, y 1210-1290; central rock ridge x ~950-1200; right rock ridge
  x ~2050-2500; dark slope top-left.

## Reliability / ambiguity
- Only one moving object, no similar objects. Camera shift < 0.05 px (static).
- Apparent length changes ~6 % across the clip; width does not. Treat the scene as planar (2D) with one scale.
- Frames 67-71 render glitch: rear edge still clear; centre extrapolated.
