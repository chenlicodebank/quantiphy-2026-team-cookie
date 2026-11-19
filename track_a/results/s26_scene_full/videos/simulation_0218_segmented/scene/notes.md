# simulation_0218_segmented – measurement notes

2D segmentation video, 1920x1080, 24 fps, 50 frames (t = frame/24). One object: a tracked drill robot
(teal body, red top box, black lens head facing left, drill cone + claw facing right, caterpillar treads with 4 big wheels)
driving to the RIGHT across a white background. Camera is static.

## Files
- `scene.json` – inventory, sizes, motion summary, events, background (frame 49) features.
- `tracks/robot.csv` – one row per frame 0-48: bbox (x0,y0,x1,y1, inclusive px), bbox centre, mask centroid & area,
  length_px (bbox width), height_px, tread band extents (rows 800-880) and length, `ref_x`/`ref_y` reference point,
  `ref_x_source`, template-match error/overlap, `clipped_by_frame_edge` (= `occluded`, cut by the image border).
- `scripts/` – probe.py (mask extents per frame), track.py (mask/bbox track), track2.py (tread template matching,
  ref_x), overlay.py (check images, frame-49 profiles).

## Method
- Mask = min(RGB) < 235 (background is pure white), 3x3 opening, components > 50 px. Overlays checked visually
  (frames 1, 9, 20, 32, 40, 47): mask covers the whole robot including drill, claw and top handle.
- Reference point: the tread/wheel band of frame 20 (x 590-1064, rows 800-880) template-matched in every frame,
  using only in-image columns, so it is a rigid point of the chassis unaffected by perspective changes of the
  silhouette. ref_x = band centre (827.0 at f20). Frames 0-1 and 45-48 (too little visible) use the linear fit.
- Result: ref_x = -188.87 + 50.789·frame px (max residual 0.4 px over frames 2-44) → constant 50.79 px/frame
  = 1218.9 px/s to the right, no vertical motion, zero acceleration. Total displacement over the video
  (frames 0→48) = 48 × 50.79 = 2437.9 px along a straight line (path length = net displacement).
- Mask centroid / bbox centre are NOT constant-speed (they change with silhouette clipping and perspective); use ref_x
  for motion.

## Sizes (pixels)
- Frame 20 (near image centre, mostly side-on): bbox 590-1225 × 270-895 → length 636 px (rear of treads/lens head to
  drill tip), height 624-626 px (624 after mask opening, 626 raw) (top handle to tread bottom); tread length 475 px.
- Perspective: when left of centre the rear face shows, right of centre the front face shows, so bbox length ranges
  616 (f9) → 698 (f32) px and tread length 475-520 px. Height stays 622-626 px. For a prior "robot length"
  the most side-on view is f20-f23 (636-647 px); 2D scale = prior / pixel size from that frame is recommended.
  Vertical extent y 270-895 in every fully visible frame.

## Events
Robot already moving at f0 (partly visible at left), fully visible f9-f32, drill tip hits right edge f33,
last sliver f48, gone at f49. No start/stop, bounce or turn inside the clip.

## Reliability / ambiguities
- ref_x very reliable (±0.5 px); bbox edges ±1 px. Frames with `clipped_by_frame_edge=1` have truncated bbox/mask.
- Frame 49 is an unsegmented background render (warehouse wall, pillars at x 643-705 and 1593-1649, floor white lines at
  y≈843 and ≈908); it has no robot and may not be exactly registered with the robot frames.
- Where the root origin sits on the robot is unknown (likely chassis bottom-centre); for speeds only horizontal
  translation matters and all rigid points move identically (50.79 px/frame).
- No motion blur problems; shadows absent (segmented).
