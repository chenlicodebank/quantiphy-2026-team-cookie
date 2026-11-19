# captured_0035bs — measurement record

Lab recording (24 fps, 49 frames, 1280x720, t = frame/24). The real background was replaced by a synthetic
blue-to-white vertical gradient (SAM2 demo; watermark box at x 1030-1280, y 690-720). Camera static (background
patch shift vs frame 0 < 0.1 px every frame).

## Scene
Two people kick two balls toward each other:
- **soccer_ball** (white with black pentagons) rests at the **front_person**'s foot (bottom centre-left, centre
  (437.5, 682.5), diameter 76 px, bottom touching the image edge) for frames 0-10, is kicked at frame 11-12 and
  travels up/right in the image, away from the camera (diameter shrinks to ~58-59 px at frames 24-26).
- **basketball** (orange) rests at the **rear_person**'s feet (upper right, centre (828.6, 280.0), diameter 52.8 px)
  for frames 0-11, is kicked at frame 12 and travels down/left toward the camera (diameter grows to ~72 px at 48).
- The balls cross at frames 24-27 (image overlap, soccer ball in front). Probable collision at frame 25
  (t = 1.042 s): the soccer ball's image y-motion reverses there and its size starts to grow again (comes back toward
  the camera, ending at (774, 525), diameter ~64 px); the basketball's downward image step drops from ~8 to ~4-5 px/frame.
- front_person turns and bends from ~frame 38-42 and puts a hand on the basketball from frame 45 (hand covers part of it at
  46-48); the basketball is still moving at the last frame. The soccer ball is still drifting slowly (2-6 px/frame) at the end.
- rear_person: visible only from the chest down (top edge cuts the body), shoes stay planted at y ~ 320-322.

No floor, walls, markings, horizon or vanishing points exist in the image (replaced background), so the only depth
cues are apparent sizes. For lab questions use f = 763 px, principal point (640, 360): a centre (u, v) with given
depth d (camera->centre distance) back-projects to d * r/|r|, r = ((u-640)/763, (v-360)/763, 1). The apparent
diameter of a ball of true diameter D at distance d is ≈ 763 * D / d (the radius columns allow checking given depths).

## Files
- `scene.json` — inventory, rest positions/sizes, events, camera.
- `tracks/soccer_ball.csv`, `tracks/basketball.csv` — every frame 0-48: `cx, cy` (circle centre, px), `radius_px`,
  `diameter_px`, `radius_px_med5` (5-frame running median, recommended for size/depth), circle bbox, raw mask extents
  (`mask_*`, mask clipped to the fitted circle + 3 px), `fit_inlier_frac`, `occluded` flag and `note`.
- `tracks/front_person.csv`, `tracks/rear_person.csv` — every frame: mask bbox (x0,y0,x1,y1,w,h), bbox centre, mask
  centroid, PCA main-axis length/width/angle, area, `cut_by_frame_edge` (always 1 for both people).
- `scripts/`: `bg.py` (median background), `track_balls.py` (initial tracking), `refine.py` (RANSAC circle fits —
  final ball centres), `assemble.py` (writes ball tracks, event diagnostics), `track_people.py`, `check_frames.py`
  (duplicate/dropped-frame and camera-motion check), `overlay.py`/`maskview.py`/`probe.py`/`pix.py` (diagnostics),
  `bg_median.png`, `raw_*.csv`, `fit_*.csv` (intermediate).

## Method
- Basketball: orange HSV mask (H<22, S>110, V>50), holes filled; soccer ball: |blur5(frame) − blur5(median bg)| > 8
  (its white panels differ from the near-white background by only ~10-15 grey levels), holes filled, basketball disc
  removed. Centre and radius = RANSAC circle fit to the mask outline (radius constrained near the running value),
  least-squares refined on inliers. Overlays of every frame were inspected (circle on the right ball and its full
  extent in all frames).
- People: |blur5(frame) − per-row gradient model| > 18, balls removed, components assigned by position. Overlays
  checked at frames 0, 12, 25, 36, 44, 48 — masks cover the full visible bodies.

## Reliability / ambiguities
- Basketball centre ±1 px, radius ±0.5 px (frames 24-27 lower-right occluded by soccer ball; 45-48 hand over it,
  fit still matches the outline).
- Soccer ball centre ±2-3 px, radius ±1.5 px (low contrast white-on-white, spinning panels). Frames 12-15 are motion
  blurred and partly merged with the shoe (fit at 15 slightly too large, r 39). Frame 33 looks ~3-4 px off (step 10 then
  1 px). Smooth over ≥5 frames before differencing.
- Frames 0-10: the soccer ball's bottom touches the image edge; the kicker's shoe touches it.
- **Dropped frames**: frames 12 and 36 change twice as much as neighbours and the basketball's image step doubles
  (11→12: 29 px; 35→36: 26 px vs ~13 px), so the source probably skipped one frame before frame 12 and before frame 36.
  Track times are nominal (frame/24) as the benchmark defines them; a per-frame speed at 12 or 36 will look ~2x.
- The collision is inferred from image motion; in-image overlap alone could be depth-separated passing.
- People references are mask bbox centre / centroid of truncated bodies (rear person headless in frame, front person
  cut at the bottom) — not true pelvis positions; heights in px are only of the visible parts.
