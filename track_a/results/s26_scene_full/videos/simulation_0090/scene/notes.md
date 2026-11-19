# simulation_0090 – measurement record (pixels, seconds)

2D simulation, 1920x1080, 24 fps, 30 frames (t = frame/24). The scene is two birds flying right to left in front of a plain blue sky. There is no ground, there are no landmarks and there are no static objects. The camera is static: the background residual against the sky-only frames 24–29 stays at noise level (mean |dBGR| < 0.2) in every frame.

## Files
- `scene.json`: inventory, visibility, extents summary, events and camera check.
- `tracks/eagle.csv`, `tracks/crow.csv`: one row per frame in which the bird is visible. Columns:
  - `cx, cy`: mask centroid.
  - `bbox_cx, bbox_cy`: bounding-box centre.
  - `body_line_y`: the image row with the widest horizontal mask run, i.e. the beak-to-tail body axis.
  - `x0 y0 x1 y1`: bounding box. `bbox_w` = horizontal extent (the flight direction, beak to tail); `bbox_h` = vertical extent, which changes with the wing beat.
  - `axis_len / axis_wid / axis_angle_deg`: principal-axis extents of the mask. These swing with the wings, so prefer `bbox_w` for body length.
  - `area`, `clipped_by_frame_edge`, `touching_other_bird`, `occluded`.
- `scripts/measure.py`: segmentation and tracks. The mask is |frame − median(frames 24–29)| summed over BGR > 20, followed by a 5x5 closing. Overlays are written to `frames/overlay/` and were checked: the masks cover the full bird, including the pale white head and tail.
- `scripts/camera_and_json.py`: camera check and scene.json.

## Objects
- **eagle**: a large bald eagle (dark wings, white head and tail, yellow beak and feet). It is the bigger and faster bird and faces and flies left. It is fully visible in frames 0–10, clipped by the left edge at 11, only a sliver at 12, and gone from 13.
  - Horizontal extent `bbox_w` = 181–182 px in all unclipped frames (2–10).
  - Vertical extent changes with the wing beat: max 200 px (frames 0–1, wings up), min 48 px (frame 6).
  - The body stays level at y ≈ 600.
  - The bbox x0 moves about −156 px per frame, steadily, from frame 1→2 onward.
- **crow**: a small blue-black crow. It is smaller and slower, starts directly behind (right of) the eagle and drops behind. It faces and flies left. It is fully visible in frames 0–18, clipped at 19, and gone from 20.
  - `bbox_w` = 110–113 px.
  - `bbox_h` cycles with a 9-frame wing-beat period: min 36 px (frames 4 and 12), max 95–96 px (frames 9 and 18).
  - The body is at y ≈ 601–611 and bobs a few px.
  - x moves about −95.5 px per frame, steadily (x0 goes from 1507 at frame 3 to 648 at frame 12).
- **Speed ratio**: crow/eagle ≈ 0.61 in pixel speed. The size ratio of the horizontal extents is ≈ 0.61 as well.

## Events
- Frames 0 and 1 are essentially identical: there is no motion between them. Motion starts at frame 1→2 and is uniform after that, with no acceleration visible in x.
- Frame 2 (t = 0.083 s): the birds stop touching each other.
- Frame 11 (0.458 s): the eagle reaches the left edge. It is gone after frame 12 (0.5 s).
- Frame 19 (0.792 s): the crow reaches the left edge. It is gone from frame 20 (0.833 s).
- Frames 20–29 show empty sky.

## Reliability and ambiguities
- **Frames 0–1 (birds touching):** the eagle's feet and tail overlap the crow's beak, so the mask was split at column x = 1707.
  - Eagle: its true x1 there is ≈ 1728 (x0 + 181). The recorded bbox_w of 159 and the centroid are biased to the left.
  - Crow: its true x0 is ≈ 1699–1700, not 1707. This is why the frame 1→2 dx shows −104 instead of −96.
  - Use x0 for the eagle and x1 for the crow (both reliable) in these two frames.
- **Reference point:** the world origin of each bird is not visible. The mask centroid and the bbox centre shift with the wing beat (eagle cy goes from 534 to 651; crow cy goes from 584 to 615). For positions and speeds, the leading/trailing bbox edges (x0, or the bbox x-centre in unclipped frames) and `body_line_y` are the most stable proxies for the origin. The flight is essentially horizontal.
- **Clipped frames:** extents in clipped frames (eagle 11–12, crow 19) are partial.
- **Shadows and blur:** there are no shadows and no significant motion blur. Mask edges are accurate to about ±1–2 px.
- **Lengths and wingspan:** the horizontal extent includes beak to tail. Wing tips never extend past it in this side view. The wingspan is not visible because the wings beat toward and away from the camera, so the vertical extent is the wing-beat height.
