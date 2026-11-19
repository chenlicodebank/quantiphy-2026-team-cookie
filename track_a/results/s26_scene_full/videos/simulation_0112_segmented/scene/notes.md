# simulation_0112_segmented: measurement record

**Video:** 1080x1080 px, 24 fps, 55 frames (0-54), t = frame/24. Source: segmentation (a Blender render with the background replaced by plain white). Labelled as a 2D scene.

**Content:** one dark-red classic sports coupe (Porsche-911-Turbo-like, with a rear spoiler) drives left to right at constant speed along a long, dark, weathered slab or platform that spans the whole image width. There are no other objects. The camera is static.

## Files
- `scene.json`: inventory, sizes, events and camera, all in px and s.
- `tracks/car.csv`: the final per-frame track for frames 0-53.
  - `ref_x, ref_y`: the reference point, i.e. the centre of the car's silhouette bbox (midpoint between the bumpers, middle of the height).
  - `ref_source`: `measured` in frames 13-36, where the car is fully in view. In frames 0-12 and 37-53 the car is cut by the image border, so the value is `fit`: a straight-line fit through the measured frames.
  - `ref_x_linfit`: the fitted value, given for every frame.
  - `bbox_*`, `mask_cx/cy`, `length_px`, `height_px`, `area_px`: from the visible mask. These are truncated when `cut_left`/`cut_right`=1, and `occluded`=1 then.
  - `rear_wheel_x`, `front_wheel_x`: Hough wheel centres.
- `tracks/car_raw.csv`: raw mask measurements.
- `tracks/car_wheels.csv`: wheel centre and radius for each frame.
- `tracks/car_pairshift.csv`: frame-to-frame texture-matching shift.
- `bg_stats.json`: platform rows and columns.
- `car_summary.json`: fit summary.
- `scripts/`:
  - `track_car.py`: median background plus a difference mask.
  - `refine_car.py`: a template-matching attempt that fails when the car is cut by the border. It is superseded and kept only for the record.
  - `pairshift.py`, `wheels.py`, `build_track.py`: produce the final track.
  - `camera_check.py`: checks for camera motion.

## Method
- **Background:** the per-pixel median of frames 0, 15, 30, 45 and 54.
- **Car mask:** pixels where |frame − background| > 40 (max over channels), above the platform top (y < 540), after a 3x3 opening. The overlays (frames 0-52) were checked by eye: the mask covers the whole car, including the spoiler, bumpers and tyres, and nothing else. The car's tyres touch the platform at y≈539; the platform top is at y≈541. There is no visible shadow.
- **Motion:** uniform and purely horizontal.
  - The silhouette-bbox centre gives x = −136.31 + 27.285·frame px (fit over frames 13-36, rms 0.85 px, max residual 1.6 px). A quadratic term is negligible: 0.0076 px/frame², i.e. noise.
  - The wheels fit at 28.28 px/frame (rear) and 28.19 px/frame (front), with rms < 0.8 px.
  - The vertical position is constant: the bbox spans y = 413-539 and ref_y = 476.5.
- **Sizes (car fully visible):**
  - Length bumper-to-bumper: 421 px median.
  - Height ground-to-roof: 126 px.
  - Wheel radius ≈ 33.5 px (diameter ≈ 67 px).
  - Near-side wheelbase ≈ 232 px. At frame 25 the wheel centres are (440.5, 504.5) and (672.5, 506.5).
  - Clearest frame: 25, bbox (335, 414)-(756, 539).

## Reliability and ambiguities
- **Perspective (important):** the render uses a perspective camera, so parts of the car at different depths move at different pixel rates.
  - The near-side wheels/hubcaps move about 3.5% faster (28.23 px/frame) than the silhouette centre (27.29 px/frame). Measured on the silhouette, the wheels drift forward by about 25 px between frames 13 and 36.
  - The silhouette (bumper extremes, near the car's centreline) is the best proxy for the origin's depth. That is why `ref_x` uses the bbox centre, and why the size and the speed are both measured on the silhouette, so they are consistent. If a question gives a car-length prior, pair it with the 421 px length and the 27.29 px/frame motion.
  - The texture shift in `car_pairshift.csv` (≈27.75 px/frame) is weighted toward the near-side panels and lies between the two. It is not recommended for the origin.
- **Apparent length:** 420-422 px near the image centre (frames 19-34), 428-429 px at frames 13-14 and 36 (near the borders), because the bumper corners are seen obliquely.
  - When the car is cut by a border, the visible edge sits about 18-25 px further out than the fitted full-car box. Front-edge tracking in frames 0-12 and rear-edge tracking in frames 37-53 therefore give about 26 px/frame. These edges are biased; do not use them for speed.
  - The fitted `ref_x` is reliable to about ±2 px.
- **Segmentation edges:** the mask edges have about ±1-2 px of noise from the background replacement.
- **Camera:** static. The platform band never shifts by more than 0.12 px in x or 0.8 px in y.
- **Events:** there are no events other than entering and leaving the view.
  - Car fully in view: frames 13-36.
  - Front bumper touches the right border: frame 37.
  - Last sliver visible: frame 53. Gone at frame 54.
  - The car is already moving at frame 0 and does not stop, accelerate, bounce or change direction (its pixel acceleration is ≈0).
- **Platform:** static.
  - Top surface at y≈541 (539-542), bottom at y≈618, about 78 px thick.
  - It extends past both image borders. Its lower part tapers: x 36-1073 at y=590, x 82-1010 at y=615.
  - Small dark rectangular brackets sit under its top lip at roughly 150 px spacing.
