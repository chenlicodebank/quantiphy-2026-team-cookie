# simulation_0255 – measurement record

2D Blender render, 1920x1080, 24 fps, 41 frames (t = frame/24, 0 to 1.667 s). Static camera on a plain grey
studio (wall above, floor below, with a soft wall/floor edge at y ≈ 544–547 px). There is **one object**: a small
olive/yellow-green ball. It moves rightward along a constant image row (y ≈ 562.6 ± 0.3 px), from x = 70.4 px
(frame 0) to x = 1622.7 px (frame 40). It is visible and unoccluded in every frame.

## Files
- `scene.json`: inventory, camera, events, ball diameter, per-frame dx list, net and path length in px.
- `tracks/ball.csv`: one row per frame (0–40) with these columns:
  - `cx, cy`: centroid of the chroma mask, used as the reference point (the ball's centre/origin).
  - `bbox_*`, `len_px`/`wid_px`/`height_px`: horizontal and vertical extents of the chroma mask.
  - `circ_cx/cy/diam`: minimum enclosing circle of the mask.
  - `area_px`, `touches_edge`, `occluded`.
  - `diff_*`: extents of a background-difference mask (median background), as a cross-check.
- `scripts/track.py`: chroma mask (HSV S > 90 and G − B > 40), largest component. Writes ball.csv and overlays to `frames/ov_XX.png`.
- `scripts/refine.py`: background-difference mask, camera-shift check and location of the wall/floor edge.
- `scripts/summary.py`: per-frame dx, path length and size medians.

## Reliability
- **Centre track:** very reliable. Mask overlays at frames 0/10/20/30/40 sit on the ball. A smooth quadratic fits x(frame) with a residual of about 0.22 px, so per-frame jitter is about 0.2–0.3 px. That noise makes single-frame second differences noisy (±1 px/frame²). Fit over many frames when a question needs an acceleration.
- **Motion:** the ball is already moving at frame 0, so there is no visible start of motion. It slows down steadily, with dx falling from 43.8 to 33.6 px per frame, which looks like roughly uniform deceleration of about 0.27 px/frame² from the fit. There is no bounce, collision or direction change, and it has not stopped by the last frame. Vertical motion is negligible, so path length (1552.39 px) ≈ net displacement (1552.35 px).
- **Diameter:** best estimate **24.5 px** (range 22–26).
  - The chroma mask gives 22–24 px because it misses the darker lower rim.
  - The background-difference mask is 24–25 px wide in the slow late/middle frames. In the fast early frames it reaches 26–29 px wide because of motion blur. Its height of 25–26 px includes a faint contact shadow.
  - Rendered 2D scene, so the size is constant across frames.
- **Camera:** static. The background shift between frame 0 and frame 40 is about 0.15 px.
- **Ambiguities:** none to speak of. There is only one moving object and no similar objects. A faint soft shadow sits just under the ball. The wall and floor are featureless, with no markings.

## Scale
No metric scale is recorded. Use one m/px scale from the question's prior: the ball's diameter (~24.5 px), its
pixel speed (dx × 24 px/s), or its pixel acceleration.
