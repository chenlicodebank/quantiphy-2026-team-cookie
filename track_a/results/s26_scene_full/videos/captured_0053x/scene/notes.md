# captured_0053x: measurement record (pixels and seconds only)

Lab recording (Orbbec, 24 fps, 48 frames, 2.0 s, 1280x720). The background was swapped for flat chroma green
(SAM2 segmentation; watermark "Modified with Segment Anything 2 Demo" at bottom right, x>1030, y>690, which is
not an object). Lab intrinsics: f = 0.5959*1280 = 763 px, principal point about (640, 360). t = frame/24.

## Files
- `scene.json`: inventory, static-object pixel extents, blue-box summary (start/end, per-frame pixel steps,
  apparent-size change), events, camera.
- `tracks/blue_box.csv`, `basketball.csv`, `cup.csv`, `notebook.csv`: one row per frame (0-47). Columns:
  frame, t, cx, cy (mask centroid = visible centre), bbox x0 y0 x1 y1 (inclusive), bbox_w/h, mask_len_major /
  mask_wid_minor (minimum-area rotated rectangle of the mask), minrect_angle, mask_area_px, occluded.
- `scripts/measure.py` does the segmentation and tracking and draws overlays into frames/ov_XX.png.
  `scripts/summarize.py` builds scene.json.

## Objects
- **blue_box** (the only moving object): a blue box or soft toy with yellow and white patches. A small white
  wheel or foot shows on its underside. It is visible in all frames and never occluded. It moves up and left in
  the image from (895, 443) at frame 0 to (537, 220) at frame 47, which is 421.5 px net. The path is almost
  straight (path length 422.4 px). It shrinks steadily: sqrt(area) goes from 106.8 to 80.1 px (ratio 0.75), and
  bbox width from 144 to 107 px. So it is moving away from the camera, and pixel distances are not metric
  without depth.
  - Its image step per frame falls from about 12 px to about 6 px, so it slows down in the image. It is already
    moving at frame 0 and is still moving at frame 47: no start, stop, bounce or contact is visible.
  - It turns slightly as it goes. The mask outline changes because it tumbles or rotates a little.
- **basketball** (static): orange-brown, right of centre. Centre (986, 370), bbox 66x61 px, diameter about
  61-66 px.
- **cup** (static): small white/grey tumbler with a dark lid, left of centre. Centre (564, 424), bbox 26x44 px
  (width x height).
- **notebook** (static): white rectangular package with green print, bottom centre, rotated about 30°. Centre
  (665, 615), rotated-rect 78x47 px, axis-aligned bbox 72x77 px. Its green print was keyed out by the
  segmentation, so the mask was hole-filled with a 25 px closing.
- The camera is static: the static centroids jitter by less than 0.2 px over the whole clip. No floor, horizon or
  vanishing point survives the background removal. The views of the cup top and the notebook face suggest an
  oblique view looking down onto a floor or table.

## Reliability and ambiguities
- Centroids: ±1 px. Box extents: ±2-3 px. Edges are soft from motion blur and the segmentation, and the white
  wheel and highlights are sometimes keyed as green.
- Two step outliers in the box track: frame 11→12 is 19.7 px and frame 35→36 is 13.1 px, against about 10 and
  6 px for the neighbouring steps. The file timestamps are uniform, so these are probably dropped capture frames
  (the true time gap is probably about 2 frames). Smooth over them, or treat each as about 2 intervals, when
  differencing.
- The visible centre is the 2D mask centroid. For 3D answers, back-project it with the given depth_info and
  f = 763 px.
- At frame 0 the box's bbox overlaps the basketball's bbox near a corner, but the masks do not touch. The static
  masks come from frame 47, so there was no cross-contamination.
