# simulation_0118 — measurement record

Video: 1080x1080, 121 frames, fps 24.003175 (t = frame/fps), Blender simulation, **2D scene**.
Overhead (top-down) static camera looking at a wooden table top. All values in pixels / seconds; no metric scale.

## Files
- `scene.json` — inventory (moving + static objects), pixel sizes and positions, camera, events.
- `tracks/toy_car.csv` — per-frame track of the only moving object (frames 0–120):
  `frame, time_s, cx_bbox, cy_bbox` (bbox centre), `cx_mask, cy_mask` (mask centroid = recommended reference point),
  `bbox_x0..y1`, `length_px` (extent along PCA main axis), `width_px` (across), `axis_angle_deg`, `area_px`, `occluded` (always 0).
- `scripts/motion_scan.py` — frame-to-frame differencing over the whole frame (proves only the car moves, camera static).
- `scripts/track_car.py` — car tracking: temporal-median background of the band y 640–820, mask = |frame−bg|>30 AND HSV saturation>85 (the saturation term removes the car's grey shadow, which otherwise added ~8–10 px on the right/bottom), largest component, holes filled. Writes overlays to `frames/ov_*.png`.
- `scripts/colour_check.py` — independent saturation-only mask used to cross-check the car's extents.
- `scripts/static_objects.py` — table (contour + polygon), tray (Hough circle), book (bright-page minAreaRect), small circles. Candle / glass jar / black disc / garland / tassels were read off zoomed grid crops (frames/tray.png, frames/beads.png).

## Scene content
- **toy_car** (moving): small orange-tan wooden toy car, 4 wheels, lower-left of the table at y≈730. Moves in a straight line to the **right (+x)**, horizontal in the image (y stays 729–731). Already moving at frame 0 and still moving at frame 120 (no start/stop, bounce or contact in the clip). Motion is uniform: centroid x vs frame fits a line (slope ≈2.62 px/frame) with a quadratic term of only −6e‑5 px/frame² and 0.5 px residual → no detectable acceleration. Centroid (155.6, 730.0) at frame 0 → (467.8, 730.2) at frame 120, net 312 px (rear edge 92 → 404, also 312 px).
  Size: length along motion ≈130 px (per-frame p10–p90 127–132; clean frame-60 colour mask gives body 126–128 px), width incl. wheels ≈42 px (41–45). Height not observable (top view).
- Static: table top (corners (158,144),(1020,246),(953,907),(94,807); sides ≈867 × 665 px, rotated ≈6.7°), round marble tray (centre (553,448), diameter 259 px), candle (centre (496,472), Ø≈51), glass jar (centre (567,420), Ø≈52), black disc (centre (623,444), Ø≈21), open book (centre (317,306), ≈214 × 154 px), bead garland (bbox x 635–892, y 228–606, beads Ø≈13–15 px) with two grey tassels (≈85 px and ≈75 px long), grey floor around.

## Reliability / caveats
- Camera: static, zero background shift (difference images non-zero only at the car). Orthographic-like view: opposite table sides agree to <0.5%, so one px scale is valid across the table plane (the car moves on the table plane, same depth as the table top; objects standing on the table are at slightly different heights but this is negligible).
- Car per-frame centroid jitter ≈0.5 px (std of frame-to-frame Δx 0.47 px); bbox edges are noisier (front edge Δx std 1.5 px due to wheel/shadow pixels). For per-frame speed, a one-frame difference of the centroid is noisy (±~20%); because the motion is a straight uniform line, a linear fit of cx_mask vs frame gives the true per-frame displacement (≈2.617 px/frame). Summing raw per-frame displacements gives a path of 314.6 px vs 312.2 px net — the excess is noise; true path ≈ net displacement.
- At frame 0 the car's rear end is at the table's left edge (x≈92); mask still complete (length 124 px — slightly short, edge contrast).
- Car "origin": mask centroid of the top view; for a symmetric rigid toy this coincides with the bbox centre within ~2 px (cx_bbox − cx_mask ≈ −2…+1 px).
- Static sizes from Hough/contours: ±2 px for table, tray, book; ±3 px for small items read from zoomed crops; garland/tassel extents ±5 px.
