# simulation_0172_segmented — measurement notes

**Scene:** a segmentation video (3D Blender render with the background replaced by plain white), 2304x1296 px, 24 fps,
80 frames (t = 0 to 3.292 s). It contains exactly one object: a **walking astronaut** in a white spacesuit with a
backpack. The astronaut is visible and unoccluded in every frame and never touches the image border. The image
shows no other objects, no ground, no horizon and no markings.

## Files
- `scene.json`: inventory, summary numbers, events, camera notes.
- `tracks/astronaut.csv`: one row per frame (0-79). Columns:
  - `pelvis_x, pelvis_y`: the reference point, a pelvis estimate (see below).
  - `centroid_x/y`: mask centroid.
  - `bbox_x0,y0,x1,y1,w,h`: bounding box (all in px).
  - `area_px`
  - `main_axis_len, across_axis_w, main_axis_angle_deg`: the mask's PCA extents.
  - `head_top_x/y`: topmost mask point.
  - `feet_x/y`: lowest point (mean x of the bottom 3% of rows).
  - `touches_border`, `occluded` (always 0).
- `scripts/track.py`: builds the mask and the track. `scripts/analyze.py`: finds extrema and draws the trajectory image.
- `check/fNN.png`: mask, box and point overlays. `check/trajectory.png`: pelvis path in green, feet in red.

## Method and reliability
- **Mask:** pixels where 255 minus the smallest RGB channel is more than 18, closed with a 5x5 kernel. I keep the
  largest blob plus small blobs near it. I checked the overlays (frames 0, 20, 40, 60, 79): the mask covers the
  whole suit, backpack, hands and boots. The boundary is accurate to about ±2 px; very pale highlights at the edge
  may lose 1-2 px.
- **Pelvis:** this is a heuristic: 47% of the bbox height below the head top, with x taken as the mean mask x in
  that row band. Depending on the pose it may sit about 10-30 px higher than the true hip joint, which is roughly at
  the belt line or slightly above the crotch. The mask centroid stays within about 10 px of it. For speeds, use
  `pelvis_x/y` or `centroid_x/y` and smooth over a few frames. Per-frame jitter is about 1-3 px.
- **Height:** `bbox_h` is the apparent height in the current walking pose, including the backpack and helmet top.
  It changes with the gait (legs spread or together) and with distance. Rest standing height is never shown. The
  image height at its tallest is about 435 px (f79).
- **Apparent size over time:** median `bbox_h` per 10-frame block is 341, 349, 382, 410, 416, 404, 405, 428. The
  astronaut gets closer to the camera overall (about 1.27x larger at the end), with a plateau or slight dip around
  f50-65.

## Motion and events
- The astronaut walks left to right the whole time. It is already moving at f0 and still moving at f79, so the
  clip has no start or stop of motion.
- The pelvis moves from (688, 759) at f0 to (1874, 834) at f79. Mean image x-speed per 10-frame block is 8.9, 18,
  29, 16, 13, 16, 11, 7 px/frame, so it is fastest between f20 and f30. Part of this is perspective or direction
  change: the path weaves vertically in the image. It goes down until about f16, up until about f35 (the highest
  point on screen), down until about f63, then stays level.
- Gait: `bbox_w` (leg spread) peaks at about f0, f54 and f79 and is smallest at about f20 and f76. I did not
  measure individual footfalls reliably.

## Camera and ambiguities
- **Camera:** the background is removed, so camera motion cannot be checked. Assume it is fixed (the simulation
  convention).
- **No perspective cues:** the image has no ground plane, horizon or vanishing points.
- **Conflicting depth cues:** in f16→f32 the figure moves up the image while growing (h 351→407). A fixed camera
  over flat ground would show the opposite, so either the terrain is uneven or the path curves strongly in depth.
  For 3D questions, use the given depth_info together with the pixel positions and estimate the focal length from
  the known size and depth.
- **Shadows and blur:** none (the background is white). There is slight motion blur on swinging limbs.
- No similar objects exist that could be confused with the astronaut.
