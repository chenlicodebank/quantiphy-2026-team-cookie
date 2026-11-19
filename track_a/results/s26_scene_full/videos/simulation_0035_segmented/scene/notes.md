# simulation_0035_segmented: measurement record

3D Blender render, segmented (plain white background). 1080x1080 px, 24 fps, 72 frames (t = frame/24).
It contains two moving objects and nothing else: a **bird** (black, flapping, upper object) and a **human** walking (lower left).
There are no static objects, ground, horizon or markings. The camera is static. Assume the principal point is at the image centre (540, 540).

## Files
- `scene.json`: inventory, ranges, events, camera.
- `tracks/bird.csv`, `tracks/human.csv`: one row per frame (0-71). Columns: frame, time, bbox (x0,y0,x1,y1 inclusive, px), bbox centre,
  darkness-weighted mask centroid, bbox width/height, PCA main-axis length / across width / angle, mask area, part count,
  occluded flag, `ref_x, ref_y` (the recommended reference point). The human file also has feet_y and head_y.
- `scripts/measure.py` does the segmentation and tracks (threshold 255-min(RGB) > 25, connected components, split at y = 670) and writes check images to `frames/`.
  `scripts/summary.py` prints the tables. `scripts/look_end.py` checks the human's head clipping.

## Reference points
- Bird: centroid of the mask's thick core (distance transform >= 50 % of max), which is about the body centre. Wing flapping moves the
  bbox centre a lot, so use ref_x/ref_y. ref_y still bobs about +-10 px with the flapping (the body may really bob too).
  Accuracy is about +-1-2 px. Its path runs almost horizontally from x 55 to 652, about 8.5 px/frame. **Frames 0 and 1 are identical** (the bird starts moving at frame 1).
- Human: pelvis estimate. ref_x = mask centroid x; ref_y = lowest foot - 0.53 x 40.5 px (median full height).
  Accuracy is about +-1 px horizontally; the vertical position is model-based. The human walks right from x 128 to 202, about 1.04 px/frame, with the feet drifting down from y 745 to 751.
  The centroid x wobbles with the leg swing.

## Sizes (px)
- Human full height 39-42 px (median 40.5) in frames 0-64. **Frames 65-71: the segmentation mask cuts the head off flat**
  (about 9 px missing). Those frames have occluded=1, and their height is not the real height. Width is 10-18 px (gait).
  The height only changes ±1 px during walking, so minimum and maximum walking height can't be resolved better than about 39 vs 42 px.
- Bird bbox width 19-31 px: widest (29-31) when the wings are flat/spread (frames 5-6, 29-31, 52-54), narrowest (19-20) with the wings raised in a V.
  Height is 6-25 px. Wingspan in the image is roughly the max bbox width, about 31 px. The bird is seen from the side or behind, so the true span may be foreshortened.
- Apparent sizes show no trend over the clip, so both objects stay at roughly constant depth (motion is mostly lateral).

## Ambiguities and reliability
- The objects are tiny (bird about 20-30 px, human about 40 px), so pixel quantisation is a few percent of their size.
- There are no perspective cues. Metric 3D work needs depth_info plus the given prior to fix the focal length.
- The edges are antialiased and grey. The threshold of 25 includes faint edge pixels, so bboxes may be about 1 px larger than the solid silhouette.
