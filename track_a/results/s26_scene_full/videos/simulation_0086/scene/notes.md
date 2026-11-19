# simulation_0086 – measurement record (pixels, seconds)

**Scene.** A 2D Blender simulation at 24 fps with 72 frames (3.0 s) and a size of 1920x1080. A static camera looks straight down at a plain grey ground (grey level 140), with no markings and no other objects. Two objects move along parallel horizontal lines in opposite directions:
- **car**: a silver pickup in the style of a Cybertruck, in the lower band (y ≈ 652). It is at rest in frames 0–1, then speeds up smoothly to the **left**. Its per-frame step grows roughly linearly: about 1 px at frame 2, about 16 px at frame 31, about 31 px at frame 56 and about 37 px at frame 68. That is roughly 0.55 px/frame², but each answering session should fit the motion itself. Its front reaches the left edge at frame 57, and it is last visible at frame 69.
- **cyclist**: a person on a bicycle, in the upper band (y ≈ 477), heading **right**. Frames 0 and 1 are identical. From frame 2 on it moves at a constant ≈16.0 px/frame (64 px per 4 frames). Its front wheel reaches the right edge at frame 58, and it is last visible at frame 65.
- There is no contact, occlusion, bounce or turn. Frames 70–71 are empty.

**Files.**
- `scene.json`: inventory, sizes at frame 0, events, camera and relative geometry.
- `tracks/car.csv` and `tracks/cyclist.csv`: one row per visible frame with these columns:
  - `frame`, `time`
  - bounding-box centre (`bbox_cx`, `bbox_cy`) and mask centroid (`mask_cx`, `mask_cy`)
  - bounding box (`x0`, `y0`, `x1`, `y1`)
  - `length_px` (along x, the motion axis) and `width_px` (across, along y)
  - `area_px`, `clipped_by_frame_edge` and `occluded` (always 0)
  - **`ref_x`, `ref_y`**, the best estimate of the object origin, with the method in `ref_src`
  - car only: `body_width_med_px`
  - cyclist only: the rider-body blob centre and extents (`rider_cx`, `rider_cy`, `rider_x0/x1/y0/y1`)
- `scripts/`:
  - `probe.py` checks the background and confirms frame 71 is empty.
  - `measure.py` does the segmentation, writes the tracks and draws the overlays in `frames/ov_*.png`.
  - `widths.py` measures the cross-axis profiles.

**Method.** Each frame is compared with the empty frame 71: pixels that differ by more than 30 grey levels are kept, gaps are closed with a 5x5 kernel, and the connected components are taken. Components with centre y > 545 are the car; the rest are the cyclist. I checked the overlays visually: the boxes cover the whole car, including its mirrors, and the whole bicycle from wheel to wheel. The soft ground shadows stay below the threshold and are excluded.

**Sizes (frame 0, at rest, sharp).**
- Car:
  - Length, bumper to bumper: **438 px**.
  - Width including mirrors: 189 px.
  - Body width without mirrors: ≈155 px.
  - Width across the front wheels: ≈172 px.
  - Height cannot be seen from a top-down view.
- Cyclist:
  - Bicycle length, wheel to wheel: **129 px**.
  - Width across the handlebars and arms: 38 px.
  - The rider's body blob spans x ≈ 918–965.
  - Height cannot be seen.

**Reference points and reliability.**
- **Car.** Motion blur stretches the trailing (rear) edge as the car speeds up. The mask length grows from 438 to 449 px by frame 56, so the bounding-box centre lags by up to about 5 px.
  - For frames 0–56, `ref_x` = front bumper x0 + 218.5. The front edge stays sharp, so this is accurate to about ±1 px.
  - From frame 57 on, the front is off-screen, so `ref_x` = rear x1 − 218.5 − 11. The 11 px is the blur offset measured at frame 56, which keeps the series continuous. Expect ±2 px error, rising to a few px at frames 68–69 when only a sliver is visible; the step at frame 69 (44 px) is unreliable.
  - `ref_y` = 651.75 (constant).
- **Cyclist.**
  - `ref_x` is the bounding-box centre (±0.5 px). After the bike is clipped at frame 58, it is rear wheel x0 + 64.
  - The human pelvis is not directly visible. The rider-blob centre (`rider_cx`) is about 11 px behind the bike's box centre and is a rough pelvis proxy (±3 px, jittery because of the legs and arms). Use bike-centre differences for speed, since both points move together.
  - `ref_y` = 477.25.
- **Scale.** The same ground plane and top-down view mean one metres-per-pixel scale for both objects. Get it from the prior, for example the car length of 438 px or the bicycle length of 129 px.
- **Distance between objects.** At frame 0 the reference points are dx = 144.5 px and dy = 174.5 px apart, or about 226.6 px. For any other frame, compute it from the `ref_*` columns.

**Ambiguities.**
- Whether the vehicle root is at the footprint centre, as assumed here, or nearer an axle cannot be seen.
- The pelvis position of the cyclist is approximate.
- Speeds near the frame edges come from the clipped-edge extrapolation.
