# simulation_0010_segmented — measurement record

3D Blender scene, segmentation version (background replaced by white). 59 frames at 22 fps (t = frame/22,
0–2.636 s), 1920×1954 px. **Static camera** (cart region shifts ≤0.3 px against frame 0).

## Objects
- **bird** (the only moving object): a dark crow/blackbird-like bird with white/grey wing undersides. It flies left
  to right in front of the house gable, at nearly constant image height (cy ≈ 760–847), from x≈355 (f0) to x≈1350
  (f50). Over f51–58 it turns away from the camera: image-x speed drops from ~20 to ~7 px/frame, it drifts down
  a little, and its apparent size falls to ~0.55–0.6 of before. It ends above the cart at (1423, 846). It is visible
  and never occluded in all 59 frames.
- **house** (static, left): half-timbered wooden shed, gable facing the camera, crossed ridge beams, dark doorway,
  plank door leaf, climbing rose. Bbox x 86–1021, y 353–1175.
- **cart** (static, right): dark two-wheeled hand cart in 3/4 view, shafts pointing front-left. Bbox x 1295–1891,
  y 1012–1268. The near wheel is ≈192×205 px.

There is no ground, no horizon and no shadows, so perspective cues are weak. The house is seen almost frontally; the
cart's long axis is foreshortened. Part sizes and positions are in scene.json.

## Files
- `scene.json`: inventory, static part sizes, camera, events, apparent-size summary.
- `tracks/bird.csv`: one row per frame with these columns:
  - `cx,cy`: mask centroid.
  - `bbox_x0..y1, bbox_w, bbox_h`: bounding box.
  - `area_px, sqrt_area`: mask area.
  - `axis_len, axis_wid, axis_angle_deg`: PCA main-axis extents.
  - `over_house`: 1 when the centroid is in front of the house (f0–33).
  - `occluded`: always 0.
  - `cx_smooth9, cy_smooth9`: 9-frame centred moving average of the centroid, about one wing-beat; the window
    shrinks at the ends.
- `static_measure.json`, `bg_median.jpg`: background model and automatic house/cart boxes.
- `scripts/`: `bg_and_track.py`, `static_and_camera.py`, `probe.py`.

## Method
- **Background:** per-pixel median of every 3rd frame.
- **Bird mask:** pixels where the max channel difference from the background is >40, or >12 on the white
  background (the white underside is ~230 on 255).
- **Clean-up:** open/close, then remove pixels that flicker in many frames along the house/cart segmentation edges.
  Keep the component nearest the previous position, plus any components touching it within 12 px.
- **Checks:** overlays at frames 0, 4, …, 48 and 50–58 were viewed (written to `frames/`, not part of the record)
  and cover the whole bird, wings included.

## Reliability and ambiguities
- **Centroid wobble:** the raw centroid wobbles ±10–20 px with the wing-beat (period ~8.6 frames, ~2.6 Hz; area
  minima at f≈1, 9–10, 19, 27, 36, 44, 53).
  - The Blender origin is the body, so prefer `cx_smooth9/cy_smooth9` for distances and path length.
  - Per-frame differences of the raw centroid add flapping noise.
- **Apparent wingspan** depends strongly on the wing phase. Use cycle maxima of `axis_len`/`bbox_w`: ~171 (f4),
  ~143–149 (f18–28), ~156 (f38), ~166 (f49), ~100 (f52), ~94 (f55).
  - Depth is roughly constant over f0–50 and increases over f51–58. That size ratio is only approximate, because the
    bird is then seen from behind/below.
- **Mask errors:**
  - f0 and f30–33 are near the house edges, with small holes or misses of 1–3 px.
  - Thin white feather edges on white can be lost at f52–58: extents are a few px low there.
- **Static parts:** sizes are hand-read from zoomed grids, ±5 px. Bboxes come from the median-background mask, ±2 px.
- **Not recorded:** no metric scale is assumed; speeds and accelerations are left to each question.
