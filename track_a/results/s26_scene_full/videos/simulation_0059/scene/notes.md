# simulation_0059: measurement record (pixels, seconds)

3D Blender street scene, 2160x1080, 24 fps, 72 frames (3.0 s), t = frame/24. **Frame 1 is an exact duplicate of frame 0**:
every object has zero displacement from frame 0 to 1. Keep this in mind when taking a one-frame difference at t = 1/24 s.
**The camera is static** (background residual < 0.05 grey levels; the parked cars shift <= 0.5 px over the clip), so no
background-shift correction is needed. No metric scale is assumed anywhere.

## Files
- `scene.json`: inventory (moving and static objects, distinguishing features, visible frames), static-object pixel
  boxes, camera/perspective cues (road vanishing point, horizon, curb lines), events, and the column meaning of each track.
- `tracks/taxi.csv`, `tracks/van.csv`, `tracks/cyclist.csv`, `tracks/pedestrian.csv`: one row per frame (0-71) with
  bbox (x_min, x_max, y_min, y_max), centre (cx, cy), object-specific reference points, sizes and an `occluded_by` column.
- `tracks/_van_patch.csv`: helper. Sub-pixel template track of the van's brown side panels.
- `scripts/`: every script used. Order: bg.py, fg.py (median background -> bg_full.png), bg_fix.py (removes ghosts),
  van_patch.py -> van_extent.py -> van_track.py; track_taxi.py; cyc_template.py -> cyc_track.py; ped_track.py ->
  ped_csv.py; occlusion.py (run last); events.py (event detection printout); checks.py (duplicate frame / static check);
  overlay.py, view.py, diffview.py, colmask.py, static_check.py, probe.py (viewers used to check the results).
- `bg_full.png`: clean background (no moving objects). `bg_half.png`: plain median at half resolution, which still
  shows the taxi ghost.

## Moving objects (all visible in all 72 frames)
| name | how to recognise it | motion |
|---|---|---|
| taxi | yellow taxi with roof sign | starts on the cross street at left in side view, heading right. Turns right toward the camera (f25-49) and ends front-on, approaching (x~870-1050, bottom y 852 at f71) |
| van | white cargo van with 2 brown side panels | at rest at f0-1, then speeds up smoothly left -> right along the cross street (image speed 0.8 -> 26.5 px/frame) |
| cyclist | dark top and jeans, silver bike | steady ~11.9 px/frame left -> right along the cross street |
| pedestrian | white T-shirt, light jeans, left sidewalk | almost still at first, speeds up over f0-20, then walks left and toward the camera at ~1.0-1.4 px/frame |

### How they were measured, and how reliable each is
- **van**: NCC template of the two brown side panels (taken from f36) at multiple scales, with sub-pixel peak:
  `patch_cx` is good to ~0.3 px (scores 0.67-1.0; lowest at f19-25, when a traffic-light pole and the taxi roof are in
  front of the panels). The ends are found in a weak foreground mask (|frame-bg|>8, because the white van barely differs
  from the white sky). Rear = leftmost column at box-body height; front = rightmost column at bumper height. Only
  measurements that were not blocked by another object are used (`rear_raw`, `front_raw`). Their offsets from the panel
  are median-smoothed and interpolated over gaps. The front end is hidden by the taxi before f35, so it is extrapolated
  there (the offset is about constant, ~176-180 px). Image length ~296-303 px for f0-60, growing to 316 px at f71 because
  the rear face comes into view. Roof y 692 and tyre contact y 799 are constant within ~2 px (read at f48, f71).
  Bbox ends +-3 px. The bbox centre is used as the origin. Occluded by the pedestrian (f0-~15), the taxi (f0-~50), the
  maroon sedan (f50-~66), the cyclist (in front, f56-71), and poles.
- **taxi**: yellow-paint mask (HSV H 12-30, S>45, V>150, plus foreground). Yellow clusters near the main one are merged so
  that the roof sign counts. x_max = yellow extent. x_min = yellow extent widened by up to 12 px of foreground (the
  shaded left flank). y_min = top of the roof sign. y_max = lowest dark tyre pixel. Visually checked at f0, 10, 18, 24, 26,
  32, 34, 36, 40, 44, 46, 52, 58, 66, 71: bbox within ~5 px. Problems: at **f0-3 the roof sign is behind the
  traffic-light pole (x~750)**, so y_min is too low (727-739 instead of ~721). Early bbox centres jitter by +-6 px
  (pedestrian and poles in front; the cyclist touches the taxi's front at f12-24). `yellow_cx/cy` is a smoother
  alternative. The taxi turns, so neither its bbox width nor its height is a fixed physical size. Side-view length
  ~300 px (f5-20); front-on width 131 px (f49-53) -> 181 px (f71).
- **cyclist**: NCC template of the rider's head and torso (from f36), tracked both ways from f36 with a constant-velocity
  prediction and sub-pixel peak. `rider_cx` is good to ~0.5 px (the per-frame dx is 11.2-12.9, with a mean ~11.9-12.1).
  The bbox uses fixed offsets measured on the clean frames 33-36 (92 x 88.5 px: rear wheel to front wheel, head top to
  wheel bottom), and was checked visually at f4, 20, 30, 45, 55, 64, 71. `pelvis_*_est` = saddle/hip point (+-4 px).
  The lower body is hidden behind the taxi for f0-~27, and the bike and legs behind the maroon sedan for f41-50.
  Template scores fall at f70-71 (traffic-light pole x~1650 in front), where the position follows the trend.
- **pedestrian**: low contrast (white shirt on a white background). From f23 on: NCC head+torso template from f40,
  score 0.85-1.0, x good to ~1 px (some 1-2 px gait jitter at f61-68). For **f0-22** the van and taxi pass directly
  behind and the template fails, so x comes from **eye readings of the head centre on 3x zooms every 4 frames**
  (617, 616, 614, 611, 607, 601, 594 at f0, 4, 8, 12, 16, 20, 24), linearly interpolated (+-1.5 px). The early speed-up
  is real but only coarsely resolved. `cx` = body axis. Bbox width 44 px (+-5). head_top is measured each frame
  (706-709 px). The soles are at y~815 and visible only for f0-24, giving a **standing height ~110 px**. From ~f25 the
  feet and lower legs are behind the garbage bags, so y_max=815 there is only a placeholder (it is flagged). The
  pedestrian approaches the camera slowly, so the true foot position at f71 is probably ~830.
  `pelvis_y_est` = head_top + 70 (waist/crotch read at f30, f40; +-5 px).

## Static objects (pixel boxes at f71 in scene.json; nothing static moves)
maroon sedan (rear to camera, 142x110 px at x 1256-1398), green car (front to camera, far, 82x56 px), silver trash can
on the road (87x107 px), pile of garbage bags in the left foreground (241x255 px), green litter bin on the left sidewalk
(38x58 px), double-lantern lamp posts and traffic-light poles (x, top, base in scene.json), road and sidewalks.

## Perspective (3D)
Vanishing point of the main road's curbs is ~(1258, 702), +-15 px; horizon y ~702. The camera is pitched down slightly,
and the main road direction is ~180 px right of the image centre. The cross street (van, cyclist) is close to parallel
to the image x axis: tyre and wheel bottoms stay at y~799-801. The van's growing image length and the taxi's rising
bottom edge (807 -> 852 px) are the size cues: the taxi approaches the camera after ~f45; the van and cyclist keep a
roughly constant camera distance, apart from their changing angle to the camera.

## Ambiguities
- Similar objects: two parked cars (maroon sedan, nearer, in the right lane; green car, far, near centre), both static.
  There are several lamp posts and traffic-light poles: use the positions in scene.json.
- Shadows: the taxi's road shadow is excluded (the right end comes from the yellow paint, the bottom from the tyres).
- Motion blur is small. The van at ~26 px/frame late in the clip has slight streaking at its ends (+-2 px).
- The bboxes are image bboxes. For a turning car (the taxi), the bbox centre is only approximately the projection of
  the vehicle root.
