# internet_0051 — rider on e-scooter crossing a parking lot

1920x1080, 30 fps, 50 frames (t = frame/30, 0–1.633 s). Internet footage, 2D (planar) scene.

## Content
One moving object: a **person standing on a black kick e-scooter** (grey-blue top, dark trousers, cap, blurred face)
riding right-to-left in front of a row of parked cars. Visible and unoccluded in all 50 frames; moving the whole clip
(no start, stop, bounce or turn). Static: parked cars (blue Subaru, brown Jeep, green Fiat 500, white Elantra, others),
a tree in a curbed planter island at image centre, three light poles, palms, a building, a dark out-of-focus object at
the right edge. Pixel boxes for all of these are in scene.json (frame-0 coordinates, eyeballed from 2x grid views,
±5 px).

## Files
- `scene.json` — summary: camera, rider positions/sizes, static object boxes, events.
- `tracks/rider_scooter.csv` — one row per frame: `cx_bg, cy_bg` = centre of the rider+scooter bounding box in
  frame-0 (pan-removed) coordinates (**use this as the reference point**); `_img` = the same point in raw image
  coordinates; bbox; `length_px` = horizontal extent = scooter wheel-to-wheel length (the main motion axis);
  `height_px` = cap top to wheel bottom; mask centroid; `tm_scooter_dx_bg` = cross-check displacement from template
  matching of the scooter band; `pan_dx/pan_dy` = camera shift vs frame 0; `edge_unreliable` = frames where a tyre edge
  was partly lost (width >4 px off trend: 21, 25, 27, 35, 46, 48, 49). `occluded` is 0 everywhere.
- `camera_shift.json` — phase-correlation shift of 4 static patches for each frame vs frame 0.
- `scripts/` — camera.py (pan), track.py (median-background subtraction on pan-compensated frames → mask/bbox),
  track2.py (frame-to-frame template matching), overlay.py (drawing masks for checks), build.py (writes the CSV).
  To rerun, go to scene_ws and run camera.py, track.py, track2.py, build.py in that order (scratch output goes to frames/).

## Measurements and reliability
- Camera: **slow pan**, content drifts +14 px in x over the clip (~0.29 px/frame) and up to +1.6 px in y. The
  rider moves ~17.6 px/frame, so the pan is ~1.6% of the motion. All `_bg` values have the pan removed.
- Rider motion: cx_bg goes 1414.5 → 551.5 (−863 px in 49 frames); mean −17.61 px/frame (first 10 frames −17.55,
  last 10 −17.85, so speed is nearly constant). Per-frame jitter from the bbox edges is ±1–2 px, so smooth over a
  few frames before differencing. Template matching gives −854 px net (about 1% less, probably pulled toward 0 by
  background pixels in the template); the bbox centre is the main value.
- Scooter length (wheel edge to wheel edge, the natural "pixel length along the motion"): mask 190 px (frames 0–9),
  192 px (frames 40–49), median 188; zoomed visual reads give 192 px at frame 0 and ~198 px at frame 49. The mask
  slightly under-reads dark tyres on dark asphalt. **Best value ≈ 192 px (range 188–198)**, getting ~3% larger by the
  end because the rider drifts a little toward the camera (bottom y 877 → 880).
- Heights: rider+scooter 322 px (cap top to wheel bottom, very stable); rider alone, cap to shoe soles, ~300 px; handlebar
  ~200 px above the ground; wheel diameter ~45 px (rough).
- Masks checked visually on frames 0, 25, 35 and 49. The bbox covers the cap, handlebar stem and both wheels. The mask
  has holes inside the dark trousers, so the mask centroid sits low or off-centre; use the bbox centre instead.
- No shadow issues: the rider is in the shaded foreground lane, so there is no separate cast shadow to remove.

## Ambiguities
- "Length" of the object: the scooter wheel-to-wheel (~192 px) is the main-axis length. The rider's body width is ~60–90 px.
- Rider height questions: 300 px if measured from cap to soles, ~322 px if the scooter/wheels are included.
- Pan correction is tiny; using raw image coordinates instead changes the displacement by +14 px (1.6%).
