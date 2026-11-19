# simulation_0037_segmented — measurement record

Video: 1080x1080, 24 fps, 72 frames (t = frame/24, 0 to 2.958 s). Segmentation video of a 3D Blender scene: the background is plain white, so there is no ground, horizon or texture. All values are in pixels and frames. No metric scale was assumed.

## Files
- `scene.json`: the object inventory, camera info, events and per-object summaries (rock extents, person trends).
- `tracks/person.csv`: one row per frame (0–71). Columns:
  - `cx, cy`: mask centroid.
  - `pelvis_x, pelvis_y`: pelvis estimate. x is the mean mask x in rows 42–55 % of the height from the top; y is top + 0.47·height.
  - `pelvis_x_smooth, pelvis_y_smooth`: Savitzky–Golay smoothing, window 11, order 2.
  - `bbox_*`: bounding box, inclusive.
  - `head_top_x`, `feet_x`, `feet_bottom_y`.
  - `main_axis_len, across_width`: PCA extents of the mask.
  - `area_px`, `occluded`: occlusion is always 0.
- `static_rock.json`: rock slab extents at frame 0.
- `scripts/`:
  - `explore.py`: connected components and a frame-difference check.
  - `track.py`: masks, tracks and overlays.
  - `crops.py`: raw crops and threshold sensitivity.
  - `summary.py`: builds scene.json and adds the smoothed columns.
- Overlays I checked visually: `../frames/ov_00/18/36/54/71.png`. The masks cover the whole figure, from head to feet.

## Objects
1. **person** (the only moving object; a human walking in side view, heading right / +x). Visible in all frames and never occluded. Small: about 64 px tall (bbox height 60–69 px, mean 65.5 in the first 10 frames and 62.5 in the last 10). Width is 15–32 px depending on the stride.
   - Pelvis x goes from 799 (frame 0) to 920 (frame 71). A linear fit gives 1.73 px/frame, which is nearly constant (no start or stop).
   - The feet's bottom edge drifts down in the image (747 → 752), while the apparent height shrinks by about 5 %. So the person may be moving slightly away in depth, or this may be gait or threshold noise. It is ambiguous; treat the depth change as small.
2. **rock_slab** (static): a large beige wedge or sand-mound terrain piece on the left.
   - Bbox x 15–715, y 594–734: 701 px wide, 141 px tall, centroid (297, 673).
   - The thick end is at the left, with a dark side face and the peak top at y≈597 near x 120–170. It tapers to a thin tip at x≈715.
   - The bottom edge slopes from y≈707 to y≈733, so the slab lies obliquely in depth.
   - Column top/bottom profiles are in the json.

## Camera and events
- The camera is static: the rock's bbox stays fixed to within 1 px in all frames.
- The only perspective cue is the slab's sloping bottom edge.
- The person walks for the whole clip: they are already moving at frame 0 and still moving at frame 71.
- There are no contacts or impacts, and the person never reaches the rock (gap ≈75 px at frame 0, growing after that).
- Gait phases (bbox-width extrema) are listed in scene.json but are only roughly reliable.

## Reliability and caveats
- **Mask threshold:** the mask uses an RGB deficit > 15. The head is pale and was partly lost at a threshold of 30.
  - Bbox edges are ±1–2 px because of compression speckle at the margin.
  - The height is ±2 px.
- **Pelvis estimate:** this is an anatomical estimate, not the true rig origin. The per-frame raw pelvis jitters by about ±1 px, so the raw path length (138 px) is inflated.
  - The smoothed path (122.6 px) is close to the net displacement (121.5 px).
  - For speeds, use the smoothed columns or a linear fit (≈1.73 px/frame ≈ 41.5 px/s horizontally).
- **3D questions:** with depth_info, focal length f = pixel_size·depth / world_size. For example, if the prior is the person's height, use the bbox height of about 64 px at the given time.
