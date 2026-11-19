# simulation_0181 — measurement record

Video: 1920x1080, 24 fps, 40 frames (t = frame/24, 0 … 1.625 s). Source: simulation, scene type 2D.
Pixel coordinates: x right, y down, full resolution. No metric scale is assumed anywhere.

## Scene
Warehouse corner seen from the front: grey breeze-block wall, a shelf top-left with a big orange
"Pizza Topping / Hot and Spicy / 8 x 500 ml" crate and a small "Seedless Jaffas" box, a blue roller ramp
running from the shelf (upper left) down to the right at ~28.8° in the image, a stack of orange "China Food"
crates at its foot (bottom right), an orange "TAKE CARE WHEN STACKING CRATES" sign, a wall vent, an orange
frame bottom-left, a blue post. **Only one object moves: the brown cardboard box** (open/torn lid flaps).
It falls vertically from rest, lands on the upper end of the ramp, tilts to the ramp angle and slides down,
accelerating, then passes behind the China Food crates. The camera is static (no shift, no shake).

## Files
- `scene.json` — inventory (all objects with pixel extents), box pixel sizes, events, camera.
- `tracks/box.csv` — one row per frame 0–39: `x_ref,y_ref` (reference point = box centre in the image),
  `ref_source`, `confidence`, `occluded`, hull-mask bounding box (`bbox_*`), mask centroid, `len_main_axis` /
  `width_across` (minimum-area rectangle, only where the box is fully visible), `main_axis_angle_deg`
  (long side angle, image coords, 180 = horizontal; ~151 = tilted 29° down-right), topmost vertex, mask area.
- `tracks/box_raw.csv` — raw per-frame mask measurements (centroid, bbox, min-area rectangle) for all frames,
  including the biased ones while occluded.
- `scripts/` — `common.py` (frame decoder), `look.py` (gridded frames), `track_box.py` (segmentation),
  `occl_track.py` / `occl_track2.py` (template tracking during occlusion; shifts in `occl_shift*.csv`),
  `build_track.py` (assembles `box.csv`).

## Method
Background = frame 39, with the region where the box sits in frame 39 replaced by frame 0. The box mask is
|frame − background| > 30 (max over RGB), opened/closed, largest component, convex hull. Overlays (checked
at frames 9, 21, 34, 38 and the full track on frame 39) show the mask covers the whole box and nothing else.
- Frames 0–29: reference point = hull-mask centroid (box fully visible). High confidence (±1–2 px).
- Frames 30–39: the bottom of the box goes behind the China Food crates. Since the box's tilt stays constant
  while sliding (28.6–29.0°), it moves rigidly; reference point = frame-28 centroid + shift found by masked
  template matching of the top 90 px of the box (only box pixels compared). Agrees with the centroid within
  ~1 px on frames 24–29 where both exist. Confidence high to frame 34, medium 35–37, low 38–39.
  Frames 35/36 show a step pair of 44/27 px (template jitter; mean ~36 px/frame) — smooth over them.

## Key numbers (pixels)
- Start (frame 0): centre (542.7, 330.2). Free fall frames 0–7, pure vertical; per-frame drops 2.1, 6.4, 10.9,
  13.7, 19.0, 21.2, 26.4 px (≈ constant increase, i.e. constant acceleration from rest at t=0).
- Impact on ramp: between frames 7 and 8 (t ≈ 0.29–0.33 s); frame 8 is the first frame with tilt/slowed drop.
  Tilt goes 0° → 29° over frames 8–12; step size drops to ~18–20 px/frame.
- Sliding (frames 12–39): direction down-right along the ramp (~28.8° below horizontal); step length grows
  from ~19 px/frame (frames 12–15) to ~37 px (29) and ~40–45 px (32–39). Still moving at the last frame.
- Box size: free fall (axis-aligned) silhouette 327 x 235 px (bbox, includes ~27 px of visible side face and
  ~20 px of lid flaps; the front face alone ~300 x ~213 px). While sliding: min-area rectangle 279.5 x 186 px
  (±3), long side along the ramp. The silhouette changes on landing (box turns slightly about the vertical
  axis), so for a size prior "length of the box" the ~280–300 px values (face) vs 327 px (full silhouette)
  bracket the choice; the free-fall bbox is the cleanest axis-aligned measure of the whole object.
- Ramp: slope 28.8° in image; visible length along slope ~990 px (x 320→1190, ±20 px); front face ~110 px thick.
- Sign 188 x 187 px; vent 188 x 90 px; bricks ~100 px pitch.

## Ambiguities / reliability
- Scene labelled 2D but rendered in 3D: slight perspective (box top and left side visible during the fall).
  Box motion stays in a plane roughly parallel to the image, so one px scale is reasonable.
- Occlusion by the China Food crates from frame 30 (partial) to 39 (most of the box hidden); the reference
  point there is inferred, see confidence column.
- No motion blur problems; shadows are faint and were not included in the mask (threshold excludes them).
- The box's lid flaps make the topmost vertex jittery — don't use `top_vertex_*` for fine motion.
