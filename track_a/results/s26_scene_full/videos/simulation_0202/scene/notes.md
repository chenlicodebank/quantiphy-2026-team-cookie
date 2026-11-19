# simulation_0202 – measurement record

3D Blender render, 2124x1080, 24 fps, 30 frames (t = frame/24, 0 … 1.208 s). Static camera, elevated,
looking slightly down at an antique desk in a dark blue room. **One moving object: a magnifying glass** that falls
from the top of the frame onto the desk top, bounces and settles. Everything else is static.

## Files
- `scene.json` – inventory (all objects, distinguishing features, pixel bboxes at frame 29), camera, events.
- `tracks/magnifying_glass.csv` – per frame 0-29: `ref_x, ref_y` = bbox centre (preferred reference point),
  `mask_cx, mask_cy` = mask centroid, bbox (x0,y0,x1,y1,w,h), `len_major`/`width_minor`/`rect_angle` = min-area
  rectangle of the mask (length along main axis, apparent thickness/height across it), mask area, occlusion flag
  (0 everywhere), phase (falling / impact / bounce / settling / rest).
- `scripts/` – `diff.py` (frame differencing), `track.py` (segmentation + overlays; writes frames/rows.json),
  `write_track.py` (CSV), `other_changes.py` (camera-stability check), `draw_static.py` (static bbox check).

## How measured
Background = frame 0 with its top strip (y<60, where the glass hangs at f0) replaced by frame 29. Mask = per-pixel
colour difference > 30, open 3x3 / close 7x7, largest component plus nearby pieces. Overlays of frames 0, 8, 11, 12,
14, 29 were inspected: the box covers the full object (lens rim to handle end) in all of them.

## Magnifying glass (moving)
- Start f0: horizontal, lens on the left, handle pointing right; bbox (1263,9)-(1450,30), centre (1356.5, 19.5).
  Apparent length 187 px, lens-ring horizontal diameter ≈82 px (ring spans x≈1263-1345, lens centre ≈ (1304, 20)).
- Falls nearly straight down (x drifts left only ~14 px). Vertical bbox-centre positions: f0 19.5, f1 25.5, f2 42.5,
  f3 70.5, f4 109.5, f5 159, f6 218.5, f7 287.5, f8 366.5, f9 455, f10 551.5 … per-frame drop grows by ~10-11 px
  each frame (6, 17, 28, 39, 50, 59, 69, 79, 89, 97) → released from rest at about frame 0.
- Impact on desk at f11 (t = 0.458 s; contact between f10 and f11). Bounces/tilts f12-f17 (highest rebound f15,
  bbox top y=613), lies flat again f18, small rocking to f23, at rest f24-f29: bbox (1249,655)-(1423,701), centre
  (1336, 678); lens ring spans x≈1250-1334 (lens centre ≈ (1292, 672)).
- Apparent size vs time: length 187 px at top → ~175 px on desk (slight shrink = farther from camera / foreshortened);
  apparent thickness grows 21 → 39-47 px because the camera sees the lens face more from above as it drops
  (ring minor/major ≈0.11 at y≈20, ≈0.22-0.27 on the desk). Camera eye height therefore lies roughly at the level
  of the glass's start position; horizon near the top image edge.
- Reference point: the Blender origin of the glass is unknown (could be the lens centre or the whole-object centre).
  `ref_x/ref_y` (bbox centre) is the whole-object centre; the lens centre is ≈ bbox_x0 + 42 px horizontally while
  the glass lies flat (falling and rest phases). Vertical motion is identical for both choices during the fall.

## Reliability
- Falling track f0-f11: ±1-2 px (crisp edges, plain wall background; mild motion blur at f9-f11).
- Bounce f12-f17: ±3-5 px; the transparent lens interior and dark parts of the ring against the dark desk are
  partly missing from the mask, so the mask centroid is biased toward the handle – use bbox centre.
- Rest f24-29: ±1 px. Mask area is not a size measure (lens interior excluded).
- Static bboxes in scene.json: read from a 100 px grid on frame 29 and checked by overlay, ±5-10 px.
- Camera: static; outside the glass only ~0.1% scattered pixels change (render noise). No shadow of the glass is
  clearly visible on the desk.

## Ambiguities
- No depth information here; for 3D distances use the given depth_info and a focal length estimated from it.
- Several paper cards and two chairs: distinguished by position in scene.json. Unidentified blurred orange/brown
  objects cut off at the right and bottom image edges.
