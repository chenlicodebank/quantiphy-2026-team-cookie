# simulation_0114_segmented: measurement notes

**Scene.** 2D segmentation video: 1080x1920 px, 24 fps, 80 frames (0-79), t = frame/24. On a uniform white background, a single
yellow/orange airplane is seen from directly above, with the nose pointing down the image. It falls (moves) straight down the
screen, speeding up from rest at frame 0, and leaves through the bottom edge in frames 76-78. Frame 79 is an unrelated
snowy-mountain photo, a leftover from the background replacement. Ignore it: the plane is not in it.

## Files
- `scene.json`: inventory, sizes, events, camera.
- `tracks/airplane.csv`: one row per frame (0-79). Columns:
  - `ref_x, ref_y`: reference point (px). This is the frame-0 bbox centre, carried forward by template matching.
  - `ref_method`: how `ref_x, ref_y` was obtained in that row.
  - `mask_cx, mask_cy`: centroid of the mask.
  - `x0, y0, x1, y1`: mask bounding box.
  - `wingspan_px`: x extent. `length_px`: y extent (tail to nose).
  - `area_px`: mask area.
  - `wing_row_y`: the widest row, i.e. the wing line.
  - `touches_edge`, `occluded` (0 throughout: nothing occludes the plane), `note`.
- `scripts/track.py`: colour/darkness mask, bbox and extents. `scripts/refine.py`: sub-pixel template matching against frame 0
  (`refine_out.json`). `scripts/finalize.py`: merges these, handles the edge frames, runs QA and draws `frames/overlay.png`.
  `scripts/crops.py`: zoomed check crops.

## How measured and reliability
- **Mask.** Pixels with saturation > 40 or max channel < 200 count as the plane. Overlays and zoomed crops (frames 0, 40, 75-78)
  confirm the mask covers the whole plane.
- **Reference point (frames 0-76).** The template match carries the frame-0 bbox centre (671.0, 160.0) to each later frame.
  Precision is about ±1 px: a smooth quadratic in time fits `ref_y` over frames 0-75 with 1.1 px RMS (3.4 px max).
  - `ref_x` stays at 671 ± 1 throughout, so the motion is purely vertical.
  - Use `ref_y` rather than the mask bbox centre or centroid for motion. Motion blur stretches the mask (see below), which
    biases both.
- **Edge frames.** In frame 76 the nose is cut by the bottom edge, but the template value (1886.0) agrees with the other
  estimates. Frames 77-78 show only the tail, so `ref_y` there is the tail-tip top edge (`y0`) + 61.84 px. That offset was
  calibrated on frames 60-75, which have similar blur. The resulting 1929.8 and 1973.8 lie off-image and agree with the smooth
  trend (1928.6, 1974.8) to about 1 px. The raw template values (1920.9, 1964.7) were wrong because the template was cut down too
  far, and were replaced.
- **Sizes.** Use frame 0, which is sharp and static: wingspan 167 px and length 107 px (tail tip to nose). The tailplane span
  (about 55 px), fuselage width (about 13 px) and wing chord (about 19 px) were read off a 3x zoom and are only good to about ±2 px.
  - From about frame 14 on, vertical motion blur adds about 2-7 px to `length_px` (up to 114 px) and lowers the frame-to-frame
    contrast. The wingspan stays 165-168 px, and the plane does not rotate.
  - Height is not visible in this top view.
- **Origin ambiguity.** The plane's true origin is not known. The bbox centre (used here) and the mask centroid differ by about
  8.5 px in y (centroid lower, nearer the wings; the wing line is at y = 176 in frame 0). This offset is constant, so it does not
  affect displacements, speeds or accelerations, only absolute positions.
- **Camera.** Static, planar top-down view. No perspective cues and no constant-depth reference, so use one px→m scale from the
  question's prior. For a size prior, use the frame-0 wingspan or length. For a speed or acceleration prior, use differences of
  `ref_y`.
- **Events.** Motion starts at frame 0 from (near) rest: step 0→1 is about 0.5 px, and the steps grow linearly, to about 46 px
  per frame by frame 75. The nose reaches the bottom edge at frame 76. The plane is effectively gone after frame 78. There are no
  bounces, contacts or direction changes. No other objects or static features exist.
