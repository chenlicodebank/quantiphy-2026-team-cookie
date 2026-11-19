# simulation_0017_segmented — measurement record

3D segmentation video (Blender render, background replaced by white), 1080x1080, 33 fps, 101 frames (t = frame/33).
Camera is static: a person-free patch moves at most 0.3 px against frame 0. All values are pixels and seconds. No metric scale.

## Scene
One moving object: **person**, a man in a light grey T-shirt and grey-blue jeans with a blank white face. He walks
steadily from left to right through the whole clip and is already walking at frame 0. He walks behind a large
foreground **bench** (4 light blue-grey cushions on a dark slab and angled base). He passes in front of
**painting_left**, then the **sculpture** (a silver flame/teardrop shape) on its **pedestal** (light top tier, dark
lower block), then **painting_right**. A **small_statue_right** (a small silver vertical piece at x~948) is never
reached. The scene.json "objects" list has the static bboxes.

## Files
- scene.json: inventory, camera, static extents, events, person summary.
- tracks/person.csv: frames 0-100, one row per frame. Columns:
  - frame, time.
  - cx, cy: centroid of the whole mask.
  - pelvis_x_band_median: median x of the mask in the hip band. Arm swing makes this noisy.
  - hip_run_cx: centre of the longest contiguous mask run in the hip band. Also noisy when an arm merges with the torso.
  - head_cx: mean x of the mask 5-40 px below the head top. This is the cleanest horizontal cue.
  - pelvis_y_est = head_top_y + 169.
  - bbox_x0/y0/x1/y1, width_px, visible_height_px.
  - head_top_y, head_width_px, chest_width_px, area_px.
  - occlusion flags.
  - **pelvis_x_raw / pelvis_x_smooth**: the recommended pelvis x. It is head_cx + median(hip_run_cx − head_cx)
    (offset −9 px), then smoothed with Savitzky-Golay (9 frames, quadratic). Frames 0-1 have head_cx extrapolated
    because the head is cut by the image edge.
- static_extents.json: bboxes of the static objects, measured on bg.png (non-white pixels).
- events_auto.json: event frames derived from the track.
- bg.png: per-pixel median of every 4th frame (person removed).
- scripts/:
  - bg.py: builds bg.png.
  - track_person.py: segmentation and track, plus overlays written to ../frames/ov.
  - static_and_camera.py: static extents and the camera check.
  - events.py: event frames.

## How the person was measured
- The mask is the frame-to-median-background difference with a threshold of 28.
- Inside the dark pedestal block (x 405-655, y 600-697) the jeans have low contrast, so a threshold of 16 is used
  there, limited to ±60 px around the upper body.
- I checked overlays at frames 0, 20, 40, 50, 60, 64, 67, 72, 75, 85, 95 and 100. The mask covers the person.

## Reliability
- **Horizontal pelvis position**: per-frame differences of pelvis_x_smooth are 6-10 px/frame. The mean is
  7.65 px/frame, which is 764.6 px over 100 frames (-1.5 to 763.1).
  - The absolute pelvis x is uncertain by about ±8 px. Visual checks put the belt centre 3 px (frame 30) to 14 px
    (frame 80) behind the head centre, because of body lean.
  - The raw head_cx frame-to-frame jitter is about ±1-2 px. For path length, use the smoothed column or fit a line,
    because one-frame differences of the raw columns add noise.
- **Vertical pelvis position**: the pelvis is estimated from the head top (feet are hidden), so it bobs with the
  gait: head_top_y ranges 368-378.
- **Feet are hidden by the bench top (y≈697)** in frames 22-100.
  - In frames 0-21 a foot is visible left of the bench end. That gives a head-top-to-sole height of 356-364 px,
    with 364 px at mid-stance (frames 4-7) as the best estimate of standing height.
  - In the other frames, visible_height_px (about 322-337) is truncated and is not the person's height.
  - bbox_y1 values of 701-711 in frames 62-75 come from shadow leaks, not feet.
- **Bounding-box width** includes the swinging arms and legs; the stride makes the width vary from about 90 to
  180 px.
  - In frames 0-4 the person is cut by the left image edge.
  - Frames ~62-67 and 72-75: the person's shadow or shading on the dark pedestal leaks into the mask. bbox_x0 can
    be pulled to about 405, and bbox_x1 can be off by about 15 px.
- **Depth**: apparent size is essentially constant. Head width is about 45 px (46.7 early, 43-45 later) and
  head-to-sole is about 360 px. The person walks roughly parallel to the image plane at almost constant camera
  distance. A slight recession cannot be ruled out: head width drops about 5% from the early to the later frames,
  but head rotation could also cause that.
- **Gait**: one step is about 17 frames.
  - Head-high (mid-stance) frames: 6, 22, 40, 56, 73, 90.
  - Head-low (double-support) frames: 14, 31, 48, 65, 82.
- **Static extents** are accurate to about ±2 px.
  - The bench bbox top (y 690) touches the pedestal bottom. The cushion top is about y 697.
  - The bench is seen nearly head-on: its width along x is its length, and its depth cannot be measured.
- **Depth order** (from floor-contact rows, lower in the image = nearer the camera): bench, then person, then
  pedestal, then paintings, then small statue. The paintings and the sculpture are behind the person, because the
  person occludes them.

## Events (frame)
- Walking throughout frames 0-100. No start, stop or turn.
- The person overlaps painting_left in frames 28-61, the sculpture/pedestal in 42-90, and painting_right in 78-100.
- The pelvis crosses the centre of painting_left at frame ~45, the sculpture at ~69, and painting_right at ~95.
