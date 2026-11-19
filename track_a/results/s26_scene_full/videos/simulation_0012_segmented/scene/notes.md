# simulation_0012_segmented: measurement notes

**Video:** a segmentation video, 2D, 22 fps, 61 frames (t = 0 to 2.727 s), 1920x1954 px. The background is replaced
by white. One bird flies from left to right in the lower half of the image. A static wooden building (plank wall with a
slanted beam ledge and a dark crate) is left over in the upper half. The camera is static.

## Files
- `scene.json`: inventory, sizes, events, camera.
- `tracks/bird.csv`: one row per frame (0-60).
  - Columns: `frame, t`; `cx_centroid, cy_centroid` (mask centroid, the recommended origin proxy);
    `bbox_x0..y1, bbox_cx, bbox_cy`; `wingspan_px_y` (bbox height = wingtip to wingtip, since the wings span along y);
    `length_px_x` (bbox width); `beak_x, tail_x, body_y` (beak tip and tail tip on the body row, which is found within
    ±30 px of the centroid row); `body_mid_x` (beak/tail midpoint); `body_len_px` (beak to tail);
    `pca_major_px, pca_minor_px` (mask extents along and across its principal axes); `area_px`; `occluded` (always 0).
- `tracks/background_shift.csv`: phase-correlation shift of the building region relative to frame 0.
- `scripts/measure.py` and `scripts/debris.py`: all of the measurements above (run them from scene_ws).

## Method
- **Bird mask:** pixels with min(RGB) < 200 below row 850, a 3x3 opening, then the largest component plus nearby
  small components (feather tips).
- **Overlay check:** I drew overlays on frames 0, 10, 20, 30, 40, 50 and 60 and looked at frames 0 and 50. The mask
  covers the whole bird (wings, tail and beak) and nothing else. Mask edges are accurate to about 1-2 px.

## Reliability and ambiguities
- **Origin:** the rig origin is not visible. Use the centroid or `body_mid_x`/`body_y` as the pelvis proxy.
  - The centroid moves ±3 px vertically with the wingbeat.
  - `body_mid_x` is smoother in x.
  - The two points differ by up to about 10 px in x.
- **Motion:** almost purely +x; body_y drifts only 1108 → 1112.
  - The step per frame grows from about 7 px (frames 0-5) to about 20 px (frames 13-45), then falls to about 6 px
    (frame 60).
  - All motion is in pixels; the scale must come from the question's prior.
- **Skipped frames:** two steps are double length.
  - Frame 18 → 19 is about 37 px and frame 42 → 43 is about 36 px, against about 20 px and about 18 px for the
    neighbouring frames.
  - The wing pose jumps by two phases at the same points, so one source frame appears to be missing at each.
  - The record keeps the video frames as they are; a speed taken at frame 19 or 43 will be about twice its
    neighbours.
- **Wingspan:** varies with flapping. In image y it ranges from 124 px at the minima (frames 9, 25, 42 and 58) to
  255 px at the maximum (frame 18). The other maxima are 252 px (frame 0), 254 px (frame 33) and 247 px (frame 50).
  - The wingbeat period is about 16-17 frames.
  - Wings swept forward or back slightly inflate `length_px_x`; for body length use `body_len_px` (median 129 px,
    range 123-136 px).
- **Bird appearance:** the bird gets darker in later frames (lighting change on the model). This has no effect on the
  mask.
- **Static building:** a segmentation leftover, cut off at the top edge.
  - Its extents in `scene.json` are approximate (±10 px). It need not be at the same depth as the bird, so its px scale may differ.
  - The small grey debris patch at about x 830-980, y 735-792 flickers in size in frames 0, 7, 8, 10, 20 and 33. This
    is segmentation noise, not motion.
- **Perspective:** the bird's body length stays constant, so there is no perspective change and a single px scale is
  appropriate.
- **No events:** there is no contact, bounce or impact.
