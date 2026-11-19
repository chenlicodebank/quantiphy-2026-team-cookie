# simulation_0201 — measurement record

3D Blender render, 2560x2560, 60 fps, 14 frames (t = 0 … 0.2167 s, t = frame/60).
Close-up: a frosted bottle of amber liquid, tilted, on a white pedestal; a clear glass dropper
leans out of its neck and a single liquid drop falls from the dropper tip. Camera is static and
looks steeply downward.

## Files
- `scene.json` — inventory (drop, dropper, bottle, pedestal, backdrop), static pixel extents,
  camera/perspective cues, events.
- `tracks/drop.csv` — per-frame track of the drop (frames 0–13; `visible=0` for 10–13).
  Columns: `cx,cy` = mask centroid (reference point for the drop's origin), bbox (x0,y0,x1,y1,w,h,
  centre), `mask_len_main_axis` / `mask_width_across` (PCA extents of the filled mask; main axis is
  ~vertical so these ≈ height / width), `main_axis_deg`, `area_px`, `equiv_diam` (diameter of a disk
  of the same area), `occluded`, `cut_by_edge`, `attached_to_spout`.
- `scripts/seg.py` — camera-motion check and coarse detection; `scripts/track_drop.py` — the track
  (writes the CSV and overlays `frames/drop_overlay.png`, `frames/path.png`).

## Method
Background = frame 13 (drop gone; camera static, verified: static regions differ by ≤0.2 grey
levels in every frame). Per frame: Gaussian blur, max-channel |frame − bg| > 15, open/close,
largest component, holes filled. Overlays checked by eye: contours follow the drop outline in all
frames 0–9.

## Drop track summary (px)
| f | cx | cy | bbox w×h | equiv diam |
|---|----|----|---------|-----------|
|0|1050.5|833.8|121×174|138.7|
|1|1051.9|864.6|122×173|137.8|
|2|1055.6|949.7|119×168|135.0|
|3|1061.5|1083.3|117×161|130.5|
|4|1068.9|1258.5|111×153|125.3|
|5|1078.6|1466.1|109×145|116.9|
|6|1088.5|1697.0|101×133|108.4|
|7|1100.8|1938.5|90×121|98.5|
|8|1111.8|2185.0|82×109|89.6|
|9|1123.8|2430.4|76×98|80.2|
Per-frame vertical steps: 31, 85, 134, 175, 208, 231, 242, 247, 245 px — the image-plane motion is
strongly compressed by perspective (drop moves away from the camera while falling; its apparent size
drops to ~0.58×). So pixel motion is NOT proportional to world motion; any metric answer needs the
depth_info and a focal-length estimate (e.g. from the drop's known size + depth), then back-projection
of the centroid, pixel size scaling ∝ 1/depth.

## Events
- Release: frame 0 (t = 0) the drop is pinching off — its top still touches the dropper tip; frame 1
  it is free. Treat motion start as ≈ frame 0.
- Leaves the image through the bottom edge after frame 9 (t = 0.15 s); absent from frame 10. No impact.

## Static objects (frame 12; ±20 px, soft frosted edges)
- Dropper tip opening centre ≈ (1045, 765), opening ≈ 85 px across.
- Bottle body: x 80–890, shoulder y≈400 to base y≈1395; width across axis ≈ 810 px, visible body
  length ≈ 1000 px; neck/threads y 0–360 cut by top edge; tilted ~10–15° (top to the left).
- Pedestal: top edge y≈1398; right vertical edge x≈980 (top) → ≈930 (image bottom), extends past left
  and bottom edges.

## Reliability / ambiguity
- Drop centroid: ±2 px frames 0–7; frames 8–9 the drop is darker/lower contrast and the mask is
  slightly ragged at the bottom (centroid ±4 px, size maybe 3–5 px small).
- Frame 0 mask may include a sliver of the neck at the tip contact (top y 738).
- The drop is transparent with refraction; the mask is its silhouette. Centroid ≈ origin of a small
  rigid drop.
- Only one moving object; no similar objects. No motion blur of note, no shadows on the drop's path.
