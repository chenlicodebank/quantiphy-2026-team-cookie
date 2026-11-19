# simulation_0195 — measurement record

3D Blender render, 30 fps, 100 frames (t = frame/30, 0 … 3.3 s), 1920x1080. Black space background, static camera.

## Objects
- **planet** — large banded Jupiter-like gas giant at image centre. Origin static: circle-fit centre (941.26, 489.60) px,
  constant to ±0.05 px. Diameter 282.66 px (circle fit to silhouette; bbox 284x284, x 800–1083, y 348–631). The surface
  texture changes slowly (the planet spins in place); its centre does not move.
- **moon** — small grey-brown cratered sphere, below-right of the planet. Moves the whole clip from (1127.7, 879.0) to
  (1475.6, 773.7) px, right and up along a smooth arc (heading -8° → -27°, y down), per-frame step 4.2 → 3.1 px. Its apparent diameter
  shrinks 27.9 → 26.6 px (about -0.45 px/s, ~-4.8 %), so it is moving away from the camera. That makes this a 3D orbit-like motion,
  so the pixel steps are not proportional to true speed. Image distance to the planet centre grows 431.7 → 605.2 px. Never occluded,
  never touches the planet. Nothing else is in the scene. Two single-pixel blobs at (844,384) and (1039,384) are planet-limb fragments, not objects.

## Events
None discrete: the moon moves continuously in frames 0–99, with no start, stop, bounce or contact. The direction changes gradually (curving path).

## Files
- `scene.json`: inventory, camera, summary positions and sizes.
- `tracks/planet.csv`, `tracks/moon.csv`: one row per frame (0–99). Columns: frame, t, bbox_x0/y0/x1/y1, width_px, height_px,
  area_px, eqdiam_px (area-equivalent diameter), cx_mask/cy_mask (mask centroid), cx_wt/cy_wt (brightness-weighted
  centroid), **cx_circ/cy_circ/diam_circ (least-squares circle fit to the silhouette contour = recommended origin and diameter)**,
  ell_major/ell_minor (ellipse fit), occluded (always 0).
- `scripts/track.py` (segmentation + fits), `scripts/analyze.py` (summaries), `scripts/overlay.py` (checks drawn to
  frames/ov_*.png, frames/moon_zoom.png), `scripts/probe.py` (threshold check).

## Method and reliability
Mask = max(RGB) > 18 (background 3–15, object edges jump to >35 within 1–2 px). The two largest connected components are the planet and the moon.
For spheres the origin is the silhouette centre, so cx_circ/cy_circ is the reference point.
- Planet centre/diameter: ±0.1 px / ±0.5 px. The dark night-side limb (lower right) is dim but still above threshold, and the circle fit matches the visible disc (overlay checked).
- Moon centre: about ±0.3 px per frame (track residual rms vs smooth quadratic 0.2–0.4 px). Moon diameter: ±0.5 px per frame (bbox 26–30 px).
  Use a linear fit over time for size (diam_circ ≈ 28.04 − 0.453·t px) instead of single frames. eqdiam_px runs ~0.9 px larger than diam_circ
  because it includes the anti-aliased rim. For apparent-size-based depth, use diam_circ consistently for both objects.
- 3D notes: there is no ground plane or horizon. Depth must come from depth_info. The focal length can be estimated from planet diameter_px × depth / true diameter
  (sphere, so f ≈ d_px·Z/D for small angular size). The moon's depth change can be checked against its diameter ratio (Z ∝ 1/d_px:
  about +5 % over the clip).
- Brightness-weighted centroids (cx_wt) are biased toward the lit side (the planet by about -4 px x and -12 px y). Do not use them as origins.
