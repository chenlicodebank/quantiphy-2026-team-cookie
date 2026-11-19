# simulation_0299 – measurement record

## Scene
- 3D Blender render: 2560x1440, 24 fps, 72 frames (t = frame/24, 0–2.958 s).
- One object, a **forklift** (yellow body, dark-grey cab, roof guard and mast, two forks, Toyota label on the mast). It sits on a seamless light-blue backdrop that also serves as the ground. There are no other objects, markings or ground texture.
- The camera is static: no pan or shake, and the backdrop shading does not move.
- The forklift drives forwards (forks leading) away from the camera, towards the upper left of the image, on a straight heading. It shrinks steadily: sqrt(mask area) goes from 521 px at frame 15 to 335 px at frame 71.

## Files
- `scene.json`: inventory, camera, events, and example sizes.
- `tracks/forklift.csv`: one row per frame (0–71) with these columns:
  - frame, time
  - bbox centre (bbox_cx, bbox_cy)
  - mask centroid (mask_cx, mask_cy)
  - bbox x0, y0, x1, y1, w and h
  - bottom_x, bottom_y: the lowest mask point, i.e. the rear-wheel ground contact
  - mask_area, sqrt_area
  - PCA length, width and angle of the mask
  - cut_by_frame_edge
- `scripts/track.py`: segmentation and tracking. It also writes the overlays `frames/chk_XX.jpg`. `scripts/summary.py` prints per-frame values. `scripts/probe.py` is the background and threshold probe.

## Method
- Background = per-frame median colour, about RGB (140,174,202).
- Mask = sum|RGB − bg| > 40, followed by a 15-px closing, then the largest component plus any nearby components (forks).
- Background noise and gradient stay below 30. The faint shadow stays below 40 and is excluded.
- Overlays at frames 0, 12, 24, 36, 48, 60 and 71 were checked visually. The contour fits the whole vehicle, including the mast tops and fork tips, and contains no shadow.

## Reliability and caveats
- **Frames 0–14: the bottom of the image clips the forklift's lower part (rear wheel).**
  - In those frames, bbox_y1, bbox_h, the centroid, area and PCA values are biased.
  - bbox_x0, bbox_x1 and bbox_y0 are unclipped and fine to use for early motion.
- Edges are accurate to about ±1–2 px. Centroids are smooth to well under 1 px per frame.
- The vehicle root (the reference origin) is not visible.
  - The mask centroid sits on the body, about mid-height.
  - The bottom point is the rear-wheel contact, which roughly marks the ground plane.
  - For speeds, use the frame-to-frame displacement of the centroid, or of bbox_x0/x1/y0. They agree once the forklift is fully visible.
  - Because the forklift recedes, image displacement understates the later world motion. Use the given depth_info for 3D.
- Apparent size versus depth: sqrt_area and bbox_h shrink roughly in proportion to 1/depth. The view angle changes only slightly (PCA angle 57→66°), so the size ratio between two frames ≈ inverse depth ratio. This gives a way to estimate focal length from a given depth plus a known length or height, e.g. f ≈ bbox_h × depth / real height (approximate, since the bbox includes perspective tilt).

## Events
- Frames 0–1: at rest.
- Frame 2 (0.083 s): motion starts.
- Frames 2–~50: the per-frame image displacement grows steadily (smooth acceleration from rest).
- Frames ~50–71: the image displacement is about constant (~18 px/frame in x and ~7 px/frame in y at the bbox top-right). Since the forklift is still receding, the world speed is still rising or roughly constant.
- No turn, stop, lift or impact occurs. The clip ends with the forklift still moving.
