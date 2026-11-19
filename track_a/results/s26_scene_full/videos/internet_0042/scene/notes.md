# internet_0042 – measurement record

Top-down (near-nadir) drone shot of a suspension-bridge deck, monochrome, 2160x3840, 44 frames at 28.703764 fps
(t = frame/fps). Two cars drive straight down the image (+y) in the same left lane: **white_car** (upper, enters
at the top) and **dark_car** (lower, ahead of it, leaves at the bottom). No other moving objects. All values are
pixels / frames; no metric scale assumed.

## Files
- `scene.json` – inventory, static extents, events, camera summary.
- `tracks/white_car.csv`, `tracks/dark_car.csv` – one row per visible frame:
  - `cx, cy` – centre of the refined mask bounding box (= visible centre). `mask_cx, mask_cy` – area-weighted mask centroid.
  - `bbox_*`, `front_y` (bottom edge = front bumper, both cars face down), `rear_y` (top edge = rear bumper).
  - `length_px` (vertical extent = along motion), `width_px` (median body width over middle 60 % of length, no mirrors),
    `width_with_mirrors_px`, `area_px`. `height_px` empty (top-down view, no height visible).
  - `occluded`=1 when cut by the image border; then `cx,cy,length` describe only the visible part.
    `front_edge_valid` / `rear_edge_valid` say which bumper is actually seen. `est_full_cy` = estimated centre of
    the whole car (front_y − 457/2 for the white car in frames 0-10; rear_y + 472/2 for the dark car in 21-34).
  - `stab_*` – same points mapped to frame-0 background coordinates with the camera similarity transform.
  - `tm_cx, tm_cy, tm_score` – template-matching centre (template from frame 25 white / 10 dark). Good for the
    white car (all frames); for the dark car only frames 0-20, blank afterwards.
- `scripts/camera_motion.csv` – per-frame similarity transform frame i → frame 0 (LK flow on a background grid,
  cars masked, RANSAC; residual ~0.3-0.6 px). `scripts/camera_shift.csv` – translation-only phase correlation (superseded).
- `scripts/road_width_vs_y.csv` – kerb positions, deck width and lane-line x per image row at frames 0, 20, 43.
- `scripts/*.py` – track.py (coarse background subtraction), track2.py (boxes), camfit.py (camera), refine.py
  (intensity masks → final extents), tmatch.py, perspective.py, finalize.py, viewcars.py (overlay check).

## Key numbers
- white_car: full length 457 px (frames 11-17, bumper to bumper); body width 172, with mirrors 196. Visible 0-43,
  fully from frame 11. Front edge advances 27-29 px/frame early, ~33-35 px/frame at the end (apparent speed rises).
  Centre x 1050 → 1036.
- dark_car: length ~472 px (median frames 0-20; 458-491, grows with y); body width 203, mirrors 214. Fully visible
  0-20, front at bottom border from 21, last sliver 34. Rear edge advances steadily 36.5 px/frame (35-38).
- Gap between the cars (frame 0): white front_y 152 → dark rear_y 2583.
- Deck (between inner kerb edges, frame 0): 1317 px at y=100, 1373 at y=1900, 1474 at y=3700.
  Cars' lane width ~375 (top) → ~414 px (bottom).

## Camera
Static (<1 px) for frames 0-23. From ~frame 24 a slow zoom-out (drone climbing or zoom): image scale relative to
frame 0 shrinks by 2.4 % by frame 43, plus ≤8 px drift. Compensated positions are in `stab_*`. For speeds, image
displacement differences between raw and stabilised are ≤ ~1 px/frame in y for the white car late in the clip.

## Reliability / ambiguities
- **Perspective**: the view is not perfectly nadir; ground scale rises ~12 % from top to bottom of the frame. A single
  planar scale (benchmark convention) is therefore approximate; the dark car (bottom) appears ~3-5 % longer than the
  white car would at the top. The white car's apparent length nevertheless shrinks slightly as it moves down
  (457 → 446 stabilised) – likely viewing-angle effects on the car's 3D shape; treat car lengths as ±2 %.
- White car mask is clean (bright car on grey road), edges ±2 px. Best reference point: `cx,cy` (frames 11-43) or
  `front_y` (all frames).
- Dark car: the dark front bumper merges with its shadow/the dark road, so `front_y` and `length_px` jitter ±10-15 px
  frame to frame; `rear_y` (light roof rails/rear window boundary) is clean (±2 px) and is the best reference for its
  motion. Its `cy` inherits the front-edge noise; smooth or use rear_y + 236.
- Both cars' mirrors are excluded from `width_px`. No occlusion between objects; only frame-edge cuts.
- Earlier coarse background-subtraction boxes were ~35 px too large (halo); final values come from refine.py.
