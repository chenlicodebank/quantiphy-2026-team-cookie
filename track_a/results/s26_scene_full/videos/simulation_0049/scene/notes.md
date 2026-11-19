# simulation_0049 — measurement record (pixels, seconds)

3D Blender street scene, 1920x1074, 33 fps, 99 frames (t = frame/33). **Static camera** (background
phase-correlation shift ≤ 0.17 px over the clip). Two moving objects, both moving roughly straight away from the
camera for the whole clip:
- **cyclist**: a man in a dark jacket on a blue bicycle in the middle of the road. Fast: apparent height goes from
  376 px to 139 px.
- **pedestrian**: a man in a white T-shirt and jeans on the right sidewalk. Slow: apparent height goes from 321.5 px
  to 241.5 px.

Neither starts, stops, turns, or touches anything, and neither is occluded.

## Files
- `scene.json`: inventory (moving and static objects with pixel boxes), camera and perspective, events.
- `tracks/cyclist.csv`, `tracks/pedestrian.csv`: one row per frame 0..98. Columns:
  - frame, time_s
  - ref_x, ref_y: estimated pelvis in image px
  - bbox_x0..y1: head top to lowest ground contact
  - height_px: bbox height
  - width_px: bbox width
  - length_px: equal to height_px. Both people are seen from behind, so their extent along the motion direction is
    not visible.
  - ground_x, ground_y: tyre contact or lowest shoe
  - occluded: always 0
  - source
- `scripts/`: every script used.
  - `bg.py`: camera shift check.
  - `track_gc.py`: GrabCut tracking.
  - `wheel_bottom.py`, `fix_cyclist_bottom.py`: fill in the tyre contact where the mask lost it.
  - `track_ped.py`: failed automatic pedestrian masks. Its output was deleted. Do not use it.
  - Background images and the pedestrian mask file were deleted to keep the record small. `bg.py` and `bg2.py`
    recreate the background images.
  - `make_tracks.py`: builds the CSVs. It also holds the pedestrian keyframe table, saved as
    `pedestrian_keyframes.csv`.
  - `overlay.py`, `boxview.py`, `crops*.py`: visual checks.
  - `masks_cyclist.pkl`: packed cyclist masks per frame.

## How measured / reliability
- **Cyclist**: GrabCut mask per frame (rectangle taken from the previous frame's mask), checked by overlays at
  frames 0, 4, 10, 30, 46, 50, 60 and 98.
  - The mask covers the rider and bike well. Head top and sides are reliable to about ±1 px.
  - In frames 3–6 and 47–54 the mask lost the thin rear tyre. In those frames the bottom (tyre ground contact) is
    taken from a robust perspective fit, y = 537.5 + 19973/(frame + 57.4). That fit has 0.8 px rms on the other
    frames and agrees with eyeball readings at f4 (≈862) and f50 (≈725). Source column: `grabcut_mask+bottom_fit`.
  - Pelvis is an estimate just above the saddle: y = top + 0.445·(bottom − top), x = body centre at that height. It
    is about ±3–5 px of the true hip at near frames and ±2 px at far frames. The rig root might instead be the bike.
    If needed, use ground_y (tyre contact) or the bbox centre.
  - Shadow: the cyclist casts a long shadow to the lower right on the road. It is excluded from the mask.
- **Pedestrian**: automatic segmentation failed (grey jeans on the grey sidewalk, white shirt on the wall). Instead,
  head top, lowest shoe, left and right extremes, hip-centre x and shirt bottom were read by hand on 2× zooms with a
  10 px grid. This was done every 7 frames (0, 7, …, 98) and linearly interpolated between keyframes (source
  `interp`).
  - Accuracy: about ±2 px at keyframes and ±3–5 px in between, because the gait's bobbing and stride are not linear.
  - Pelvis: y = shirt bottom + 0.04·height.
  - Width includes the swinging arms and is noisy. Bbox height includes the stride: legs apart lowers the head
    slightly, so this is not the rest standing height.
- **Apparent size vs time** (depth ∝ 1/size for a fixed object):
  - Cyclist height: 376 (f0), 352 (f4), 279 (f20), 223 (f40), 186 (f60), 160 (f80), 139 (f98).
  - Pedestrian height: 321.5 (f0), 295 (f20), 281 (f40), 266.5 (f60), 251 (f80), 241.5 (f98).
- **Perspective**: the road vanishing point is about (975, 530) ±20, from the two curbs. The cyclist's tyre-contact
  fit has its asymptote at y ≈ 537 (the image centre row). Together these say the camera is nearly level and the
  road-plane horizon is about y 530–537.
  - The grey sea/land band at y 612–625 and the road's far end at about y 638 are scenery, not the horizon.
- **Static objects**: pixel boxes measured at frame 0. Precision:
  - Telephone booth: ±2 px. Box (1006, 409)–(1109, 659), 103 × 250 px.
  - Manhole: ±2 px. Outer ellipse 212 × 34 px, centre (686, 840).
  - Parked bicycle: ±4 px. Seen end-on.
  - Stairs, small stone box, bush and buildings: rough, ±10–20 px.

## Ambiguities
- Two bicycles: the moving blue one under the cyclist, and a parked brown one with a basket at the far left.
- Two people: the cyclist (dark jacket, on the road) and the pedestrian (white shirt, on the sidewalk).
- The camera focal length is unknown. Combine the depth_info values with a known size or pixel separation.
- 3D distances need depth: for a level camera with principal point (960, 537), back-project ref_x/ref_y using the
  given depths and an estimated focal length.
