# simulation_0035 – measurement record

This is a 3D Blender render: 1080x1080 px, 24 fps, 72 frames (3.0 s). Time t = frame/24. **Frames 0 and 1 are
pixel-identical** (the first frame is duplicated), so the first one-frame displacement is zero. Use frame 1->2 for the start of motion.

## Scene
The view is a sea / beach landscape. The sea fills y 708-1080 and a sand-dune backdrop sits behind it (y ~625-708) under a
cloudy sky. Bottom-left are a pale rock slope, a sandstone ledge, a dark wooden structure and a light sand strip at the water's edge.
Two objects move: a **bird** (dark, flapping) that flies left to right across the sky just above the dunes, and a
**person** (white top, grey/blue trousers) who walks rightward along the sand strip. Both are visible in all 72 frames. Nothing else
moves. The water ripples are effectively frozen.

## Files
- `scene.json`: inventory (moving and static objects with pixel extents), camera, perspective cues, events, and track column definitions.
- `tracks/person.csv`: per-frame pelvis estimate (`ref_x, ref_y`), sole point (`foot_x, foot_y`), head top, mask centroid, bbox,
  width/height in px, area, occlusion flag.
- `tracks/bird.csv`: per-frame mask centroid (`ref_x, ref_y`, the recommended origin proxy), bbox centre, dark-body centroid, bbox,
  horizontal span (wingspan proxy), height, PCA length/width, area, occlusion flag.
- `tracks/*_raw.csv`: first-pass tracks (no row filtering; person bbox bottom sometimes includes the reflection). Superseded; kept for reference.
- `scripts/`: `common.py` (decoding helpers), `motion_map.py` (median background, motion map, camera-shift check),
  `track.py` (first pass), `finalize.py` (final tracks and overlays), `view_*.py` (inspection crops).
  `finalize.py` needs `frames/median_gray.png` from `motion_map.py`.

## Method
- Background = per-pixel median of all 72 grey frames. Each object is segmented as |frame − median| > threshold (bird 30, person 18)
  inside its own region (bird: y 480-690; person: x 90-260, y 690-757), followed by a 1-iteration closing, keeping the largest blob plus
  blobs within 30 px of it.
- Person: rows with ≥2 mask pixels, gaps up to 6 rows allowed (the trousers sometimes blend into the background). Below the knees, a gap of ≥4
  rows cuts off the faint reflection on the wet sand (y ~751-755).
  The pelvis is **estimated** at 0.53·(height−1) above the sole row. Its x is the mask mean in that row band.
- Bird: the mask centroid is used as the origin proxy. The bbox centre and the darkest-pixel centroid are also given. These differ by up to a
  few px depending on the wing pose.
- Overlays checked visually (`frames/ov_*.png`, `frames/trajectories.png`, `frames/person_traj.png`): boxes cover the full
  bird and the full person from head to soles. The person's reflection is excluded.

## Key numbers (px)
- Person: pelvis x 128.4 -> 201.6 (frames 0 -> 71), steady, about 1.03 px/frame in image x; soles y 745 -> 751. Height 41 px median
  (range 39-43; ±1 px pixelisation). The height is essentially constant, so the camera distance barely changes. Width 11-20 px, varying with the stride.
- Bird: centroid x 55.5 -> 652.4, y 583.6 -> 598.2. The path has a ±8 px vertical wave tied to the wing phase. Horizontal span 18-31 px
  (largest with the wings level). Peak span is ~30-31 px in the first half and ~25-28 px in the second half, and the image-x step falls from ~9.5 to ~7.6 px/frame,
  so the bird is probably receding slightly. Treat this as a perspective hint, not a measurement.

## Camera / perspective
The camera is static (sub-0.02 px shifts). The focal length is unknown, so use the question's depth_info together with a known size to get it, assuming the principal point is at (540,540).
The far water edge is at y ≈ 708. The true horizon is hidden by the dunes (so it is at y ≤ 708). The objects are small and distant, so pixel
quantisation (±0.5-1 px on sizes of ~20-40 px) is the main error source: ~2-5% on sizes.

## Ambiguities / reliability
- Pelvis height is a body-proportion estimate (±2 px). Its x is good to ±1 px. The mask centroid (cx, cy) is an alternative.
- The bird's origin is uncertain by ~2-3 px because of the wing pose. Its wingspan is best taken from `span_x_px` at the wings-level frames
  (5-6, 30-31, 54, 62-64: 25-31 px). Min/max "width during flight" = min/max of `span_x_px` (18 / 31 px). Caution: at frames
  32 and 55 the edge-on wings are only 1-2 px thick and partly drop out of the mask, so the span reads low (19-20 px). These are
  segmentation losses, not real minima. The true minimum span occurs with the wings raised (~18-20 px at frames 9-14, 21-24, 44-48).
- Person reflection: the water/wet sand under the person shows a faint mirrored copy. It is not a separate object.
- There is no occlusion, motion blur is negligible, and there are no contacts or impacts. Both objects move throughout, with no start or stop inside the clip.
