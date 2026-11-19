# simulation_0061: measurement record

3D Blender street scene, 2160x1080, 24 fps, 72 frames (t = frame/24, 0 to 2.958 s). **The camera is static.** Phase correlation between frame 0 and frame 71 on the ground gives a shift under 0.01 px, so the background shift per frame is 0. All values are in full-resolution pixels (x to the right, y down) and seconds. No metric scale is assumed.

## Files
- `scene.json`: inventory of moving and static objects, events, camera and perspective cues, and how the apparent size of each mover changes over time.
- `tracks/taxi.csv`, `tracks/van.csv`, `tracks/cyclist.csv`, `tracks/pedestrian.csv`: one row per frame, 0 to 71. Every object is visible in every frame.
  Columns: `frame`, `t_s`, `cx`/`cy` (bbox centre, the default reference point for the object origin), `x0 y0 x1 y1` (bbox), width/length and height in px, `bottom_cx`/`bottom_y` (ground-contact point), `source` (how each row was obtained) and `occluders`.
  - Cyclist only: `hip_x`/`hip_y` give a saddle/pelvis estimate (anchor + (6, 44)).
  - Pedestrian only: `hip_*_est` = bottom − 0.53·height, and `mask_cx`/`mask_cy` is the silhouette centroid.
- `scripts/`: every script used, in pipeline order:
  1. `bg.py` checks the camera.
  2. `bg2.py` → `bg3.py` build the background.
  3. `track_cyclist.py`, `track_all.py`, `select_van.py`, `track_van.py` and `track_van_early.py` do the tracking.
  4. `build_tracks.py` writes the CSVs.
  5. `write_scene.py` writes scene.json.
  6. `static_measure.py` and `poles.py` measure the static objects.
  7. `check_sheet.py`, `zoom*.py` and `cmp.py` are viewers.
  8. `events.py` prints per-frame steps.
  - These scripts write scratch into `../frames/`, which is not part of the record.

## Moving objects (what tells them apart)
- **taxi**: the only yellow car.
  - Frames 0 to ~20: seen from the side, in front of the van, moving right.
  - After that it turns left toward the camera, ending in a front three-quarter view. Image x peaks around f36, then the taxi moves left and down (approaching the camera).
  - Its bbox width is **not** the car length after ~f20 because the car rotates. Side-view length (bumper to bumper) at f0–12 is about 285–287 px; height from tyre bottom to roof sign is about 85–90 px at f0.
  - How measured: the pale-yellow paint (hue 12–26) gives seeds; their convex hull plus the dark tyres below form the mask. The resulting box is clipped to within ±10 px (x) / ±6 px (top) / ±3 px (bottom) of boxes I read by eye from zoomed frames at f0, 6, 12, 18, 24, 36, 48, 60 and 71 (linearly interpolated between them).
  - Reliability: about ±5 px per edge, and the box centre jitters by ±3–4 px from frame to frame. Smooth over several frames before taking differences.
- **van**: the only white vehicle, a full-size van with tan side windows. Seen side-on throughout, moving right and slightly toward the camera.
  - It starts from (near) rest: rear edge 625 at f0–1. It then speeds up steadily, from about 1 px/frame at f2 to about 25 px/frame at f65–71, with about 0.35 px/frame² image-x growth.
  - Apparent length grows from about 281 to 345 px.
  - **f0–40**: tracked by matching a template of the roof and window band (taken at f30). The front edge is accurate; the rear edge is template x + 13, calibrated on six visual readings. Length is a linear fit, 281 + 0.39·frame.
  - **f41–48**: tracked with a template from f50; rear edge + 7 px (checked at f48).
  - **f49–71**: segmentation.
  - The **front is hidden behind the cyclist at f55–63**, so there front = rear + length, with length interpolated between f40 (296) and f64 (328).
  - Rear edge interpolated at f63 (behind lamp post C) and f70 (behind lamp post D).
  - The **bottom is hidden behind the taxi at f0–46**. There it is estimated as top + 0.383·length, a ratio measured at f49–71.
  - Bottoms at f49–71 include about 5 px of shadow.
  - Reliability: about ±5 px per edge where measured, about ±8 px where estimated (see the `source` column).
- **cyclist**: a man on a bicycle (dark top, white-rimmed wheels) riding left to right in the far lane at a steady 11–13 px/frame. The image y is constant (head top about 535–541) and the size is constant, so his depth is roughly constant.
  - How measured: the rider's head and torso are tracked with a masked colour template and a tight constant-velocity search. The box = anchor + fixed offsets measured at isolated frame 24: (−20, −1, +66, +91), i.e. 86 × 92 px, rear-wheel edge to front-wheel edge and head to wheel bottom.
  - Occlusion:
    - The bike is hidden behind the taxi at f0–14.
    - The rider is behind lamp post C at f41–45.
    - He is **in front of** the van at f52–71 (overlapping).
    - The f0 position is less certain (the f0→f1 step is 6 px instead of 10).
  - Reliability: anchor ±2 px.
- **pedestrian**: a man in a white T-shirt and jeans on the left pavement, walking left and slightly toward the camera.
  - His height grows from 123 to 138 px. He moves about 2 px/frame on average. The bbox centre oscillates with his gait and is nearly still at f24–28 and f58–62, probably gait phase rather than real stops.
  - He is partly behind lamp post A (x 543–549) at f0–~12.
  - How measured: foreground mask, x < 615. Reliability: ±2 px, with the legs causing width variation.

## Static objects
Listed in scene.json. They were measured at f71, partly by mask and partly by reading a grid by eye (±3 px). Examples:
- Metal trash can on the road, foreground: 83 × 106 px.
- Green bin on the left pavement: 36 × 55 px.
- Big lamp post C: pole x 1302–1314, top y 353, base y 1001.
- Drain grate on the right pavement: 190 × 30 px.
- Several more lamp posts and traffic lights.

## Perspective
- Vertical poles appear vertical, so pitch and roll are about 0 and the horizon is near the image centre row. The row of lamp posts on the right converges at about (1700, 534), so **horizon y ≈ 535 ± 20**. Principal point assumed at (1080, 540).
- The ground is flat: road plus pavements.
- No focal length was estimated; that is for the answering session, from the depth_info it is given.

## Ambiguities
- Similar objects: there are many similar lamp posts and traffic lights; names and positions are in scene.json.
- The bbox centre is used as a stand-in for the object origin. Vehicle roots in Blender may sit at ground level: use `bottom_y` if needed.
- Car shadows add a few px to the bottoms.
- No motion blur problems were seen.
