# internet_0026 — measurement notes

Indoor handheld clip, 29 frames at 19.68 fps (1.47 s), 1920x1080, labelled 2D. A toy dump truck
(blue cab, red bed, yellow chassis, black wheels) rolls right to left across a glossy tiled floor, from a
crouching man (right, black T-shirt, jeans) towards a sitting toddler (left, against a red sofa). Everything
is in pixels and seconds. t = frame / 19.68.

## Files
- `scene.json` – inventory, pixel sizes, camera summary, events.
- `tracks/toy_truck.csv` – one row per frame (0-28): `cx,cy` bbox centre; `centroid_x/y` mask centroid;
  `bbox_x0..y1`; `length_px` (bbox width = bumper to bumper, the motion direction), `height_px`;
  `front_x` (leftmost blue cab pixel = leading edge), `rear_x` (rightmost red bed pixel); `area_px`; `occluded`;
  `floor_dx/dy` (camera shift at the floor); `*_floorcomp` = position minus floor shift (motion relative to the
  floor); `cx_armchaircomp`, `front_x_armchaircomp` = minus the far-background shift (alternative).
- `tracks/camera_shift.csv` – cumulative background shift per frame: KLT medians for bands
  (armchair/wall, floor y600-700, floor y700-800, sill) and `floor_y765_dx_at_x1000 / floor_y765_dy` from the
  grout-line fit (the recommended truck-depth reference).
- `tracks/camera_phasecorr.csv` – phase correlation of armchair band and sill (cross-check).
- `scripts/` – measure.py (truck segmentation + phase correlation), floor_shift.py (KLT bands), grout_fit.py
  (grout-line floor motion), finalize.py (compensated columns), view_*.py / check_grout.py (visual checks).
  Run order: measure -> floor_shift -> grout_fit -> finalize.

## Truck
- Mask: HSV thresholds for blue, yellow, red + dark tyres below the body, in a window around the previous box.
  Overlays checked at frames 0,1,2,3,4,8,...,28: the box covers cab nose to rear bumper and bed top to tyre
  bottoms. Mask is a little ragged on the dim red bed, but the bbox is good to ~±3 px.
- Pixel length (bumper to bumper, along motion) = **312 px** (median of frames 3-28, range 310-318).
  Height ≈ 255 px, wheel diameter ≈ 78 px, wheelbase ≈ 155 px (by eye, ±5 px).
- Frames 0-2: the rear of the bed is hidden behind the man's knee (`occluded=1`, length reads 304-306). Use
  `front_x` (never occluded) for motion if those frames matter.
- Motion is near-horizontal (cy constant within ±4 px). Raw front_x: 1004 -> 640 (−364 px).
  Floor-compensated front_x: 1004 -> 552.7 (−451 px), i.e. ~16 px/frame on average, slightly slower at the end.
- Frame-to-frame steps alternate big/small (e.g. 20.5, 12.7, 20.7, 14.5 ...) for the whole clip: uneven frame
  timing in the source (frame-rate conversion), not real jerks. Average over pairs of frames for speeds;
  second differences from single frames will be dominated by this jitter.

## Camera
- Not static: handheld sideways move that accelerates through the clip, with parallax. Cumulative
  rightward image drift at frame 28: far armchair/wall ≈ 42-44 px, floor at y≈765 (grout lines just in front
  of the truck) ≈ 87 px (dy ≈ −11), foreground sill ≈ 75 px. Early frames barely move (f7: ~5 px).
- The floor value comes from fitting 4 grout lines on 7 scanlines (y 735-795) per frame, solving for uniform
  dx, dy (rms < 0.3 px). KLT on the floor bands gives lower values (45-53 px) because many floor features are
  reflections of distant furniture, which move like the far background — don't use those for the truck.
- Truck wheels touch the floor at y≈725, slightly farther than y=765, so the true background shift at the
  truck is maybe 80-87 px at f28 (uncertainty ~±7 px out of ~450 px displacement, ~2%).
- No measurable zoom (truck length and armchair width constant).

## Static / quasi-static objects
Man (crouching, bbox ~450x665 px) and child (sitting, ~295 px tall) only make small limb movements; their image
drift follows the camera. Bboxes read by eye at frames 0 and 28 (±10 px). Sofa, armchair (320 px wide),
small black stool, bar stools, back sofa/coffee table, floor tiles (grout spacing ≈ 410-430 px along y=765)
and window sill are static; positions in scene.json (frame 0).

## Events
- Truck already rolling at frame 0 (the push happened before the clip); man's hand is near the top of the
  bed rear in frames 0-3 with no clear contact, so release ≤ frame 0-1 (ambiguous).
- Rear un-occluded from frame 3.
- From frame 26 the cab front overlaps the child's right shoe in the image (truck passes in front of it; no
  visible impact or stop). Truck is still moving at the last frame (28).

## Ambiguities
- Which background to use: recommended floor (grout) shift; armchair alternative provided. Raw image
  positions are also given.
- Strong floor reflections of the truck below it (y 730-860), not part of the mask.
- Child, sofa and armchair are red/blue like truck parts; the search window kept them out (checked).
