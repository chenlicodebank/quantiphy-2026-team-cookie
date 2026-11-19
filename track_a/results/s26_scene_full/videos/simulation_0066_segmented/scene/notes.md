# simulation_0066_segmented — measurement record

3D simulation (Blender) scene, segmentation version: the background is pure white (255) and only objects plus a few ground pieces are rendered. 2160x1080 px, 24 fps, 72 frames (t = frame/24, 0 to 2.958 s). All values are in **pixels and seconds**. There is no metric scale.

## Files
- `scene.json`: the inventory (moving and static objects with descriptions), camera and perspective cues, events, and each moving object's apparent size at frames 0/12/24/36/48/60/66/71.
- `tracks/pedestrian.csv`, `tracks/taxi.csv`, `tracks/van.csv`, `tracks/cyclist.csv`: one row per frame (0–71). All four are visible in every frame.
  Columns:
  - `cx,cy`: mask centroid.
  - `bx,by`: bbox centre.
  - `x0,y0,x1,y1`: inclusive bbox. `bw,bh`: bbox width and height.
  - `L,Wd`: mask extent along and across its principal axis. `axis_deg`: the image angle of that axis (y down).
  - `bottom_x,bottom_y`: lowest mask row (ground contact).
  - `area`, `occl`.
  - Cyclist only: `head_top_y`, `full_y0`, `full_bh` (see below).
- `camera_shift.csv`: per-frame phase-correlation shift of 3 static patches against frame 0.
- `check_overlay.jpg`: masks, bboxes and centroids drawn on frames 0/24/48/60/66/71 (magenta = pedestrian, orange = taxi, blue = van, green = cyclist).
- `scripts/`:
  - `fg.py`: background image and foreground masks.
  - `split_vc.py`, `split_vc_back.py`: van/cyclist split.
  - `build_tracks.py`: the CSVs.
  - `static_and_camera.py`, `events.py`, `write_scene.py`.
  - Viewers: `cropsheet.py`, `overlay.py`, `headcrops.py`.
  - The `dbg_*` and `explore.py` scripts are exploratory, and `track_all.py` is a superseded first attempt.
  - The scripts write scratch to `../frames/cache`.

## Method
- **Background:** frame 0, with the frame-0 areas of the moving objects replaced by frame 71 (empty there).
- **Foreground:** pixels differing by more than 8 grey levels from the background, then opening, closing and hole filling. The sidewalk area (y > 890, x 480–1160) is ignored because of texture flicker.
- **Pedestrian and taxi:** each is its own connected component. Small detached fragments within 35 px (pedestrian) or 25 px (taxi) are merged in. The pedestrian's swinging leg sometimes renders detached (e.g. frames 13, 46).
- **Van + cyclist:** these form one merged blob in every frame. The blob is split by label propagation: each label is warped by its own LK/RANSAC similarity transform, the cyclist wins where it overlaps the van unless the pixel is white, and the rest goes to the nearer label.
  - Seeded at frame 30, propagated forwards to frame 71 and backwards to frame 0.
  - A second backward pass from frame 71 gives the final masks.
- **Checks:** masks were checked visually on many frames (overlays). Camera shift is ≤ 0.53 px, so the **camera is static**.

## Reliability
- **Taxi and van:** the most reliable. Bbox and centroid are good to about ±2 px.
  - The van's silhouette includes its dark lower front (bumper, tyres). Where the cyclist covers the van's front-left wheel area, those pixels go to the cyclist, so the van mask is slightly incomplete there.
  - At frame 71 the van spans x 1395–2094 and y 512–1047. It is still fully inside the frame.
  - Frame 0: the taxi is seen nearly nose-on, so its `L` is not its length until about frame 24, when it is side-on.
- **Pedestrian:** centroid jitters ±1–2 px with gait. `bh` (head top to lowest foot) is 83–100 px.
  - The figure leans and the leg is sometimes detached, so use the max/min of `bh` for standing-height questions.
  - The centroid is a proxy for the pelvis (it sits at roughly mid-height).
- **Cyclist:** the least reliable.
  - The mask reliably covers the bicycle and legs; `bottom_y` is the lowest wheel point.
  - The head and upper torso overlap the van's dark front parts. From about frame 0 to 64 they are mostly **missing** from the mask, so the mask centroid sits low (on the legs and frame, roughly near saddle/pelvis level or below).
  - `head_top_y` was read by hand on zoomed crops at frames 0, 8, …, 64, 71 (±5 px early, ±8 px late) and PCHIP-interpolated. `full_bh = y1 − min(y0, head_top_y)` is the apparent cyclist height including the bike.
  - The centroid step jitters by ±1–2 px early on.
  - `occl` = 1 for the van and cyclist in all frames, because they overlap in the image throughout.
- **Static objects** (`scene.json`): measured on the clean background, good to ±2 px.
  - The purple sedan is cut by the left edge (x0 = 3), so its true length is larger than 597 px.
  - The sidewalk is cut by the bottom edge.

## Timing and events
- Frames 0 and 1 are almost identical: every object moves ≤ 0.6 px. Motion starts at frame 1→2.
- Van: speeds up steadily in the image (0.3 to 67 px per frame), mostly through approach and perspective.
- Taxi: turns. It moves toward the camera first, then leftward, ending side-on after about frame 36. Its axis angle goes from 36° to −12°.
- Pedestrian: walks left at about 3.6 px per frame.
- Cyclist: rides parallel to the van at about 37°.
- No impacts or bounces. The pedestrian–taxi bboxes touch from frame 56 on, but the masks stay apart.

## Ambiguities
- A translucent grey human-like figure is rendered *inside* the parked purple sedan (near the windshield, around x 380–450, y 650–760). It is static. Do not confuse it with the walking pedestrian.
- Two similar cars are parked (purple near, green far); the taxi is the only yellow car. "Person" could mean the walker or the cyclist.
- Faint reflection flicker on the purple sedan's roof (x 382–445, y 654–679) shows up as foreground. It is not an object and is excluded.
- No shadows (segmentation render); mild motion blur on the van in the last frames.
