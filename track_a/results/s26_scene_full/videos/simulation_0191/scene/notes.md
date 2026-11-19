# simulation_0191 — measurement record

Video: 2D simulation (Blender), 120 fps, 200 frames (t = frame/120, 0..1.658 s), 1920x1080. Camera static.
Pixels: x right, y DOWN, full resolution.

## Scene
Side view of a white catering truck (cab right) in a hangar. A brown cardboard box ("FRAGAIL" symbols, one open
flap at its right end) falls straight down from the top of the frame onto the cargo-box roof, bounces slightly
and settles. Meanwhile the truck's rig animates slowly: two red-footed stabilizer legs (and two small black jacks)
lower, and a dark tail-lift plate behind the truck folds up and disappears behind the cargo box.

## Files
- `scene.json` — inventory, static extents, rest/start positions, events, camera.
- `tracks/box.csv` — every frame: `cx, cy` = centre of the box's front face; `face_x0..face_y1` = front-face
  rectangle (rest size 408 x 191 px shifted by the track); `mask_*` = brown colour-mask bbox (includes underside strip
  and flap, clipped at y=0 early); `length_px` = mask width; `height_px` = rest face height; `match_score`;
  `cut_by_top_edge` (face top above y=0, frames 0..22).
- `tracks/rear_leg.csv`, `tracks/front_leg.csv` — red foot centroid and bbox per frame.
- `tracks/tail_lift_plate.csv` — visible part (x<128) of the dark plate; partial object, occluded=1 always.
- `scripts/` — diff.py (motion detection), track_box.py, profile_rest.py (rest edges), track_rig.py,
  check_overlay.py (overlay check + per-frame drops), crops.py (viewing helper).

## How measured / reliability
- Box: rest edges from saturation/intensity profiles at frame 120 (left 529.5, right 937.5, top 216.5, bottom
  407.5 → centre (733.5, 312.0), 408 x 191 px). Per-frame displacement by normalised template matching of the logo
  patch with sub-pixel refinement (scores 0.95–0.996); accuracy ~±0.3 px. The box translates purely vertically
  (cx = 733.5 ± 0.03), no rotation. Overlays (frames 0, 30, 60, 61, 68, 120) confirm the rectangle sits on the
  front face. Use `cy` for positions; the colour mask's vertical extent is inflated by the visible underside
  (perspective, up to ~34 px at frame 0) and cut by the image top early, so don't use mask height as size.
  Frame 0: cy = 59.26; rest cy = 312.0 → drop 252.8 px. The box's centre is a little behind its front face; for a
  pure vertical drop in a 2D scene this doesn't change the pixel displacement.
- Box size: length 408 px horizontal is the cleanest prior-matching size; height 191 px (front face, flap excluded).
  The box depth (into the screen) cannot be seen.
- Truck extents: read off grid images, ±5–8 px. Overall length (rear bracket x 122 → cab front x 1812) 1690 px;
  mirrors reach x≈1840. Height ground (y 1062) → top of railing (y 348) 714 px. Cargo box 1330 x 435 px. Wheel
  diameter ≈165 px, wheelbase ≈875 px. The truck side is slightly nearer the camera than the box's front face, so a
  scale taken from the truck may differ by a few % from the box's plane.
- Legs: red-colour centroid, ±0.5 px; lower ~33 px over the clip, slowly accelerating.
- Tail-lift plate: only a partial, occluded view — positions not reliable.

## Events (box)
- Starts falling from rest at frame 0–1 (per-frame drop 0.04 px at 0→1, growing ~linearly).
- Per-frame drop just before impact: 8.0–8.2 px/frame (frames 59–60).
- Impact with truck roof: frame 61 (t = 0.508 s); frame 60 bottom edge 403.0, frame 61 407.5.
- Small rebound up to 2.6 px (highest at frame 68, t = 0.567 s), second contact ~frame 74 (t = 0.617 s), at rest
  frames 74–199.

## Ambiguities
- Box top is cut by the frame top in early frames; the tracked centre is still valid (template on the visible logo).
- The open flap is part of the mesh; whether the reference's box "height" includes it is unknown (flap adds ~15 px).
- No other free-moving objects; nothing else falls.
