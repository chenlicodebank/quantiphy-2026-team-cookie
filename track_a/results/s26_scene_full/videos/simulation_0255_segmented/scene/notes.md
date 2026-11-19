# simulation_0255_segmented — measurement record

2D segmentation video: 1920x1080, 24 fps, 41 frames (t = frame/24, 0 to 1.667 s). Pure white background, static camera.
All values are in pixels and seconds. Image coordinates: x to the right, y down.

## Files
- `scene.json`: scene metadata, the object inventory, diameter statistics, per-frame step lengths, net displacement and path length, events, and camera.
- `tracks/ball.csv`: one row per frame (0–40). Columns: frame, time_s, x_px, y_px (intensity-weighted centroid = sphere centre/origin), bbox_x0/y0/x1/y1 (inclusive, mask threshold = darkness > 60 from white), length_px (horizontal bbox extent, along the motion), width_px = height_px (vertical bbox extent), equiv_diam_px (diameter of a circle with the same soft-mask area), mask_area_px, rgb (core colour), occluded (always 0), touches_edge (always 0).
- `scripts/track.py`: the tracker (connected components on the non-white mask, then a weighted centroid). `scripts/check.py`: per-frame dx/dy, a check for faint pixels away from the ball, and overlays. `scripts/write_scene.py`: builds scene.json.
- `../frames/overlay.png` and `../frames/overlay_zoom.png` (in scene_ws/frames): mask contours (red) and centroids (blue) for every 4th frame. Visually confirmed: each contour covers the whole ball.

## Content
- **Only one object, the ball**: a small olive / dark yellow-green shaded sphere (core RGB about (80,87,6)). It is visible and unoccluded in every frame 0–40. No other objects, ground, markings or static props. The faint pixels that check.py finds are compression ringing next to the ball (plus a 2-pixel speck at (768,572)), not objects.
- **Size**: diameter ≈ **25 px** (equivalent diameter 25.06 ± 0.35, vertical extent median 25). The horizontal extent is about 26–27 px because of slight motion blur and antialiasing. For a size prior, use 25 px (±1 px, about 4%).
- **Motion**: a straight horizontal line to the right at constant y = 564.15 px (std 0.07 px). It moves from x = 69.07 (frame 0) to x = 1623.06 (frame 40). Net displacement = path length = 1554.0 px.
  - The per-frame step falls steadily from 44.26 px (frame 0→1) to 33.51 px (frame 39→40), so the ball is slowing down.
  - The second difference averages about −0.28 px/frame² but is noisy frame to frame (±0.5 px from centroid jitter). Smooth or fit over several frames before using pixel speed or acceleration.
  - Centroid precision is about ±0.15 px per frame.
- **Events**: the ball is already moving at frame 0 (no visible release) and is still moving, slower, at frame 40 without leaving the frame. There are no bounces, impacts, contacts or direction changes.
- **Camera**: static. The background is featureless white, there is no perspective, and one metres-per-pixel scale applies, set from the question's prior (ball diameter in px, pixel speed or pixel acceleration).

## Reliability / ambiguity
- Positions are reliable to well under 1 px. The diameter is reliable to about ±1 px.
- Single-frame speeds from backward differences carry about ±0.2 px/frame of noise. Single-frame accelerations are noisy; the deceleration looks roughly uniform.
- There is no ambiguity between objects (only one ball) and no occlusion. There are no shadows because the background has been replaced.
