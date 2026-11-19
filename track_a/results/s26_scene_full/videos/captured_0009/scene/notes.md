# captured_0009 — measurement record (pixels and seconds only)

Lab video (real recording), 3D scene, 1280x720, 24 fps, 49 frames (t = frame/24, 0 … 2.000 s).
Content: a person standing right of centre holds an orange basketball out in front with both hands, then releases it. The ball
falls to the floor, bounces once (lowest at frame 37) and rises to an apex at frame 46. It is falling again at frame 48.
The background was blurred by "Segment Anything 2" (watermark at bottom right). Ball and person are sharp.

## Files
- `scene.json`: inventory, camera, events, key positions and apparent ball diameters.
- `tracks/ball.csv`: **final ball track**, every frame 0–48. Columns: frame, t_s, cx_px, cy_px (centre of the ball disc),
  bbox_x0..y1, diam_horiz_px (horizontal diameter), extent_vert_px (vertical mask extent including motion blur; free frames only),
  mask_ctr_x/y_raw (raw HSV-mask centroid, for comparison), occluded (1 = hands/arms cover part of the ball), state
  (held / release / free), method.
- `tracks/ball_raw.csv`: first-pass HSV mask (convex hull) stats plus a RANSAC circle fit. In free frames 33–48 the circle-fit centres
  (circ_cx/cy) agree with ball.csv within about 3 px. In held frames the raw values include the hand, so do not use them there.
- `tracks/person.csv`: per-frame centroid and bbox of the black tank top, and the extent of the blue overalls.
- `scripts/`: track_ball.py (raw pass), finalize_ball.py (final track), frame_check.py (PTS, frame differences, camera shift),
  person_track.py, probe_hsv.py, make_sheet.py / draw_track.py (overlays checked visually), write_scene.py (builds scene.json).

## How the ball was measured
Ball pixels are those with (R−B) ≥ 50 and (R−G) ≥ 45. This is the half-maximum edge: the ball plateau is ~90–140, the grey
background ~0 and skin ~25–50 in R−G.
- Frames 0–26 (held; hands cover the lower half): a least-squares circle through the left/right edge points of the top 50 rows and the
  top edge. D ≈ 145.5 px (±1.5), centre ≈ (483, 193→186).
- Frames 27–30 (release; hands and arms over the ball, motion blur): centres read by eye on a 10 px grid (`frames/release_grid.png`),
  **±6 px**. Diameter assumed 145→137.
- Frames 31–32: circle fit to the lower 45 rows (arms cover the top), ±4 px.
- Frames 33–48 (free, unoccluded): centre = horizontal middle of the widest rows, vertical middle of top and bottom edges. D is the
  horizontal width (unaffected by vertical blur), ±2 px. In falling frames the vertical extent exceeds D by 6–13 px (motion blur).
  In frames 38–42 the vertical extent is about 5 px less than D (soft highlight on top), so cy there may be ~2–3 px too low.
- Overlays (`frames/fin_*.png`, `frames/track_overlay.png`) were inspected. The circles sit on the ball outline in every frame.

## Events (frame / t)
- Held 0–26 (0–1.083 s): nearly still, drifts up ~7 px.
- Start of fall / release: **frame 28 (1.167 s)**, ±1 frame. Frame 27 moves +2.6 px and frame 28 +10 px. Hands open over frames 27–29.
  Both arms then swing outward and up (frames 27–33) and stay raised.
- Floor contact / bounce: **frame 37 (1.542 s)**, the lowest image point: centre (547.5, 656.5), ball bottom y ≈ 705.
  Frame 38 moves up.
- Apex after bounce: **frame 46 (1.917 s)**, centre (527.5, 479.5). Frames 47–48 descend again.
- Image-y steps while falling: 31→32: 45, 32→33: 51, 33→34: 56, 34→35: 56, **35→36: 116**, 36→37: 56. The doubled step, plus a
  doubled shrink in apparent diameter, suggests **one capture frame was dropped between frames 35 and 36**. PTS are uniform, so
  nothing in the file shows this. The track is not corrected for it. Treat speeds or accelerations that span 35–36 with care.
  Rising steps after the bounce are −24, −31, −31, −27, −23, −17, −13, −10, −2, then +3 and +8.

## Camera and 3D cues
- Static: background phase-correlation shift < 0.05 px over all frames.
- Lab intrinsics (from the benchmark convention): f = 763 px, principal point ≈ (640, 360). Back-project with the given depth_info:
  X = (u−640)·Z/763 and so on. No zoom.
- The view is oblique, looking down at the floor. The floor fills the lower part of the image, a grey wall is behind, and no horizon
  is visible. Floor stripe markings run diagonally.
- The ball's apparent size changes with depth: held D ≈ 145.5 px; frame 33: 115; bounce (37): 96; apex (46): 112; frame 48: 110.
  So the ball moves **away from the camera as it falls** (depth at the bounce ≈ 1.5× the held depth, if size ∝ 1/Z) and back toward it
  on the rebound. Image-plane pixel distances therefore do not map to one metric scale; use depth_info and the 3D back-projection.
  Size-based depth estimates: Z ∝ 1/D.

## Static objects and person (by eye on the blurred background, ±10 px)
- Person: black tank top and light-blue denim overalls, face blurred, ponytail. Torso static (top centroid ≈ (835, 365) ±4 px).
  Body spans x ≈ 715–965. The head top is cut at y = 0 and the legs at the bottom edge, so full height is **not measurable**.
  Arms reach left to x ≈ 415 while holding the ball.
- Black metal frame (thin bars) at the left: a diagonal bar from about (0, 470) to (400, 290), vertical bars around x 340–440, and a leg to the bottom left.
- Tripod with a small white-topped device at the right (head ≈ (1000–1090, 260–300)).
- Dark cart at the far right with items (a white bottle, an orange/red item at about (1220, 325) that is **not** the ball, and a light-blue box at about (1110–1220, 540–600)).
- Floor: grey, with light diagonal stripe markings and an orange cable at the left.
- No other moving objects.

## Ambiguities
- Hands occlude the ball until frame 32. Release timing is ±1 frame.
- Motion blur is strongest in frames 29–37.
- There is probably a dropped frame between 35 and 36.
- The ball centre is the visible disc centre. The projected sphere centre differs negligibly here (< 1 px at these angles).
