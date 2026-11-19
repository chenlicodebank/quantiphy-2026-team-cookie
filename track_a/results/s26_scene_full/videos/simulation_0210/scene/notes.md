# simulation_0210 – measurement record (pixels, seconds)

2D Blender render, 1920x1080, 24 fps, 50 frames (t = frame/24, 0 to 2.042 s). Static camera.
Scene: a black cat with a light-grey/white head and white paws walks left to right along the floor in
front of a plain wall. At the right there is a wooden slatted table holding a table lamp (left end) and two
blue-and-white vases, with a tall wood-framed mirror leaning on the wall behind it. The cat is the only moving object.

## Files
- `scene.json`: inventory (cat plus static objects with pixel bboxes and extents), camera, events, cat summary stats.
- `tracks/cat.csv`: one row per frame (0–49). Columns: frame, t; `cx_mask,cy_mask` = mask centroid (**best proxy
  for the rig origin**, which isn't visible); `cx_bbox,cy_bbox` = bbox centre (the bbox includes the raised tail);
  `cx_torso,cy_torso` and `torso_x0..y1` = box around the dense black torso band (no tail, no legs); `bbox_*` = full
  mask bbox; `length_px` (horizontal, nose to tail) and `height_px` (tail tip/ear top to paws); `area_px`;
  `front_x` (nose); `foot_y` (lowest paw); `occluded` (always 0).
- `scripts/track_cat.py`: median-background subtraction with a colour-difference threshold, removal of the floor
  contact shadow, and morphology. Writes the CSV and the overlays `frames/ov_XX.png`. `scripts/summarize.py`
  writes scene.json.

## Key numbers
- Cat mask centroid moves from x=375.7 (f0) to x=1253.0 (f49), a net +877 px. Per-frame dx is 13–21 px (mean 17.9).
  It oscillates with the gait at a period of about 9 frames. That wobble comes from leg and tail pose, not from
  speed changes, so averaging or fitting over several frames gives a speed that is close to constant (~430 px/s).
  y stays at 929–936 px, so there is no vertical drift.
- Cat bbox including the tail: length 301–323 px (median 307.5), height 212–226 px (median 220).
  Rump-to-nose body length (nose minus rear of the torso band): 258–309 px (median 279); noisy, since it depends on
  the hind-leg pose.
  Torso band height is about 84 px. Paws are at y≈1030 and the top of the tail is at y≈806–818.
- Static objects (frame 0, read off grid overlays, ±3–5 px):
  - Table: x 1455–1920, top at y=790, feet at y=1000 (height ≈210 px). Its right end reaches the frame edge.
  - Lamp: x 1410–1625, y 512–800 (height 288 px, shade width 215 px).
  - Mirror: x 1632–1900, y 400–978 (height 578 px).
  - Large vase: 104 × 214 px. Small vase (behind it): visible width 55 px, height 196 px.
  - Floor/wall boundary: y≈955.
- Events: the cat is already walking at f0 and is still walking at f49. There are no starts, stops, turns, jumps or
  contacts; the cat never reaches the table (its nose is at x≈1399 at f49, the table starts at x≈1455).

## Reliability and ambiguity
- The mask was checked on overlays of frames 0, 12, 24, 36 and 49 and covers the whole cat, including the head and tail.
  - Some grey lower-leg pixels close to the floor colour drop out, but the bbox extents are still set by the paws and tail.
  - The floor shadow is removed. Without that step, foot_y would be about 4 px lower.
  - The bbox is accurate to about ±3 px.
- The origin is unknown. The mask centroid sits on the torso and moves like the body, but the tail and legs swing it
  by a few px per frame. The torso-box centre is an alternative; it jumps more when legs enter the band.
  - For a size prior "cat length", it's unclear whether the reference includes the tail. The full bbox length (~308 px)
    corresponds to a world AABB that includes the tail; the body without the tail is ~279 px.
  - Cat height: the full bbox (~220 px) includes the raised tail. The ear-top-to-paw height is ~170 px
    (ear top y≈860, paws y≈1030).
- 2D scene with the cat at a single depth: use one scale factor from the prior. The furniture is slightly behind the
  cat's plane (against the wall), so cat-scaled sizes for furniture are approximate.
