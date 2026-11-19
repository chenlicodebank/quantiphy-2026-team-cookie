# captured_0035a – measurement record

Lab recording, 3D, 24 fps, 49 frames (t = frame/24, 0 to 2.0 s), 1280x720. The background (everything except the
two people and two balls) was blurred by a "Segment Anything 2 Demo" edit (watermark at bottom right).
Benchmark camera convention: fx = fy ≈ 763 px, principal point ≈ (640,360). All values here are in pixels and
seconds. No metric scale has been estimated.

## Scene
An indoor floor seen from above at an angle. Two people pass two balls between them at the same time:
- **person_A** (far, top-left, light-grey T-shirt, dark jeans, white sneakers, head cut off by the top edge) kicks
  the **soccer_ball** (white with black panels, ~44 px) toward the lower right.
- **person_B** (near, right edge, long dark hair, dark-grey oversized T-shirt, black trousers) kicks the
  **basketball** (orange Wilson, ~84 px at rest) toward the upper left.
- The balls collide at frame ~20 (t ≈ 0.83 s). The soccer ball rebounds and rolls back to person_A's right shoe
  by frame 48. The basketball nearly stops, then keeps rolling slowly (~5 px/frame) toward the upper left.
- Static: grey wall/cabinets at top-left (wall–floor line from (5,375) to (630,195)), white floor tape strips
  (lower-left (315,620)–(405,715) and mid (610,425)–(680,475)), a blurred blue/white object (bag or ball) at
  ~(735,228), a wooden door at (720–870, 0–210), a metal post at x≈650, and blurred seated people at the top right.

## Files
- `scene.json`: inventory, camera, perspective cues, events, file index.
- `tracks/basketball.csv`, `tracks/soccer_ball.csv` (**final ball tracks**, one row per frame 0–48):
  - `cx,cy`: visible centre, which is the centre of the fitted circle.
  - `bbox_*`: bbox of the fitted circle.
  - `diam`: circle diameter.
  - `len_main_axis,width_across,height`: visible-mask extents. For the basketball these equal `diam`. For the
    soccer ball they come from the white-region hull in frames 0–4, 10–11 and 13–46; in other frames they equal
    `diam`.
  - `mask_*`: bbox of the visible pixels.
  - `occluded`, `blur`, `contact`, `note`.
- `tracks/person_A.csv`, `tracks/person_B.csv`: mask centroid and bbox from background subtraction. **Low
  reliability**: the people barely move, so the median background contains parts of them and the masks are
  partial. Person_B's box also picks up motion from the blurred seated people. Both people are always cut off by
  the image edges. Use these only for rough positions; better hand-read positions are in scene.json `key_positions`.
- `camera_shift.csv`: phase-correlation shift against frame 0. It stays at or below 0.46 px, so the **camera is
  static**.
- Intermediate files: `*_raw.csv` (HSV mask / Hough first pass), `*_bgsub.csv` (background-subtraction masks,
  which include the shadows, so do not use them for size), `soccer_ball_fit.csv` (white-hull extents and
  inscribed circle), `*_ransac.csv` (circle fits used for the final tracks).
- `scripts/`: `track.py` → `refine.py` → `soccer_final.py` → `soccer_ransac.py`, `basketball_ransac.py` →
  `assemble_balls.py` → `people.py`, `check_final.py`. Viewers: `view.py`, `zoom_sheet.py`.

## How the measurements were made and how reliable they are
- **Basketball**: RANSAC circle fit to the edge of an orange HSV mask (holes filled). I checked the circle overlays
  on every frame (frames/basketball_ransac.jpg) and they fit the ball's rim well. Centre is good to about ±1 px in
  frames 18–48 and about ±2 px in the blurred frames 8–17.
  - In frames 0–7 the ball is at rest. Its right ~20% is hidden behind person_B's black trousers and her hand rests
    on top. The circle is fitted through the hidden part: centre (885,615), diameter 84.
  - Diameter shrinks with distance: 84 px at rest (y ≈ 615), 76–80 px during the kick, 70–73 px from frame 18 on.
- **Soccer ball**:
  - Frames 0–9: the ball merges with person_A's white shoes, so I read the centre by hand from a 3x zoom
    (±3–4 px). At rest in frames 0–4: centre (353,303.5), visible extent 45x42 px.
  - Frames 10–48: RANSAC circle fit to the edge of the white-region mask. Centre is good to about ±1.5 px. The
    circle diameter (38–44) runs slightly small because the black panels break the rim. The hull width/height
    (about 42–47) is the better size.
  - Frames 5–21 are motion-blurred: the centre is the middle of the blur streak and the size is inflated.
- **Suspected dropped frames**: both balls jump ~1.7x their normal step between frames 11 and 12 and ~2x between
  frames 35 and 36. Treat these as recording glitches. Per-frame speeds around them will spike.
- **Shadows**: each ball casts a soft shadow just below it. It is excluded from the final tracks but included in
  the `*_bgsub.csv` masks.
- **Perspective**: the floor recedes upward, and both balls move across depth. The basketball goes from near and
  low in the image to farther and higher; the soccer ball goes from far to nearer and back. Pixel sizes therefore
  change with image y, so pixel distances are not proportional to metric distances. Use the depths together with
  f ≈ 763 px to back-project.

## Events (frame / t)
- Soccer ball at rest 0–4. Person_A's kick contacts it from frame 5 (0.208 s); release ≈ frame 9 (0.375 s).
- Basketball at rest 0–7. Person_B's foot contacts it from frame 8 (0.333 s); release ≈ frame 11 (0.458 s).
- Collision between frames 19 and 20 (0.79–0.83 s; listed as frame 20). The soccer ball reverses direction. The
  basketball drops from ~17 to ~2–7 px/frame and keeps going upper-left at ~5 px/frame.
- The soccer ball decelerates as it rolls back and touches person_A's right shoe at frames 47–48 (end of video).

## Ambiguities
- Two balls of different size and colour: "soccer ball", "white ball" or "football" means the black-and-white ball;
  "basketball" or "orange ball" means the Wilson ball. The blurred blue/white object in the background (~735,228)
  is static and is not either of them.
- Event frames are ±1 frame: kick start/release (blur, foot contact) and collision (blur).
- The people are tracked only roughly. Neither is ever fully in frame, so no full person height can be measured.
