# captured_0008 — measurement record (lab video, 3D, 24 fps, 49 frames, 1280x720)

## Scene
A woman (blue denim overalls, face masked) stands behind a small square wooden-top table and holds an orange
basketball in her extended right hand. She lets it drop at about frame 23. The ball falls onto the table top,
bounces twice (impacts at frame 30 and between frames 41 and 42) and is still bouncing and descending when the
video ends at frame 48. The footage was edited with "Segment Anything 2 Demo" (watermark bottom right): everything
except the ball, the table top and the thrower's hands is blurred, including the thrower's body, a seated person
at the left, a monitor, a white shelf and a tripod at the right. The camera is static: the background and table
patches shift by less than 0.15 px across all frames (phase correlation, `scripts/static_measure.py`).
Benchmark intrinsics for this lab camera: fx = fy = 763 px, principal point about (640, 360).

## Files
- `scene.json`: inventory (ball, table, thrower, seated person, background), table corner pixels, apparent ball
  diameters, events with frame and time, and camera information.
- `tracks/ball.csv` (**use this one**): for every frame 0-48: `cx, cy` = ball centre (mean of the two circle fits
  below), `diam_px`, the circle bounding box, the mask PCA extents (`mask_len_major_px`, `mask_width_minor_px`), the
  mask bbox, both fits' values, `center_disagree_px` (distance between the two fit centres; use it as the
  uncertainty), `occluded` (1 = hand touching the ball, frames 0-23) and `flags` (motion_blur, hand contact,
  table-contact shadow merge).
- `tracks/ball_fit.csv`: fit A. HSV mask of saturated orange (H<=22 or >=175, S>=140, V>=50), then a RANSAC circle
  on the mask contour, which rejects the hand edge and the merged shadow/reflection blob.
- `tracks/ball_edgefit.csv`: fit B. 180 rays from fit A's circle; on each ray, the steepest outward drop of Lab
  (a*+b*). Then a RANSAC plus least-squares circle fit. This version includes the low-saturation highlight on top of
  the ball.
- `tracks/ball_raw.csv`: first-pass convex-hull mask extents. These include the hand and shadow where they touch
  the ball, so they are a rough cross-check only.
- `scripts/`: every script used (`track_ball.py`, `track_ball2.py`, `refine_edges.py`, `finalize.py`,
  `static_measure.py`, `event_crops.py`, `montage.py`, `probe_colors.py`).

## Ball (the only moving rigid object)
- **Held, frames 0-20:** centre about (523, 97), diameter 125.7 ± 0.5 px. The fitted circle was checked against the
  overlays; the right-hand fingers cover the ball's right edge.
- **Release:** downward motion starts at frame 21. The fingers still touch the ball in frames 22-23 and it is free
  from frame 24.
- **Falling, frames 24-29:** heavy vertical motion blur. The centre is the mid-streak estimate and is uncertain by
  4-12 px, mostly in y. Diameter in these frames about 110-102 px.
- **First impact, frame 30:** lowest point, cy about 414. Its dark contact shadow merges with the mask; fit A
  rejects it.
- **First bounce apex, frames 35-36:** cy about 305.
- **Second impact, between frames 41 and 42:** cy about 413 in both frames.
- **Second bounce apex, frame 46:** cy about 371. At frame 48 the ball is descending again.
- **Image motion:** mostly vertical, drifting right by about 55 px in x while falling and left by about 25 px
  after the first bounce.
- **Apparent size:** the diameter shrinks from about 126 px while held to about 100-110 px near the table, so the
  ball is moving away from the camera. Depth ≈ 763 × D_true / diam_px. With a given depth_info, back-project as
  X = (cx − 640)·Z/763 and Y = (cy − 360)·Z/763. Treat that depth as distance to the ball centre along the ray (the
  benchmark convention).
- **Reliability:**
  - Held and slow frames (0-21, 32-48 apart from blur flags): centre ±1.5 px, diameter ±2 px.
  - Blurred fall frames 22-29: centre ±5-10 px, diameter ±4 px.
  - Diameters during blur are taken across the blur. For size, prefer frames 0-20, 35-37 or 44-48.

## Static objects (frame 0 pixels)
- **Table top corners:** near-left (440, 605), left-back (477, 417), far-right (681, 384), near-right (755, 542).
  - Edge lengths in the image: near 323 px, left 192 px, back 207 px, right 175 px. Strong perspective, so these
    are not equal even though the top is probably square.
  - Front edge thickness about 12 px. The single metal pole at x about 645 runs from y about 610 to the bottom of
    the frame.
  - The corners were read by eye on a zoomed grid, ±4 px. The colour segmentation leaked into the floor, so it was
    not used.
- **Thrower:** standing extent about y 12 (head top) to y 640 (feet), x about 690-820, so about 628 px tall. Her
  body is blurred by the edit, ±10 px. She does not walk; her arms move after the release.
- **Seated person** (grey shirt, left background, bbox about [180, 130, 460, 480]): blurred, only roughly located.

## Ambiguities
- The thrower's skin (hand and arm) is orange-ish but less saturated (S about 120 vs ≥150 on the ball). The
  thresholds separate them, but the hand overlaps the ball until frame 23.
- The ball's shadow and reflection on the table merge with it at the impacts (frames 30, 41, 42).
- The bright highlight on the top of the ball is less saturated; fit B captures it, fit A partly misses it.
- No metric scale is assumed anywhere.
