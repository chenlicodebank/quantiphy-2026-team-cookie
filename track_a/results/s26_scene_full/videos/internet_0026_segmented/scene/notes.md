# internet_0026_segmented: measurement notes

**Scene.** This is 2D internet footage with the background replaced by white. It is 1280x720, 36 frames at 30.0003 fps (1.2 s), with t = frame/fps. A man in a black T-shirt and jeans crouches on the right. He has just pushed a toy dump truck (blue cab facing left, red dump bed, yellow chassis, black wheels). The truck rolls right-to-left toward a toddler in navy clothes sitting on the left with legs stretched toward it. The truck is the only object with real motion. No floor, markings or other static objects are visible.

**Files**
- `scene.json`: inventory, sizes, events, camera summary.
- `tracks/truck.csv`: one row per frame (0-35). Columns:
  - `cx, cy`: mask centroid.
  - `bbox_x0..y1`, `bbox_cx/cy`: bounding box and its centre.
  - `length_px` (bbox width, bumper to bumper), `height_px`, `area`.
  - `mask_source`: `component` (separate blob) or `template` (frames 0 and 3, where the truck touches the man).
  - `rear_occluded` / `occluded` (frames 0-3) and `hand_contact` (frames 0-5).
  - `front_x`: front bumper, the leftmost pixel, never occluded.
  - `cx_from_front` = front_x + 103: centre estimated from the full length of 207 px.
  - Camera-stabilised versions in frame-0 coordinates: `front_x_stab`, `cx_from_front_stab`, `bbox_cx_stab`, `cy_stab`.
  - `cam_scale/tx/ty`.
- `tracks/man.csv`, `tracks/child.csv`: the same box, centroid and PCA-extent columns. `child.csv` also has `head_torso_dx/dy`, the child's head+torso shift relative to frame 0.
- `tracks/camera.csv`: per-frame pan+zoom fit (`scale, tx, ty, fit_rms_px`) plus the shift of each patch.
- `scripts/`:
  - `measure.py`: masks and tracks.
  - `camera.py`: camera fit.
  - `augment.py`: derived truck columns.
  - `gap.py`: child-truck gap.
  - `parts.py`: wheel and wheelbase sizes.
  - `overlay.py`: visual check.
  - `show.py`, `probe.py`: helpers.

**Method.** The foreground is every non-white pixel (min channel < 200), split into connected components. The truck is a separate component in every frame except 0 and 3. In those two frames it is located by masked template matching with its frame-1 appearance. I drew overlays at frames 0-6, 8, 10, 20, 30 and 35 and checked them: the boxes hit the truck and cover its full extent from frame 4 on.

**Truck sizes (reliable to about ±2 px)**
- Bumper-to-bumper length: 207 px (median over frames 6-35; range 205-210).
- Height: 170 px.
- Wheel diameter: about 59 px.
- Wheelbase: about 103 px.

In frames 0-3 the man's knee hides the rear corner of the dump bed. Those boxes are therefore 2-5 px short and their centres are biased forward, so use `front_x` or `cx_from_front` there. The truck's apparent size does not change, so there is no depth change.

**Motion and events**
- The truck is already moving at frame 0.
- The man's fingertips touch the rear top of the bed until frame 5; the release is at about frame 6 (±1).
- Front bumper in the image: x 669 → 426 (−243 px) over frames 0-35. Its y drifts by only a few pixels.
- The truck reaches the child's feet around frames 31-33: the gap is 2 px at frame 31 and the x-ranges overlap from frame 33. It may touch the foot at frames 33-35, but the depth order is unclear.
- The truck is still moving at the end; no stop is observed.

**Duplicate frames.** Each of the pairs (1,2), (6,7), (11,12), (16,17), (21,22), (26,27) and (31,32) shows the same image. One-frame differences are therefore 0 / about 1.2x the true step there. Smooth the data or use longer intervals when fitting.

**Camera.** The camera is hand-held: it pans to follow the truck and zooms in slightly. Over the clip the scene content shifts by about +40 px (child) to +57 px (man) in x, and the scale grows by 1.8%, accelerating toward the end. Because the background was removed, I estimated this from patches on the child (head, torso) and the man (head, back, shoe), assuming they stay still. The fit rms is 1-2 px, and the man's and child's own small movements add uncertainty of a few px.

Relative to the background (stabilised, frame-0 coordinates), the front bumper moves 669 → 379 (−290 px) instead of −243 px in the raw image. The original annotators had the real background. If a question concerns motion over the ground, the stabilised columns follow the "measure against the background" convention; the raw columns are what the image shows directly.

**Scale.** Following the benchmark convention, there is one scale for everything: prior / pixel value. For example, a truck-length prior divides by 207 px.

**People (approximate)**
- Man, crouched: 296 x 444 px box at frame 1.
- Child, seated, head-back to toes: 224 x 194 px at frame 0.
- Heads: about 100x130 px (man) and 78x80 px (child), rough.
- Neither travels.
