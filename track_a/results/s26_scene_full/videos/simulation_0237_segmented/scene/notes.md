# simulation_0237_segmented – measurement record

2D segmentation video: 1920x1080, 24 fps, 50 frames (t = frame/24, frames 0–49). The background is plain white.

## Files
- `scene.json`: inventory, building extents, animal motion and size summary, camera, events.
- `tracks/animal.csv`: one row per frame (0–49) for the only moving object. Columns:
  - `cx, cy`: mask centroid. This is the reference point.
  - `bbox_cx, bbox_cy`: bounding-box centre.
  - `x0, y0, x1, y1, bbox_w, bbox_h`: bounding box.
  - `axis_len, axis_wid, axis_angle_deg`: PCA main-axis length and the width across it.
  - `brown_cx, brown_cy, brown_x0, brown_x1`: centroid and x-extent of the reddish-brown pixels only, excluding the whitish tips.
  - `area_px`, `n_components`, `occluded` (always 0).
- `scripts/track.py`: segmentation and tracking. Non-white pixels are thresholded, the largest component is taken as the building, and components below y=730 are taken as the animal. It also writes overlay PNGs to `frames/`.
- `scripts/camera_static.py`: camera-shift check and building row/column extents.

## Objects
- **animal** (moving): a small elongated reddish-brown body, about 148 px long and 39 px wide, just below the building.
  - It has a pointed whitish tip at its right (leading) end and small knobs on its top edge.
  - The species is unclear; it could be a fox or small mammal, or a bird body seen side-on.
  - It moves right along a horizontal line the whole clip. The centroid goes from x 753.9 to 879.4, about 125.5 px in 49 frames (≈2.56 px/frame on average), while y stays at 775.9–777.0.
  - The frame-to-frame centroid step is noisy (≈1–5 px) because the shape changes with the limb/gait cycle. Smooth over several frames, or use bbox edges, if needed. The right edge `x1` is the steadiest (837 → 966, ≈2.63 px/frame).
  - The main-axis length cycles between 139 and 165 px (maxima near frames 8, 31 and 48). The left end is the most variable part.
  - It is never occluded. No start, stop, bounce or contact happens in the clip; it is already moving at frame 0 and still moving at frame 49.
- **building** (static): an oblique corner view of a box-shaped brick building with a protruding horizontal band around its middle.
  - Overall bounding box: x 621–1422, y 24–744 (802 × 721 px).
  - Main block: x 662–1361 (700 px wide). The vertical corner is at x≈1018 and is ≈720 px tall (y 24–744); the side edges are ≈615 px tall.
  - Middle band: ≈800 px wide (x 621–1422) and spans y≈270–520.
  - Left face (dark) is ≈356 px wide; right face (cream) is ≈343 px wide.
- There is no ground, horizon or markings (segmented background).

## Camera
The camera is static: phase-correlation shift of the building is under 0.11 px in every frame. The scene is 2D: the animal moves parallel to the image rows at constant apparent size, so one m/px scale (from the question's prior) applies to it. The building is drawn in perspective, so its edges are not all at one scale. Prefer its vertical corner height or overall extents.

## Reliability
- Masks were checked visually on overlays (frames 0, 12, 24, 36, 49) and cover the full animal, tips included.
- Centroid positions are good to about ±1 px (H.264 edges). Lengths are good to ±2 px but vary with the animal's pose.
- Ambiguities:
  - The animal's origin, such as its pelvis or root, is not visible. The mask centroid is used instead; it is roughly 5 px right of the brown-only centroid.
  - Whether its "length" includes the whitish tip: `axis_len` includes it, the brown-only length is ≈128 px.
