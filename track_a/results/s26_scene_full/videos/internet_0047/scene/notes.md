# internet_0047 – measurement record (pixels, seconds; no metric scale)

**Scene.** This is real handheld footage looking straight down at a wooden basketball-court floor. It runs 30 frames at 30 fps, 1920×1080, with t = frame/30.
- One basketball (orange-brown with black seams) rolls from the left edge to the right edge at nearly constant image speed. It moves along and just below a maroon court line, slightly upward in the image.
- There is no bounce, impact, release or direction change.
- Other objects are all static: the maroon court lines (a horizontal one, plus left and right verticals forming a rectangle's corners), a light-blue stripe, the operator's two shoe toes at the bottom edge, and floor reflections.

## Files
- `scene.json` holds:
  - the inventory and static-object pixel extents (measured in frame 29);
  - the events;
  - the per-frame camera shift;
  - perspective remarks;
  - ball summary values.
- `tracks/basketball.csv` has one row per frame for frames 0–25. Columns:
  - `cx, cy`: the visible centre (raw image pixels).
  - `bbox_x0..y1`: the extents of the motion-blurred ball.
  - `diameter`: the un-blurred ball diameter, 2R.
  - `blur_len, blur_angle_deg`: the smear length and direction within the exposure.
  - `extent_x_blurred`: the horizontal span of the smeared ball, 2R + L.
  - `extent_y`.
  - `cam_dx, cam_dy`: the camera shift.
  - `cx_stab, cy_stab`: the centre minus the camera shift, i.e. in frame-29 floor coordinates.
  - `fit_rms`.
  - `cut_by_edge` / `occluded`.
- `camera_shift.json`: the raw phase-correlation shifts for the top and bottom floor strips.
- `scripts/`:
  - `camera.py`: camera shift.
  - `track_ball.py`: ball tracking, and draws `frames/overlay.png`.
  - `static_objects.py`: line and stripe measurements.
  - `build_scene_json.py`.
  - Debug helpers: `debug_mask.py`, `view_crops.py`, `sample_colors.py`.
  - `_fits.json` holds the raw fit parameters.

## Methods
**Camera.** The camera shift is measured by phase correlation of floor strips (y 0–350 and y 650–1000) against frame 29.
- The camera drifts smoothly by up to −22 px vertically and −2…+1 px horizontally, and rotates very slightly.
- Convention: a floor point at (x, y) in frame 29 appears at (x + cam_dx, y + cam_dy) in frame i.
- The camera's vertical drift is at most ~1.3 px/frame, while the ball moves ~78 px/frame. That is a ≤2 % effect, so raw and stabilised tracks give nearly identical speeds.

**Ball.** The background is the median of frames 27–29 (ball gone), registered for camera shift. For each frame I took the LAB difference to that background and converted it to a soft coverage map.
- I fitted a motion-blurred disk model (a disk swept along a short segment, a "stadium") by least squares, using only pixels whose background is floor.
- Pixels over the maroon line are excluded because the dark-brown ball has almost no contrast against it. Plain thresholding gave notched masks and errors of 30–100 px, so I dropped it.
- Overlays (`frames/overlay.png`) confirm that the fitted circles hug the ball in frames 0–23.

**Static objects.** Line edges were found from colour masks in frame 29.

## Results and reliability
**Ball diameter.** 225 px is the median over frames 1–21 (range 222–231). It grows slowly from ~223–225 px on the left to ~229–231 px on the right, about +3 %. That suggests the ball is slightly nearer the camera on the right, or the camera is tilted; the floor lines also show mild keystone.
- Use `diameter` as the ball's pixel size (vertical extent, essentially blur-free).
- `extent_x_blurred` (median ~251 px, i.e. ~225 + 10–55 px of smear) is the smeared horizontal extent. Someone reading the size off a single frame by eye along the motion direction might get this larger value instead.

**Centre accuracy.** Estimated at ±1–2 px in frames 1–21.
- Frame 0 (left-cut, ~85 % of its width visible): about ±3 px.
- Frames 22–23 (right-cut): about ±3–5 px.
- Frames 24–25 are only a sliver and are unreliable. The frame-24 fit (x 1922) lies outside the image; do not use 24–25 for speeds.

**Motion.** The image step is 75–85 px/frame (median 78.0) along a direction tilted ~3.7° upward (dy ≈ −5 px/frame). There is no clear acceleration trend; steps scatter by ±3 px, which is within the fit noise.

**Events.**
- Frame 0: ball already moving.
- Frame 1: first fully visible.
- Frame 2: crosses the left vertical line.
- Frames 13–14: passes over the blue stripe.
- Frame 21: crosses the right vertical line; last fully visible frame.
- Between frames 23 and 24 (~0.78 s): the centre leaves the image.
- Frame 25: last pixels visible.

**Static extents (frame 29).**
- Maroon lines are ~43–47 px thick.
- The horizontal line runs from y≈487–529 at x=300 to y≈445–489 at x=1800.
- Vertical lines: left at x≈211–260, right at x≈1713–1800.
- Spacing between the vertical lines at y=550: 1453 px between inner edges, 1542 px between outer edges, ~1497 px between centrelines. The spacing widens downward (~1560 px between centrelines at y=1050).
- The blue stripe is ~46 px wide, at x≈1172–1241, running from y≈507 to the bottom edge (~573 px visible).

**Ambiguities.**
- The ball rolls on top of the dark maroon line in frames ~8–21, which is low-contrast; this was handled by excluding those pixels from the fit.
- Motion blur is 10–55 px; the shape model removes it from the diameter.
- No shadow is distinct from the ball.
- The bright floor reflections and the whitish streak near x≈110 are not objects.
- The shoes belong to the camera operator and do not move apart from camera shake.
- No pixel-to-metre scale is assumed. An answering session should take one scale from its prior: for example, the ball's pixel diameter 225 px, or the pixel speed ~78 px/frame = ~2340 px/s.
