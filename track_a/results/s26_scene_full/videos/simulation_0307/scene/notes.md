# simulation_0307 – measurement record (pixels, seconds; no metric scale)

Video: 2560x1440, 24 fps, 72 frames (t = frame/24, last frame 71 = 2.958 s). Simulation, 3D scene.
Letterboxed: black bars at rows 0..~80 and ~1360..1439.

## Scene
Elevated, oblique, **static** camera looking down onto a forest clearing (grey ground with pale gravel patches,
tree line at the top and right, two sparse trees at lower left). One moving object: a dark grey **aircraft**
(VTOL jet/gunship with twin wings, ducted-fan rings, camouflage cockpit pod on top). Three static grey
**battle tanks** on the ground below/left of the aircraft start.

## Files
- `scene.json` – inventory, static-object pixel boxes, camera, events, apparent-size summary.
- `tracks/aircraft.csv` – one row per frame 0..71: `cx,cy` (raw mask centroid), `hull_cx,hull_cy`
  (centroid of the filled convex hull of the mask – **recommended reference point / origin proxy**),
  `hull_area`, `bbox_cx,bbox_cy`, bbox `x0,y0,x1,y1,bbox_w,bbox_h`, `mask_area`, `main_axis_len`
  / `cross_width` (PCA extents of the mask; main axis is ~horizontal in the image, i.e. roughly the wingspan
  direction as seen), `main_axis_deg`, `height_px` (= bbox_h), `occluded` (always 0).
- `scripts/bg.py` – camera-motion test + median background (`scripts/bg.png`); `scripts/track.py` –
  segmentation/track + tank change check (`scripts/tank_motion.json`); `scripts/summarize.py` – writes scene.json.

## Method & reliability
- Camera: phase correlation of four background corners vs frame 0 → max shift 0.011 px. Static.
- Aircraft: |frame − median background| > 18, morphological clean-up, components near the largest blob.
  Overlays (frames 0, 12, 24, 36, 48, 60, 71) confirm the box hugs the full aircraft (wingtips, fins, nose
  pods). The mask has holes where dark wings match dark ground/trees, so the raw centroid `cx,cy` is biased;
  the hull centroid and bbox centre are robust (agree within ~10–25 px; the bbox centre is skewed by the
  asymmetric fin/wingtip silhouette). Box edges ±2–3 px; per-frame centre steps carry ~±3 px jitter, so
  smooth over several frames for speeds.
- Aircraft motion: frames 0 and 1 are identical (motion starts after frame 1, t = 0.042 s). After that it moves
  steadily up-left in the image (~−150°, y down), receding from the camera: pixel step ~21 px/frame at the
  start falling to ~9 px/frame at the end (largely perspective). Hull centre goes (1696.6, 857.8) → (782.5, 350.2).
  Apparent size shrinks monotonically: bbox 651x283 px (frame 0) → 440x141 px (frame 71); 1/bbox_w is
  near-linear in frame (fit residual < 3 %), consistent with steadily increasing depth. Attitude nearly
  constant (main axis ~176° all clip). No bounce, contact, turn or stop.
- Tanks: static (crops at frames 0 and 71 are identical; small mean-difference variation, ≤5 grey levels, is
  lighting/shadow from the aircraft passing over). Pixel boxes measured by eye on unscaled crops, ±8–10 px:
  - tank_middle (upper of three, gun up-right): bbox (1248,978)-(1450,1112), centre ~(1350,1050), hull length
    along its axis ~210 px.
  - tank_left (lower-left, gun up-left): bbox (988,1115)-(1202,1280), centre ~(1095,1215), hull ~225 px.
  - tank_right (lower-right, closest, gun up-left): bbox (1378,1195)-(1622,1360) – bottom cut by letterbox;
    centre ~(1500,1295), hull ~250 px.
- Ambiguities: three near-identical tanks – identify by position (middle/upper, lower-left, lower-right).
  Focal length unknown: use the given depth_info with a known size (f ≈ pixel size × depth / world size;
  for the aircraft use bbox_w at the same frame, noting it is a projected oblique silhouette) and check by
  reproducing other given depths. No motion blur of consequence; no occlusion of the aircraft.
