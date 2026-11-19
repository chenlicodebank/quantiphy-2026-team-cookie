# simulation_0227_segmented — measurement record

Video: 1920x1080, 24 fps, 50 frames (t = frame/24, 0 … 2.0417 s). Segmentation clip of a Blender render: white
background, labelled 2D. All numbers are pixels (x right, y down) and seconds; no metric scale is assumed.

## Scene
- **cat**: black-and-white cat (black body and raised tail, white/grey head and paws) walking right in profile, in
  front of the chairs. It moves the whole clip.
- **flamingo_float**: pink/purple inflatable flamingo pool ring (neck and head on its right side). It is the lowest
  object in the image and slides right without visible rotation. It moves the whole clip.
- Static objects: **six wooden lounge chairs** in two rows and a small **round_item** (side table or bucket) between
  the front-left and front-middle chairs. The back row (left, middle, right) has its top at y=713. The front row
  (left, middle, right) has its top at about y=735 and its leg tips at about y=901. Each chair's extents are in
  scene.json.
- Camera: static (shift 0 px). There is no ground or horizon. The back-row chairs look about 145 px tall and the
  front-row chairs about 167 px, so the rows are at different depths. The cat and the float are lower in the image,
  so they are probably nearer the camera than the chairs. Their apparent sizes stay constant (float about 158 px
  wide, cat about 106 px), so each moves parallel to the image plane at constant depth. The cat and the float may
  not be at the same depth as each other. If a question gives the prior on one object, applying that scale to the
  other assumes equal depth, as the 2D convention does.

## Files
- `scene.json`: inventory, static extents, camera, events.
- `tracks/cat.csv`, `tracks/flamingo_float.csv`: one row per frame (0–49) with these columns:
  - `cx_px, cy_px`: the mask centroid, used as the reference point.
  - `bbox_x0..y1, bbox_w, bbox_h`: the bounding box.
  - `mask_len_main_axis_px, mask_width_across_px, main_axis_angle_deg`: PCA extents of the mask.
  - `mask_area_px`.
  - `occluded`: for the cat, 1 means it overlaps the front-left chair's left front leg. The cat is in front of the
    leg, not hidden by it.
- `scripts/bg.py`: median background from every 2nd frame, rows ≥ 600. It writes the scratch file
  frames/bg_rows600.npy, which the other scripts need; rerun it first.
- `scripts/track.py`: background difference (threshold 40) for the moving objects. The float is the
  pink/purple/blue changed pixels. The cat is the low-saturation or dark changed pixels away from the float. The
  script writes the overlays frames/ov_XX.png.
- `scripts/static.py`: extents of the static objects. `scripts/show.py`: prints the tracks with per-frame dx, dy.

## Motion summary (for orientation; no fits)
- **Float**: about 0.8 px/frame at frame 1. It speeds up roughly linearly to a peak of about 13.5 px/frame at frames
  22–25 (t ≈ 1.0 s), then slows roughly linearly to about 1 px/frame at frame 49, when it is still creeping. Its x
  goes 733.2 → 1162.7 and its y drifts 972 → 969. This looks like speeding up then slowing down, possibly a pushed or
  braked slide.
- **Cat**: a steady walk. x goes 567.4 → 836.0, a mean of 5.48 px/frame. The per-frame dx varies from 3 to 9.6 px
  and y wobbles by ±3 px because of the gait and changes in the mask shape. Smooth over several frames before using
  it for speed.

## Reliability and ambiguities
- **Float**: the mask is clean and the extents are stable to ±1–2 px. The centroid sits slightly toward the ring;
  the true origin may be offset by a few px, but the offset is constant, so displacements are unaffected. For the
  float's size use bbox_w 158 px (horizontal length) and bbox_h of about 125–132 px (neck top to ring bottom).
- **Cat**: parts of the white head can blend into the white background, but in the checked overlays the head was
  mostly detected. Paws and tail are included. The mask length (about 104–114 px) runs from tail to nose. In frames
  26–27, chair-leg pixels inflate bbox_w to 120–123 px; prefer the median of about 106 px. The cat height (tail tip
  to feet) is 66–83 px; its head top is about 10–15 px below the tail tip. The centroid includes the raised tail, so
  it is a little above and behind the pelvis. Per-frame centroid noise is about ±1–2 px.
- Static extents come from the median background and are good to about ±2 px. The chairs overlap each other, and
  the back-middle chair is mostly hidden. Segmentation edges flicker near the round item and the chair legs.
- Overlays checked at frames 0, 12, 24, 26, 36 and 49: the masks cover the correct objects.
