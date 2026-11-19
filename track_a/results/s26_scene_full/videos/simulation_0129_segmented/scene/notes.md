# simulation_0129_segmented — measurement record

2D scene, 1920x1080, 24 fps, 40 frames (t = frame/24, 0 … 1.625 s). Segmentation video: plain white background, only one object.

## Files
- `scene.json` — inventory, sizes, wheel/part positions, events, camera, per-frame displacements of the bbox centre.
- `tracks/forklift.csv` — every frame 0–39: frame, time_s, cx_bbox/cy_bbox (bbox centre = reference point), cx_mask/cy_mask (mask centroid), bbox x0,y0,x1,y1, length_px (horizontal extent = main axis), height_px, area_px, n_components, touches_edge, occluded.
- `scripts/measure.py` (mask = min RGB channel < 200, 3x3 opening, blobs > 50 px; writes CSV and overlays frames/ov_*.png), `scripts/write_json.py`.

## Content
- **forklift** (only object): orange/black Toyota forklift, side view, counterweight on the LEFT, mast + forks on the RIGHT. Drives to the right (forward) along a horizontal line, wheel bottoms at y ≈ 927–928 the whole time. Visible in all frames, never occluded, never at the frame edge.
  - Size: bbox length ≈ 257 px (frames 0–20: 254–259), shrinking to 246 px by frame 39 (the mast/fork tips look slightly different as it crosses the view); height ≈ 193–195 px. Use ~256 px length / 195 px height near the start (frame 0: 257 × 195).
  - Approx parts at frame 0 (read by eye from a 3x zoom, ±3 px): rear wheel centre (73, 915), front wheel centre (231, 910), wheelbase ≈ 158 px, front wheel diameter ≈ 67 px, rear ≈ 55 px.
- No static objects, no ground markings. Camera static (nothing in the background to check against; the object's y stays constant to ~2 px).

## Motion / events
- At rest frames 0–2 (bbox centre x = 169 at frames 0–1, 169.5 at frame 2). Motion starts at frame 2→3 (t ≈ 0.083–0.125 s). After that the per-frame displacement rises about linearly (≈ 0.9 px/frame per frame), so it looks like uniform acceleration from rest; it is still speeding up at the last frame (≈ 36 px/frame at frame 39). Bbox-centre x: 169 (f0) → 863.5 (f39), net ≈ 694.5 px; path length ≈ 695 px (motion is almost purely horizontal).
- No bounce, contact or change of direction.

## Reliability
- bbox edges are good to ±1 px. Per-frame centre differences are noisy (±1 px) because the length changes by a few px; for speed/acceleration, fit over several frames or use the rear edge x0 (counterweight, very sharp) as a rigid-point track. The vehicle root (origin) is not visible; for a 2D horizontal motion any rigid point gives the same displacement. Scale should come from the question's prior (e.g. forklift length ↔ ~256 px).
- Motion blur is small; the antialiased mask edge is light-grey at most 1 px.
