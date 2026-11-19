# simulation_0121_segmented — measurement notes

2D segmentation video, 1920x1080, 30 fps, 80 frames (t = frame/30). White background, static camera.
All values are pixels (x right, y down) and seconds; no metric scale has been assumed.

## Scene
Three identical grey spheres (diameter ~164 px) hang in a row, like a Newton's cradle. The strings, frame and ground
are not rendered. **ball_left** starts raised up-left at (285, 654) and swings down along an arc
(fitted pivot (645, 226), radius 559 px). It hits **ball_middle** (at (806.4, 792.3)) at frame ~28 (t ≈ 0.933 s).
**ball_right**, at rest at (1311.8, 792.4), is then knocked out along an arc (fitted pivot (1308.7, 240.4), radius 552 px).
It reaches its apex at frame 54 (t = 1.8 s, centre (1660.2, 666.9)) and swings back. At frame 79 it is at (1355.4, 790.9),
still moving left. ball_middle almost stays put: x drifts 806.5 → 796.6 (f51–55) → 805.1. After the impact ball_left nearly
stops: max x 643.5 at f29, then a slow drift to x 623.2 (f52–55) and back to 637.9 at f79.
The resting ball_left centre is about 8 px higher (y 784.6) than the other two (y 792.3).

## Files
- `scene.json`: inventory, sizes, arc fits, events, bad frames and reliability.
- `tracks/ball_left.csv`, `tracks/ball_middle.csv`, `tracks/ball_right.csv`: one row per frame (0–79). Columns: frame, t,
  cx, cy (reference point = sphere centre = object origin), radius_fit, bbox_x0/y0/x1/y1 (inclusive mask bbox), mask_w,
  mask_h, mask_area, occluded (always 0), bad_frame. For spheres, length = width = height = diameter ≈ 2·radius_fit
  or mask_w/mask_h.
- `scripts/`: `survey.py` (per-frame components), `track.py` (makes the tracks), `overlay.py` (check drawings),
  `analyze.py` (diameters, centre gaps, arc fits, extrema), `probe.py`.

## Method
Mask = pixels with any RGB channel < 235. Components smaller than 100 px are dropped. Each pixel is assigned to the
nearest predicted ball centre (constant-velocity prediction). A least-squares circle is fitted to the densely
sampled convex-hull outline of each ball's pixels, and its centre is the reference point. The fitted circles, centres
and bboxes were drawn on frames 0, 9, 16, 18, 28, 29, 30, 54 and 79 and checked: they hit the right ball and cover its
full extent.

## Reliability / caveats
- **Frame 1 is a broken segmentation frame.** All balls are missing; only a stray half-dome blob sits at x 560–717,
  y 861–936. Its centres are linearly interpolated from frames 0 and 2 (bad_frame = 1), and its size columns are empty.
  A one-frame backward difference at frame 1 or 2 uses these interpolated values.
- In frames 0–17 the segmentation cuts a white sliver through ball_left, so its raw mask pieces are not the full
  ball. The hull-circle fit still gives the true outline (radius 82 ± 0.5), and the centre is good to ~1–2 px. The
  mask_area column is reduced in those frames.
- Frames 28–30, ball_left: a light crescent at the contact edge makes the fitted radius 83–85 px, so the centre is
  uncertain by ~2 px.
- In all other frames the centres are good to ~0.5 px. Diameters: left 164.0, middle 163.8, right 165.6 px (fit
  medians). mask_w/h medians are 163–166 px.
- Release: ball_left moves only 0.4 px/frame over frames 0–2, then accelerates (2.4, 2.9, 4.7, 6.1 px/frame), so motion
  starts at frame 0.
- Impact: the left–middle centre gap is 184.3 (f27), 167.0 (f28) and 164.0 (f29, one diameter). ball_right first moves
  at f28, so contact falls between frames 27 and 28.
- No occlusion, shadows or camera motion. Motion blur is small. The balls are told apart only by position: left =
  striker, middle = hit ball, right = ejected ball.
