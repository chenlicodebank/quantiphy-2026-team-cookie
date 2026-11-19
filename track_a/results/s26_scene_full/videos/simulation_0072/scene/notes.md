# simulation_0072 — measurement record (pixels, seconds)

Video: 2160x1080, 24 fps, 72 frames (t = frame/24; last frame 71 = 2.958 s). Source: simulation, **2D** scene.
View: straight top-down onto a 4-way street intersection (grey roads, beige sidewalks). The ground plane faces the
camera, so one metres-per-pixel scale (from whatever prior a question gives) applies to all ground-level motion.
Camera is **static** (zero frame-difference on all static props over the whole clip; background shift 0 px).

## Files
- `scene.json` — inventory, static-object pixel boxes, moving-object summaries, events, camera.
- `tracks/cyclist.csv`, `tracks/pedestrian.csv` — every frame 0..71: `frame, time, cx, cy` (mask centroid = reference
  point), `bbox_x0..y1` (inclusive pixel box), `bbox_cx, bbox_cy`, `mask_len` / `mask_wid` (min-area-rectangle long /
  short side of the mask, px), `area` (px), `occluded` (0 everywhere).
- `scripts/` — `diff.py` (find movers), `track.py` (tracking), `overlay.py` (check images into frames/),
  `static.py`, `ball.py` (static props, per-frame steps), `write_scene.py` (builds scene.json),
  `rename_and_rebuild.py` (housekeeping).

## Moving objects (only two things move)
1. **cyclist** — person on a bicycle riding up the image (-y, "north") on the vertical road, lane x ≈ 918.5.
   Seen from above: front wheel at the top, rider, rear wheel at the bottom. Mask length along travel 61 px (58–63),
   width across 19 px (17–20). Centroid y: 829.3 (frame 0) → 205.0 (frame 71); ≈ 8.9 px/frame (≈ 214 px/s),
   per-frame steps 7.8–10 px (mask noise ±1 px), no trend → constant speed. Fully visible all frames.
2. **pedestrian** — small person walking to the right (+x) along the lower-right sidewalk at y ≈ 844 (white
   shirt/shoulders, dark head, seen from above). Mask ≈ 23–32 px along x (arm/leg swing), 13–23 px across.
   Centroid x: 1331.8 (frame 0) → ≈ 1474 (frame 71); ≈ 2.0 px/frame (≈ 48 px/s) average, per-frame centroid steps
   noisy (0.4–4.4 px) because of gait; smooth over several frames before using. Passes just below the lamp post
   at x ≈ 1416 around frames 35–45 (not occluded; lamp base nearby can slightly perturb the mask).

Reference point: mask centroid (top-down view, so centroid ≈ pelvis / bike root projected on the ground plane).
Tracking: per-object ROI, median background over all 72 frames, |diff| > 25, small morphology; overlays checked
visually at frames 0, 20, 40, 60, 71 — boxes cover the full cyclist and full pedestrian.

## Events
- Frame 1 is essentially identical to frame 0 (both movers displace ~0 px between frames 0 and 1); steady motion
  from frame 1 → 2 onward. A one-frame backward-difference speed at frame 1 will be ~0.
- No stops, turns, bounces, contacts or direction changes; both move until the clip ends.

## Static objects (frame 71, px boxes [x0,y0,x1,y1])
- Vertical road x 616–1081 (466 px wide); horizontal road y 290–755 (466 px wide); four beige sidewalk blocks at
  the corners with rounded curbs.
- white ball on horizontal road: centre (2028.7, 432.5), diameter ≈ 19 px (white disc 2020–2038 × 423–441), shadow left. Static.
- grey rock cluster on road: [2027,596,2092,651] (66×56 px), centre (2063,622). Static.
- dark square (grate/pit) top-right sidewalk: [1234,27,1321,117] incl. reddish rim (~88×91; dark interior ~80×80).
- brown square patches (~84×80): [369,182,452,260], [369,808,452,890], [1177,806,1258,885].
- street lamps (Y-shaped, 2–3 heads from above), 4 along each curb: top row y 184–243 at x 167–237, 1395–1430,
  1704–1760, 2014–2089; bottom row y 784–842 at the same x ranges.
- bench/rack props at sidewalk corners: [516,196,573,252], [1140,200,1191,240], [508,786,576,827], [1114,801,1146,856].
- green/teal round object (bin/hydrant): [1330,794,1355,818], centre (1342,806).

## Reliability / ambiguities
- Cyclist track: good (±1 px). Pedestrian: centroid noisy ±1–2 px per frame due to limbs and small size; the mask
  extents vary with gait — use median sizes. Object identity labels (cyclist vs. "person", lamps vs. racks, bin)
  are visual interpretations of a small top-down render; check against the question's wording.
- Sizes are top-down footprints only (no height visible in this view).
