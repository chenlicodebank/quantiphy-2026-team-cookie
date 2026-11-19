# simulation_0031_segmented — measurement record

3D Blender scene, segmentation version (background replaced by flat white), 960x960, 25 fps, 75 frames (t = frame/25).
All values in pixels / frames. No metric scale assumed.

## Objects (all three move; no static objects / ground features visible)
- **boat** — large red-hull, white-cabin fishing boat with tall mast and a dark crane arm, lower left. Moves left
  (~4 px/frame) and slightly up (~1.6 px/frame) while slowly shrinking (bbox h 453 px at f0 → ~430 px at f50), i.e.
  moving away from the camera. Seen 3/4 from front-right. Stern clipped by the left image edge from f54 to f74.
- **human** — small walking man (white T-shirt, dark trousers) right of centre. Walks left and slightly toward the
  camera (centroid 755,602 → 665,642). Height in image 67–78 px (median ~73), roughly constant; visible all frames.
- **bird** — dark flapping bird, flies right and slightly down (~11–14 px/frame), exits the right edge f54–f58,
  absent from f59. Wing-flap period ~12 frames. Image wingspan (bbox_w) max ~70 px (f31–33), min 30 px (wings up).

## Files
- `scene.json` — inventory, visibility ranges, sizes, events, camera notes.
- `tracks/boat.csv`, `tracks/human.csv`, `tracks/bird.csv` — one row per visible frame: frame, t, mask centroid (cx, cy),
  bbox centre, bbox x0/y0/x1/y1, bbox_w/h, mask area, PCA main-axis length/width/angle, touches_edge (clipping flag).
  boat extra: bow tip (bow_x/y, rightmost hull pixel), mast top, keel bottom, and **ref_x/ref_y** = edge-robust
  reference (bbox centre when unclipped; for f54+ extrapolated from the bow with a mast-to-bow scaled offset,
  tested on unclipped frames: mean 3 px, max 9 px error). human extra: head_top_y, feet_y.
- `scripts/track.py` (segmentation + tracking + overlays), `scripts/boat_ref.py`, `scripts/explore.py`.

## Method
Mask = pixels with min(R,G,B) < 248 (background is 255), 2x2 opening, components grouped after 25 px dilation;
largest group = boat (+ pieces inside its box, e.g. the detached crane arm), nearest to previous position = human,
remaining = bird. Overlays checked at f0,10,…,74: masks cover the correct objects and their full extents.

## Reliability / ambiguities
- Camera: assumed fixed (simulation convention); cannot be verified because the background is blank. No horizon or
  ground plane; depth only from given depth_info and apparent size.
- Boat: white parts close to background brightness → mask has holes (area underestimates) but bbox is good (±2 px).
  The Blender origin is not visible; bbox centre includes the mast so it lies above the hull centre (hull spans roughly
  y 690–920 at f0). Bbox y1 occasionally jumps a few px (f57). After f53 bbox width/centroid are clipped — use ref_x/ref_y,
  bow and mast-top columns.
- Human: pale head/face partly blends into background; head top may be 1–3 px above the recorded y0. Small object
  (~73 px), so centroid noise ~1–2 px; gait makes bbox h/w oscillate.
- Bird: shape changes strongly with flapping, so centroid wobbles ±3 px vs. the body; wingspan/width min-max over the
  flap is in scene.json. f54–58 clipped at the right edge (centroid biased left/unreliable).
- Speeds/accelerations deliberately not computed.
