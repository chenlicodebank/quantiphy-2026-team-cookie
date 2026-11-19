# simulation_0108 – measurement record (pixels, seconds)

2D simulation (Blender render), 1920x1080, 24 fps, 72 frames (t = frame/24). Pixel coords: x right, y DOWN.
The background is plain uniform grey (204,204,204). There are no static objects, no ground and no markings. The camera is static.

## Objects
- **virus_A**: the left, smaller particle (dark-blue spherical body with dark-red-tipped spikes). It starts with its centre at
  (721.5, 568.4) px and moves almost straight UP, drifting slightly left (~-0.35 to -0.5 px/frame in x). Its pixel speed rises steadily:
  per-frame displacement is 11.48 px at frame 2, 12.40 at frame 27 and 13.10 at frame 47, so |d| grows by about 0.034–0.04 px/frame
  each frame. It leaves through the top edge. It is fully in frame for frames 0–27, the centre leaves at frame 48 and the last pixels are seen at frame 67.
- **virus_B**: the right, larger particle with the same look. It starts with its centre at (1305.7, 614.6) and moves RIGHT, drifting slightly up.
  Its pixel speed is constant: per-frame displacement is (13.78, -0.68), |d| ≈ 13.8 px/frame. It leaves through the right edge.
  It is fully in frame for frames 0–23, the centre leaves at frame 46 and the last pixels are seen at frame 68.
- Sizes (full mask incl. spikes, fully-visible frames). A at frame 0 is 511 w x 513 h; over frames 0–27 the width is 511–533 and the height is 513–528.
  B at frame 0 is 571 x 578; over frames 0–23 the width is 571–593 and the height is 577–579.
  Body (spike-free core) circle diameter is A 251 (frame 0) to 263 (frame 27) and B 283–286. The spikes rotate slowly, so their pixel extent
  changes by a few percent. B's height and mask area stay constant.
- **Caveat for A**: its mask area grows steadily, from 99117 px² at frame 0 to 108041 at frame 27 (+9%, i.e. about +4.4% in linear size).
  Its body diameter grows by a similar amount. A may therefore be slowly approaching the camera or scaling up, or the growth may be partly
  the rotation of the spikes. If a question uses A's size as the prior, frame 0 is the clean reference. Measuring at a different frame changes the scale by up to about 4%.

## Events
- Frames 0 and 1 are identical (both objects at rest).
- Motion starts at frame 2 (t = 0.083 s), and both objects are at full speed from the first step. There is no ramp from rest:
  if motion is extrapolated back, A would already have a speed of about 11.4 px/frame at frame 1.
- B first touches the right edge at frame 24 and A first touches the top edge at frame 28.
- The centres leave the image at frame 46 (B) and frame 48 (A).
- Frames 69–71 are empty.
- A and B never touch: the gap between their extents is 57 px at frame 0 and grows. The centre distance at frame 0 is 586.1 px.

## Files
- `scene.json`: summary of everything above.
- `tracks/virus_A.csv`, `tracks/virus_B.csv`: one row per frame (0–71) with these columns:
  - `cx`, `cy`: the centre, i.e. the origin.
  - `centre_source`: `measured`, `extrapolated` or `out_of_frame_extrapolated`.
  - `bbox_x0..y1`, `bbox_w`, `bbox_h`: mask bounding box. When clipped, this is only the visible part.
  - `mask_area_px`.
  - `full_extent_valid`: 1 if the whole object is inside the frame.
  - `core_w`, `core_h`: spike-free body box. `core_circle_diam`: circle fit to the body.
  - `occluded_or_clipped`: 1 if the object is cut by the image border. There is no mutual occlusion.
- `scripts/measure.py`: background-difference mask (threshold 25), split into objects by connected components, body = morphological
  opening with a 61-px disk, circle fit to the body edge points that are not on the image border. Output: `scripts/raw.json`.
- `scripts/flow.py`: frame-to-frame displacement of each virus by sub-pixel template matching, using the previous frame's object patch
  cropped to the part that stays in frame. Output: `scripts/flow.json`. Match scores are 0.986–0.994.
- `scripts/build_tracks.py`: builds the centre track and writes the CSVs and `scripts/summary.json`. The centre is the cumulative template
  displacement, anchored to the mean body-circle centre over the fully visible frames (anchor scatter is 0.3–1 px).
- `scripts/overlay.py`: makes check images in `frames/`. The centres, boxes and body circles land on the right virus, and the full spike extent is covered.

## Reliability
- **Frame-to-frame displacements** (measured for A up to frame 61 and B up to frame 59): about ±0.05 px per frame, which makes them the best
  quantity for speed or acceleration questions. Two exceptions:
  - B shows a small dip to 13.62–13.72 px/frame at frames 37–48. This is most likely a template artefact while B is half clipped
    (a constant-velocity object).
  - A is noisier after frame 48: ±0.5 px at frames 55–61, when only a small patch is visible.
- **Absolute centres**: ±1 px.
- **Extrapolated centres**: A from frame 62 and B from frame 60 come from a linear fit of the displacement trend (A) or a constant
  displacement (B).
- **Sizes**: ±2 px plus the rotation and growth effects described above. Tips are dark red with soft antialiasing, and there is no motion blur.
