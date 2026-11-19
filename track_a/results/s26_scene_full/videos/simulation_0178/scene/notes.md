# simulation_0178 – measurement record

2D simulation scene (Blender render), 1920x1080, 24 fps, 60 frames (t = 0 … 2.458 s). Static camera, side view.
Two elephants walk left to right across a meadow in front of trees and a sea horizon. All values are in full-resolution
pixels (x right, y down) and seconds. No metric scale is assumed.

## Files
- `scene.json`: inventory (moving and static objects), summary positions/extents, separation, events, camera.
- `tracks/elephant_big.csv`, `tracks/elephant_small.csv`: one row per frame (0–59). Columns:
  frame, time_s, bbox_cx/bbox_cy (bbox centre), centroid_x/centroid_y (mask centroid, **recommended reference point**),
  bbox_x0,y0,x1,y1 (full mask incl. tail, trunk, tusks), length_px (horizontal extent = main axis), height_px,
  area_px, body_centroid_x/y and body_x0..y1 (mask after a 25 px disk opening, which removes tail, trunk tip and tusks),
  occluded (always 0).
- `scripts/bg.py`: camera-stability check (phase correlation) and a first background attempt (its masked-median
  background was not used). The .npy background files the scripts write were deleted to keep the record small.
- `scripts/segment.py`: background from frames where a pixel is outside rough moving boxes, then segmentation
  (|frame − background| summed RGB > 22 after 3x3 blur, open/close, split between the two elephants by a moving vertical line).
  Writes tracks and overlays (frames/seg_XX.png, not part of the record).
- `scripts/stats.py` → `scripts/stats_out.json`: summary displacements, path lengths, extents; static-object pixel rows.
- `scripts/summ.py`: prints per-frame series.

## Main numbers
- elephant_big (front/right, larger): centroid (817.4, 574.7) at f0 → (1228.5, 583.4) at f59; net dx 411 px; path 413 px;
  mean step 6.99 px/frame (linear fit 6.88). Full length (tail tip to trunk/tusk) median 404 px (353–428), height 230 px
  (221–236, top of head/back to feet); body-only length ~320 px, height ~228 px.
- elephant_small (behind/left, smaller): centroid (473.0, 616.1) → (833.3, 611.3); net dx 360 px; path 362 px;
  mean step 6.13 px/frame (fit 6.13). Full length median 272 px (254–291), height 156 px (147–161); body-only length ~211 px.
- Height ratio big/small ≈ 1.47; length ratio ≈ 1.48. Both share the same ground line (feet y≈693–696) → same depth,
  one scale applies to both.
- Gap small-front to big-rear bbox: 12 px at f0 → 69 px at f59 (big is faster). Centroid separation 344 → 395 px.
- Static: left foreground trunk x≈65–205 (≈140 px wide); right background trunk x≈1444–1510 (≈65 px, low contrast);
  horizon/sea line y≈640; grass back edge y≈690–700.

## Events
Both elephants walk the whole clip (already moving at f0, still moving at f59). No starts/stops, contacts or direction
changes. Per-frame centroid steps oscillate with the gait (≈4.5–7.6 px/frame small, ≈5.6–8.8 px/frame big).

## Reliability / ambiguity
- The simulation origin of an animal rig is not visible; the mask centroid is the best proxy (body centroid differs by
  ≤ ~8 px vertically, < 6 px horizontally). For speeds, a linear fit or multi-frame difference of centroid_x is much
  more robust than one-frame differences (single-frame step noise ±1–2 px from leg/trunk motion).
- Mask edges: good against sky/sea (±1–2 px). Against dark foliage (big elephant's back/head late in the clip, both
  heads near the end) contrast is low: top edge may be off by ~5 px, and the big elephant's centroid_y drifts ~+9 px over
  the clip partly from head lowering and partly from this. Thin tusk tips are sometimes lost for a frame
  (e.g. small f21–23, big f9, f12–13 show dips in bbox_x1/length_px) – use the median extents, not single frames.
- Full length includes the swinging tail and trunk, so it varies ±20 px with gait; body length is steadier.
- No occlusion between elephants (they never overlap) or by scenery. No shadows on the ground were significant
  (feet sit on the grass edge).
