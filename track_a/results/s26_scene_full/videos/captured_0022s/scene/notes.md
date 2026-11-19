# captured_0022s – measurement record

Lab video (24 fps, 49 frames, 1280x720, 3D). Real recording, background replaced with a static sky-blue image by
Segment Anything 2 (watermark bottom-right). For lab videos: fx = fy ≈ 763 px, principal point ≈ (640, 360).

## Scene
- **ball**: the only white object, small (ping-pong-ball-like). At rest on the far (upper-image) edge of a wooden board in
  frames 0–11, starts rolling at frame 12 (t = 0.500 s), rolls down the sloping board toward the camera (image path nearly
  straight, down and slightly left), rolls off the near front edge around frame 45/46 (t ≈ 1.88–1.92 s) and falls; frames 46–48
  are free fall with strong vertical motion blur. Video ends before it lands.
- **board**: static light-brown wooden rectangular table top, tilted (higher at the far edge, lower toward the camera),
  ~10 px thick front edge. Corners (median frame): far-left (290,416), far-right (599,364), near-right (671,516),
  near-left (228,619) (near corners = bottom of the front edge). Image edge lengths: far 313, near 455, left 212, right 168 px.
- **leg**: static dark-grey post under the board, visible part bbox (462,568)-(509,691), ~123 px visible length.
- No people, no other moving objects. Camera static (fixed lab camera; no background shift).

## Files
- `scene.json`: inventory, static extents, events, camera notes.
- `tracks/ball.csv`: one row per frame (0–48). Recommended columns: `x_ref, y_ref` (ball centre, px), `diam_px` (apparent
  diameter = width of the white core), `phase` (rest / rolling_on_board / falling_off_edge), `ref_method`.
  Other columns: `cx, cy` = centroid of a first-pass mask (difference to median background ∧ white); `bbox_*` = that
  mask's bbox (for 46–48 replaced by the full blurred blob bbox); `mask_len_main_axis, mask_width_across,
  main_axis_angle_deg, area_px, equiv_diam_px` of the first-pass mask; `core_*` = bbox of the bright white core
  (S<40, V>190, differs from background); `cx_circ, cy_circ` = core x-centre and top-edge + half width.
  occluded = 0 everywhere (ball always visible).
- `scripts/`: track_ball.py (first pass + median background), refine_ball.py (core), finalize_ball.py (x_ref/y_ref),
  blur_frames.py (frames 46–48), static_objects.py (board/leg), strip.py/montage.py/probe.py (viewing helpers).

## Method and reliability
- Frames 0–45: centre = (core bbox x-centre, core top + width/2). The ball's lower half is grey-shaded and has a shadow
  under it on the board, so a plain centroid is biased; the top edge is crisp. Expected error ±1 px (±2 px in 12–14, where
  the board's top edge near the ball has SAM2 mask artifacts: a notch/strip of sky appears in the board edge after release,
  probably where a hand/holder was masked out).
- Frames 46–48: ball falls with vertical blur up to ~50 px tall (frame 48 blob 587–639). Centre = blurred blob bbox centre
  (≈ centre of exposure) → ±3 px vertically.
- Apparent diameter grows 17 px (rest, far edge) → ~19 (f20) → ~21 (f30) → ~24 px (f40–45): the ball approaches the camera.
  Core width may under-read the true edge by ~1–2 px (soft rim). Use it with depth_info: D_px ≈ f·D/Z.
- Per-frame step along the slope grows from ~4 px (f12–13) to ~8 px (f44–45): the ball speeds up. One irregular step
  35→36 (~12 px vs 5–7 px around it) seen by both detectors; could be a dropped/irregular capture frame – treat with care.
- For metric answers: back-project (x_ref, y_ref) with the given depth(s) and f = 763 px; where depth is only given at a
  few times, interpolate it or use the apparent diameter (Z ∝ 1/diam_px) as a relative-depth cue.
- Board corners are good to ±3 px (mask edge); the far-left corner is soft.
