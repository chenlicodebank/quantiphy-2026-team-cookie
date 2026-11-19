# simulation_0079 – measurement record (pixels, seconds; no metric scale)

Video: 1920x1080, 24 fps, 72 frames (3.0 s), simulation, 2D. t = frame/24. Pixel coordinates: x right, y down,
origin top-left, full resolution.

## Scene
Static top-down (bird's-eye) camera over a plain uniform grey floor. No static objects or markings. Two moving people,
both going right -> left (-x) in straight lines, never touching or overlapping:
- **cyclist**: rider in a black jacket on a light-cyan bicycle (front wheel leading, rear rack), lower lane (bike axis
  y ~ 648). Visible frames 0-40, fully in frame 4-32, partly cut by the right edge in 0-3 and by the left edge in 33-40, gone from 41.
- **walker**: man in a white/light-grey T-shirt, jeans, black sneakers, upper lane (head y ~ 429-438). Visible in all
  72 frames (cut by the right edge in 0-2).

## Files
- `scene.json`: inventory, camera, sizes, events, summary pixel motion.
- `tracks/cyclist.csv`: per frame 0-40: `bike_center_x/y` (reference point = midpoint of the cyan front and rear tips,
  used as the vehicle-root proxy; frames 0-3 use front tip + 205.5, frames 33-40 use rear tip - 205.5, from the median length of 412 px),
  front/rear tip x, cyan bike bbox, bike length/width (only when fully visible), `rider_torso_x/y` (centroid of the dark
  jacket+hair blob, a pelvis/saddle proxy, ~28 px behind the bike centre), rider+bike union bbox and PCA extents, truncation flag.
- `tracks/walker.csv`: per frame 0-71: `head_x/y` (hair-blob centroid, main reference point), `shirt_x/y`
  (light-shirt centroid), mask centroid, bbox, PCA length/width/axis angle, truncation flag. Frames 0-1 head is
  extrapolated because the head is cut by the edge (flagged in `note`).
- `tracks/*_raw.csv`: raw per-object segmentation output (bicycle = cyan pixels only; cyclist = rider+bike union).
- `scripts/`: `segment.py` (median background + threshold/saturation masks, overlays), `points.py` (tips, head blob,
  shirt), `assemble.py` (final CSVs), `check.py` (summary checks).

## Key measurements
- Bicycle length tip to tip: 412 px (range 408-418; it is ~2% longer near the right of the frame than near the left, so the
  camera is slightly tilted or the lens is not quite uniform). Handlebar y-extent ~100 px, up to 124 px including the pedals. Rider+bike y-extent 126 px.
- Cyclist pixel motion: constant velocity, -51.3 px/frame (fit over frames 1-40; per-frame diffs 50-52 px).
- Walker head: mean -14.4 px/frame (1912 -> 904 from frame 0 to 71). The per-frame values swing between 12.4 and 16.9 with the
  17-frame step cycle. Lateral sway is ±4 px in y over a 34-frame cycle.
  Feet are widest apart (bbox x-extent ~239 px) at frames 9, 26, 43, 60 and together (~101 px) at 17, 34, 51, 68.
  The bbox y-extent (shoulders + arms) is 127-146 px. Head (hair) ~50 px across. Standing height cannot be seen in a top-down view.
- Events: no starts, stops, contacts or turns. Bike fully visible from frame 4 to 32, front edge reaches the left edge at frame 33, last visible
  at frame 40. The object positions in frames 0 and 1 are identical (repeated first frame, codec noise only), so the
  motion between frames 0 and 1 is zero.

## Reliability and ambiguities
- Bike tips: ±1 px per frame (thin wheel rims, anti-aliasing). Very reliable for speed.
- Walker head blob: ±1-2 px. The head is not the pelvis. Perspective pushes elevated points radially away from the image
  centre (the head sits right of the shirt centre near x~1700 and is centred near x~1060), so head and pelvis can differ by about
  10-25 px near the frame edges. Head pixel speed may differ by a few % from pelvis pixel speed (different height).
- The shirt is only ~15 grey levels brighter than the floor, and its shadowed side is sometimes missed by the mask, so `shirt_x`
  and the mask centroid are biased. Use bbox/head instead. Soft shadows are darker than the floor and are excluded (only
  pixels darker by more than 30 grey levels, brighter pixels, or saturated pixels count).
- The bicycle "root" in Blender is unknown (it could be the bike centre or a wheel contact). For a rigid translating bike every point gives the same speed.
  `bike_center` is the geometric middle.
- Camera is static. Single 2D scale is appropriate (both move in planes facing the camera; ~2% scale variation across the frame).
