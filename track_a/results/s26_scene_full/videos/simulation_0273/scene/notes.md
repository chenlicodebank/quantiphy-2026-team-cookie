# simulation_0273 — measurement record

2D Blender render, 2560x1440, 24 fps, 72 frames (3.0 s). t = frame/24. Pixels: x right, y down, full resolution.

## Content
- **phoenix** (only moving object): fantasy bird in side view, head pointing left; green body/neck, green-purple-pink
  wings, long red/pink tail with peacock-like eye spots and a golden flame-shaped tip. Flies leftward across the
  whole clip at nearly constant height while flapping. Visible and unoccluded in all frames 0-71.
- **sky_background**: static sunset sky with grey and pink clouds. No ground, horizon, or other objects.

## Files
- `scene.json`: inventory, camera, events, summary extents.
- `tracks/phoenix.csv`: one row per frame (0-71). Columns:
  frame, time_s; `cx_mask, cy_mask` (centroid of the whole mask); `cx_green, cy_green, green_px` (centroid of the
  green body pixels inside the mask, G > R+8); `head_x, head_y` (leftmost mask pixel = beak tip, and mean y there);
  bbox_x0/y0/x1/y1/w/h/cx/cy (bounding box of the mask); mask_area_px; pca_len/pca_wid/pca_angle_deg (mask extent
  along and across its principal axis); occluded (always 0).
- `bg_median.png`: half-resolution median background.
- `scripts/bg.py` (median background + camera-motion check), `scripts/track.py` (segmentation, track, overlays),
  `scripts/summary.py` (duplicate-frame check, summary stats).

## Method
Median of every 4th frame gives a clean background, since the bird keeps moving. Mask = max-channel |frame - bg| > 25,
then open/close. Components are grouped with a 51 px dilation around the largest blob, and specks < 80 px are dropped.
I checked overlays at frames 0, 6, …, 66 and 71 (frames/ov/): the masks cover head, wings and tail correctly.

## Reliability / ambiguities
- Camera: static (phase-correlation shift < 0.07 px).
- Frames 0 and 1 are virtually identical (mean diff 0.03 grey levels against about 0.7 for later pairs), so motion
  starts after frame 1.
- **Reference point**: the rig origin isn't visible. `head_x` is the most body-fixed horizontal coordinate (±3 px
  noise, with a few glitches where the leftmost pixel jumps: frames 16-17, 24-25, 29-30). The head bobs a little
  with each wing beat. `cx_green` is close to the body but shifts with wing pose because the wing roots are also
  green. `cx_mask/cy_mask` swing by about ±50 px with the wings, so don't use them for speed.
- Motion: the bird speeds up leftward. Mean head speed is 5.6 px/frame over frames 0-24, 17.9 over 24-48 and 29.7
  over 48-71. Net head displacement over frames 0→71 is −1246 px in x and about −2 px in y (head_y stays at
  663-687). Per-frame differences are noisy, so smooth or fit before differentiating.
- Sizes: bbox_w (horizontal, beak to tail tip, the bird's main axis) is 550-634 px, median 600, with no trend over
  time, consistent with 2D. bbox_h (vertical) is 232-458 px and is set by wing pose: minimum at mid-stroke (frames
  9, 21, 34, 46, 59, 71), maximum with wings down (12, 37, 62). The wings beat roughly in the image plane (side view),
  so the true wingspan isn't directly visible. bbox_h max (about 458) is the largest vertical wing extent.
- Mask edges: the pale pink tail and wing feathers are close to the background colour, so the mask has interior
  holes, and the faint feather tips may lose ±5-10 px at the edges. Mask area is therefore a rough figure. The bbox is
  more reliable.
- Wing-beat period is about 12.4 frames (0.52 s).
