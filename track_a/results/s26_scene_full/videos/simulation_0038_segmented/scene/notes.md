# simulation_0038_segmented — measurement record

3D Blender scene, segmented (white background), 1536x1536, 25 fps, 75 frames (t = frame/25, 0–2.96 s).
Static camera, high and looking steeply down. Two objects: one walking **human** (small, lower left) and one
large static **rock** (top centre/right). No other objects, markings or ground features survive the segmentation.

## Files
- `scene.json` — inventory, camera, summary numbers, events, image distances.
- `tracks/human.csv` — every frame 0–74: `pelvis_x, pelvis_y` (reference point, see below), `pelvis_y_bboxframe`
  (alternative: head top + 0.55 × that frame's body height; noisier), `body_cx/cy` (body pixel centroid),
  `shirt_cx/cy` (centroid of the white shirt/upper body pixels — a stable upper-body point), body box
  `body_x0,y0,x1,y1`, `body_height_px` (head top to lowest foot pixel), `body_bbox_width_px` (fixed band = 18),
  `torso_width_px` (median row width over upper 60 % of body), `blob_*` (body + shadow box), `shadow_tip_x/y`,
  `shadow_len_px`, `occluded` (always 0).
- `tracks/rock_static.json` — rock mask at frame 0: bbox, centroid, PCA major-axis length/angle, width, area,
  and its stability over the clip.
- `scripts/` — `probe.py` (component inventory per frame), `look.py`, `strip.py` (zoomed views),
  `track_human.py`, `static_rock.py`, `summarize.py`.

## How measured
- Mask = pixels with min(B,G,R) < 200 (background is pure white). Human = largest component below y = 680;
  rock = largest component above y = 680 (holes filled).
- The human's long shadow (dark, ~92 px toward upper right) is joined to the feet. Body = mask pixels within 18
  columns of the leftmost mask column; checked on overlays every 8 frames (frames/check_human.png): the box
  covers head to feet and only a sliver of shadow at its right edge.
- Pelvis: the view is from above, so the pelvis is not directly visible. `pelvis_y` = head top + 0.55 × median
  body height (39 px); `pelvis_x` = mean x of body pixels. Head top is stable (±0.7 px about a straight line), so
  this point is smooth; its absolute offset along the body (±3 px) is a convention. For speeds, any of
  pelvis / shirt / head-top tracks give the same motion within noise (all ≈1.33 px/frame).

## Key results (pixels)
- Human walks the whole clip (already moving at f0, still at f74), uniformly: linear fit dx = 0.077, dy = 1.331
  px/frame (|v| ≈ 1.333 px/frame ≈ 33.3 px/s); net f0→f74 ≈ (5.7, 98.5) px, i.e. straight down the image
  with slight rightward drift = walking roughly toward the camera, away from the rock. Raw per-frame steps are
  noisy (±1 px); raw path sum 100.8 px is inflated by noise — use a smoothed/fitted track for path length.
- Human apparent size: body height median 39 px (33–44, oscillating with gait; minima ≈ f0, 18, 35, 53, 70,
  step ≈ 17.5 frames ≈ 0.7 s); torso width ≈ 16 px. Size essentially constant (40.3 → 38.7 px mean over
  first/last 15 frames), so its distance to the camera changes little relative to its depth. Because the view is
  steeply from above, the 39 px "height" is a foreshortened standing height — not a true side-on height.
- Rock (static): bbox (556,18)–(1256,642) = 701 × 625 px, centroid (887.1, 292.8), major axis 779 px at
  142.9° from image x, width across 576 px, area 317k px. Top edge touches near y = 18 (not cut off).
- Image distance human pelvis → rock centroid: 643 px at f0, 720 px at f74.

## Reliability / ambiguities
- Human track: good (±1 px per frame); pelvis y has a convention offset (±3 px); body height/width ±1–2 px
  and depend on gait phase; very small object (≈16 × 39 px), so any size-based scale has ~5 % error.
- Shadow vs body: shadow dark, attached at the feet; occasionally a dark leg/shadow streak extends below the
  body (e.g. f8–9, f62–63), raising body_height_px by 2–4 px.
- Rock: mask edge reliable to ±2 px; a small detached loop at the top right (~1180–1256, 25–90) is part of the
  mask. Its 3D height can't be separated from its ground extent in this top-down view. Huge relative to the
  person (~18× the person's apparent height) — could be a boulder or hill mesh.
- Camera static: verified (rock mask stable within 1–2 px over all frames).
