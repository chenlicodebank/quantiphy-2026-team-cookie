# simulation_0027_segmented — measurement notes

3D segmentation video (Blender render, background replaced by pure white), 960x960, 25 fps, 75 frames (t = frame/25).
Static camera. Two objects: one **walking human** (moves) and one large **rock** (static). No ground, horizon, shadows
or other objects are visible.

## Files
- `scene.json` — inventory, camera, static-object extents, events, summary numbers.
- `tracks/human.csv` — per-frame (0–74) human track: `pelvis_x/y` (pelvis estimate), `centroid_x/y` (mask centroid),
  bbox `bbox_x0,y0,x1,y1`, `height_px` (top-to-sole), `width_px`, `foot_x/foot_y` (lowest mask rows), `area_px`,
  `occluded` (always 0), plus `pelvis_x_smooth`, `pelvis_y_smooth`, `height_px_smooth`.
- `scripts/explore.py` (connected components per frame), `scripts/track.py` (tracker + rock mask + overlays),
  `scripts/rawcrop.py` (contrast-stretched crops for visual checking), `scripts/finalize.py` (smoothing + summary).

## Method
Mask = pixels with min(RGB) < 240. Human = largest connected component (after 5x5 dilation) in a window around the
previous position, restricted to y > 315 (below the rock). Pelvis y = foot_y − 0.53·height (hip joint ≈ 53 % of
height above the soles); pelvis x = mean mask x in the rows around that y. Verified on overlays and on
contrast-stretched crops at frames 0, 25, 50, 74: the mask covers shirt, trousers and feet; belt line at frame 0 is
y≈364, consistent with pelvis_y 363.2.

## Results (pixels)
- Human pelvis moves in a straight line down-right in the image: (406.2, 363.2) at f0 → (441.7, 408.7) at f74,
  ~52° below +x; net ≈ 56 px; smoothed path ≈ 57 px (≈0.77 px/frame, roughly steady; raw unsmoothed per-frame
  path sums to 83 px because of ±1–2 px stride jitter — use smoothed values for speed questions).
- Human apparent height ≈ 58 px (raw 54–63, smoothed 58.6 → 58.3: no measurable change), width ≈ 19 px. Constant
  apparent size means the camera distance to the human changes little; the image motion is mostly lateral/along the
  obliquely-viewed ground.
- Rock: static, bbox x 328–959, y 25–309 → 632 px wide × 285 px tall; filled-mask centroid (640.8, 166.7).
- Events: human walks for the whole clip (frames 0–74); no start/stop, contacts, or direction changes.

## Reliability / ambiguities
- Human head and shirt are very pale, nearly the background colour: top of the figure (≈ y 336 at f0) is uncertain by
  2–4 px, so per-frame `height_px` jitters; prefer median 58 px or `height_px_smooth`. Leg swing changes
  `foot_y`/width by 1–3 px per frame (walking gait), and min/max of `height_px` partly reflect this noise.
- Pelvis point is an anatomical estimate (±2 px). With only ~0.8 px/frame image motion, one-frame differences are
  dominated by noise; fit over many frames.
- Rock touches the right image edge, so its horizontal pixel extent may be slightly truncated. Its origin/centre in 3D
  is unknown; the filled-mask centroid is the best image proxy.
- No perspective cues; focal length must come from the question's depth_info plus a known size (e.g. human height
  ≈ 58 px at its given depth: f ≈ 58·Z/H).
