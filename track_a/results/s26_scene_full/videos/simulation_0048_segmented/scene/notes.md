# simulation_0048_segmented – measurement record

3D segmentation clip (Blender render with the background replaced by white), 1920x766, 33 fps, 99 frames (t = frame/33).
**The camera is static.** The kiosk pixels match in all frames apart from compression noise along its edges.

## Objects
- **pedestrian**: a man in a light-grey T-shirt and dark jeans, just right of the kiosk. He walks slowly toward the camera
  and slightly left (in the image, down-left) for the whole clip and is visible in frames 0-98. His bbox height grows from
  185 px to 232 px (the gait makes it fluctuate by a few px).
- **cyclist**: a rider in a dark navy jacket over a blue shirt, on a bicycle; the right-most object. Rides toward the
  camera and grows fast in the image. Fully visible in frames 0-59 (bbox height 179 -> ~310 px). From frame 60 the image
  bottom cuts them off, and they are last visible in frame 91 (only the head and shoulders by ~84+). The bicycle is part of this mask.
- **kiosk**: a static grey box/cabinet in the centre-right foreground with a flat light-grey top, a dark front panel and
  a graffiti poster on its right side. The image bottom cuts off its base. Corners and edge lines are in scene.json.
- Nothing else: no ground, markings or other props are visible (white background).

## Files
- `scene.json`: inventory, camera and perspective info, kiosk geometry, events, and sampled track values.
- `tracks/pedestrian.csv`, `tracks/cyclist.csv`: one row per visible frame. Columns: frame, t, mask centroid
  (cx_mask, cy_mask), bbox x0/y0/x1/y1/w/h, PCA main-axis length / across width / angle, area, head_top_y,
  foot_bottom_y, cut_by_frame_edge, adjacent_to_kiosk, **pelvis_x/pelvis_y (reference point)**,
  pelvis_y_alt_bbox047 (pedestrian only: y0 + 0.47*h), occluded, note.
  `*_raw.csv` hold the same rows before the pelvis/occlusion columns were added.
- `scripts/`: probe.py (static check), track.py (segmentation), refine.py (pelvis, flags), overlay.py (visual
  check), static_summary.py (kiosk edges, vanishing point), write_scene.py.

## Method and reliability
- **Masks:** non-white pixels (min RGB < 235) minus the frame-0 kiosk mask (dilated 3 px), split into connected
  components; the left component is the pedestrian and the right one the cyclist. Overlays at frames
  0/10/30/40/58/60/62/70/80/84/90/98 confirmed both masks cover the full person (and bike) and nothing else. Bbox values are accurate to about 1-2 px.
- **Pedestrian pelvis:** the mask centroid, which sits on the belt/hip line in the overlays. Expect ±5 px, with gait wobble.
- **Cyclist pelvis:** hidden under the torso, so it is estimated. In frames 0-59: head_top + 0.35*bbox_h, at about the
  bottom of the jacket and just above the handlebars. From frame 60 the body is cut off, so it is extrapolated as head_top + 1.172*bbox_w (ratio
  fitted on frames 40-59, stable at 1.13-1.21). The estimate leaves the image at frame 83 (y > 765). Values after
  ~frame 75 are increasingly uncertain (±10-20 px). Frames 0-59 are best for speed or size work.
- **Occlusion:** the cyclist is flagged occluded from frame 60 (cut by the frame edge). From frame 84 the pedestrian's
  left arm/elbow overlaps the kiosk's right edge (x ≈ 1467-1471), which clips the mask by a few px. The body is not
  hidden, and the pelvis is barely affected.
- **Perspective:** the camera is elevated and pitched down. The kiosk's vertical edges converge downward to a vanishing point near
  (1031, ~6500), which is rough. The horizon is above the image. Both people move toward the camera, so their apparent
  size grows: about 1.25x for the pedestrian and about 1.7x for the cyclist over frames 0-59. Image motion is mostly vertical (+y), which
  is mainly depth change, so a single pixel scale is NOT valid. Use depth_info with a focal estimate: the focal
  length is unknown, so derive it from a given depth plus a known size, e.g. person height in px ≈ f·H/depth.
- **Events:** both people are already moving at frame 0. There are no contacts, collisions or releases. The cyclist
  starts leaving through the bottom edge at frame 60 (1.818 s), the pelvis estimate leaves the image at frame 83 (2.515 s),
  and the cyclist is last seen at frame 91 (2.758 s). The pedestrian keeps a steady slow walk.
- **Ambiguity:** "person"/"man" could mean either figure. The walker is the pedestrian in the grey T-shirt; the cyclist is
  on the bicycle in the dark jacket. The kiosk could also be called a box, cabinet, booth or bin.
