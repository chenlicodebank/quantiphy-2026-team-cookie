# captured_0016s — measurement record

Lab video (24 fps, 49 frames, 1280x720, 3D). The people and the ball were cut out with Segment Anything 2 and pasted
on a static synthetic blue-white gradient with sparkle noise ("Modified with Segment Anything 2 Demo" watermark at
the bottom right). So there is no floor, wall or furniture. **Camera is static.** It looks rolled/tilted by about
25-30°: the standing catcher's body axis is 29° from image vertical. Image x/y are therefore not world horizontal/vertical.
Benchmark intrinsics: f = 763 px, principal point ≈ (640, 360).

## Scene
A near person at the left edge (the **thrower**: light-grey T-shirt, glasses, mostly outside the frame) holds a
black-and-white soccer **ball**. They wind up and throw it underarm to a far person on the right (the **catcher**:
dark-grey T-shirt, black trousers, white sneakers, long hair, head cut by the top edge). The catcher stands still,
raises her arms and catches the ball. The scene has one ball and two people, so names are unambiguous.

## Files
- `scene.json`: inventory, camera, static extents, events (frames and times).
- `tracks/ball.csv`: every frame 0-48. `ref_x, ref_y` is the visible ball centre (px). Also the bbox, `mask_length_px`
  (along the motion/blur direction), `mask_width_px` (across it), `mask_height_px` (bbox height), `diameter_est_px`
  (best estimate of the true apparent diameter: the circle diameter, or the width across the blur), `occluded`,
  `source` and `note`.
- `tracks/catcher.csv`, `tracks/thrower.csv`: per-frame mask centroid, bbox and area.
- `scripts/`: `ball_hough.py` (frames 0-25), `ball_flight.py` (run as `ball_flight.py 25 41`; frames 32-40 are used),
  `people.py` (masks from a fitted smooth background model), `build_record.py` (assembles the tracks and holds the
  manual readings), `check_overlay.py` (overlays plus step lengths), `static_extents.py` (catcher PCA axis),
  and the viewers `view.py`, `sheet.py`, `crops.py`, `batch_crops.py`.

## How the ball was measured, and how reliable it is
- **Frames 0-25 (in the thrower's hands):** Hough circle near the previous position, checked on 2x zoomed crops.
  The centre is good to about ±4 px. The diameter is noisy at about ±6 px: Hough gives 120-134, and reading the
  frame 0/1 edges by eye gives about 129 (x 256-385). The thrower's fingers always cover the lower right of the ball.
- **Frames 26-31 (swing and release):** heavy motion blur, with the hand and forearm overlapping the ball. Centres were
  read by hand as the middle of the blur streak, good to about ±8 px. The bbox is of the streak. The diameter is
  estimated as the width across the streak (~105-120).
- **Frames 32-40 (free flight):** automatic mask (difference to frame 10, skin removed, convex hull), checked visually.
  The centre is good to about ±2 px. In these frames `mask_length` includes the blur and `mask_width` ≈ the diameter.
- **Frames 41-48 (catch):** manual circle and extent readings on 3x crops, good to about ±4 px. The catcher's forearm
  and hands hide parts of the ball.
- The ball's apparent diameter falls from about 128 (near, held) to about 105 at release, about 88 at frame 40, and
  about 62 at frame 48. The ball moves steadily away from the camera, so pixel displacements are not proportional to
  metric ones. Each frame needs its own depth (from depth_info, or from diameter_px with the known ball size:
  Z ≈ f·D/d_px).

## Events (see scene.json)
- Ball nearly still in the thrower's hands: frames 0-17.
- Wind-up down and back toward the hip: frames 18-25.
- Forward swing begins: frame 26.
- Last hand contact: frame 30 (t = 1.250 s). First free frame: 31 (t = 1.292 s).
- Image apex: frames 37-38.
- First contact with the catcher's hands: frame 41 (t = 1.708 s); firm contact at frame 42. Ball held from frame 43-44.
- The catcher starts raising her arms at about frames 34-36.
- **Probable dropped capture frame between frames 35 and 36.** The ball moves 88 px in that step, against 58 px and
  35 px in the neighbouring steps, and the blur length implies about 45 px per frame. I checked both positions on crops.
  The benchmark's reference values use the frame indices as they are.

## People
- **Catcher:** the mask comes from the residual against a quadratic background model. It is reliable for her body.
  From frame 41 the mask also includes the ball. Her feet never move: the lowest point is at y ≈ 437-439, the left
  shoe at x 925-975 / y 375-398, and the right shoe at x 968-1005 / y 405-437. At frame 0 she spans 511 px along her
  body axis and 193 px across it. Because her head is cut at y = 0, the 511 px is a lower bound on her full pixel height.
- **Thrower:** only partly visible. The mask misses parts of the light-grey shirt (it blends with the near-white
  background), and it includes the ball up to frame 30. The bbox is only a rough cue to arm motion.

## Ambiguities
- The motion-blurred frames 27-36 have elongated shapes. Use the centre and the width, not the length, as the ball size.
- The thrower's shoulder and face are cut off by the left edge. The catcher's head is cut off by the top edge.
- Shadows: none (the background is synthetic). There are no other balls or props.
