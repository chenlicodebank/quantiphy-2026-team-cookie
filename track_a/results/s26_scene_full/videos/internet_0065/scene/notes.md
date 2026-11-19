# internet_0065 – measurement record

**Scene:** a handheld phone looks straight down at a polished hardwood gym floor. Over 31 frames (30 fps, 1.03 s, 1920x1080), one
basketball rolls left to right across the upper half of the image. It travels in a straight line, close to horizontal, at
roughly constant pixel speed. The filmer's shoe toes show at the bottom centre. Static markings: a maroon horizontal line
near the top, maroon vertical lines at the left border and at x≈1680, and a pale-blue vertical stripe at x≈1076. No bounce,
impact, release or direction change is seen. The ball is already moving when it enters and is still moving when it leaves.

## Files
- `scene.json`: inventory, static-object pixel geometry (frame 0), ball size summary, camera summary and events.
- `tracks/basketball.csv`: one row per frame (0–30).
  - Columns: `visible`; mask centroid `cx_px, cy_px`; bbox `x0,y0,x1,y1,w,h` with its centre; `length_main_axis_px` /
    `width_across_px` (mask extents along and across the PCA axis); `area_px`, `equiv_diam_px`; minimum enclosing circle;
    stabilised (frame-0 coordinates) centroid and bbox centre; `truncated_by_frame_edge`; `occluded`; and
    **`cx_est, cy_est`**, the recommended reference point.
  - `cx_est, cy_est` equals the centroid when the ball is fully in view. When the ball is cut by the image border, it is
    the visible leading or trailing bbox edge ± L/2, with L = 274.6 px (the median blurred length).
  - `cx_est_stab, cy_est_stab` is the same point mapped into frame-0 coordinates. Use it when measuring motion against
    the background.
  - `main_axis_deg` means little because the blob is nearly round.
- `tracks/camera.csv`: per-frame 2x3 similarity transform (frame i → frame 0). `bg_shift_x/y_px` is how far the image
  content at the image centre has moved since frame 0.
- `camera_affine.json`, `camera_shift_raw.json` (phase-correlation cross-check), `static_raw.json`: raw outputs.
- `track_check.jpg`: stabilised centres and bboxes drawn on frame 0. They sit on the ball's path as expected.
- `scripts/`:
  - `camera_affine.py`: ORB features + RANSAC similarity. The ball band and the shoes are masked out.
  - `camera_shift.py`: phase correlation, used as a cross-check.
  - `track_ball.py`: segmentation and per-frame measurements.
  - `finalize_track.py`: edge correction, visibility fixes and writes `camera.csv`.
  - `static_lines.py`: measures the static markings.
  - `draw_track.py`, `montage.py`, `crops.py`, `probe_colors.py`: visual checks.

## Method
- **Camera:** the camera is not static. It drifts smoothly. Relative to frame 0, content moves up to −9.8 px in x and
  +56.8 px in y by frame 30. Rotation is ≤0.41° and scale change is ≤0.5%. ORB and phase correlation agree within about
  2 px.
  - Against the ball's ~98 px/frame horizontal motion this is small (≈0.3 px/frame in x, up to ≈3 px/frame in y).
  - The raw image y of the ball rises by ~60 px over the clip. About 40 px of that is camera drift; the stabilised drift
    is only ~20 px.
- **Ball mask:** I took the colour difference (Lab) to two ball-free background frames (0 and 30), each warped into the
  current frame with the camera transform, and kept the smaller of the two differences. A pixel counts as ball when that
  difference is above 22 **and** Lab a > 136 (reddish).
  - The colour condition removes the ball's soft grey shadow, which otherwise added ~60 px to the length. It also removes
    the pale-blue stripe.
  - a > 136 sits halfway between ball and floor, so the mask edge is at the 50% point of the motion blur.
  - Where the ball crosses the maroon lines, pieces of the mask are merged and filled with a convex hull, because the
    ball and the maroon line have the same colour.
  - I checked the overlays visually for frames 1–24.

## Ball size (pixels)
- **Diameter:** the unblurred extent across the motion (vertical, bbox_h) is a median of **258 px** over frames 5–21
  (range 253–268). It is ~255 px near the image centre and grows towards the left/right edges, probably from wide-angle
  lens stretch.
- **Blurred length along the motion (horizontal):** median 274.6 px (254–293). That is the diameter plus ~15–20 px of
  motion blur.
- An annotator's "pixel diameter" would probably fall in 255–275 px. 258 is my best estimate of the true diameter.

## Reliability
- **Centre x, frames 5–21:** ±3–4 px per frame, judging from frame-to-frame scatter (per-frame steps 93–103 px).
- **Centre y:** ±2 px.
- **Frames cut by the border:** in frames 3–4 and 22–24, `cx_est` is ±10 px. In frame 24 only a 43 px sliver is visible,
  so its y is a low-confidence centroid.
- **Frame 2:** only the ball's leading edge is visible (x≈0–45 px). It merges with the left maroon line, so there is no
  mask.
- **Frame 1:** the ball's shadow enters, but the ball itself is not in view (the first detection there was the shadow and
  has been removed).
- **Frames 0 and 25–30:** no ball.

## Ambiguities
- **Rolling or in the air:** I can't confirm from a top-down view whether the ball rolls on the floor or is airborne. Its
  near-constant size and the shadow staying close beside it suggest it is rolling on the floor.
- **Shadow side:** the shadow changes side (right of the ball mid-clip, left of it near the right edge) because of
  several overhead lights.
- **Motion blur:** it stretches the ball horizontally, so prefer the vertical extent for size and the centroid for
  position.
- **Bright spots:** the bright reflections and the bluish window reflections on the left are reflections, not objects.
- **No metric scale:** there is none in this record. Use one scale from the question's prior, applied to the pixel
  quantity it refers to. For example, ball diameter ≈ 258 px, or ~275 px if the prior is measured along the motion
  including blur.
