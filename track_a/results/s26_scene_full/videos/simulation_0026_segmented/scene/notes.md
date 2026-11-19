# simulation_0026_segmented – measurement record

Video: 960x960, 25 fps, 75 frames (t = frame/25, 0 … 2.96 s). Source: segmentation of a Blender 3D render;
the background is plain white, so only the two foreground objects are visible. All values are pixels / seconds.

## Files
- `scene.json` – inventory, camera/perspective cues, events, apparent-size summary.
- `tracks/boat.csv` – boat, every frame 0–74. Columns: bbox (x0,y0,x1,y1), bbox centre, mask centroid,
  `length_px` (bow→stern, horizontal extent), `height_px` (mast top→keel), `mast_top_y`, `keel_y`, `mast_x`
  (mean x of top 15 mask rows), `body_*` (boat without mast: cabin roof→keel), `hull_*` (from bow-tip row down to keel),
  `main_axis_len`/`across_axis_w` (PCA of whole mask – dominated by the mast, not very meaningful), area, occluded.
- `tracks/human.csv` – walking person, every frame 0–74: bbox, bbox centre, centroid, `feet_y`, `head_y`,
  `pelvis_est_x/y` (estimate: mean x of mask below its top 40 %, y = feet − 0.53·height), `height_px`/`width_px`
  (mask d>20), `core_height_px`/`core_width_px` (mask d>60), PCA extents, area, occluded.
- `scripts/track.py` (produces the tracks + `frames/overlay.png`), `scripts/summary.py`, `scripts/explore.py`, `scripts/crops.py`.

## Method
Mask = pixels with 255 − min(R,G,B) > 20. Human = pixels in a window around its previous position, cut at the
empty column separating it from the boat (gap ≈ 7 px at frame 0, grows afterwards). Boat = remaining mask pixels
in the largest blob after a 15 px closing. Overlays (frames 0, 20, 40, 60, 74) were inspected: both masks cover
the full objects (boat incl. mast, crossbar, rudder; human head to feet).

## Objects
- **boat** (red hull, white/grey wheelhouse, black funnel, tall mast with rotating crossbar). Moves left, bow first,
  for the whole clip, at ~4.0 px/frame (start) → ~3.5 px/frame (end); smooth, no stops. It also recedes: length
  261 → 228 px, total height 330 → 304 px, keel 633 → 619, mast top 304 → ~314, cabin roof fixed at y = 466.
  The origin is not visible; bbox centre, centroid, body centre and hull centre are all recorded (their x-shifts
  agree to ~1 px/frame). Bbox x is quantised to 1 px → per-frame dx jitters ±0.5–1 px; smooth over a few frames.
- **human** (white top, dark trousers, pale head), right of the boat. Walks slowly left (bbox_cx 559.5 → 521.5,
  ≈0.5 px/frame) and slightly toward the camera (feet y 580 → 590). Height: 54 px at frame 0, then 46–52 px (d>20);
  core 44–47 px (d>60). The pale head is faint against white, so head_y/height carry ±3 px error; legs swing so
  width varies 14–18 px. Per-frame dx is mostly 0 to −1 px (quantisation) – use long baselines.

## Camera / perspective
Camera assumed static (uniform white background; no reference to check pans, but motions are smooth).
Horizon ≈ y 466 (boat cabin roof stays there while points above/below converge toward it as the boat recedes).
Principal point assumed at the image centre (480, 480). No ground plane, vanishing lines or static objects visible.

## Events
No discrete events (no release, bounce, contact, start/stop or direction change). Both objects move from frame 0
to frame 74. At frame 0 the human stands right beside the boat's stern (closest approach in the image; they are not
necessarily at the same depth).

## Caveats
- Depth differs between objects (3D scene); any single px→m scale only holds for the object it was derived from.
- Boat mast crossbar changes apparent width (rotates) – excluded from size use; mask PCA extents are mast-dominated.
- Faint pink/grey halo around objects from segmentation; threshold 20 includes some halo (±1–2 px on extents).
