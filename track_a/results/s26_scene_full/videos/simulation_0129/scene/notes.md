# simulation_0129 – measurement record (pixels, seconds)

2D Blender render, 1920x1080, 24 fps, 40 frames (t = frame/24, 0–1.625 s). Pixel coords: x right, y **down**.
Static camera (background diff 0.04 grey levels between frame 0 and frame 39 in untouched areas). The view faces a
warehouse facade: concrete pillars, black steel columns, X-braced wall panels, a glass curtain wall with a dark doorway,
and a floor with white stripes. There are two moving objects: a **red ball** falling straight down and a **forklift**
driving right (forks first), accelerating from rest. Both start moving between frames 1 and 2.

## Files
- `scene.json`: inventory (moving and static objects with pixel extents), events, camera notes.
- `tracks/red_ball.csv`: frame, t, x, y (blob centroid = sphere centre), bbox, diam_w/diam_h (bbox size), diam_from_area,
  occluded, note. Frame 39 is occluded: its x/y are extrapolated (x = 956, y from a parabola fit) and marked occluded=1.
- `tracks/forklift.csv`: frame, t, x, y (reference point), tmpl_shift_x (rigid shift from frame 0), bbox (rigid frame-0
  box shifted), length 256, height 208, orange_rear_x/orange_front_x/orange_len (raw orange-paint extents in that frame), occluded.
- `scripts/`: explore.py (first pass), ball.py (red blob per frame), forklift.py (template-matching shift, writes
  forklift_raw.json), fk_extent.py / fk_profile.py / fk_orange.py (extent studies), probe.py (shadow check),
  static.py (static features and camera check), write_record.py (writes the final CSVs and overlays).

## Red ball
- Glossy red sphere, diameter **~20 px** (visual edge-to-edge 20–21 px; the thresholded bbox is 19–22 wide and 16–20 tall
  because the dark rim is lost and frames 37–38 are motion-blurred). It is the only red object besides small red
  details on the forklift (rear lamp, mast lights), so its track is restricted to x 900–1020.
- It starts at (956.1, 85.6) just under the ceiling beam and falls vertically. x stays 955.1–956.4.
- Frames 0 and 1 are identical (at rest). y(f) = 0.4508 f² − 0.260 f + 86.78 (frames 2–38) has rms 0.41 px, so the
  pixel acceleration is constant at ~0.90 px/frame² (≈519 px/s²). This is only a consistency check: answer sessions
  should fit their own motion.
- Centroid accuracy is about ±0.5 px (slightly worse in 37–38 because of blur).
- At frame 39 the ball is behind the forklift's mast and overhead guard. Only red slivers are visible at x≈952–960,
  y≈752–765, which fits the extrapolated centre y≈762. There is no visible bounce or contact: it passes behind the forklift.

## Forklift
- Orange-and-black Toyota counterbalance forklift seen side-on, moving +x. It is never occluded and ends in front of
  concrete pillar 1.
- Reference x = 170.5 (frame-0 bbox centre) + rigid shift. The shift comes from template matching of the
  body and wheels (y 820–928), refined to sub-pixel. It was cross-checked: the counterweight hole moves 96.5→801 (704.5 px),
  the wheels 700–705 px and the template 703.9 px. Shift accuracy is about ±1 px. Per-frame second differences are
  noisier (0.65–1.35 px/frame²) than the ball's. y = 824.5 is constant: the floor is level and there is no vertical motion.
  The rig root's exact position in the body is unknown, but it moves rigidly with the body, so any body-fixed point gives
  the same speeds and displacements.
- Size: length **256 px**, from the rear of the counterweight to the fork-tine tip, measured at frame 0 (x 43–298).
  Height **208 px**, from the overhead-guard top (y 721) to the tyre contact (y 928), ±2 px.
  Wheelbase ≈164 px. Rear wheel r≈34, front r≈33 (Hough fit, ±3 px).
- Perspective caveat: the raw orange extent shrinks from 256 px (frame 0, near the left image edge) to 250 px
  (frame 39, near the centre), and the wheelbase from ~164 to ~159 px. Its height is unchanged, so this is an
  off-axis view of a 3D body (the camera sees part of its rear face), not a change of depth.
  If a question gives the forklift length as the prior, the pixel length is ~250–256 (~254 mid-clip).
  This gives about ±1.5 % scale uncertainty.
- The bg-difference masks were not used for extents. The forklift casts a dark shadow on the glass wall ahead of
  itself (about 45 px in front of the forks), which contaminates difference masks. There is also an orange floor
  reflection below y≈928.

## Events
- Frames 0–1: both objects at rest. Motion starts between frames 1 and 2 (t≈0.042 s) for both.
- Ball: constant downward acceleration until the end. Forklift: accelerates rightward throughout.
- Frame 38 (t=1.583): the forklift's tine tip reaches the ball's column (x≈946–966).
- Frame 39 (t=1.625): the ball is hidden behind the forklift mast. The clip ends with both still moving.

## Static objects (frame 39; the camera is static so any frame works)
- Concrete pillars: x 721–759 and 1163–1201 (38 px wide), y≈75–910; centres 442 px apart.
- Black steel columns: x 39–78, 482–519, 1402–1439, 1843–1882 (~38 px wide).
- Horizontal beams: y≈35–75 (ceiling), 195–215, 435–470, 670–700.
- Doorway (dark opening): x 885–1037, y 745–910.
- Floor: the kerb/base is at y≈910–925. White floor lines run at y≈926–928, 938–942, 1015–1020 and 1036–1041.
  Parking stripes come in four groups at y 945–1015, each stripe ~8–11 px wide (positions in scene.json).

## Reliability summary
- Ball track: high (±0.5 px). Ball diameter: ±1 px.
- Forklift shift: high (±1 px). Forklift length: 250–256 px (perspective). Height: ±2 px.
- Static extents: ±2 px.
- No metric scale was assumed anywhere.
