# simulation_0064 — measurement record (pixels, seconds)

Blender render, 3D scene, 2160x1080, 24 fps, 72 frames (t = frame/24, 0 … 2.9583 s).
All coordinates are original-resolution pixels, x right, y down, origin top-left.
No metric scale is given here; answering sessions set it from their own prior/depth_info.

## Files
- `scene.json`: camera, perspective (curb lines, vanishing point, horizon), object inventory with
  descriptions and visible frames, static objects (pixel boxes), events.
- `tracks/taxi.csv`, `tracks/van.csv`: every frame 0–71. `ref_x, ref_y` = bbox centre (proxy for the
  vehicle root, which isn't visible); `bbox_*`; `bottom_y` = lowest mask row (≈ tyre/ground contact);
  `mask_cx, mask_cy, mask_area`; `mask_len_main_axis` and `mask_wid_across` (min-area rectangle);
  `occluded`, `occluded_by`. The van also has `paint_x0/x1/w/top_y`, the extent of its light paint
  (body width without the mirrors).
- `tracks/cyclist.csv`: frames 0–71. `ref_x` = centre of the body column band. `head_top_y_best`,
  `wheel_bottom_y_best`, `height_px_best` (person + bike height). `ref_y_pelvis_est` = wheel_bottom −
  0.57·height (approximate saddle/pelvis). Raw values are also given.
- `tracks/pedestrian.csv`: frames 33–71. `ref_x` = mask centroid. `head_top_y`, `feet_y`, `feet_visible`.
  `ref_y_pelvis_est` = head_top + 0.47·103 px.
- `scripts/`: every script used. Pipeline: `make_bg.py` builds a clean background (median of every 3rd
  frame, van area patched from frame 71). `seg.py` does foreground + shadow detection: a shadow is a
  bluish darkening that keeps the cobble texture (local NCC test). `track2.py` builds the per-frame masks
  and writes frames/raw_tracks.json. `write_record.py` writes the CSVs and scene.json. Other scripts:
  `camera_check.py`, `vanishing.py`, `static_measure.py`, plus the viewers (zoom_mask, ovsheet, cyc_strip).

## Scene
Static elevated camera looking down a straight cobbled street. Near the camera is a cross street
(sunlit band, far curb y≈307–320, near corners ≈(600,560) and (1810,540)). Traffic signals stand on all
four corners. The road and near corners have large static shadows.
- Camera: **static**. Phase correlation on three background regions gives a maximum shift of 0.5 px.
  **Frame 1 is a duplicate of frame 0**, so all motion starts between frames 1 and 2. Keep this in mind
  when using backward differences at t = 0.04 s.
- Perspective: street vanishing point ≈ (1075 ± 50, −103 … −187). Best combined estimate: (≈1060, −121).
  The horizon is above the image (y ≈ −120, roughly horizontal) and the camera is pitched down.
  Carriageway width between the curb lines ≈ 1.708·(y+121) px, so ground depth along the street is
  ∝ 1/(y+121) for a ground contact row y. Use this as a cross-check only; prefer depth_info.

## Moving objects (all move during the whole clip; none stops; no contacts or collisions)
1. **taxi**: the only yellow car (NYC-style, roof sign). At f0 it faces the camera left of the van
   (bbox 880–1006 × 196–324). It drives toward the camera while turning to the image left into the
   near side of the cross street. It ends side-on, moving right to left (f71 bbox 76–470 × 248–379).
   The bbox length grows 127 → 395 px, mostly from the turn (front view → side view), not from depth.
   From f38 the left signal head and pole cross it. The mask bridges them, but some pixels behind the
   pole are missing. Reliability: x-extent ±5 px; the bottom can include ≤10 px of the car's own ground
   shadow; the top is good.
2. **van**: white/light-grey full-size passenger van, the only one. It comes straight toward the camera
   in the right-centre of the street. Bbox 1116–1245 × 137–305 at f0, 1126–1399 × 326–719 at f71.
   Width grows 130 → 274 px and paint width 120 → 249 px. Image speed rises sharply in the last ~8
   frames (top y: 293 at f70 → 326 at f71). The bottom row is the dark under-body/shadow line (±15 px).
   The roof top and the paint/mirror sides are crisp (±2 px). Never occluded.
3. **cyclist**: one person in dark clothes on a bicycle riding toward the camera between the taxi and
   the van. Body x 1054 → 1031; height (head top to wheel bottom) 87 px at f0, ~113 at f26, ~146 at f38,
   ~162 at f50–60, 169 at f71. They look different after ~f64 (dark jacket) only because they ride out
   of the sun into shadow. It is the same person. From f29 to f59 the rider crosses the van's shadow and
   the shadow edge. There the raw boxes are noisy, so the `*_best` columns use smoothed values
   (median-5 + Savitzky–Golay; `bbox_unreliable_shadow=1`); I checked them visually against zoomed
   crops (±5 px). Frame 70's wheel bottom is interpolated. Bbox width includes the arms and handlebars.
4. **pedestrian**: man in a white T-shirt and dark trousers on the far-left sidewalk. He walks right to
   left at nearly constant depth (feet y ≈ 298–300). He is hidden behind the left signal head in
   f0–32 (only the feet show briefly) and emerges at f33. Full height ≈ 103 px (median of f36–52).
   ref_x goes 345 → 231 px. From ~f53 the passing taxi hides his legs (`feet_visible=0`,
   `occluded_by` includes taxi), so feet_y and bbox_h are too short there; use head_top_y + 103.
   The head top and centroid x are reliable to ±3 px. Walking makes ref_x oscillate by a few px.

## Static objects (pixel boxes in scene.json)
Near-left signal: warning sign top y=67, head bbox [337,147,473,307], pedestrian signal
[393,343,445,410], pole base ≈(430,572). There is also a near-right signal, two far signals, two trees in
planters on the far sidewalks, the sidewalks, a grate at the near-left, and the curb lines (fitted line
parameters in scene.json).

## Events
f0–1 identical (no motion). f2 (0.083 s): first visible motion of taxi, van and cyclist.
f33 (1.375 s): pedestrian emerges. f38 (1.583 s): taxi reaches the left signal pole.
f57 (2.375 s): taxi passes in front of the pedestrian. f71: end, everything still moving.

## Caveats
- The reference points are image proxies. The true 3D origins (vehicle root, pelvis) are not visible.
  The bbox centre of a car is above its root; the ground contact is `bottom_y`.
- The taxi's apparent length mixes depth change with its heading change, so don't use it as a pure
  depth cue. For the van, width ∝ 1/depth is a clean cue (it heads straight at the camera).
- Masks come from background subtraction. Dark parts on dark cobbles (tyres, the under-body, dark
  clothes) are the least certain. Overlay checks are in ../frames/ov (scratch, not part of the record).
