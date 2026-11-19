# captured_0052 — measurement record (pixels, seconds)

Lab video (real recording), 3D scene, 1280x720, 24 fps, 49 frames (t = frame/24, frame 0 at t = 0).
In the clip, a person in black clothes crouches behind a large dark-grey exercise ball, pushes it, and it
rolls toward the camera and to the left. It leaves the frame through the lower-left corner (last visible
frame 44). Everything else is static: an orange basketball, a blue recycling bin, a white sneaker, two
black tripods, a wall TV, padded grey walls and carpet. No metric scale is assumed anywhere.

## Files
- `scene.json`: inventory with descriptions, static-object pixel extents and positions, events with
  frames and times, camera info and perspective cues.
- `tracks/exercise_ball.csv` (frames 0-44): the main track. Columns: `frame, t, cx, cy` (reference
  point = centre of the fitted circle = visible ball centre), `method`, `diameter_px` (circle
  diameter = apparent ball size), `extent_major_px/extent_minor_px`, `ellipse_*` (ellipse fitted to the
  convex hull of a colour/texture mask; diagnostic only, see below), `bbox_*` (bbox of the full fitted
  circle, may extend outside the image), `vis_*` (bbox, area and centroid of the in-image silhouette
  mask), `truncated_by_frame`, `occlusion`, `quality`.
- `tracks/exercise_ball_raw.csv`: the raw edge-circle fit for frames 0-44. It is the same as the main
  track for frames 0-31; ignore it after frame 31.
- `tracks/person.csv` (frames 0-48): centroid, bbox, width and height of the dark-clothing mask, head-top
  y, occlusion flag.
- `static_measure.json`: colour-mask measurements of the basketball, bin and shoe at frames 0, 24 and 47
  (identical, so they are static).
- `camera_check.json`: per-frame mean absolute difference to the previous frame (whole image and static
  wall region) and the phase-correlation shift of the static region vs frame 0.
- `scripts/`: `track_ball.py` (edge-circle fit → raw csv), `track_ball_final.py` (final ball csv; run
  after track_ball.py), `track_person.py`, `static_objects.py`, `frame_diffs.py`, `check_crops.py`
  (visual check), plus the `probe.py`, `maskview.py` and `texmask.py` experiments. Run all from the
  scene_ws folder.

## How the ball was measured
- Frames 0-31: rays from a rough circle (from a Lab b<128 colour mask: the ball is bluish and the room
  yellowish), the strongest radial gradient per ray, then a RANSAC circle fit and a least-squares refit.
  Checked at full resolution: the circle sits on the silhouette within about 1-2 px. Diameter accuracy is
  about ±2 px (±3-4 px in frames 20-31, which have motion blur).
- Frames 32-44: the ball is blurred (up to ~10 px), its bottom is cut off by the image border and merges
  with its shadow. A silhouette mask (smooth texture + not yellow, convex hull) was taken, and a circle
  was fitted only to its upper rim (points more than 25° below horizontal dropped, border points
  dropped). Overlays confirm the circle follows the top and sides. Centres are about ±3-5 px for frames
  32-37 and about ±10 px for 38-44, where the centre lies below the image (cy > 719 from frame 39) and
  only a cap is visible. Diameters for 38-44 are about ±5-10 %.
- Near the lower-left corner the wide lens (80° HFOV) stretches the sphere into an oval elongated toward
  the corner. Motion blur adds to this. The `ellipse_*` columns show the stretch, but for frames ≥32 they
  are biased by the truncated, shadowed bottom. Use `diameter_px` (circle) as the apparent size.
- Apparent diameter: 130-136 px at rest (frames 0-18, mean ~133), 138 (f22), 158 (f26), 189 (f31), 214
  (f35), 238 (f36), 265 (f38), 301 (f40), 349 (f42-43). The growth shows the ball approaching the camera.
  With the lab focal length (763 px), depth ∝ 1/diameter_px for a known ball size.
- The rest position wobbles slightly (cx 614-621, cy 509-518) while the person's hands rock the ball in
  frames 0-18. That is real small motion plus fit noise, not rolling.

## Events (see scene.json)
- Frames 0-18: ball at rest under the person's hands.
- Frame 19 (t 0.792 s, ±1 frame): the ball starts rolling.
- Frame ~22 (t 0.917 s, ±1): release; arms thrown up.
- Frames 20-44: the ball rolls down-left in the image toward the camera with no bounce or impact. It passes
  in front of the shoe (occluding it in about frames 36-41) without moving it.
- Frame 32: the ball first touches the bottom image border.
- Frame 44 (t 1.833 s): last visible frame. From frame 45 on it is gone.
- The person stays crouched throughout. After the push their hands go to the floor (frames ~36-48).

## Camera / timing
- The camera is static: the background shift is < 0.1 px in all frames.
- No duplicated frames. Frame 35→36 shows about twice the normal change, and the ball moves about 46 px
  vs ~20-25 px in the neighbouring steps, so one camera frame was probably dropped there. Per-frame
  differences across 35→36 therefore span ~2 real frame intervals. The benchmark's own reference uses
  video frame indices, so this is recorded only as a caution.
- Lab intrinsics by the benchmark convention (not measured): f ≈ 763 px, principal point ≈ (640, 360).
- Perspective cues: floor/wall base lines and the room corners at x ≈ 450 and x ≈ 860, read off a grid.
  They are approximate (±5-10 px).

## Static objects (pixel extents at a clear frame, image axes)
- Basketball: centre (800.6, 667.4), bbox 756-847 x 624-709, diameter 92 (horizontal) × 86 (vertical) px.
  Its bottom is close to the image edge but inside it. Reliable to ±2 px.
- Recycling bin: bbox 680-775 x 483-591, i.e. 95 px wide and 108 px tall (front face). Use the frame
  24/47 values; at frame 0 the mask missed the bottom. ±3 px.
- Shoe: bbox 256-318 x 625-676, length ~71 px along its axis (~40-45° diagonal), width ~27 px. ±4 px.
- Tripods, TV: approximate (±10-15 px), see scene.json.

## Person (tracks/person.csv), lower reliability
- The mask is dark pixels (L<45) in a box around the person, minus the ball disc, the bin and the baseboard
  band, then closed. Its centroid is a "visible centre" of the dark clothing and hair. It excludes the bare
  arms and hands and the grey face patch (filled only partly), and the lower body is hidden by the ball in
  frames 0-~21. bbox ±5-10 px. The person crouches throughout, so no standing height is available.
  Bbox height (head top to lowest visible dark pixel) is 183-203 px for the unoccluded crouched body in
  frames 22-48. Frames 0-19 show only the upper body above the ball: 88-120 px.

## Ambiguities
- "Ball": there are two balls. The **exercise ball** (large dark grey, moves) and the **basketball**
  (orange, static, lower right).
- Shadows: the ball's shadow on the carpet is dark and merges with its lower rim. Upper-rim fits avoid it.
- Ball reference point = image centre of the sphere's silhouette. For a sphere this projects close to,
  but not exactly onto, the 3D centre when far off-axis (late frames).
