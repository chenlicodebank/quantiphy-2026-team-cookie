# captured_0031: measurement record

Lab recording (real footage, 3D), 24 fps, 49 frames (t = frame/24, 0 to 2.0 s), 1280x720.
Everything here is in pixels and seconds. No metric scale has been assumed.
Lab convention (from the task, not measured here): f = 763 px, principal point about (640, 360).

## Scene
A seated person behind a small wooden table holds two balls on the far edge of the table, then lets go.
- **yellow_ball**: a yellow-green tennis ball, the larger of the two, on the right.
- **white_ball**: a small white ball (about ping-pong size), on the left.

Both balls roll toward the camera across the table top. The yellow ball rolls off the front edge (about frame 42-43), falls in front of the pedestal leg and the person's jeans, and leaves the bottom of the image after frame 47. It is not visible in frame 48. The white ball drifts left and is still rolling on the table at the end of the clip.

Static objects are listed in scene.json with pixel positions and extents: table (top-surface corners, front-edge length 499 px, back edge 273 px, front face 20 px thick, pedestal leg 55 px wide), the seated person, a black tripod carrying a second camera, a tripod leg at the far left, the TV at top right, a ceiling light, the grey wall panels and the floor cables.

## Files
- **scene.json**: inventory, events, camera information, perspective notes, and summary diameters and positions.
- **tracks/yellow_ball.csv** and **tracks/white_ball.csv**: one row per frame. Columns:
  - `frame`, `t`
  - `visible`
  - `occluded`: 1 while the hands touch the balls (frames 0-15), or while the ball is cut off by the image bottom.
  - `method`
  - `cx`, `cy`: the ball centre.
  - `diam`: the apparent diameter in px.
  - `x0`, `y0`, `x1`, `y1`: the bounding box of the colour mask.
  - `mask_w`, `mask_h`
  - `area`
- **camera_shift.json**: background shift relative to frame 0 for each frame (phase correlation).
- **scripts/**: the scripts used.
  - track.py: tracking.
  - camera.py: camera shift.
  - build_json.py: builds scene.json.
  - views.py, mont.py, probe.py: viewing and probing helpers.

## How the tracks were measured
1. The balls were found by colour segmentation (HSV) inside the table region.
2. **On the table (`circle_fit`):** a circle is fitted to the top, left and right silhouette edges only. The shaded bottom of each ball blends into the table and its reflection, so the bottom edge is not used. Edge points that stick out because of touching fingertips are rejected iteratively. `cx`, `cy` and `diam` come from this circle. Accuracy is about ±1 px for the centre and ±1.5 px for the diameter. The white ball is somewhat worse (about ±2 px) in frames 26-34, where it passes in front of the person's left hand.
3. **Falling yellow ball, frames 43-46 (`bbox_blur`):** heavy vertical motion blur. The centre is the centre of the mask's bounding box and the diameter is the mask width. Accuracy is about ±5 px in y (part of the blurred halo is missed).
4. **Frame 47 (`cut_at_image_bottom`):** only the top of the ball is visible, so `cy` is NaN. `y0` is the top of the ball.

I checked overlays of every frame: the fitted circles sit on the balls.

## Events
- Frames 0-15: both balls are at rest, held by the person's hands. The fitted diameters are slightly low here (the hands cover part of the edge).
- Frame 15 (±1): release. Both balls start moving at the same time.
- About frame 42-43: the yellow ball rolls off the front table edge (the front top edge is at y ≈ 487-490 near x ≈ 725).
- Frames 43-47: the yellow ball falls. It is out of the image at frame 48.
- Frame 48: the white ball is still rolling.
- I saw no bounce and no collision between the balls.

## Camera and perspective
- The camera is static: the largest background shift is 0.12 px.
- The camera sits at about table height, looking slightly down at the table top. The back edge of the table is at y ≈ 426 and the front edge at y ≈ 484-497.
- Both balls move mainly toward the camera, so their pixel displacement badly understates the 3D motion. The depth change shows up in the apparent diameter:
  - yellow ball: 29.5 px (rest) → 56 px (frame 42)
  - white ball: 16.4 px → 29.6 px (frame 48)
- To get depth: Z ≈ 763 · D_true / diam_px, or scale from the given depth_info (depth ∝ 1/diam). Then back-project (cx, cy) with f = 763 px and principal point (640, 360).

## Ambiguities
- "Ball" alone is ambiguous: name them by colour or size (yellow tennis ball versus small white ball).
- The balls' reflections on the glossy table and the motion blur while falling are the main error sources.
- The hands touching the balls before release make the diameters in frames 0-15 about 1 px too small.
