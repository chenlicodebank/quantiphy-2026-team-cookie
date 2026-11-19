# simulation_0025 — measurement record (pixels, seconds)

Video: Blender render, 3D scene, 960x960, 25 fps, 75 frames (t = frame/25, 0 to 2.96 s).
Scene: a beach in front of a large sandstone cliff, with rippling water in the foreground. **Two moving objects**: one
walking person and one flying dark bird. The camera is static (phase correlation of the cliff band against frame 0: max shift
0.012 px; per-frame values in `camera_shift.csv`).

## Files
- `scene.json`: inventory (moving and static objects), summary pixel sizes, events, camera/perspective notes.
- `tracks/person.csv`: frames 0-74, one row per frame. Columns: `cx, cy` = mask centroid; `pelvis_x, pelvis_y` = pelvis
  estimate (the reference point); `feet_y` / `head_y` = lowest / highest mask pixel; bbox; `height_px`, `width_px`, `area_px`;
  `occluded` (always 0); and smoothed `pelvis_*_smooth`, `height_px_smooth`, `feet_y_smooth` (Savitzky-Golay, window 11).
- `tracks/bird.csv`: frames 0-66. Columns: `cx, cy` = mask centroid (the reference point); bbox; `width_px`/`height_px` (bbox);
  `main_axis_len_px` / `cross_axis_px` / `main_axis_angle_deg` (PCA extents of the mask; main axis is about the wingspan);
  `area_px`; `occluded` = 1 when the bird is cut off by the right image edge (frames 63-66); `cx_smooth, cy_smooth`
  (Savitzky-Golay, window 7).
- `camera_shift.csv`: per-frame dx, dy of the background against frame 0 (all ~0).
- `scripts/`: `bg.py` (median background + camera check), `track.py` (segmentation, tracks, overlays in ../frames),
  `finalize.py` (smoothing, scene.json; it deletes the median-background PNG to keep the record small, so re-run bg.py before
  track.py), `size_trend.py`, `inspect_bg.py`.

## Method
The median of all 75 frames gives a clean background: neither the person nor the bird stays long enough at any pixel to show
up in it (checked visually). Masks come from the per-pixel max-channel difference to that background:
- Person: threshold 10 inside ROI x470-640, y515-625. A 5x1 vertical opening removes the thin horizontal ground shadow to the
  person's right. The bright reflection blob below the feet is a separate component and is excluded.
- Bird: threshold 25 and darker than the background (sum of RGB change < -40), inside y200-505.

I checked the overlays (frames/overlay_a.png, overlay_b.png) at frames 0, 12, 24, 32, 37, 48, 60, 66 and 74. Masks cover the
full body and head of the person and the full silhouette of the bird, including the wings.

## Objects
- **person** (only human; white T-shirt, dark trousers; on the beach near image centre). Visible and walking in all frames
  0-74, with no stop or turn. They walk toward image left and slightly toward the camera.
  - Pelvis (smoothed) goes from (559.1, 552.3) to (521.8, 562.0) px. Feet y goes from 581 to 591.
  - Image path length is about 40 px (net 38.6 px), roughly 0.53 px/frame. The motion is about uniform.
  - Apparent height is 54-55 px (min 53, max 57) and stays essentially constant: mean 54.7 for frames 0-14, 54.3 for 60-74.
    So the person's depth hardly changes (it may shrink slightly while their image moves down).
  - Width is 14-17 px, depending on gait phase.
  - The pelvis is a model, not observed: 0.53 x mask height above the lowest foot pixel. Treat it as ±2 px.
  - The head top is pale and low-contrast, so `head_y` may be off by about 1-2 px.
- **bird** (only animal; dark raptor-like silhouette, flapping). It flies left to right in front of the cliff at
  y ≈ 355-410, from x = 233 (frame 0) to the right edge.
  - Fully in frame for frames 0-62. Touches the right edge from frame 63, last partially visible at frame 66, gone from frame 67.
  - Mean image motion is about 11 px/frame (smoothed path length 731 px over 66 frames).
  - Vertical motion undulates. The centroid y dips to about 395 near frames 10-12 and 36, and rises to about 370 near
    frames 24 and 48-52. This is partly wing pose, partly real motion.
  - Wing-beat: the bbox height peaks (wings up or down) near frames 1, 12, 26 and 50. Edge-on and level-wing frames, such as
    frame 32, have a very thin mask (bbox height 6-7 px).
  - Wingspan (bbox width or main-axis length) is at most 44 px in frames 0-19, about 37 in 20-29, 46-49 in 30-59 and 52 in
    60-62. The maximum spread seems to grow slightly over time, so the bird is possibly approaching the camera, but this is
    confounded with wing pose.
  - The bbox width median over full-frame frames is 40 px.
  - **Reliability:** the centroid moves with the wing shape. Per-frame displacements are noisy (raw dx 4-19 px/frame), so
    use `cx_smooth/cy_smooth` or fits over several frames for speeds. The body itself is not separable from the wings.
- Static objects (positions at frame 74; the camera is static, so they hold for every frame):
  - **cliff**: spans the full width. Top edge at y ≈ 250 (left) to 290 (right), with a plateau block at x 0-137, y 228-248.
    Base at y ≈ 500 on the left half.
  - **cliff-base columns**: a vertical stripe pattern at x 185-460, y 462-500.
  - **beach**: sand from y ≈ 500 to the waterline at y ≈ 575 (left) to 600-605 (centre).
  - **right rock/dune**: white, rounded, at the right edge, bbox x 810-959, y 455-582.
  - **water**: y 600-959. Its texture animates but it is not a tracked object.
  - **sky/clouds**: above the cliff.

## Events
- Frame 0: the person is already walking and the bird already flying. No starts, stops, contacts or bounces in the clip.
- Frame 63 (2.52 s): the bird reaches the right image edge. Frame 66 (2.64 s): the bird is last seen.
- Frame 74 (2.96 s): end of clip.

## Perspective / ambiguity
- The camera is roughly level. Vertical cliff features are near-vertical in the image. The horizon is hidden behind the cliff,
  so it lies above y ≈ 250.
- The principal point is assumed at the image centre (480, 480). The focal length is unknown: estimate it from the given
  depth_info plus a known size, e.g. person height 55 px or bird wingspan.
- The bird flies in front of the cliff, but its depth relative to the person is unknown from the image. Use depth_info.
- The person is at image row ~552-562 for the pelvis. The pixel offsets of the pelvis/centroid from (480, 480) can be combined
  with the depths for 3D back-projection.
