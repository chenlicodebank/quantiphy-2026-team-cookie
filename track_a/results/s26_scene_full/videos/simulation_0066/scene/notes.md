# simulation_0066 — measurement record (pixels / seconds only, no metric scale)

Video: 3D Blender render, 2160x1080, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s).
Street intersection seen from an elevated, **static** camera. Background shift measured by phase correlation:
< 0.01 px in all frames, so it is zero.

## Files
- `scene.json`: inventory (moving and static objects), apparent sizes, events, camera and perspective cues.
- `tracks/<object>.csv`: one row per frame (0–71) for `taxi`, `van`, `cyclist`, `pedestrian`. Columns:
  `frame, time_s, ref_x, ref_y, ref_kind` (reference point, see below), `bbox_x0..y1` (inclusive px),
  `bbox_cx, bbox_cy`, `bottom_cx, bottom_y` (bottom-centre of the box, roughly the ground contact),
  `bbox_w, bbox_h`, `mask_cx, mask_cy, mask_area`, `length_px, width_px, axis_angle_deg` (min-area rectangle
  of the mask: long side, short side, angle of the long side in the image, 0 = +x, measured clockwise because y points down),
  `occluded` (1 = partly hidden or overlapping another object in the image), `notes` (why).
- `bg.png`: clean background (median over frames; the parked-van ghost patched from f71).
- `scripts/`: `bg.py`/`bg2.py` (background, camera check), `track2.py` (final segmentation),
  `cyc.py` (hand-read cyclist boxes), `measure.py` (writes the CSVs), `static.py` (static extents),
  `events.py`/`early.py` (motion onset and headings), and viewers (`overlay.py`, `gridcrops.py`, `trajview.py`,
  `shadowview.py`, `ratioview.py`, `diffview.py`, `crops.py`, `comps.py`). `track.py` and `cycspec.py` are earlier attempts and are not used.

## How the tracks were measured
Foreground = |frame − bg| > 25 (max over BGR). The threshold is 12 in the sidewalk band x150–560, y340–520, because the
pedestrian's pale clothes sit on a pale sidewalk. Soft cast shadows are removed: a pixel counts as shadow when its
frame/bg ratio is 0.6–0.95 and the same in all channels. Bumpers and tyres have ratios below 0.55, so they stay in the mask.
Objects are separated by marker watershed, propagated forward and backward from hand seeds at f30, and checked on overlays at
many frames (masks cover the right object and its full body).
- **taxi, van**: `ref` = mask centroid of the visible body. This is the best image proxy for the vehicle origin, but it is
  not the projected 3D origin. The centroid of a car seen from above sits slightly higher in the image than the
  ground-level root; `bottom_y` is the lowest body or wheel point. Box accuracy is about ±3 px; the bottom edge is about ±5 px
  (residual contact shadow under bumpers).
- **cyclist**: touches or overlaps the van in every frame, and the thin bike wheels fall out of the mask, so the **bbox is
  read by hand** from 2–3x gridded crops every 4 frames (`cyc.py`, about ±3 px) and linearly interpolated in between.
  `ref` = box centre (rider + bicycle). `length_px/width_px` are left blank, and `mask_*` contain van pixels, so do not use them.
  The keyframe reading makes the trajectory slightly jittery (±3 px), e.g. f20–f32.
- **pedestrian**: `ref` = pelvis estimate = head top + 0.47 × 103 px, where 103 px is the median box height of
  unoccluded frames (range 95–110). x = the mask centre in that row band. Head top or feet are sometimes lost (pale
  hair/shoes), so box height is ±5 px. The box height varies with the walking stride (legs apart = wider box).

## Moving objects (all visible f0–f71)
- **taxi** (yellow, roof sign): moves from f1. It drives from the far side toward the camera, turning to the image left
  (heading ~120° → ~160–170° over f14–f25) and ends side-on at the left, just above the parked purple car. Its apparent
  length grows from 129 to 478 px, mainly from the change of view (front → side). f24–50: the near traffic-light pole and
  sign plate cross it; a thin strip is hidden, but the box spans both sides. From ~f56 its box touches the pedestrian's.
- **van** (white, brown windows): nearly still f0–6 (steps < 0.6 px), starts ~f7 and accelerates toward the camera and
  right. Its box grows from 142x128 to 694x515 px; it stays inside the frame. The cyclist overlaps its left/front side throughout.
- **cyclist** (dark jacket, grey trousers, black bicycle): rides in front-left of the van the whole clip, toward the camera
  and right. Box 30x72 → 154x190 px.
- **pedestrian** (white T-shirt, grey jeans): walks steadily left on the far-left sidewalk (x 480 → 250, ~3–4 px/frame)
  at a nearly constant depth. Behind the trash can f0–~24 (lower legs hidden); behind the lamp post ~f40–60.

## Static objects
These are in scene.json with pixel boxes. The parked purple sedan (left foreground, cut off by the left edge) and the
green coupe (far side, right) were read by hand from gridded crops, because automatic segmentation loses their pale roofs.
Image wheelbases are 362 px and 82 px. Also recorded: trash can, lamp posts, four traffic-light assemblies, and red-brown
sidewalk mats (auto-segmented, ±2 px). Lamp-post and traffic-light boxes were read from a 100-px grid (±10 px).
The purple car, green car and trash can were verified static (they only differ where other objects pass).

## Camera / perspective
Static. Vanishing points (rough, from curb lines read by eye): road A (receding up-left) ≈ (621, 80); road B
(left-right) ≈ (3033, 96). Horizon ≈ y 80–96, nearly level. If the roads are perpendicular and the principal point
is the image centre, then f ≈ 830 px (HFOV ≈ 104°). That is beyond the stated 8–100° range, so treat it as an
order-of-magnitude estimate only and calibrate with the question's depth_info + a known size. Apparent sizes per object
are listed in scene.json (van and cyclist grow strongly as they approach; pedestrian roughly constant).

## Ambiguities
- Vehicle reference = image centroid, not the true 3D root. For speeds from depths, use the centroid consistently.
- Taxi and van early frames (f0–2) are crowded together with the cyclist; the splits were checked visually.
- Shadow/body boundary under vehicles: ±5 px on bottom edges.
