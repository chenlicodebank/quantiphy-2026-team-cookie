# simulation_0287 – measurement record

Video: Blender simulation, labelled **2D**, 2560x1440, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s).
Letterbox: black bars at rows ~0-79 and ~1361-1439. All units are pixels (x right, y down) and seconds.

## Scene
A static, side-on camera looks at a grassy field with a tree line behind. **One moving object**: a dark grey
VTOL fighter jet (Harrier-like, nose pointing left) that flies **right to left horizontally** through the
upper part of the frame (y ≈ 312-526). Three static grey-blue main battle tanks stand in the field, guns pointing
left, plus a small shell/projectile lying on the ground to their left. No people, animals or other vehicles move.

## Files
- `scene.json` – inventory (all objects, static extents, visibility), events, camera, perspective notes.
- `tracks/jet.csv` – the jet, every frame 0-71: `ref_x, ref_y` (reference point), `step_dx, step_dy`
  (displacement from the previous frame), mask bbox (`bbox_*`, clipped at the image edge), estimated full
  bbox x-range for clipped frames (`full_bbox_x0_est/x1_est`), PCA mask length/width, bbox length/height, mask area,
  `clipped_by_frame_edge`, `occluded` (always 0), `match_score`.
- `scripts/` – all measurement code: `track_jet.py` (median-background subtraction mask, camera-shift check),
  `template_track.py` (first rigid template attempt, superseded), `chain_track.py` (final frame-to-frame rigid
  matching), `build_record.py` (writes csv/json), `overlay.py`, `aligned_crops.py`, `zoom.py` (checks),
  `static_seg.py` (failed automatic tank segmentation; tanks measured by hand on zooms instead).

## Jet – how measured, reliability
- Per-frame displacement: the colour crop of the jet in frame k is matched (normalised cross-correlation,
  sub-pixel parabola fit) in frame k+1, only using the part inside the image. Scores 0.94-0.98 everywhere.
  Precision ≈ ±0.1 px per step.
- **Frame 0 → 1: no motion** (frames identical up to compression noise). From frame 1→2 on, the jet moves
  41.6-42.4 px/frame leftwards (mean ≈ 42.1); |dx| ≈ 41.6-41.9 near the image edges and ≈ 42.3-42.4 at the
  centre (frames 25-45) – a ~1.5 % perspective/appearance effect, essentially constant velocity.
  Vertical motion < 1 px over the whole clip (ref_y 420.1 → 419.0).
- Reference point (`ref_x, ref_y`): a rigid point integrated from the steps, anchored to the bbox centre during
  the side-on frames 28-40 (sits at the wing root, mid-fuselage). It is the best estimate of the object origin;
  the true Blender origin is unknown and could differ by ~10-20 px (constant offset, does not affect steps).
  ref_x lies outside the image (>2559) in frames 0-2 and (<0) from frame 65 on; values there are extrapolated
  from the visible part's rigid motion and are still reliable.
- Visibility: frames 0-71 (partially). Fully inside the frame frames 12-55. Enters on the right with nose
  visible at frame 0 (x0 = 2266); tail still visible at frame 71 (x1 = 118).
- Size: bbox height ≈ 214 px (fin top y 312 to lowest store/gear y 525-526), stable. Bbox x-length varies
  670-740 px over the fully-visible frames (≈716 at frame 12, minimum ≈670 at frames 26-30, ≈740 at frame 55)
  because the 3D model is seen slightly from the front on entry and slightly from behind on exit (silhouette
  extremes shift); the side-on value (frames 28-33) is ≈ 676-685 px (frame 33: x 984-1668, 685 px).
  The mask has small holes where the jet matches the background brightness, but bbox extremes were checked on
  overlays (nose, fin top, tail, under-stores all inside). For clipped frames, `full_bbox_*_est` adds the
  frame-12 length (entry) or frame-55 length (exit) to the visible edge – approximate (±20 px).

## Static objects (measured on zoomed crops of frame 70, ±3-5 px)
| name | hull x | overall x (incl. gun) | y top-bottom | length / height |
|---|---|---|---|---|
| tank_A_back_left (farthest, upper left of group) | 1283-1613 | gun elevated/foreshortened, muzzle x≈1323 | 1101-1205 | 330 / 104 |
| tank_B_front_centre (nearest, lowest) | 1601-1999 | 1502-1999 | 1159-1300 | hull 398, overall 497 / 141 |
| tank_C_right | 2035-2412 | 1957-2412 | 1115-1247 | hull 377, overall 455 / 132 |
| shell_on_ground (left of tanks) | 785-862 | – | 1204-1220 | 77 / 16 |
Heights include turret MG/antenna tops; bottoms partly hidden by grass. Tanks are at slightly different depths
(B nearest, A farthest), so their pixel sizes differ – one scale applies only to objects at the same depth.
Background: tree line (canopy from y≈560, base y≈1062), pale strip under the canopy y 1021-1062, taller tree
on the right (x≈1700-1900, top y≈360; the jet passes in front of it ~frames 10-25), field y 1062-1360.

## Camera
Static: phase correlation of the ground band vs frame 0 gives < 0.1 px shift in all frames.
Perspective: labelled 2D; the jet flies in a plane parallel to the image (constant pixel speed within 1.5 %,
constant height). The ground plane recedes upward (tanks at different depths); the jet's depth relative to the
tanks is unknown – do not assume the tanks and jet share a scale unless the question implies it.

## Events
- f0 (0 s): jet already entering on the right (nose in frame).
- f0→f1: jet stationary (duplicate frame); motion at full speed from f1→f2 (t = 0.083 s).
- f12 (0.5 s): jet fully in frame. ~f34-35 (≈1.42-1.46 s): ref point crosses image centre x = 1280.
- f55 (2.29 s): last fully visible frame; f71: tail still partly visible.
- No bounces, impacts, releases or direction changes.
