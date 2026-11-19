# captured_0014x – measurement record (lab video, 3D, 24 fps, 49 frames, 1280x720)

All values are in pixels and seconds. No metric scale is assumed. t = frame / 24 (frame 0 at t = 0).
Lab intrinsics (benchmark convention): fx = 0.5959*1280 ≈ 763 px, principal point ≈ (640, 360).

## Scene
A light wooden table with one dark-grey pedestal leg, seen from the front and above (about 45°). The background
has been replaced with white (segmented footage). On the table: a white rectangular **board** (back-middle;
the ball rolls down it), a white **cup**/tumbler (back-left), a **cookie** standing in front of the cup, a
black/silver **pen** (front-left) and a light-blue **notebook** with a ribbon bookmark (right).
The only moving object is one **ball** (light beige/pink, about 30 px across).
The ball sits at the top edge of the board, rolls down the board toward the camera, drops/rolls onto the table,
rolls off the front edge of the table and falls in front of the table until it leaves the bottom of the image.

## Files
- `scene.json`: inventory (description, moves, visible frames, pixel extents/corners of static objects),
  events, camera status and per-frame background shift `[frame, dx, dy]`.
- `tracks/ball.csv`: one row per frame (0-48). Columns: `ref_x, ref_y` = best estimate of the ball's visible centre
  (use this); `mask_cx, mask_cy` = mask centroid; bbox; `len_main_px` / `width_across_px` = mask extent along / across
  its principal axis; `height_px` = bbox height; `occluded` and `flag` say how reliable the frame is.
  Frames 30-48: not visible.
- `scripts/`: `track_ball.py` (background-difference tracker; the background is the median of frames 30-48, when the
  ball is gone), `static_objects.py` (rough colour segmentation, only used as a check), `camera_shift.py`
  (phase correlation), `build_record.py` (writes the CSV and JSON; the static corners were read by eye from zoomed,
  gridded frames at frame 42), `montage.py`, `diffscan.py`.

## How reliable each item is
- Ball centre: ±1 px in frames 9-16 and 21-22 (clean, round, about 30 px wide).
- Frames 0-8 (at rest): the board's top edge cuts across the lower part of the ball, so its lower part is hidden.
  The mask also takes in a few pixels of the board edge, so the centroid is ±2 px.
- Frames 17-20: the ball crosses the board's front edge onto the table. The video shows it ghosted or
  semi-transparent, with a dark shadow and ghost below it. The mask keeps only the upper part, so `ref_y` = bbox top
  + 15 px (the radius) and `ref_x` = the middle of the bbox. Error is about ±3-4 px. The raw centroid is in `mask_cy`.
- Frames 23-28 (falling): strong vertical motion blur. The streak is 46-75 px long and 38-44 px wide, and the
  reference point is the centre of the streak (the mean position during the exposure). The across-motion width
  grows from about 30 px to about 40 px. Part of that is the ball getting closer to the camera (it falls in front of
  the table) and part is the blur halo; use it with care as a depth cue.
- Frame 29: only the top of the ball is visible (y 711-719), so its centre is unreliable (the true centre is probably
  about y 740, off the image).
- The steps are uneven: frame 11→12 jumps 20 px while 10→11 moves only 4.6 px and 12→13 moves 11.5 px. This may be
  capture-timing jitter, so smooth over several frames, as the reference does.
- Image steps of ref_y: about 3-5 px/frame at the start (9-11), rising to about 20 px/frame at 16-17. After that the
  ball is on the table (17-22) and the step drops to about 6-12 px/frame, because the table recedes from the camera
  (foreshortening). In the fall (23-28) the step grows: 22, 31, 39, 47, 51 px/frame.
- Static extents: corners read by eye, ±2 px. The board and table are seen in perspective, so their image side lengths
  are not true proportions (the table's front edge is 301 px, its back edge 222 px).
- Camera: static. The background shifts by at most 0.15 px in x and 0.62 px in y, so no compensation is needed.

## Events (frame / t)
- At rest on top of the board: frames 0-8 (t = 0-0.333 s).
- Motion starts: between frames 8 and 9 (first clear move at frame 9, t = 0.375 s).
- Rolls down the board: frames 9-17.
- Goes from the board onto the table (change of direction and speed): frames 17-20 (t = 0.708-0.833 s).
- Rolls on the table toward the front edge: frames 20-22.
- Leaves the table's front edge (y ≈ 481 at x ≈ 547): between frames 22 and 23 (t ≈ 0.94-0.96 s).
- Falls freely in front of the table: frames 23-29.
- Leaves the bottom of the image: frame 29 is the last partial view, frame 30 (t = 1.25 s) has none.

## Ambiguities
- Whether the board is tilted (a ramp) or flat cannot be told from the image. The ball speeds up while rolling
  down it, which suggests a slope.
- The ball's shadow on the table (dark, below the ball in the image) is not part of the ball; the tracker excludes it.
- The ball's colour (light beige) is close to the white board's, so its edges there are soft.
