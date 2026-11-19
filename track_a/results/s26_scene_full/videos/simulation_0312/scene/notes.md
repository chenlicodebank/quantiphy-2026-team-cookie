# simulation_0312 — measurement record

Video: 1080x1080, 72 frames, 24.008 fps (t = frame / 24.008), simulation (Blender), 3D scene.

## Content
- **star** (the only object): a red/orange flat five-pointed star with visible thickness (cookie/toy-like). Visible in all
  frames 0–71, never occluded, never leaves the frame. It is already moving at frame 0.
- **background**: uniform beige surface (RGB ~196,186,155) filling the whole frame. No horizon, markings, edges or
  shadows; only faint render noise along the bottom edge. No other static objects.

## Files
- `scene.json`: inventory, camera, events, apparent-size summary.
- `tracks/star.csv`: one row per frame (0–71). Columns: frame, t, cx, cy (silhouette centroid in px, used as the object
  origin), bbox_x0/y0/x1/y1 (inclusive), bbox_w/h, area_px, equiv_diam_px (2*sqrt(area/pi)), len_main_axis_px and
  width_across_px (silhouette extents along/across the PCA main axis), main_axis_deg (image angle of the main axis,
  0 = +x, y down), red_core_cx/cy (centroid of the strongly red pixels only, a cross-check), and occluded (always 0).
- `scripts/track.py` (segmentation + tracking), `scripts/overlay.py` (checks: frames/overlay.png, frames/path.png,
  frames/stretch0.png), `scripts/summarize.py` (writes scene.json and prints per-frame steps).

## How it was measured
Each frame is decoded. The strongly red pixels give a seed, and the full silhouette is every pixel within ±60 px that
differs from the median background colour by more than 45 (sum of |RGB|). The overlays confirm that the box and centroid
cover the whole star, including the anti-aliased edges, at frames 0, 10, …, 71. The centroid and the red-core centroid
agree within about 0.3 px. Centroid accuracy is about ±0.3 px and extents are about ±1 px.

## Motion (image space)
- The image path is a smooth hook. The star starts at (427, 818). It moves right and up while receding. Its horizontal
  image motion slows to zero at **frame 51** (t ≈ 2.124 s, x max ≈ 939 px) and reverses to leftward from frame 52.
  Its vertical image motion stays upward (dy ≈ −6 px/frame early, ≈ −3.2 px/frame at the end). The star ends at
  (895, 448) at frame 71.
- The per-frame pixel step falls smoothly from 23.0 px (frame 1) to about 4.5 px around frames 50–60, then rises
  slightly to about 5 px by frame 71. There are no jumps, bounces, impacts or contacts. The clip ends mid-motion.
- Rotation: at frame 0 the star is tilted and seen nearly edge-on (a narrow, tall silhouette). By about frame 15 it has
  turned to a nearly face-on view, and after that it keeps a similar orientation (main axis 75–83° in the image).

## Camera / perspective
- The camera is static: the background is uniform and the corner-region brightness is constant (std < 0.03 grey levels).
- There are no ground-plane, horizon or vanishing-point cues. Depth information comes only from the shrinking apparent
  size. Equivalent diameter: 36.1 (frame 0, edge-on so too small), about 37 (frames 6–12), 35.1 (frame 24),
  32.5 (frame 36), 29.4 (frame 48), 26.4 (frame 60), 24.6 px (frame 71). bbox_h: 58 → 52 → 47 → 43 → 38 → 35 → 31.
  The star therefore moves away from the camera throughout. Its depth is roughly proportional to 1/apparent size once it
  is face-on (frames ≥ ~15). Early sizes are affected by the rotation.
- For focal-length estimation, use the given depths together with the star's pixel size (prefer the face-on frames and
  the main-axis length or bbox_h, which are tip-to-tip extents) or with pixel displacements. Assume the principal point
  is at (540, 540).

## Caveats
- The 2D centroid is a proxy for the 3D origin. For a symmetric rigid star the difference is negligible.
- A world AABB "size" of a star depends on its orientation. The image extents are silhouette extents, not world AABB extents.
- With a single object, distance-between-objects questions can only concern the star and the camera (or the star's own
  positions at different times).
