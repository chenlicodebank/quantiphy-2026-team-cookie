# simulation_0310 – measurement record (pixels and seconds only)

Video: 3D Blender render, 2560x1440, 24 fps, 72 frames (t = frame/24, 0 to 2.958 s). Static camera
(phase correlation of the tree band against frame 0 shifts it by less than 0.05 px). The camera looks obliquely down at flat bare forest
ground. There is no horizon.

## Files
- `scene.json`: inventory, static-object pixel extents, events, camera notes, and manual ground-contact estimates for the forklift.
- `tracks/forklift.csv`: one row per frame (0-71). Columns:
  frame, time; `centroid_x/y` (full-mask centroid); `orange_cx/cy` (centroid of the orange body panels,
  which is the smoothest point, with about 1 px noise); `orange_area_px`; `bbox_cx/cy`, `bbox_x0,y0,x1,y1,w,h`; `mask_len_major`,
  `mask_wid_minor`, `mask_angle_deg` (cv2.minAreaRect of the mask); `mask_area_px`; `touches_frame_edge`; `occluded`
  (both are 0 in every frame).
- `scripts/bg2.py` builds a clean median background (half resolution) from frames where each pixel is free of the forklift.
  `scripts/track.py` does the background subtraction, removes the cast shadow, and writes the CSV and overlays.
  `scripts/analyze.py` computes step sizes, the line fit and the vegetation boxes. `scripts/bg.py` is the first median attempt plus the camera check.

## Objects
- **forklift** is the only moving object. It is orange/yellow with a black cab, mast and roll cage, and has two orange forks.
  It drives forks-first in a straight line toward the upper left, away from the camera. Its image direction is about −156° (y down),
  and the path is the line cy = 0.468·cx + 86.5 (max residual 7 px). It is visible and unoccluded in all frames.
- Static objects: the left pine (bbox 250–664 × 170–624, base ≈ (470,636)); the centre leafy bush/young tree (bbox 1258–1916 ×
  52–540, base ≈ (1650,535)), which has a thick trunk rising out of the top of the frame; the right pine, cut by the right edge (2268–2560 ×
  174–664); and the flat ground with static diagonal shadow stripes from off-screen trees. The forklift never occludes these objects
  and is never occluded by them.

## Events
- The forklift starts from rest at frame 0–1. Its step size is 0.2 px for 0→1 and 1.3 px for 1→2.
- Its image speed rises roughly linearly up to about 26 px/frame near frame 48 (t ≈ 2.0 s), then stays about constant until the end.
  This is image speed only. The apparent size shrinks from a bbox height of 780 px to 510 px, so the world speed keeps rising if the
  image speed is constant. Answering sessions should fit their own motion using the depths.
- The clip ends with the forklift still moving. No turns, stops or contacts.

## Reference point and reliability
- Mask: background difference with the shadow suppressed (uniform darkening of the ground). The overlays at frames 0, 42 and 71 were checked
  visually and cover the whole vehicle, forks included. The bbox is good to about ±4 px (half-resolution masks). Small notches remain
  where dark bottom parts meet the forklift's own shadow, so the area and centroid are slightly biased (a few px).
- The Blender vehicle root is most likely on the ground under the vehicle, which is lower than the visual centroid. Manual
  wheel-contact points and footprint-centre estimates for frames 0 and 71 are in scene.json (±30–50 px).
  For displacement or speed questions, use the orange or mask centroid together with depth_info. Per-frame differences of `centroid_x/y`
  carry 2–4 px noise, so prefer `orange_cx/cy` or smooth over several frames.
- Apparent size: bbox_w and bbox_h, mask_major and mask_minor per frame. The viewing angle changes during the clip (side-rear at the
  start, more from behind at the end), so the width and length ratios change differently. Bbox height is the most depth-like size
  cue. Ratios: bbox_h 780 → 690 (f36) → 510 (f71); bbox_w 870 → 736 → 492.
- The focal length is unknown. Estimate it from depth_info plus a known size (for example the forklift length or height) and pixel
  extents at the matching frame, with the principal point assumed at (1280,720).
