# simulation_0077: measurement record (pixels, seconds)

**Scene:** a simulation (Blender) video marked 2D. 24 fps, 72 frames (3.0 s), 1920x1080. The camera looks straight down
at a plain grey floor. There are two walking men and nothing else: no props, furniture or floor markings.
- **person_black**: black t-shirt, jeans, brown hair. He starts as the upper of the two (torso at about (1006,418)) and walks
  to the RIGHT in a straight horizontal line (y ≈ 405–420). He stays fully in frame through frame 71.
- **person_white**: white/light-grey t-shirt, jeans, brown hair. He starts as the lower one (torso at about (1014,610)) and walks
  to the LEFT in a straight horizontal line (y ≈ 600–612). The left edge cuts him from frame 62. The head is cut from frame 63,
  and only part of the body is visible at frames 67–71.

**Camera:** static. Frames 0 and 1 are identical. Phase correlation of the background between f0 and f71 is about 0.06 px.
Background shift is 0 for every frame.

## Files
- `scene.json`: inventory, events, camera, pixel extents, inter-person distances, perspective notes.
- `tracks/person_black.csv`, `tracks/person_white.csv`: one row per frame (0–71). Columns:
  - `frame`, `t`
  - `head_x, head_y`: centroid of the hair blob. Blank when the head is cut by the edge.
  - `torso_x, torso_y`: centroid of the shirt-coloured pixels. This is the **recommended pelvis/origin stand-in**.
  - `mask_cx, mask_cy`: centroid of the whole silhouette. It shifts with arm/leg swing.
  - `bbox_x0..y1, bbox_w, bbox_h`: silhouette bounding box. x is the walking direction.
  - `mask_len_major, mask_width_minor, major_axis_deg`: PCA-axis extents of the silhouette.
  - `area_px`, `head_w, head_h`
  - `truncated_by_frame_edge`
  - The two people never overlap (minimum torso distance is 191 px at frame 0), so there is no occlusion flag other than edge truncation.
- `summary_px.json`: step statistics, extents, camera check numbers.
- `scripts/track.py` (segmentation and tracking), `scripts/summarize.py`, `scripts/sample_colors.py`.

## Method
1. **Background:** the per-pixel median of 12 frames.
2. **Foreground:** pixels with a max channel difference above 28, followed by morphological open/close. This excludes the soft shadows.
3. **Assigning blobs:** each blob goes to a person by its count of black (grey<50) vs white (grey>185) shirt pixels.
4. **Head:** the hair is detected by colour: brown, r>g+5, r>b+7, grey 50–110. The largest blob is kept.
5. **Checking:** contours, boxes and points were drawn on frames 0, 10, 24, 40, 60, 66, 69 and 71 and inspected. They cover the full body, including arms and legs.

## Key numbers (px)
- **Motion start:** both people are still at frames 0–1 and start walking between frames 1 and 2 (t = 0.083 s). From the first step
  they walk at near-constant speed. There are no stops, turns, contacts or bounces.
- **Torso step per frame:**
  - black: mean 11.48 (frames 2–71), range 10.6–12.6.
  - white: mean 15.18 (frames 2–61), range 12.9–18.0.
  - The head-point steps are about 5% larger, because of perspective (see below).
  - Mean velocity, frames 2–60: black (+11.46, −0.09) px/frame; white (−15.17, −0.03) px/frame.
- **Path length / displacement:** sum the per-frame steps from the CSV. The paths are straight, so displacement ≈ path length.
  - Torso x for black: 1006.2 at frame 0 to 1808.9 at frame 71.
  - Torso x for white: 1014.1 at frame 0 to 104.9 at frame 61.
- **Gait:** bbox_w (along the walk) swings from about 115 to 255–295 px with the stride. Legs are apart at frames ≈7–8, 25, 44–45 and 61, and
  together at frames ≈1, 18, 34 and 52, so one step takes about 18 frames.
- **Size across the walk** (bbox_h, shoulders/arms): median 146 px for both.
- **Hair blob:** black ≈62x48, white ≈60x44.
- **Standing height cannot be seen from above.** The only body sizes available are the plan-view extents: length along the walk, width
  across it, and head size.
- **Torso-to-torso distance:** 191.5 px (f0), 646 (f24), 1104 (f42), 1575 (f60), 1810 (f71). See `scene.json`.

## Reliability and ambiguities
- **Torso centroids** are smooth to about ±1 px. The shirt centroid sits at chest/abdomen height, not exactly at the pelvis. In a top-down
  perspective view, points higher above the floor are pushed outward from the image centre (around 960,540).
  - The head is ahead of the torso by about 20–25 px near the centre, rising to about 55–60 px near the edges.
  - The pelvis is therefore probably a few px closer to the image centre than the torso centroid. This makes a ~1–3% difference
    in pixel speeds. Use the torso values unless a question's prior concerns the head.
- **Perspective and scale:** apparent sizes stay constant over time, so both people walk at the same depth. One px-to-metre scale from
  the prior applies to both. Use the same kind of measurement as the prior: torso speed for a speed prior; for a size prior, the
  matching extent (e.g. head width or bbox_h).
- **person_white at frames 62–71:** the box, mask and torso centroid are biased by edge truncation (`truncated_by_frame_edge=1`).
  Do not use these frames for speed or size.
- **Silhouette boxes:** they include swinging hands and feet, and the mask misses a little of the pink hands where they are pale. The
  soft shadows are excluded.
