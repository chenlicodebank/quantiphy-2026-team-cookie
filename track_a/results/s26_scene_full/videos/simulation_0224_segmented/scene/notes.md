# simulation_0224_segmented — measurement record

Video: 1920x1080, 24 fps, 45 frames (t = frame/24, 0 … 1.833 s). Source: segmentation of a Blender render
(background replaced by pure white). Labelled **2D**. All values are pixels (x right, y down) and seconds; no
metric scale is assumed.

## Scene
- **block** (the only moving object): small cream/beige rounded rectangular block (eraser-like) lying lengthwise in
  the trough of the ramp. Starts at rest near the upper-right end, slides down-left along the trough, speeding up,
  drops off the lower-left end of the ramp.
- **ramp** (static): long reddish-brown wooden ramp/incline with a grey trough on top, raised rims, moulded sides,
  two feet; inclined 26.0° below horizontal in the image, high end at the right. Lower-left foot touches the
  bottom image edge.
- No people, other props, ground or markings (white background). Camera static (ramp silhouette identical in
  every frame).

## Files
- `scene.json` — inventory, pixel sizes, path direction, events, camera, frame-timing irregularity.
- `tracks/block.csv` — one row per frame 0–44:
  `cx, cy` reference point (block centre, see below); `ref_source` (template / mask_centroid / none);
  `match_score` (NCC of template); `mask_cx, mask_cy` mask centroid; `bbox_*` mask bounding box;
  `len_main_axis`, `width_across`, `main_axis_deg` (PCA axis of the mask); `area_px`; `occluded` flag;
  `duplicate_of_prev` (frame identical to previous); `note`; `s_along_path` (projection of (cx,cy)−start onto the
  down-slope unit vector (−0.899, 0.438), px from frame-0 position); `perp_offset` (px across the path).
- `scripts/` — `track_block.py` (masks + template tracking, overlays), `static_and_scene.py` (ramp extents, camera
  check, path coordinate columns), `check.py` (step check, ramp rim extremes), `endframes.py` (end crops, frame
  duplicate test), `probe.py` (colour probe). Run from the scene_ws folder.

## Method
- Median of all 45 frames (crop around the ramp) = clean background. Block mask = colour difference > 45 to that
  median, excluding saturated wood colours and white, opened 5×5 / closed, largest component near the previous one.
- Reference point (frames 0–39): the grey block patch of frame 24 was template-matched (masked NCC, sub-pixel peak)
  in every frame; `cx, cy` = frame-24 full-silhouette centroid + matched shift. Scores 0.97–1.0. Agrees with the mask
  centroid within ~1–2 px. For a rigid block in a 2D video this image centroid stands for the object origin.
- Frames 42–43: mask centroid (block rotated, template not valid). 40, 41, 44: no usable centre.
- Overlays (contour + centre) were inspected for frames 0, 12, 24, 36, 39, 40, 43: contours follow the block
  (top face plus the shaded near side; the lowest shaded edge sometimes merges with the dark trough and is lost by
  1–3 px).

## Key numbers
- Block silhouette length along its main axis (≈ motion direction): **81.3 px** (median, range 79.6–83.6 on the
  ramp; 83.3 px in the air at frame 43). Width across: ~30.5 px on the ramp (top + side face; 34.9 px at frame 43).
  Bbox ≈ 76 × 51 px. A block-size prior would normally be its long side ↔ ~81 px.
- Block start (frame 0): (1233.7, 526.9). Frame 39 (last clean): (561.1, 855.8); distance along path 748.6 px.
  Path is straight (perpendicular scatter std 0.4 px), 25.97° below horizontal.
- Ramp silhouette: bbox (424, 487)–(1421, 1079); length along its axis 1060 px, width across 244 px (includes
  moulding and feet). Top rim from (1356, 489) to (432, 939): ~1028 px. Lower end lip tip ≈ (432, 939).

## Events
- Frames 0–2 at rest (< 1 px jitter). Motion starts between frames 2 and 3 (t ≈ 0.10–0.125 s; s = 2.5 px at 3).
- Frames 3–39 slide down with growing per-frame steps (~2 px → ~38 px per frame).
- Frames 40–41 (t 1.667–1.708): block at the lower end, almost completely hidden (only a sliver at ≈ (466, 910)).
- Frame 42 (t 1.75): dropping off the lip, partly hidden (mask centroid (452.5, 965.4), biased).
- Frame 43 (t 1.792): airborne below the ramp end, tilted, fully visible at (419.8, 1019.0).
- Frame 44: block not visible.

## Frame-timing irregularity (important for speeds/accelerations)
Frames 6, 13, 25, 28, 35, 38, 41 are exact repeats of the previous frame, and frames 5, 10, 23, 27, 34, 37 show
a step about twice the neighbouring steps. Mapping each frame to an estimated true render index
(5→6, 10→11, 11→12, 12→13, 23→24, 24→25, 27→28, 34→35, 37→38; repeats share the index of the previous frame;
others unchanged) makes the per-render-frame step grow smoothly (4.6, 6.5, 6.5, 9.0, 9.5, 11, 12, 13.7, 14, 16.1,
… 33.9, 35.0, 36.0, 38.3 px), i.e. steady acceleration along the ramp. Raw one-frame backward differences are 0 at
the repeats and ~2× after the skips, so a speed asked "at time t" should be read from a smooth fit of
`s_along_path` (or using the true-index mapping), not from a single raw difference. Which convention the reference
used is unknown; both are recoverable from the CSV.

## Reliability / ambiguities
- Centre positions frames 0–36: ±1 px; 37–39: ±2 px (lower edge behind the trough rim); 42: biased (partly
  hidden); 43: ±2 px.
- Block size: ±2 px; the silhouette is the oblique view (top + side face), so "width" is not a clean dimension;
  the length along the motion axis is the most reliable size.
- Perspective: the ramp is seen obliquely (its top and front side are both visible) but no ground or grid exists;
  treat as planar with one px scale along the ramp as the 2D label suggests. The block's apparent length is
  constant (79.6–83.6 px) along the whole ramp, so no measurable depth change.
- No shadows of note (segmented), no motion blur visible.
