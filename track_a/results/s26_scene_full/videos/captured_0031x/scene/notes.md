# captured_0031x — measurement record

Lab video (real camera, 24 fps, 49 frames, 1280x720, 3D). The background has been blacked out by segmentation;
only a small wooden table (top + single grey pedestal leg) and two balls remain. Camera is static
(max background shift 0.28 px). Lab camera convention: f = 0.5959 x 1280 = 763 px, principal point ~(640, 360).

## What happens
- Frames 0-14: both balls rest at the back of the table top: yellow tennis ball at (758.5, 410.5) px,
  diameter ~30 px; small white ball at (679, 416) px, diameter ~17 px.
- Frame ~15 (t = 0.625 s, ±1 frame): both start rolling toward the camera (image motion down and slightly left).
- Yellow ball reaches the front edge at frame 42 (t = 1.75 s) and leaves it between 42 and 43. It then falls in front
  of the leg (frames 43-47, strong vertical motion blur). At frame 47 its lower part is cut off by the image bottom.
  It is gone at frame 48.
- White ball keeps rolling on the table to the end (frame 48 at (642, 459) px, diameter 29 px).

## Files
- `scene.json`: inventory, static geometry, camera, events.
- `tracks/yellow_ball.csv`, `tracks/white_ball.csv`: one row per frame. Columns: frame, t, visible, cx, cy
  (reference centre, see below), cx_mask/cy_mask (mask centroid), bbox_x0..y1, bbox_w/h, diam_px (horizontal mask
  width = apparent diameter), mask_len_major / mask_wid_minor (PCA extents of the mask), major_angle_deg,
  area_px, truncated_by_frame, occluded (always 0, nothing occludes them), note.
- `scripts/`: track.py (masks + tracks + overlay), static.py (table/leg geometry, camera shift), summarize.py
  (step sizes / diameters), dupcheck.py (no repeated frames), sample.py (colour sampling), crops.py, probe.py.

## How measured
- Yellow ball mask: hue 20-40 and Lab b* >= 156 (includes its shaded lower half; table is b* ~137-152), largest
  component near the previous position. White ball mask: S < 55, V > 175.
- Reference centre (visible centre of the ball):
  - On the table (yellow frames 0-42, white all frames): cx = bbox horizontal middle, cy = top edge + (diam-1)/2.
    The top and side edges are crisp; the bottom is not reliable (yellow: glossy reflection on the table joins the mask
    in frames 1, 2, 4; white: shaded lower part has table-like colour so the mask misses it).
  - Yellow falling (43-46): cx, cy = bbox centre of the blurred streak (mid-exposure position); bbox_h /
    mask_len_major there include blur (streak up to ~95 px tall), diam_px (width) is the real diameter.
  - Yellow frame 47: truncated by the image bottom; cy = top + diam/2 (approximate, blur makes it ~±10 px).
- Overlays of masks/centres were checked visually on frames 0, 20, 36, 42, 44-48.

## Reliability
- On-table centres: ±1 px, but quantized (integer bbox edges), so per-frame steps jitter (some 0-px steps between
  2-3 px steps; dupcheck confirms these are NOT repeated frames). Smooth over >=5 frames or fit before
  differentiating. Frame 36 shows a larger-than-neighbour step for both balls (likely irregular capture timing).
- Diameters: ±1-2 px (yellow 30 -> 54 px on the table, white 17 -> 29 px), i.e. both balls get ~1.8x closer to the
  camera while rolling; with a known ball size or depth_info, depth ~ f * D / diam_px.
- Falling yellow ball (43-47): ±3-5 px vertically because of motion blur; only 4-5 airborne frames.
- Static table geometry from the frame-48 non-black mask: ±2 px; corners of the table top are estimated from
  row/column scans (front edge ~500 px wide, back edge ~285 px, front face ~20 px thick, leg ~40 px wide,
  leg cut off by the image bottom).

## Ambiguities
- Two balls: "yellow/tennis/large" vs "white/small". No other moving objects, no people.
- The segmentation edge leaves thin black outlines around the balls; the faint halo of the motion-blurred
  falling ball is not fully in the mask.
- The cause of the motion start (push or tilt) is not visible; both start at the same frame.
