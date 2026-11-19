# simulation_0225_segmented — measurement record

2D segmentation video, 1920x1080, 24 fps, 50 frames (t = frame/24, 0–2.0417 s). White background, static camera.
A black-and-white cat walks left to right in front of six pink-brown wooden sun loungers (two rows of three),
with a dark-blue cushion/bag-like object behind them and a small dark round item in the gap between the
front-left and front-middle loungers. Only the cat moves.

## Files
- `scene.json` – inventory, static object pixel boxes, camera, events, cat summary.
- `tracks/cat.csv` – per frame (0–49): time, ref_x/ref_y (mask centroid = reference point), bbox x0,y0,x1,y1,
  bbox centre, length_px (= bbox width, horizontal; the walking direction), height_px (bbox height incl. raised tail),
  PCA main-axis length/width of the mask, mask area, occlusion flag (always 0), note.
- `tracks/cat_raw.csv` – same data, raw script output.
- `scripts/probe.py` (median background of a crop → `frames/bg_crop.npy`, scratch, outside the record), `track_cat.py` (background subtraction,
  connected components, overlays), `montage.py`, `static_objects.py` (→ `static_extents.json`), `finalize.py`.

## Method and reliability
- Cat mask: |frame − median background| > 25 in a crop (x 300–1600, y 550–1000), largest component near the
  previous position plus touching components (≥25 px). Overlays (every 6th frame) checked by eye: mask covers
  body, tail, white head and paws. The white head/paws are faint against white but captured.
- Reference point: mask centroid (proxy for body centre/pelvis). Gait makes it jitter ±1–2 px per frame
  (per-frame step 5.56 ± 1.26 px; mean x slope 5.40 px/frame; net displacement 265.8 px right, −2.4 px vertical;
  centroid path length 272.6 px, inflated slightly by the jitter). bbox centre is noisier (tail/legs).
- Cat size: length 107 px median (103–123), height 76 px median (71–84); constant over the clip
  (first-10 vs last-10 median length 106.5 vs 107.5) → constant depth, motion parallel to the image plane.
  Frames 27–30 bbox right edge may include a few px of the lounger leg that the head touches (flagged).
  Frames 10–11, 37–39, 46–49 lengths are larger because of tail/leg pose, not segmentation errors.
- Static boxes: from the median background with ROIs chosen by eye; ±2 px for visible edges. Loungers overlap,
  so back-row lounger boxes are only their visible parts. Front loungers: width ~185–215 px, height ~168 px,
  legs spanning ~182 px. Blue object 180 x 88 px visible (bottom hidden).
- No shadows, no motion blur of note, no camera motion. No ground plane/horizon cues (white background).

## Ambiguities
- The six loungers are the same model; name them by row (front/back) and position (left/middle/right).
- The blue object's identity (cushion, bag, ottoman) and the dark round item are unclear; both are static.
- Cat origin in Blender is unknown; the mask centroid sits mid-body. For speeds use ref_x/ref_y (or a smoothed
  fit) with one planar scale from the question's prior (e.g. cat length 107 px).
