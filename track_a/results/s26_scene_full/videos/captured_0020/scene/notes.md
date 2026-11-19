# captured_0020 – measurement record (pixels, seconds)

Lab video (real recording), 3D scene, 1280x720, 24 fps, 49 frames (t = frame/24, 0 … 2.000 s).
The footage is a "Segment Anything 2 Demo" render: the background is blurred and the people and
objects are sharp. **The camera is static**: the background shift is ≤ 0.2 px in every frame, from phase correlation in `scripts/sharp.py`.
Lab convention (not measured here): fx = fy ≈ 763 px, principal point ≈ (640, 360).

## Scene content
Two people throw objects to each other at the same time:
- **left_person** (near the camera, at the left image edge, long dark hair, dark-grey T-shirt, black trousers)
  throws the **white_ball**, a small white crumpled roundish ball, to
- **right_person** (far, near the room corner, light-grey T-shirt, navy jeans, head cut off by the top border),
  who throws the **yellow_fruit**, a pale-yellow lemon/mango-like fruit with a green stem end, back.
Static items: a white wall radiator panel (bbox x 871-1055, y 137-296), the room corner (x ≈ 575-605, floor at ≈ (605,190))
and the wall-floor baseboard lines (see scene.json `perspective_cues`). Neither person's full height is visible.

## Files
- `scene.json`: inventory, visibility and holding phases, static extents, perspective cues, events, and apparent sizes.
- `tracks/white_ball.csv`, `tracks/yellow_fruit.csv`: one row per frame (visible = 0 when hidden).
  Columns: cx, cy = centroid of the colour mask (the reference point is the visible centre); x0 y0 x1 y1 = mask bbox;
  length/width = extent along/across the mask's main (PCA) axis; height = vertical extent; area; eq_diam = 2·sqrt(area/π);
  axis_deg = image angle of the main axis; occluded = 1 if a hand, body or the other object covers part of the object.
- `tracks/right_person.csv`: per frame, the jeans bbox (dark mask, opened with a tall kernel) and the white-sneaker centroid
  and extent. The sneakers are fixed at about (730, 256), with soles at y ≈ 267.
- `tracks/left_person.csv`: per frame, the bbox of the dark clothing and hair (arms are excluded) and the visible right-sneaker
  centroid, fixed at about (366, 675). The person is cut off by the left and bottom borders, so the bbox is clipped.
- `scripts/`: `probe.py` (colour blob listing), `track_objects.py` (object tracks and overlay sheets),
  `people.py`, `static.py`, `sharp.py` (camera check), `crops.py` (viewer), `gc_test.py` (discarded grabCut test).
  The overlays I checked (`frames/trk_*.png`, `frames/people.png`) are in the work folder and can be regenerated with these scripts.

## Method and reliability
- Objects: an HSV mask inside a 42 px circle around hand-checked seeds. White: S<45, V>200. Yellow/green: H 21-55, S>45, V>100.
  The mask is the main blob plus touching fragments, closed with a 5x5 kernel. I checked every frame's overlay by eye.
- **white_ball**: the centre is reliable to about 1-2 px in free flight (frames 12-26). In frames 0-11 and 27-48 it is in a hand
  and fingers cover part of it, so the centre is roughly ±3 px and the size is too small. The mask misses the blurred
  halo, so the sharpest in-flight size (frames 21-25: about 26-30 x 22-26 px, eq_diam 23-27) is a slight underestimate.
  Frames 13-19 are motion-blurred along the path, so their length (up to about 50 px) is inflated and their width is closer to the true size.
  The apparent size shrinks from about 28-30 px near left_person to about 19-21 px in right_person's hands, consistent with the depth increasing.
- **yellow_fruit**: frames 12-17 and 19-24 are free flight. The centre is good to about 2-3 px, but motion blur stretches
  the length (40-79 px) along the path; the width is about 35-39 px. The very pale yellow rim is sometimes missed.
  Frame 18 is partly hidden behind the white ball, so its centre is biased up and right. Do not use it for motion.
  Frames 25-27 are the catch: the shape is smeared and mixed with hands. Frames 37-38 show only a few pixels.
  In frames 39-48 it is held by left_person and the mask includes the green stem end (top right), so the centre is roughly ±5 px.
  Hidden frames: 4-7 (backswing behind right_person) and 28-36 (behind left_person's hands and hair).
- **People**: coarse. Both stand with their feet fixed, as the sneaker centroids move by 2 px or less. Use the sneaker positions as
  ground-contact points. Torso and pelvis centres are only approximate (right_person jeans waist y ≈ 55-83, centre x ≈ 710).
  right_person bends forward in about frames 27-40.

## Events (frame / t s)
- 0 / 0.000: both objects are held low. The white_ball backswing low point is at frames 4-5, (277, 553).
- 12 / 0.500: both objects are released. Frame 11 is the last frame in the hand for both.
- 17 / 0.708: the yellow_fruit is at its image apex (cy ≈ 76).
- 18 / 0.750: the objects cross in the image (the white ball is in front). Neither path is deflected, so this is not a collision.
- 22 / 0.917: the white_ball is at its image apex (cy ≈ 37).
- 25-27 / 1.04-1.125: left_person catches the fruit; it is hidden from frame 28 to 36 and reappears at frame 37.
- 27 / 1.125: right_person catches the white_ball. The hands go down until frame 35-36 and are raised until frame 48.

## Ambiguities
- Image paths are projections of 3D throws between a near person and a far person, so depth changes strongly along both
  paths. Converting to metres needs the depth_info given with each question and the 763 px focal length.
- Motion blur inflates the extents along the motion direction. For object size, use the width across the motion or the sharp frames above.
- The SAM2 render adds a bright halo around the foreground; the masks exclude most of it.
- The white sneakers, the right_person's light-grey shirt and the radiator are also white or bright. The tracker excludes them through the seeded ROI.
