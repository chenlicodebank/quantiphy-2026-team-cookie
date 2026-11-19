# captured_0033x – measurement record

Lab recording (24 fps, 49 frames, 1280x720, 3D), background replaced by black with Segment Anything 2.
Visible: one wooden table (top + single grey pedestal leg) and one small white/pale-pink ball. A watermark
"Modified with Segment Anything 2 Demo" sits at the bottom right (not an object). All values in pixels / seconds.
Benchmark intrinsics for this camera: f = 0.5959 x 1280 = 763 px, principal point ~ (640, 360).

## Files
- `scene.json` – inventory, table geometry, camera, ball apparent sizes, events.
- `tracks/ball.csv` – final ball track, frames 0-48 (visible 0-38). Columns: frame, t, visible, occluded
  (1 = cut by image bottom), cx, cy (mask centroid = reference point), bbox_cx/cy, bbox x0 y0 x1 y1 w h,
  area_px, eq_diam_px, minor_extent_px (across the main axis = best diameter estimate), major_extent_px
  (along the main axis; includes motion blur), major_axis_deg (image angle, 90 = vertical), note.
- `tracks/ball_raw.csv` – first-pass track (stricter low-saturation mask); kept for comparison only.
- `scripts/track_ball.py` (median background + raw track), `refine_ball.py` (final mask: pixels brighter than
  the median background by >14 grey levels in a window around the raw box), `overlay.py` (check montages),
  `table.py` (table geometry from the median background), `camera_check.py` (phase correlation), `probe.py`.

## Motion summary (events, see scene.json)
Ball nearly static at (625, 235) in frames 0-2 (held; the hand was segmented out), moves up from frame 3
(release f3-4), apex frame 8 (cy 181), falls and hits the table top near its back edge at frame 14, rebounds
to a second apex at frame 20 (cy 315), lands again at frame 25 (cy 435), small hop f26-27, then moves on the
table toward the camera and to the left (f28-35), leaves the table's FRONT edge at frame 35, falls past the
front edge (f36-38) and exits through the bottom of the image; not visible from frame 39 (t = 1.625 s) on.
The ball approaches the camera during the whole clip: its apparent diameter grows from ~21 px (f0) to ~31 px
(f19-20) to ~33-36 px (f25-28) and ~37-42 px (f29-34), i.e. depth roughly halves (diameter ratio ~2).
For 3D back-projection use the given depths (or depth ∝ 1/diameter) with f = 763 px.

## Static objects
Table top (trapezoid in image): back edge y≈430-437 from x 461 to ~765 (~304 px); front top edge from
(302, 520) to (911, 538) (~609 px); front slab face bottom y 548 (left) - 561 (right), thickness ~23-26 px.
Leg: x 559-607 (45 px wide), from y 561 to the image bottom (cut, ≥159 px visible). Table is static.

## Camera
Static: shift of the table region vs frame 0 is ≤1 px in all frames (segmentation edge jitter). No pan.

## Reliability / ambiguities
- Centres: ±1-2 px in clear frames (0-11, 15-20, 26-34). Frames 12-14, 21-24, 36-37 have strong vertical motion
  blur: the mask is the blur streak, its centroid ≈ mid-exposure centre (±3-5 px); use minor_extent_px as size.
- On the table (f25-35) the lower edge of the ball is low-contrast against the table and the ball's
  shadow/reflection lies just below it (excluded since it is darker); height may be under-estimated by a few px
  and cy biased up by ~1-3 px. Width there is inflated by horizontal blur (bbox_w > diameter).
- Frames 37-38: ball cut by the image bottom (occluded = 1); centroid biased upward.
- The first bounce (f14) happens right at the table's back edge in the image; it is on the table top (rebound
  is immediate), but contact position along depth is uncertain.
- Hop at f26-27 is small (~7 px); could be a rolling bump rather than a bounce.
- Segmentation can drop thin parts of the ball in single frames (area jumps); minor_extent_px is the most
  stable size measure.
