# simulation_0156 – measurement record

Clip: Blender render, 2D scene, 1920x1080, 24 fps, 48 frames (t = frame/24, 0–1.958 s). Underwater scene,
**static camera**. Two animals swim right-to-left; the seabed and the water are static scenery.

## Files
- `scene.json` – inventory, pixel sizes, events, camera, summary numbers.
- `tracks/shark.csv`, `tracks/turtle.csv` – one row per frame (0–47). Columns:
  `frame, t_s, visible, truncated_edge` (L/R/T = mask touches that image border, so the object is cut off),
  `cx_mask, cy_mask` (mask centroid = reference point / origin proxy), `cx_bbox, cy_bbox`,
  `x0,y0,x1,y1` (bbox, inclusive px), `bbox_w, bbox_h`, `axis_len, axis_wid, axis_angle_deg` (PCA main axis
  extent of the mask; angle in image coordinates, y down), `area_px`, `occluded` (always 0 – the animals never
  overlap and nothing passes in front of them).
- `scripts/bg.py` (median background + camera check), `scripts/bg2.py` (background re-estimated excluding object
  pixels), `scripts/seg.py` (segmentation trial), `scripts/tracks.py` (final masks, CSVs, overlays). Scripts write
  scratch to `../frames/` (outside the record). Run from the scene_ws folder in that order.

## Method
Per-pixel background from frames where the pixel is not covered by an animal; per frame, max-channel |frame − bg| > 7,
open 5x5, close 9x9, rows y ≥ 790 (seabed caustics) excluded; components with centroid y < 450 = shark, below =
turtle. Overlays at frames 0, 6, 12, 18, 23, 24, 36, 40, 46, 47 checked by eye: the masks cover both animals incl.
fins/flippers.

## Objects
- **shark** – big grey-blue shark, upper half (centroid y ≈ 322, constant). Visible frames 0–46; fully in frame only
  14–30 (enters at the right edge until frame 13, nose leaves the left edge from 31, only tail tips at 46, gone at 47).
  Full-view size: nose-to-tail-tip length ≈ 911 px (median of frames 14–30, range 883–928), height dorsal-fin tip to lower
  tail-lobe tip ≈ 273 px (270–282), horizontal. Motion: uniform leftward, tail-tip x1 changes by ≈ −57 px/frame
  (−52…−61), no vertical motion.
- **turtle** – blue ridged-shell sea turtle (leatherback-like), lower-middle (centroid y 549–580). Visible all frames,
  cut by the right edge in frames 0–9, fully visible 10–47. Leftward ≈ −21 px/frame (centroid 1715→930 over frames
  10–47). Pose changes: oblique view with a flipper hanging down early (bbox ≈ 345 x 240 px, frames 11–19), side-on
  later (bbox ≈ 300–340 x 130 px, frames 37–47). Flipper strokes change the extents by ±20 px.
- **seabed** (static): pale dunes from y ≈ 800 (crest, x 800–1100) to the bottom edge, full width; animated caustic
  patches. **water** with animated light shafts. No other objects.

## Events
Nothing starts or stops: both animals swim the whole clip. Shark fully in view frames 14–30, exits left by frame 47;
turtle fully in view from frame 10. No contacts, bounces or direction changes. The turtle's pose changes from about
frame 20 to frame 37 (centroid y drifts 580 → 552).

## Reliability / ambiguities
- Shark snout (light grey, translucent-looking head) is low contrast against the water: x0 jitters by about ±30 px, so
  shark length is ±~20 px. The tail end x1 is crisp (±2 px), so it is the best edge for shark motion. The mask centroid
  is only a true centre in frames 14–30. In cut-off frames it is biased toward the visible part. For speed in other
  frames, use x0 (frames 0–13) or x1 (frames 31–45) differences.
- Frames 22–25: a faint water-light blob touched the shark's belly. The mask is clipped at y < 442, so bbox_h there
  (≈ 281) is ~8 px too big. Shark frame 46 is only the upper tail lobe, and the detached lower lobe is missing.
- Turtle: the light-coloured front flipper is sometimes partly missed (e.g. frame 36), and the oblique pose in early
  frames makes bbox size and centroid vary with pose, not only with motion. The centroid is good to about ±5 px.
- 2D scene: both animals swim in planes facing the camera. One px→m scale from the prior object applies (shark
  ~911 px long, turtle ~310 px long side-on), unless a question implies different depths. The shark appears much
  larger than the turtle, which is consistent with a real-size difference. No perspective change of the apparent size
  over time (the shark's full length stays constant, frames 14–30).
- Mask extents are silhouettes incl. fins/flippers, not world AABBs. Real AABB extents may differ slightly.
