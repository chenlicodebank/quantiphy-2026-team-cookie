# simulation_0144 – measurement record

3D Blender scene, 1920x1080, 24 fps, 35 frames (t = frame/24). A HIMARS-style olive 6-wheel truck sits
static on a dirt track in a desert in front of a sandy hill. Its raised launcher pod fires **one missile**,
which flies up and to the left in a straight image line and leaves through the top edge. The **camera is static**
(phase correlation gives a 0.00 px shift in every frame). The missile is the only moving object.

## Files
- `scene.json`: inventory (missile, launcher_truck, launcher_pod, hill, dirt_track, rocks), static pixel
  extents, the image flight line, camera/perspective cues and events.
- `tracks/missile.csv`: one row per frame (0-34). Columns:
  - `origin_x, origin_y`: estimated missile centre (origin), with `origin_method` saying how it was found
  - `vis_cx, vis_cy`: centroid of the visible mask
  - `bbox_*`, `len_px` (along the axis), `wid_px` (across, 2-98 percentile), `height_px` (bbox vertical extent)
  - `nose_*` and `tail_*`: end points of the mask
  - `s_*`: signed positions along the fitted flight line (unit direction d=(-0.6619,-0.7496) from point
    (987.58, 371.32); s increases toward up-left). Image displacement between frames = difference of `s_origin`.
  - flags: `occluded` (tail inside the tube), `clipped` (cut by the image edge), plus a `note`.
- `scripts/`: `diff.py` (camera/motion check), `track_missile.py` (first mask pass), `track_missile2.py`
  (strip-limited mask, overlay), `nose_profile.py` (early nose positions), `assemble.py` (writes the CSV),
  `crops.py` (viewer). Run them in order from the scene_ws folder. The `_*.json` files are intermediate results.

## How it was measured
- Mask = pixels differing by more than 30 (any colour channel) from BOTH frame 0 (missile in its tube) and frame 34 (missile
  gone), limited to a ±14 px strip around the flight line. The line was fitted to frames 15-30 centroids; these centroids lie within 0.4 px of it, so the path is
  straight in the image. Overlays (masks plus nose, tail and centre points) were checked visually for frames 5-32: the mask covers the whole body.
- Frames 13-30 (fully visible): origin = midpoint of nose and tail. This cancels the symmetric motion-blur streak. Accuracy is about
  ±2-3 px; the blurred tail end makes frame-to-frame increments jitter by ±4 px. Smooth over 2-3 frames
  before differencing twice.
- Frames 3-12 (tail still inside the tube): the nose comes from a 1-D change profile along the line, and the
  origin = nose − 145.6/2 px along the axis. 145.6 px is the apparent length at frames 13-14, the first frames that are fully out and have little blur.
  The nose is accurate to ±2 px (checked against a close-up at frame 10). Frames 3-6 show only the nose tip, so they are less reliable.
- Frames 31-33 (nose beyond the top edge): origin = tail + L/2. L is extrapolated from the linear length trend of frames 20-30
  (len ≈ 53.3 + 5.30·frame). These frames are less reliable (±5 px).
- The truck, pod and terrain extents were read off gridded zoomed frames (±3 px).

## Key numbers (px)
- Image speed of the missile centre (|Δs_origin| per frame): f4 6, f8 17, f12 20, f14 29, f16 30, f20 40, f24 43, f28 57,
  f30 61, f32 66. It speeds up steadily, with no bounce or direction change. Apparent direction: 131.4° (up-left).
- Missile apparent length 145 px (f13-14) → 160 (f20) → 213 (f30); width 13.2 → 15.4. Length includes the
  motion-blur streak (which grows with speed); width is blur-free and suggests about +15 % apparent scale from f15 to f30.
  So the missile comes somewhat nearer to the camera (or turns more side-on) as it climbs. For a size prior, prefer the
  least-blurred full view: f13-14 (len ≈ 146 px, width ≈ 13.3 px).
- Truck (static, 3/4 front-left view): body x 1002-1437, cab roof y 852, front-wheel bottom y 1034; with pod the bbox is
  (1002, 648)-(1470, 1034). Pod bbox (1203, 648)-(1470, 898); tube mouth used by the missile at (1285, 708).

## Events
Launch flash and lighting change at f2. Nose first visible at f3 (motion start f1-3). Tail clears the tube at f13.
The missile is above the ridge (sky background) from f18. Nose reaches the top edge at f31. Last visible at f33; gone at f34.

## Ambiguities
- The model's true origin may not be at the geometric centre (rockets are sometimes rigged at the base). The midpoint is
  used here; nose and tail are also given, so other conventions can be used.
- Motion blur lengthens the silhouette by roughly the per-frame image motion times the shutter fraction.
- Launch-flash lighting changes the pod and handle frame in frames 2-13. These pixels are excluded from the missile mask.
- No other moving objects. Only one missile is fired; the other tubes show no change.
