# simulation_0115_segmented — measurement record

2D segmentation video (Blender render, background replaced by white), 1920x1080, 24 fps, 37 frames (t = 0 … 1.5 s).
Top-down view of a small **boat** (leaf/lens-shaped dinghy, grey-blue rim, light planked interior, pointed end to the right)
moving **left (-x)** alongside a static wooden **dock** (long pinkish-brown planked rectangle above it). No other objects.
Camera static. All values are in pixels and seconds; no metric scale has been assumed.

## Files
- `scene.json` – inventory, static sizes, camera, relations, events.
- `tracks/boat.csv` – boat, every frame 0–36: `frame, time_s, cx, cy` (mask centroid = reference point/origin),
  bounding box `bbox_x0..y1` (inclusive pixels), `bbox_w, bbox_h`, `length_px` / `width_px` (mask extents along / across
  its principal axis), `axis_angle_deg` (principal axis, image coords, y down), `area_px`, `occluded` (always 0).
- `tracks/dock_check.csv` – dock centroid/bbox/extents per frame (used to confirm the camera is static).
- `scripts/measure.py` – the whole measurement (threshold non-white pixels, max(255-RGB) > 40, 3x3 opening,
  connected components > 2000 px; component with mean y < 600 = dock, other = boat; PCA for axis extents).
  Overlays (contour + centroid) for frames 0, 18, 36 were checked visually: masks cover each full object, no merging.

## Key numbers
- Boat size (frame 0, sharpest): length 226 px along its axis, width 89 px (bbox 225 x 88). Mask length shrinks to
  ~216 px by the end as the boat moves faster (soft/blurred pointed tip) — prefer the early-frame ~226 px for the
  length prior; width is stable 87–90 px.
- Boat motion: x from 1452.5 (f0) to 1150.6 (f36), y constant 643 ± 0.5, no rotation (−3.2 ± 0.3°). Per-frame x step
  grows roughly linearly from ~3.5 px (f0→1) to ~12 px (f35→36): steady speed-up throughout. Net displacement 301.9 px;
  path length ≈ the same (straight line), but compute from the CSV.
- Dock (static): length 574 px, width 97 px, axis −1.05° (right end slightly higher), centroid (1201.5, 539.5),
  bbox x 913–1486, y 487–590.
- Boat centre passes the dock centre in x between frames 31 and 32 (t ≈ 1.30–1.33 s). Boat's right end reaches the dock's
  right end at frame 14. Gap hull–dock ≈ 9 px; no contact.

## Events
Motion already under way at frame 0 and still accelerating at frame 36: no start, stop, bounce, contact or direction change.

## Reliability / caveats
- Centroid noise ≈ ±0.5 px per frame (segmentation edge and compression), so one-frame differences of the centroid
  carry ~±0.7 px/frame noise (e.g. f16→17 step 8.9 vs neighbours ~7.5–8); smooth or fit if a question allows.
- The centroid of the top-view mask is taken as the object origin; for a symmetric hull this is the geometric centre.
- Dark post shadows along the dock edges are included in the dock mask (they are part of the rendered object outline).
- 2D scene: use a single metres-per-pixel scale from whichever object the prior names (boat length 226 px / width 89 px,
  or dock length 574 px / width 97 px, or the boat's pixel speed/acceleration from the CSV).
