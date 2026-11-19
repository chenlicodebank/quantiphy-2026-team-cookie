# captured_0062s – measurement record

Lab clip (24 fps, 49 frames, 1280x720, 3D). The background was replaced by the SAM2 demo: it is a smooth
colour gradient, and there is a watermark in the bottom-right corner (x>=1025, y>=688). That leaves only the
segmented objects. Camera intrinsics follow the benchmark convention: f = 763 px, principal point ~ (640, 360).

## Files
- `scene.json`: inventory, static-prop pixel sizes and positions, events, camera.
- `tracks/white_board.csv`: the only moving object, all 49 frames. Columns:
  - `frame`, `time_s`
  - `cx, cy`: centroid of the white mask (the visible centre; the reference point).
  - `bbox_*`
  - `minrect_cx/cy`, `length_px`, `width_px`, `long_axis_angle_deg`: min-area rectangle of the mask (deg in the image, y down).
  - `area_px`
  - `pca_length_px`, `pca_width_px`: extents along the mask's principal axes.
  - `quad_corners_xy`: 4-corner approximation of the outline, `x y;x y;...`.
  - `occluded_or_cut`: 1 = touches the image edge or the watermark.
- `scripts/`:
  - `measure.py` (segmentation, track, overlays)
  - `props_axes.py` (static-prop axis sizes)
  - `view.py` and `print_track.py` (helpers)
  - `props_raw.json` (per-frame prop centroids/bboxes)
  - `inspect.py` is an accidental name clash that I turned into a harmless shim. Run the scripts with `python -I`.

## Objects
- **white_board**: a flat white rectangular board/tray with two small grey knobs on its far (upper) edge.
  - Frames 0-15: at rest at the lower right, bottom part outside the frame.
  - Frame 16: starts moving (sub-pixel change); clear motion from frame 17.
  - It travels in a nearly straight line up-left in the image to (548, 278) at frame 48, still moving at the end.
  - Image step per frame: peaks at ~25 px around frame 21, then ~15 px (frames 31-35) and ~12.5 px (frames 44-48).
  - It shrinks steadily (length 326→203 px, width 163→86 px, area 42k→14k px² from frame 21 to 48), so it is moving away from the camera across the floor.
  - Its width shrinks faster than its length, so foreshortening increases with distance (oblique downward camera).
- **Static props** (centres and sizes in scene.json; the centre's std over the clip is <0.6 px):
  - `trash_bin`: navy confetti-pattern bin, top-left, ~90x100 px.
  - `tote_bag`: navy bag lying flat with a pink logo, ~125x75 px.
  - `carton`: small white drink box, ~52x69 px.
  - `teddy_bear`: brown plush toy lying down, ~116x76 px along its own axis.

## Camera
Static: the static props' centroids vary by ≤0.1–0.5 px. There is no floor texture, horizon or vanishing point,
because the background is replaced. The only perspective cue is the board's shrinking size; image-up means farther away.

## Reliability and ambiguities
- **Board mask**: rule V>185 & S<45, largest component, holes filled. I checked it on overlays (`frames/ov_*.png`) and it
  covers the white surface well.
  - The small grey knobs and some soft, blurred edge pixels are not included, so extents may be ~2-5 px short.
  - Frames 17-21 have motion blur, which inflates the extents by a few px along the motion direction.
- **Frames 0-20 are cut**: the board is clipped by the bottom image edge (and the watermark at frames 19-20). The centroid
  and sizes there describe the visible part only; the true centre is lower. For full-object sizes, use frames ≥21.
- **Likely dropped frame**: the step from frame 35 to 36 is 31 px against ~15 px for its neighbours. Treat 35→36 as two
  frame intervals when differencing.
- **Motion onset**: frame 16 (t = 0.667 s) shows the first sub-pixel change, and motion is unambiguous from frame 17 (t = 0.708 s).
- **Prop sizes**: these are image extents of oblique views (bin top rim plus side; carton top plus side), with masks
  accurate to ~±3 px. No metric scale was assumed anywhere.
